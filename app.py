from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return "hi bro from python<br>" + render_template('index.html')

@app.route('/bayes')
def bayes():
    return render_template('bayes.html')

# def bayespy():
#     if dx == 0:
        

if __name__ == "__main__":
    app.run(debug = True) #set debug to false in production 