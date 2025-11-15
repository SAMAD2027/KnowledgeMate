import json
import os

class MemoryBank:
    """
    MemoryBank: Handles both short-term (session) and long-term memory for students
    """
    def __init__(self, storage_file: str = "data/memory_bank.json"):
        self.memory = {}  # in-memory storage
        self.storage_file = storage_file
        self.load_memory()

    def store(self, student_id: str, key: str, value):
        """
        Stores data for a student
        """
        if student_id not in self.memory:
            self.memory[student_id] = {}
        self.memory[student_id][key] = value
        self.save_memory()

    def retrieve(self, student_id: str, key: str):
        """
        Retrieves data for a student
        """
        return self.memory.get(student_id, {}).get(key, None)

    def load_memory(self):
        """
        Loads memory from persistent JSON file
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as f:
                try:
                    self.memory = json.load(f)
                except json.JSONDecodeError:
                    self.memory = {}
        else:
            self.memory = {}

    def save_memory(self):
        """
        Saves memory to persistent JSON file
        """
        with open(self.storage_file, "w") as f:
            json.dump(self.memory, f, indent=2)
