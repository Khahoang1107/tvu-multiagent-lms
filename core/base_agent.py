from abc import ABC, abstractmethod
from typing import Any, Dict, List
from dataclasses import dataclass
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

@dataclass
class AgentMessage:
    """Standard message format between agents"""
    sender: str
    receiver: str
    intent: str
    content: Dict[str, Any]
    correlation_id: str
    timestamp: str

class BaseAgent(ABC):
    """Abstract BDI Agent - all agents must inherit this"""
    
    def __init__(self, agent_id: str, config: dict):
        self.agent_id = agent_id
        self.config = config
        self._beliefs = {}
        self._message_bus = None
        logger.info(f"Agent [{self.agent_id}] initialized")
    
    @abstractmethod
    async def perceive(self, event: dict) -> None:
        """Receive event from environment"""
        pass
    
    @abstractmethod
    async def reason(self) -> List[str]:
        """Decide which intentions to execute"""
        pass
    
    @abstractmethod
    async def act(self, intentions: List[str]) -> List[AgentMessage]:
        """Execute intentions"""
        pass
    
    async def run(self):
        """BDI cycle"""
        while True:
            # Perceive
            event = await self._message_bus.get_next_event(self.agent_id)
            await self.perceive(event)
            
            # Reason
            intentions = await self.reason()
            
            # Act
            messages = await self.act(intentions)
            
            # Send messages
            for msg in messages:
                await self._message_bus.send_message(msg)
