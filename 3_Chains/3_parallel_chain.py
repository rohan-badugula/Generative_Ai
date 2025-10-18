from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv 

load_dotenv()

model1 = ChatOpenAI(model = "gpt-3.5-turbo")
model2 = ChatOpenAI(model = "gpt-3.5-turbo")

prompt1 = PromptTemplate(
    template = 'generate breif summary from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template= 'please make 5 short questions from the following text\n {text}', 
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template= "merge the provided notes and quiz into a single document \n notes: \n {notes} \n quiz: \n {quiz} ",
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2| parser
})

merge_chain = prompt3 | model1 | parser

final_chain = parallel_chain | merge_chain

text = """
Machine learning and data mining often employ the same methods and overlap significantly, but while machine learning focuses on prediction, based on known properties learned from the training data, data mining focuses on the discovery of (previously) unknown properties in the data (this is the analysis step of knowledge discovery in databases). Data mining uses many machine learning methods, but with different goals; on the other hand, machine learning also employs data mining methods as "unsupervised learning" or as a preprocessing step to improve learner accuracy. Much of the confusion between these two research communities (which do often have separate conferences and separate journals, ECML PKDD being a major exception) comes from the basic assumptions they work with: in machine learning, performance is usually evaluated with respect to the ability to reproduce known knowledge, while in knowledge discovery and data mining (KDD) the key task is the discovery of previously unknown knowledge. Evaluated with respect to known knowledge, an uninformed (unsupervised) method will easily be outperformed by other supervised methods, while in a typical KDD task, supervised methods cannot be used due to the unavailability of training data.

Machine learning also has intimate ties to optimisation: Many learning problems are formulated as minimisation of some loss function on a training set of examples. Loss functions express the discrepancy between the predictions of the model being trained and the actual problem instances (for example, in classification, one wants to assign a label to instances, and models are trained to correctly predict the preassigned labels of a set of examples).[36]
"""


result = final_chain.invoke(text)

print(result)

final_chain.get_graph().print_ascii()


