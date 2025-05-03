
import uuid
import datetime
class ConversationManager:
    def __init__(self):
        self.conversations = {}
        self.context_memory = 15
    def start_conversation(self):
        conversation_id = str(uuid.uuid4())
        self.conversations[conversation_id] = {
            "messages": [],
            "created_at": datetime.datetime.now()
        }
        return conversation_id
    def add_message(self, conversation_id, message):
        if conversation_id in self.conversations:
            self.conversations[conversation_id]["messages"].append({
                "message": message,
                "timestamp": datetime.datetime.now()
            })
            if len(self.conversations[conversation_id]["messages"]) > self.context_memory:
                self.conversations[conversation_id]["messages"].pop(0)
    def get_conversation(self, conversation_id):
        return self.conversations.get(conversation_id)
# Example usage:
manager = ConversationManager()
conversation_id = manager.start_conversation()
manager.add_message(conversation_id, "Hello")
manager.add_message(conversation_id, "How are you?")
print(manager.get_conversation(conversation_id))
