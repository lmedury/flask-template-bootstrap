from flask import Flask, render_template
from routes.sentiment_analysis import sentiment_analysis_router

app = Flask(__name__)

app.register_blueprint(sentiment_analysis_router, url_prefix='/sentiment-analysis')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)