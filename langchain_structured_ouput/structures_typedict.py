from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict , Annotated , Optional ,Literal
load_dotenv()

model=ChatOpenAI()

#schema

class Review(TypedDict):
    summary: Annotated[str,"a brief summary of review"]
    sentiment:Annotated[str,"return a sentiment of the review either positve ,negative and neutral"]

structed_model=model.with_structured_output(Review)

result=structed_model.invoke("""this hardwarwe is great, but the software feels bloated.there are too many pre-installed apps that i cant remove .Also , the ui looks outdated""")

