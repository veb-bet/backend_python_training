from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

users = []

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello')
def hello():
    return render_template('index.html')

@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            users.append(name)
            return f"Name added: {name}"
    return render_template('add_name.html')

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)