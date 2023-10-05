# File: app.py
from flask import Flask, request, jsonify
from autogen_container import AutoGenContainer
import logging

app = Flask(__name__)
container = AutoGenContainer('config.json')

@app.route('/input_chat', methods=['POST'])
def input_chat():
    chat_data = request.json
    agent_name, message = chat_data['agent_name'], chat_data['message']
    response = container.initiate_chat(agent_name, message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)