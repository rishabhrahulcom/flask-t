from flask import Flask
from langchain_community.llms import Ollama

app = Flask(__name__)
llm = Ollama(model="codellama")

@app.route('/')
def hello_world():  # put application's code here

    return "hello"


if __name__ == '__main__':
    app.run()
