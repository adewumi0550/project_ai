from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A customer support agent specializing in waste management inquiries.',
    instruction='Answer waste management related questions and provide support to customers.',
)



