
from flask import Flask, request,render_template
app = Flask(__name__)
import joblib,pickle
import numpy as np
app = Flask(__name__)
ct= joblib.load("cred")
model = pickle.load(open("modelcredit.pkl","rb"))

@app.route('/') # rendering the html template
def home():
    return render_template('index.html')

@app.route('/predict')
def prediction():
    return render_template('index1.html')

@app.route('/out', methods=['POST']) # route for our prediction
def data_predict():
    
    x_test = [[(x) for x in request.form.values()]] 
    #x_test = np.array(x_test)
    #x_test=ct.transform(x_test)
    pred= model.predict(x_test)
    #print(pred)
    if pred[0]==0:
        prediction="Not Eligible"
    else:
        prediction="Eligible"
    
    return render_template("result.html", predictiont=prediction)

if __name__ == '__main__':
    app.run(debug=True)