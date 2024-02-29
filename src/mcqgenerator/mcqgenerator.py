# Import all the required dependicies
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain.callbacks import get_openai_callback
import os
import json
import pandas as pd
import traceback
from dotenv import load_dotenv
import PyPDF2

# Load the API Key
key=os.getenv("OPENAI_API_KEY")

# Load the Chat API model
llm=ChatOpenAI(openai_api_key=key, model_name="gpt-3.5-turbo", temperature=0.7)

# Opem=n the input file in read mode
with open("E:\Generative_AI\MCQ_Generator\Response.json","r")as f:
    RESPONSE_JSON=json.load(f)

# Tempelate to generate the MCQ questions
TEMPLATE='''
Text:{text}
You are anexpert MCQ maker. Given the above text, it is your job to \
create a quiz of {number} multiple choice questions for {subject} student in {tone}
Make sure the questions are non repeated and check all the questions to be conforming
Make sure to format your response like RESPONSE_JASON below and use it as a guide.
Ensure to make {number} MCQs
### RESPONSE_JASON
{response_json}
'''

# Pass the above template to prompt template
quiz_generator_prompt=PromptTemplate(
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    template=TEMPLATE
)

# Create the model using above template to generate questions for given text in JSON format
quiz_chain=LLMChain(llm=llm, prompt=quiz_generator_prompt, output_key='quiz', verbose=True)

# Create another model to review the above questions
TEMPLATE2='''
You are an expert emglish grammarian and writer. Given a multiple choice quiz for {subject} students.\
You need to evaluate the complexity of the questiob and give a complete analysis of the quiz. Only use at max 50words for complexity analysis.
if the quiz is not as per with the cognitive and analytical abalities of the students,\
update the quiz questions which need to be changed and change the tone such that it perfectly fit the student abilities
Quiz_MCQ:
{quiz}

Check from an expert English Writer of the above quiz:
'''
quiz_evaluation_prompt=PromptTemplate(input_variables=["subject", "quiz"],template=TEMPLATE2)

review_chain=LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key='review', verbose=True)

# Creating a sequential chain to combine the both models
generate_evaluation_chain=SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=['text', 'number', 'subject', 'tone', 'response_json'],
    output_variables=['quiz','review'],
    verbose=True
    )
