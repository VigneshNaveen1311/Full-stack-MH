from flask import Flask, render_template,request,jsonify, url_for,redirect
from bayes_fn import bayes_fn
import os
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return "hi bro from python<br>" + render_template('index.html')

@app.route('/bayes_page')
def bayes_page():
    return render_template('bayes.html')

@app.route('/product_finder_page')
def product_finder_page():
    return render_template('productfinder.html')

@app.route('/productfind', methods = ['POST'])
def product_find():
    if 'image' not in request.files:
        return 'No file part'
    
    file  = request.files['image']

    if file.filename == '':
        return 'No selected file'
    
    if file:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
        file.save(file_path)
        return redirect(url_for('display_image',filename = file.filename))
    
@app.route('/uploads/<filename>')
def display_image(filename):
    return render_template('display_image.html', filename=filename)

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