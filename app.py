from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Believe in yourself.",
    "Keep learning, keep growing.",
    "Small steps lead to big results.",
    "Never stop improving.",
    "Success comes from consistency."
    "Truth has no color, no religion, no nationality.",
    "The only way to do great work is to love what you do.",
]

@app.route("/")
def home():
    quote = random.choice(quotes)

    return f"""
    <html>
        <head>
            <title>Daily Quote</title>
        </head>
        <body>
            <h1>Hey there! Here's your daily dose of inspiration:</h1>
            <h1>🌟 Daily Quote</h1>
            <h2>"{quote}"</h2>
            <p>Have a great day ahead!</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

