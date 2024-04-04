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

# App main flow
def main():
    welcome_message = "Welcome to Mind Master Memory Coach! I'm here to help improve your memory. "                      "For what type of information do you wish to enhance your memory today? (e.g., names, numbers, study material, speeches)"
    print(welcome_message)

    memory_coach = GPTCall()  # Assuming GPTCall class is defined elsewhere and injected here.
    memory_coach.messages.append({'role': 'system', 'content': "You are a memory coach trained to help users improve their memory. Provide techniques, exercises, and supportive feedback."})

    while True:
        user_input = input("Enter the type of information or 'exit' to stop:
")
        if user_input.lower() == 'exit':
            print("Thank you for using Mind Master Memory Coach. Keep practicing and see you soon!")
            break
        response = memory_coach.get_gpt3_response(user_input)
        
        print("

If you want to learn another memory technique or practice more, just tell me. Or type 'exit' if you're done for now.")

if __name__ == "__main__":
    main()