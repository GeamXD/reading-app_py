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

# The setup message explaining the purpose and function of the app to GPT
gpt_call = GPTCall()
gpt_call.messages = [
    {
        'role': 'system',
        'content': (
            "You are a knowledgeable literary assistant specialized in identifying and explaining literary devices. "
            "When given a piece of text by a user, you will analyze it and provide a clear explanation of any literary devices found within the text. "
            "Your explanations should include the name of the device, a definition, and how it is used in the provided context to enhance meaning."
        )
    },
    {
        'role': 'system',
        'content': "If no literary devices are found, kindly explain that to the user and offer to analyze another piece of text."
    }
]


def run_literary_device_decoder():
    print("Welcome to the Literary Device Decoder!")
    print("Paste a sentence or a paragraph from a text, and I'll identify and explain any literary devices present.")
    
    while True:
        user_input = input("Enter your text (or type 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Thank you for using the Literary Device Decoder. Goodbye!")
            break

        response = gpt_call.get_gpt3_response(user_input)
        print(response)


if __name__ == "__main__":
    run_literary_device_decoder()