from langchain_openai import OpenAI
from typing import TypedDict , Annotated ,Optional 
from pydantic import BaseModel ,Field
from  dotenv import load_dotenv

load_dotenv()
model=OpenAI()

structed_model=model.with_structured_output()

result=structed_model.invoke()