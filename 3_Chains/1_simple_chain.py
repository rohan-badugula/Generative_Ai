from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template = "Generate {n} intresting facts about {topic}",
    input_variables = ['n','topic']
)

model = ChatOpenAI(model = "gpt-3.5-turbo")
parser = StrOutputParser()

simple_chain = prompt | model | parser
result = simple_chain.invoke({'topic': 'cricket', 'n': 7})
print(result)