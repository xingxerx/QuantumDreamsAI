
import uuid
import datetime
from typing import Dict, List, Any, Optional

# Define type aliases for clarity
Timestamp = datetime.datetime
Message = Dict[str, Any] # Could be more specific, e.g., TypedDict if using Python 3.8+
Conversation = Dict[str, Any] # Could also be more specific
ConversationID = str

class ConversationManager:
    def __init__(self, context_memory: int = 15):
        self.conversations: Dict[ConversationID, Conversation] = {}
        if context_memory <= 0:
            raise ValueError("Context memory must be a positive integer.")
        self.context_memory: int = context_memory

    def start_conversation(self) -> ConversationID:
        conversation_id: ConversationID = str(uuid.uuid4())
        self.conversations[conversation_id] = {
            "messages": [],
            "created_at": datetime.datetime.now() # Consider timezone awareness if needed: datetime.now(datetime.timezone.utc)
        }
        return conversation_id

    def add_message(self, conversation_id: ConversationID, message_text: str) -> None:
        if conversation_id in self.conversations:
            self.conversations[conversation_id]["messages"].append({
                "message": message_text,
                "timestamp": datetime.datetime.now() # Consider timezone awareness
            })
            # Trim messages if context memory is exceeded
            if len(self.conversations[conversation_id]["messages"]) > self.context_memory:
                self.conversations[conversation_id]["messages"].pop(0)
        else:
            raise KeyError(f"Conversation with ID '{conversation_id}' not found.")

    def get_conversation(self, conversation_id: ConversationID) -> Optional[Conversation]:
        return self.conversations.get(conversation_id)
# Example usage:
manager = ConversationManager()
conversation_id = manager.start_conversation()
manager.add_message(conversation_id, "Hello")
manager.add_message(conversation_id, "How are you?")
print(manager.get_conversation(conversation_id))
