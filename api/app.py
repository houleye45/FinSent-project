from flask import Flask
from routes.stock import stock_bp
from routes.news import news_bp
from routes.events import events_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(stock_bp, url_prefix='/stocks')
app.register_blueprint(news_bp, url_prefix='/news')
app.register_blueprint(events_bp, url_prefix='/events')

@app.route('/')
def home():
    return """
    <html>
    <head>
        <title>FinSent API</title>
        <link rel="stylesheet" href="/static/style.css">
    </head>
    <body>
        <h1>FinSent Financial Sentiment API</h1>
        <p>Available endpoints:</p>
        <ul>
            <li>/stocks → list of stock records</li>
            <li>/stocks/&lt;date&gt; → stock data by date</li>
            <li>/news → list of news articles</li>
            <li>/news/&lt;id&gt; → single news article</li>
            <li>/events → list of events</li>
            <li>/events/&lt;id&gt; → single event</li>
        </ul>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True, port=5001)
