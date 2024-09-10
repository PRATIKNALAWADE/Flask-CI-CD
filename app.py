# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []
#comment
@app.route('/todos', methods=['GET', 'POST'])
def manage_todos():
    if request.method == 'POST':
        todo = request.json.get('todo')
        todos.append(todo)
        return jsonify({'message': 'Todo added!'}), 201
    return jsonify({'todos': todos})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

