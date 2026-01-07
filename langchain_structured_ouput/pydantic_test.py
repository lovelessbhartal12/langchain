from pydantic import BaseModel , EmailStr ,Field

from typing import Optional


class student(BaseModel):
    name:str= 'lovelss'# default value
    age: Optional[int]=None #optinal value
    # email: EmailStr #validation
    cgpa:float =Field(gt=0 ,lt=10 , default=5 , description='this is the cgpa filed') 


new_student={'age':'21' ,'cgpa': 5} #course


student=student(**new_student)

print(student)
