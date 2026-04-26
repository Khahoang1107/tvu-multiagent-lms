from typing import Any, Dict, Callable
from dataclasses import dataclass
from datetime import datetime
import json

class MessageBus:
    """Inter-agent communication bus"""
    
    def __init__(self):
        self.api_endpoints = {}
        self.handlers = {}
    
    def register_service(self, service_name: str, host: str, port: int):
        """Register service endpoint"""
        self.api_endpoints[service_name] = f"http://{host}:{port}"
    
    async def send_message(self, message: dict):
        """Send message between agents"""
        pass
    
    async def get_next_event(self, agent_id: str):
        """Get next event for agent"""
        pass

message_bus = MessageBus()
