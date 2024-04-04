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

# Begin the application loop
print("Welcome to Exam Ace! I'll help you craft the perfect study plan for your upcoming exams!")
while True:
    user_input = input("To get started, could you tell me which exam you're studying for and when it is? (Type 'exit' to end) ")
    if user_input.lower() == 'exit':
        print("Thank you for using Exam Ace! Good luck with your studies.")
        break
    
    # Instantiate the GPTCall class
    gpt_instance = GPTCall()
    
    # Customize the system message based on the app's logic flow
    gpt_instance.messages[0]['content'] = "You are a helpful assistant designed to help users create a personalized study plan and offer strategic advice for preparing for exams. Help the user by generating a study schedule, suggesting effective study techniques, and providing motivational messages if needed."

    # Pass the user input to the GPT instance and get the tailored advice
    response = gpt_instance.get_gpt3_response(user_input)

    # Depending on the conversation, implement a flow that talks about study habits, preferences, and offer to create a study schedule or give tips.
    additional_input = input("
Would you like to receive study tips, create a study schedule, or learn about focus techniques? (Type 'tips', 'schedule', or 'focus', or 'exit') ")
    
    if additional_input == 'exit':
        print("Thank you for using Exam Ace! Good luck with your studies.")
        break

    gpt_instance.get_gpt3_response(additional_input)

    # Offer motivational support and ask if they want to enable daily check-ins
    additional_input = input("
How are you feeling about your studies? If you need a motivational boost or want to set up daily check-ins for accountability, just let me know! (Type your feelings or 'exit') ")
    
    if additional_input == 'exit':
        print("Thank you for using Exam Ace! Good luck with your studies.")
        break

    gpt_instance.get_gpt3_response(additional_input)