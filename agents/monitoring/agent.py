from core.base_agent import BaseAgent
from typing import List, Dict, Any

class monitoringAgent(BaseAgent):
    """monitoring Agent implementation"""
    
    async def perceive(self, event: dict) -> None:
        """Perceive environment events"""
        pass
    
    async def reason(self) -> List[str]:
        """Reason about beliefs and decide intentions"""
        pass
    
    async def act(self, intentions: List[str]) -> list:
        """Execute intentions"""
        pass
