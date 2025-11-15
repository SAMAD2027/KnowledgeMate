class Evaluation:
    """
    Evaluation class to evaluate agents collectively
    """
    def __init__(self):
        self.metrics = {}

    def evaluate_agents(self, agents_list):
        """
        Dummy evaluation: logs agent names
        """
        print("[Evaluation] Evaluating agents...")
        for agent in agents_list:
            agent_name = agent.__class__.__name__
            print(f"[Evaluation] Agent: {agent_name}")
            self.metrics[agent_name] = "Success"
        print("[Evaluation] Metrics:", self.metrics)
        return self.metrics

# Helper function for convenience
def evaluate_agents(agents_list):
    evaluator = Evaluation()
    return evaluator.evaluate_agents(agents_list)
