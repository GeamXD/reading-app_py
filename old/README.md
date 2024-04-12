**Reading Application with Streamlit**

Welcome to my reading application! This application utilizes Streamlit and various AI tools to enhance your reading experience. Here's a brief guide to get started:

### Installation

Before running the application, make sure you have Python installed on your system. Then, clone this repository and navigate to the project directory.

```bash
git clone <https://github.com/GeamXD/reading-app_py>
cd reading-app_py
```

Next, install the required dependencies using pip.

```bash
pip install -r requirements.txt
```

### Usage

To launch the application, run the following command in your terminal.

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can access the application through your web browser at the provided URL (usually http://localhost:8501).

### Features

1. **Text Extraction from Images:**
   - Our application utilizes the Claude3 Haiku model to extract text from images.
   - Simply upload an image containing text, and the extracted text will be displayed to you.

2. **Audio Recording and Transcription:**
   - You can record your voice saying something using the built-in audio recording feature.
   - The application transcribes your speech into text using either the OpenAI Whisper model or Fast Whisper.

3. **Text-to-Speech:**
   - Take the extracted text from Claude3 or your transcribed speech and convert it into audio.
   - We use the OpenAI Text-to-Speech model to generate the audio, which you can play directly on the page.

### How to Use

1. Upload an image containing text or use the audio recording feature to provide input.
2. Depending on the input, the application will process the text extraction or transcription.
3. Once the text is available, you can choose to convert it into audio.
4. Enjoy listening to the extracted or transcribed text as audio!

### Support and Feedback

If you encounter any issues or have suggestions for improvement, please feel free to open an issue on GitHub or reach out to us via email.

### Acknowledgments

This application makes use of the following AI models:
- Claude3 Haiku model for text extraction from images.
- OpenAI Whisper and Fast Whisper models for speech transcription.
- OpenAI Text-to-Speech model for generating audio from text.

### License
