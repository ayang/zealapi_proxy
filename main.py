from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/d/<path:text>")
def proxy(text):
    resp = requests.get(f'https://go.zealdocs.org/d/{text}', allow_redirects=False)
    url = resp.headers['Location']
    url = url.replace('tokyo.kapeli.com', 'sanfrancisco.kapeli.com')
    print(url)
    return redirect(url)
