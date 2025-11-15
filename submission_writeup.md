# KnowledgeMate Submission Writeup

## Problem
Students need personalized guidance and structured learning paths.

## Solution
KnowledgeMate uses multi-agent AI:
- PlannerAgent: creates learning plan
- TutorAgent: provides explanations
- ContentGenAgent: generates practice
- AssessorAgent: evaluates progress

## Architecture
See `assets/architecture_diagram.png`.

## Implementation
- Python, ADK for agents
- MemoryBank for session & long-term memory
- Tools: CurriculumTool, CodeExecTool, WebSearchTool
