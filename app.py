from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    memes = [
        {"src": "images/meme1.jpg", "alt": "Meme 1", "link": "https://example1.com"},
        {"src": "images/meme2.jpg", "alt": "Meme 2", "link": "https://example2.com"},
    ]
    return render_template('index.html', memes=memes)

if __name__ == "__main__":
    app.run(debug=True)