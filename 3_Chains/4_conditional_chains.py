from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
# from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

class Sentiment(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description= 'Give the sentiment of the feedback')


model = ChatOpenAI(model = "gpt-3.5-turbo").with_structured_output(Sentiment)
model2 = ChatOpenAI(model = "gpt-3.5-turbo")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "classify the following feedback as positive or negative \n feedback: {feedback}",
    input_variables= ['feedback']
)

prompt2 = PromptTemplate(
    template = "Appriciate the positive feedback and explain them, saying thankyou for reaching out and expressing this: \n feedback: {feedback}",
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template="Express sorry and dissatisfaction for thier negative feedback, ensure them that we are with them and will get this resolved, and mention we are directing them to dedicated team \n feedback: {feedback}",
    input_variables=['feedback']
)

classifier_chain = prompt1 | model 

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model2 | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model2 | parser),
    RunnableLambda(lambda x: "Sorry trouble to identify the issue")
)

final_chain = classifier_chain | branch_chain
result = final_chain.invoke({"feedback":"This is a Awesome phone, I need my refund rightaway! "})
print(result)

final_chain.get_graph().print_ascii()