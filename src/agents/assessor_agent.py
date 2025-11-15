class AssessorAgent:
    """
    AssessorAgent: Evaluates student understanding and performance
    """
    def __init__(self, memory):
        self.memory = memory

    def assess(self, student_id: str):
        """
        Performs a dummy assessment based on the student's learning plan and last answer
        Stores results in memory
        """
        print(f"[AssessorAgent] Assessing performance for {student_id}...")
        plan = self.memory.retrieve(student_id, "plan")
        last_answer = self.memory.retrieve(student_id, "last_answer")
        # Dummy scoring (replace with real evaluation logic)
        score = 90  # Example fixed score
        feedback = f"Assessment complete. Score: {score}/100. Last answer reviewed: {last_answer}"
        self.memory.store(student_id, "assessment", {"score": score, "feedback": feedback})
        print(f"[AssessorAgent] Assessment for {student_id}: {feedback}")
        return feedback
