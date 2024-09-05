from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')

def index():
    return "hi bro<br>" + render_template('index.html')

if __name__ == "__main__":
    app.run(debug = True) #set debug to false in production 