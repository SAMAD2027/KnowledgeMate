class TutorAgent:
    """
    TutorAgent: Provides explanations, answers questions, and guides the student
    """
    def __init__(self, memory, web_search_tool=None):
        self.memory = memory
        self.web_search_tool = web_search_tool

    def tutor(self, student_id: str, question: str):
        """
        Tutors the student on a given question
        Uses memory and optional web search for enhanced explanations
        """
        print(f"[TutorAgent] Tutoring {student_id} on: {question}")
        # Fetch plan to contextualize
        plan = self.memory.retrieve(student_id, "plan")
        # Dummy LLM-generated response (replace with Gemini/ADK)
        answer = f"Answer to '{question}' based on plan: {plan}"
        # Optionally enhance answer with web search
        if self.web_search_tool:
            search_results = self.web_search_tool.search(question)
            answer += f"\n[WebSearch] Top result: {search_results[0] if search_results else 'N/A'}"
        # Store tutor interaction in memory
        self.memory.store(student_id, "last_answer", answer)
        print(f"[TutorAgent] Provided answer to {student_id}: {answer}")
        return answer
