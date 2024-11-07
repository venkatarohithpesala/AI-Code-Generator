import os
import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# calling the function to load the variables from the .env file
load_dotenv()

#Intializing the flask app
app = Flask(__name__)

# setting the openai api key 
openai.api_key = os.getenv("OPENAI_API_KEY")

#Route to generate the code
@app.route("/generate_code", methods=['post'])
def generate_code():
    # Get the user request
    data = request.get_json()
    prompt = data.get("prompt")

    #call the openai API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes code."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=100,
        temperature=0.2
    )

    generated_code = response['choices'][0]['message']['content'].strip()
    return jsonify({"code":generated_code})

if __name__ == "__main__":
    app.run(debug=True)

