from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.json or {}
        return f"POST data: {data}", 200
    return "Hello, GET request!", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)