from langchain.prompts import PromptTemplate



# Define the prompt template
sql_generate_prompt_template = PromptTemplate(
    input_variables=["question"],
    template="""
You are an expert in translating natural language to SQL.
The user asks: "{question}"
Write only the SQL query. Do not add explanations or formatting.
"""
)
