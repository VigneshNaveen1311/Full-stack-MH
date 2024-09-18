from flask import Flask, render_template,request,jsonify
from bayes_fn import bayes_fn
app = Flask(__name__)
@app.route('/')
def index():
    return "hi bro from python<br>" + render_template('index.html')

@app.route('/bayes_page')
def bayes_page():
    return render_template('bayes.html')

@app.route('/calculate_bayes',methods = ['POST'])
def calculate_bayes():
    data = request.get_json()
    px = float(data['px'])
    py = float(data['py'])
    pxy = float(data['pxy'])
    pyx = float(data['pyx'])

    result,prob = bayespy(px,py,pxy,pyx)
    return jsonify({'bayes_result': result, 'prob': prob})

def bayespy(px,py,pxy,pyx):
    if px == 0:
        return bayes_fn(pxy,py,pyx),"Prior probability P(X): "
    elif py == 0:
        return bayes_fn(pyx,px,pxy),"Marginal Likelihood P(Y) : "
    elif pxy == 0:
        return bayes_fn(pyx,px,py),"Posterior probability P(X|Y) : "
    else:
        return bayes_fn(pxy,py,px),"Likelihood P(Y|X) : "

if __name__ == "__main__":
    app.run(debug = True) #set debug to false in production 