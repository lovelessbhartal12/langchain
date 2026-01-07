from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, load_prompt
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI(model='gpt-4-3-user' , temperature=0.5)

import streamlit  as st
st.header('Research tool')
paper_input=st.selectbox("select research paper name", ["attention is all you need", "BERT:pretraining of deep bidirectional transformer","gtp3:language model are few short learners","diffusion models beats gan on image synthesis"])
style_input=st.selectbox("select the explanation style", ["beginner-friendly","technical ","code oriented","mathematical"])

lenght_input=st.selectbox("select the explanation lenght ", ["short(1-2)" ,"medium(3-5 paragraph) ","large(detailes explanation)"])

#template

template=load_prompt('template.json')
#fill the placeholder

# prompt=template.invoke({
#     'paper_input':paper_input,
#     'style_input':style_input,
#     'length_input':lenght_input

# })

if st.button('summarize '):
    chain=template | model

    result=chain.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':lenght_input

})
st.write(result.content)

        