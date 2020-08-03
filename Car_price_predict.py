# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:34:15 2020

@author: MYPC
"""
man=None
from flask import Flask,request,render_template
import joblib
from datetime import date
app=Flask(__name__)

@app.route("/predict_car_price",methods=['GET','POST'])
def predict_car_price():
    km=int(request.form['one'])
    yr=int(request.form['two'])
    fuel_t=request.form['three']
    seller_t=request.form['four']
    trans_t=request.form['five']
    owner_t=request.form['six']
    yr=date.today().year-yr
    fuel_dict={'Diesel':0,'Electric':0,'LPG':0,'Petrol':0}
    for k,v in fuel_dict.items():
        if fuel_t in k:
            fuel_dict[k]=1
    seller_dict={'Individual':0,'Trustmark Dealer':0}
    for k,v in seller_dict.items():
        if seller_t in k:
            seller_dict[k]=1
    global man
    if trans_t=='Manual':
        man=1
            
    owner_dict={'Second Owner':0,'Fourth & Above Owner':0,'Third Owner':0,'Test Drive Car':0}
    for k,v in owner_dict.items():
        if owner_t in k:
            owner_dict[k]=1
    f1,f2,f3,f4=tuple(fuel_dict.values())
    s1,s2=tuple(seller_dict.values())
    o1,o2,o3,o4=tuple(owner_dict.values())
    load_model=joblib.load(open("F:/Carprice/car_price_pred_final_model.pkl",'rb'))
    result=str(round(load_model.predict([[km,yr,f1,f2,f3,f4,s1,s2,man,o1,o2,o3,o4]])[0],2))
    return render_template('predict_car_price.html', price='{} lakhs '.format(result))
        
if __name__=="__main__":
    app.run()
    