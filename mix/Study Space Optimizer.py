import openai
import os

""" 
IMPORTANT >>> pip install openai 1.1.0 or later for the code below to work <<<
!!! CODE FILES ARE AI GENERATED. REVIEW THEM BEFORE RUNNING THEM. MAKE SURE THEY WORK AS YOU INTEND THEM TO !!!
"""

openai.api_key = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY"

class GPTCall:
    def __init__(self):
        self.messages = [{'role': 'system', 'content': "You are a helpful assistant."}]

    def add_message(self, role, content):
        self.messages.append({'role': role, 'content': content})

    def get_gpt3_response(self, user_input):
        self.add_message('user', user_input)
        
        response = openai.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=self.messages,
            temperature=1,
            stream=True
        )

        responses = ""
        for chunk in response:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
                responses += str(chunk.choices[0].delta.content)

        self.add_message('assistant', responses)

        return responses

""" 
!!! CODE FILES ARE AI GENERATED. REVIEW THEM BEFORE RUNNING THEM. MAKE SURE THEY WORK AS YOU INTEND THEM TO !!!
"""

# App starts with printing the type of input expected from the user
print("Welcome to Study Space Optimizer! To help you create an effective study space, please describe your current study area and any challenges you face.")

# Main app loop to interact with the user
study_optimizer = GPTCall()
user_input = input("Describe your study space and challenges: ")

while True:
    response = study_optimizer.get_gpt3_response(user_input)
    
    # Following the response, dynamic interaction continues
    follow_up_question = input("
Would you like more suggestions or help with another aspect of your study space? (yes/no) ")
    if follow_up_question.lower() == 'yes':
        user_input = input("Please provide more details or specify another challenge: ")
    else:
        print("We hope your study space is now optimized for success! If you ever need more advice, we're here to help. Happy studying!")
        break