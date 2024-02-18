# Flask Text-to-Speech Web Application

This is a simple web application implemented using Flask, a Python web framework. The application allows users to input text, which is then converted to speech using the Text-to-Speech (TTS) functionality.

## Features
- Web interface for inputting text.
- Text-to-Speech functionality to convert the input text into speech.
- Ability to adjust the speech rate.

## Requirements
- Python 3.x
- Flask library
- pyttsx3 library

## How to Run
1. Ensure you have Python installed on your system.
2. Install the required libraries using pip:
   ```
   pip install flask pyttsx3
   ```
3. Clone or download this repository to your local machine.
4. Navigate to the project directory in a terminal or command prompt.
5. Run the following command to start the Flask server:
   ```
   python app.py
   ```
6. Open a web browser and go to `http://localhost:5000` to access the application.
7. Enter text in the provided input field and click the "Speak" button to hear the text spoken aloud.

## Adjusting Speech Rate
- You can adjust the speech rate by modifying the value of the `rate` property in the `TextToSpeech` function.

## How It Works
- The main route `/` renders the `index.html` template, which provides the web interface for inputting text.
- When the user submits the form, the text is sent to the `/speak` route via a POST request.
- The `/speak` route retrieves the text from the request, converts it to speech using the `TextToSpeech` function, and then redirects back to the main page.

Feel free to customize and extend this project according to your needs. Thank you for using the Flask Text-to-Speech Web Application!