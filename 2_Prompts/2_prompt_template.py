from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

paper_name = str(input("Enter the title of the paper"))
style = str(input("Enter the style you want it in"))
length= str(input("Enter number of paragraphs you want"))

# template
template = PromptTemplate(
    template = "Explain about the paper titled: {paper_input}, in a very {style_input} tone and be it max {length_input} paragraphs, please state you donot know, if you cannot recognize the research paper, or esle explain about the most similar paper you know",
    input_variables=['paper_input', "style_input", 'length_input'],
    validation = True
)

model = ChatOpenAI(model="gpt-3.5-turbo", temperature = 0)
# prompt = template.format(
#     paper_input=paper_name,
#     style_input=style,
#     length_input= length
# )
# result = model.invoke(prompt)

# the above lines can be combined and written as

chain = template | model
result = chain.invoke({
    'paper_input': paper_name,
    'style_input':style,
    'length_input': length
})

print(result.content)