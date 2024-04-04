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

# Assume the GPTCall class is already imported above this code snippet

# Create an instance of the GPTCall class
gpt_study_buddy = GPTCall()

# Adding system message to guide GPT on the app's purpose and capabilities
gpt_study_buddy.messages[0]['content'] = """
You are a GPT-powered Smart Study Buddy designed to assist users in their studies by providing
targeted information and creating learning materials on various subjects. Your capabilities include 
generating explanations, quizzes, summary notes, and answering questions. Be informative, concise, 
and engaging to facilitate a productive learning experience.
"""

# Starting conversation with the user
print("Welcome to GPT Smart Study Buddy! Please enter the subject or topic you need help with:")

while True:
    # Get user's input on topic or question they need help with
    user_topic = input("Enter a subject, topic, or question: ")
    
    # Add user's topic to the messages and ask for preferred mode of assistance
    gpt_study_buddy.add_message('user', user_topic)
    modes = ["Explanation", "Quiz", "Summary Notes", "Q&A"]
    print("
How would you like to learn about '{}'? Please choose from the following:
- {}".format(
        user_topic, "
- ".join(modes)))
    user_mode = input("Enter your choice: ")
    gpt_study_buddy.add_message('user', user_mode)
    
    # GPT provides the requested help
    gpt_response = gpt_study_buddy.get_gpt3_response(user_mode)
    
    # Secondary interaction: checking if the user needs further assistance
    print("
Do you need assistance with another topic or have more questions on this one? (yes/no)")
    user_decision = input()
    gpt_study_buddy.add_message('user', user_decision)
    
    # If the user says no, we end the conversation
    if user_decision.strip().lower() == 'no':
        print("Great job studying today! Remember, consistent effort leads to remarkable progress. Goodbye!")
        break