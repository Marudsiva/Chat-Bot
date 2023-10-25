from flask import Flask, request, render_template
import openai

# Set your OpenAI API key
api_key = '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'
openai.api_key = api_key

app = Flask(__name__)

def chat_with_bot(user_input):
    # Use GPT-3 to generate a response
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct-0914",  # You can choose the appropriate engine
        prompt=f"You: {user_input}\nBot:",
        max_tokens=50
    )
    return response.choices[0].text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']
    if user_input.lower() == 'bye':
        bot_response = "Goodbye!"
    else:
        bot_response = chat_with_bot(user_input)
    return bot_response

if __name__ == '__main__':
    app.run(debug=True)
