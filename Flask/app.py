from flask import Flask,request,render_template
import numpy as np
import pandas as pd
import pickle
import os

app=Flask(__name__)

with open(r'E:/creditcard/Flask/model.pkl','rb') as handle:
    model=pickle.load(handle)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Prediction',methods=['POST','GET'])
def prediction():
    return render_template('index1.html')

@app.route('/predict',methods=["POST","GET"])
def predict():
    input_feature=[int(x) for x in request.form.values() ]
    feature_values=[np.array(input_feature)]
    feature_name=['gen','car','estate','annualin','intype','edu','marital','housetype','Dbirth','DEmployed','Fam_mem','paid_off','pastdue','no_loan']
    x=pd.DataFrame(feature_values,columns=feature_name)

    pred=model.predict(x)

    if(pred==0):
        prediction="Eligible"
    else:
        prediction="Not Eligible"
    
    return render_template("result.html",prediction=prediction)

if __name__ =="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=False,use_reloader=False)