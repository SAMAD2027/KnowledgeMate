import json
import os

class CurriculumTool:
    """
    CurriculumTool: Generates a learning plan for a student based on seed curriculum
    """
    def __init__(self, curriculum_file: str = "data/seed_curriculum.json"):
        self.curriculum_file = curriculum_file
        self.curriculum = self.load_curriculum()

    def load_curriculum(self):
        if os.path.exists(self.curriculum_file):
            with open(self.curriculum_file, "r") as f:
                return json.load(f)
        else:
            # Default dummy curriculum
            return {
                "Math": ["Algebra", "Geometry", "Calculus"],
                "Science": ["Physics", "Chemistry", "Biology"]
            }

    def generate_plan(self, student_id: str):
        """
        Generates a simple sequential learning plan
        """
        plan = {}
        for subject, topics in self.curriculum.items():
            plan[subject] = topics  # Could randomize or prioritize
        return plan
