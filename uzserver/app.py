from flask import Flask, render_template, request
import json

app = Flask(__name__)

with open('data/data.json', 'r', encoding='utf-8') as f:
    DATA = json.load(f)

@app.route('/', methods=['GET'])
def index():
    query = request.args.get('q', '').lower()
    results = []

    if query:
        results = [item for item in DATA if query in item['title'].lower() or query in item['desc'].lower()]

    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/suggest')
def suggest():
    q = request.args.get('q', '').lower()
    suggestions = [item['title'] for item in DATA if q in item['title'].lower()]
    return json.dumps(suggestions[:5])

with open('data/data.json', 'r', encoding='utf-8') as f:
    DATA = json.load(f)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

    from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Salom, bu Flask server!'

