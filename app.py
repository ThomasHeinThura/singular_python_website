from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/text_summarization')
def text_summarization():
    # Add code to activate Docker Compose for text summarization here
    return render_template('text_summarization.html')

@app.route('/stable_diffusion')
def stable_diffusion():
    return render_template('stable_diffusion.html')

@app.route('/etl')
def etl():
    return render_template('etl.html')

if __name__ == '__main__':
    app.run(debug=True)
