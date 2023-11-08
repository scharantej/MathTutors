 
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/tutors')
def tutors():
    return render_template('tutors.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run()
