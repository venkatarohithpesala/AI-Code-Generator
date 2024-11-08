# AI-Code-Generator

This project demonstrates how to use the OpenAI API to generate code based on user prompts. Currently, prompts can be sent via testing tools like Postman.

### Steps to Run the Project

1. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
2. **Set up your openAI API Key**:\
    * Place your OpenAI API key in a .env file with the following format:
    ```plaintext
    OPENAI_API_KEY=your_api_key_here
3. **Start the application**:
    ```bash
    python app.py
4. **Use postman to test the API**:
    * Open Postman, select a POST request, and enter the following URL:
    ```plaintext
    http://127.0.0.1:5000/generate_code
5. **Add your prompt in JSON Format**:
    * In the Body section, select raw and choose JSON format. Enter a JSON object with your prompt, such as:
    ```json
    {
    "prompt": "Write a Python function to add two numbers."
    }
6. **Click send** to receive the generated code in the response.

### Future plans

The goal is to develop a web interface where users can input prompts directly on the frontend, eliminating the need for external testing tools like Postman.
