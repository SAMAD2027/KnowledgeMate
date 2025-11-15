from tools.curriculum_tool import CurriculumTool

class PlannerAgent:
    """
    PlannerAgent: Plans personalized learning paths for students
    Uses CurriculumTool to select topics and sequence learning.
    """
    def __init__(self, curriculum_tool: CurriculumTool, memory):
        self.curriculum_tool = curriculum_tool
        self.memory = memory

    def plan(self, student_id: str):
        """
        Generates a learning plan for a given student_id
        Stores the plan in memory
        """
        print(f"[PlannerAgent] Planning learning path for {student_id}...")
        plan = self.curriculum_tool.generate_plan(student_id)
        self.memory.store(student_id, "plan", plan)
        print(f"[PlannerAgent] Plan stored for {student_id}: {plan}")
        return plan
