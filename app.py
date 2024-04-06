from flask import Flask, request
from langchain_openai import ChatOpenAI
import config

app = Flask(__name__)

@app.route('/')
def llm_chat():
    text_value = request.args.get('text', '')
    chat = ChatOpenAI(
                temperature=0.5,
                model=config.keys["model_name"],
                openai_api_key=config.keys["openai_api_key"],
            )
    response = chat.invoke(text_value)
    return response.content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
