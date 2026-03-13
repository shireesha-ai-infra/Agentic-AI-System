"""
Agent Core Runtime - Implements a minimal autonomous agent loop:

Observe → Think → Act → Update State → Repeat
"""

from typing import Dict, Any
from llm_inference import LLMCLient

# Core agent runtime class responsible for reasoning and acting toward a goal.
class Agent:
    def __init__(self, goal: str,max_iterations: int = 5):
        self.goal = goal
        self.max_iterations = max_iterations

        self.llm = LLMCLient()

        # defining internal state
        self.state = {
            "goal": goal,
            "history": [],
            "iteration": 0,
            "done": False
        }

    # step 1 - OBSERVE : Gathers current agent context.
    def observe(self) -> Dict[str, Any]:
        observation = {
            "goal": self.state["goal"],
            "history": self.state["history"]
        }
        return observation

    # step 2 - THINK : Ask the LLM what to do next.
    def think(self, observation: Dict[str, Any]) -> Dict[str, Any]:
        system_prompt = """
            You are an autonomous AI agent.

            You must decide the next action to achieve the user's goal.

            Return output strictly as JSON with the format:

            {
            "thought": "...",
            "action": "...",
            "input": "..."
            }

            Available actions:
            search
            finish
            """

        user_prompt = f"""
            Goal:
            {observation["goal"]}

            Previous steps:
            {observation["history"]}
            """

        response = self.llm.structured_chat(system_prompt, user_prompt)

        return response

    # Step 3 - ACT : Execute the chosen action.
    def act(self, reasoning: Dict[str, Any]) -> str:
        action = reasoning.get("action")
        action_input = reasoning.get("input")

        if action == "search":
            # Simulated tool instead of calling for now
            result = f"Simulated search results for '{action_input}'"
        elif action == "finish":
            result = "Goal completed."
            self.state["done"] = True
        else:
            result = "Unknown action."

        return result

    # UPDATE STATE - Stores the result of the step.
    def update_state(self,reasoning: Dict[str, Any],result: str):
        step_record = {
            "iteration": self.state["iteration"],
            "thought": reasoning.get("thought"),
            "action": reasoning.get("action"),
            "input": reasoning.get("input"),
            "result": result
        }
        self.state["history"].append(step_record)

    # RUN LOOP - Main agent execution loop.
    def run(self):
        print("\nAgent started")
        print("Goal:", self.goal)

        while (not self.state["done"] and self.state["iteration"] < self.max_iterations):
            print("\n-----------------------------")
            print(f"Iteration {self.state['iteration']}")
            print("-----------------------------")

            observation = self.observe()

            reasoning = self.think(observation)

            print("Thought:", reasoning.get("thought"))
            print("Action:", reasoning.get("action"))
            print("Input:", reasoning.get("input"))

            result = self.act(reasoning)

            print("Result:", result)

            self.update_state(reasoning, result)

            self.state["iteration"] += 1

        print("\nAgent finished.")

        return self.state


# Run agent
if __name__ == "__main__":

    goal = "Find ideas for Agentic AI projects"

    agent = Agent(goal=goal, max_iterations=5)

    final_state = agent.run()

    print("\nFinal Agent State:")
    print(final_state)