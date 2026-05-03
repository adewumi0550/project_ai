# Import the Agent class from the Google ADK library.
# This class is used to define and configure our AI agent.
from google.adk.agents.llm_agent import Agent

# Create an instance of the Agent.
# This is our main AI agent, configured for waste management customer support.
root_agent = Agent(
    # Specifies the AI model to be used. 'gemini-2.5-flash' is a powerful and fast model.
    model='gemini-2.5-flash',
    # A unique name for this agent instance.
    name='root_agent',
    # A brief description of the agent's role. This helps in understanding its primary function.
    description='A customer support agent specializing in waste management inquiries.',
    # The core instruction for the agent, guiding its responses and behavior.
    # It tells the agent what kind of questions to answer and its general purpose.
    instruction='Answer waste management related questions and provide support to customers.',
)



