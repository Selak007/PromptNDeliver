from sqlalchemy.orm import Session
from ..database.models import AgentMemory, AgentLog
import datetime

class MemoryManager:
    def __init__(self, db: Session):
        self.db = db

    def log_action(self, agent_name: str, action: str, result: str):
        log = AgentLog(agent_name=agent_name, action_taken=action, result=result)
        self.db.add(log)
        self.db.commit()
        self.db.refresh(log)
        return log

    def update_memory(self, issue_type: str, trend: str = None):
        memory = self.db.query(AgentMemory).filter(AgentMemory.issue_type == issue_type).first()
        if memory:
            memory.frequency += 1
            if trend:
                memory.trend = trend
        else:
            memory = AgentMemory(issue_type=issue_type, trend=trend, frequency=1)
            self.db.add(memory)
        
        self.db.commit()
        self.db.refresh(memory)
        return memory

    def get_recent_logs(self, limit: int = 10):
        return self.db.query(AgentLog).order_by(AgentLog.timestamp.desc()).limit(limit).all()

    def get_memory_stats(self):
        return self.db.query(AgentMemory).order_by(AgentMemory.frequency.desc()).all()
