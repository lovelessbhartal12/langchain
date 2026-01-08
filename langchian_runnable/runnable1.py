import math
class naklillm():
    def __init__(self):
      print('llm created')

    def predict(self ,prompts):
       response_lost=[
          'ktm is the capital of nepal',
          'NPL is the nepal premeier league',
          'loveless is a person'

       ]
       return {'response':math.random(response_lost)}
    


llm=naklillm()

llm.predict('what is the capital of nepal')
    
       