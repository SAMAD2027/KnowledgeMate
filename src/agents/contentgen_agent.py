class ContentGenAgent:
    """
    ContentGenAgent: Generates content and practice problems for students
    """
    def __init__(self, memory):
        self.memory = memory

    def generate_content(self, student_id: str, topic: str):
        """
        Generates sample content for a topic
        Stores generated content in memory
        """
        print(f"[ContentGenAgent] Generating content for {student_id} on {topic}...")
        # Dummy generated content
        content = f"Practice exercises and notes on {topic}"
        self.memory.store(student_id, f"content_{topic}", content)
        print(f"[ContentGenAgent] Content stored for {student_id}: {content}")
        return content
