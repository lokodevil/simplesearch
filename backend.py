from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
SERPAPI_KEY = '76778a3222ac5cab73dce162db4b80d16e5308a9cb0a5cec53851fc253ac3b54'

@app.route('/search')
def search():
    query = request.args.get('q')
    params = {
        'q': query,
        'api_key': SERPAPI_KEY,
        'engine': 'google'
    }
    response = requests.get('https://serpapi.com/search', params=params)
    data = response.json()
    results = [{
        'title': r['title'],
        'link': r['link'],
        'snippet': r['snippet']
    } for r in data.get('organic_results', [])]
    return jsonify(results)
