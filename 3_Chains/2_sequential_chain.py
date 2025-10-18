from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv 


load_dotenv()

prompt1 = PromptTemplate(
    template = "Generate a detailed report on {topic} in {n} paragraphs",
    input_variables = ['topic','n']
)

prompt2 = PromptTemplate(
    template="generate 3 points summary from the following text \n {text}",
    input_variables= ['text']
)

model = ChatOpenAI(model = "gpt-3.5-turbo")
parser = StrOutputParser()

sequential_chain = prompt1 | model | parser | prompt2 | model | parser
result = sequential_chain.invoke({
    'topic' : 'indian cricket team',
    'n': 2
})
print(result)