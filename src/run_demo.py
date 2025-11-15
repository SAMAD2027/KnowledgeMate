from agents.planner_agent import PlannerAgent
from agents.tutor_agent import TutorAgent
from agents.assessor_agent import AssessorAgent
from agents.contentgen_agent import ContentGenAgent
from memory.memory_bank import MemoryBank
from tools.curriculum_tool import CurriculumTool
from tools.code_exec_tool import CodeExecTool
from tools.web_search_tool import WebSearchTool
from eval.evaluation import evaluate_agents

def main():
    print("Initializing KnowledgeMate demo...")
    
    # Initialize memory
    memory = MemoryBank()
    
    # Initialize tools
    curriculum_tool = CurriculumTool()
    code_exec_tool = CodeExecTool()
    web_search_tool = WebSearchTool()
    
    # Initialize agents
    planner = PlannerAgent(curriculum_tool, memory)
    tutor = TutorAgent(memory, web_search_tool)
    assessor = AssessorAgent(memory)
    content_gen = ContentGenAgent(memory)
    
    # Sample workflow
    student_id = "student_001"
    planner.plan(student_id)
    tutor.tutor(student_id, "Explain Pythagoras theorem")
    content_gen.generate_content(student_id, topic="Pythagoras theorem")
    assessor.assess(student_id)
    
    # Evaluation
    evaluate_agents([planner, tutor, content_gen, assessor])
    
    print("KnowledgeMate demo complete.")

if __name__ == "__main__":
    main()
