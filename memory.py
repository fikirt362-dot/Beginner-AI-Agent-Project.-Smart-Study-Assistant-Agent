# memory.py

class Memory:
    def __init__(self, limit=5):
        self.limit = limit
        self.messages = []

    def add(self, role, content):
        self.messages.append(f"{role}: {content}")
        if len(self.messages) > self.limit:
            self.messages.pop(0)

    def get_context(self):
        return "\n".join(self.messages)
