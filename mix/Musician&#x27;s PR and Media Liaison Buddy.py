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

# Assuming GPTCall is already defined above and available for use
from datetime import datetime

# Initialize the PR and Media Liaison Buddy
gpt_pr_liaison = GPTCall()

# Customize the system message for our PR and Media Liaison application
gpt_pr_liaison.messages[0]['content'] = "You are a helpful assistant skilled in public relations and media interaction for musicians. Provide guidance for interviews, social media engagement, press release writing, and PR crisis management tailored to the needs of artists in the music industry."

def format_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def pr_assistant_intro():
    print("Hello! I'm your Musician's PR and Media Liaison Buddy.")
    print("How can I assist you today with your PR and media relations? You can ask for help with interviews, press releases, social media, or managing a PR crisis.")

def handle_user_interaction():
    while True:
        user_input = input("Your scenario (or type 'exit' to end): ")
        if user_input.lower() == 'exit':
            print("Thank you for using the Musician's PR and Media Liaison Buddy! Have a great day.")
            break

        response = gpt_pr_liaison.get_gpt3_response(user_input)
        print("
[{}] Assistant: {}".format(format_time(), response))
        print("Would you like more assistance on another topic?")

# Start the interaction with the user
pr_assistant_intro()
handle_user_interaction()