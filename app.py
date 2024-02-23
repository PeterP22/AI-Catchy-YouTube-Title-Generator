from flask import Flask, render_template, request, jsonify
import openai
from openai import OpenAI

# Initialize the Flask application
app = Flask(__name__)

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = 'your-api-key'
gpt_model = "gpt-4-1106-preview"
client = OpenAI(api_key=openai.api_key)


def generate_catchy_titles(youtube_title):
    response = client.chat.completions.create(
        model=gpt_model,
        temperature=0.7,
        messages=[
            {
                "role": "system",
                "content": "You are a cutting-edge AI trained in generating catchy YouTube titles. Generate several compelling and catchy titles for a YouTube video based on the following input."
            },
            {
                "role": "user",
                "content": youtube_title
            }
        ]
    )
    return response.choices[0].message.content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_titles', methods=['POST'])
def generate_titles():
    if request.method == 'POST':
        youtube_title = request.form['youtube_title']
        titles = generate_catchy_titles(youtube_title)
        return jsonify(titles)

if __name__ == '__main__':
    app.run(debug=True)