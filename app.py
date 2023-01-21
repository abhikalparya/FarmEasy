from pickle4 import pickle
import numpy as np
from flask import Flask,request,render_template
import sklearn
from sklearn.model_selection import RandomizedSearchCV
from data import *
import weather

global cropfinal

app=Flask(__name__)


@app.route('/')
def home():
    return render_template('landing.html')

@app.route('/form', methods=["GET","POST"])
def form():
    state = request.form.get('state')
    district = request.form.get('district')
    la = weather.temp(state)
    rain = int(la[0][0])
    temp = int(la[1][0])
    humd = int(la[2][0])
    #print(rain,temp,humd)
    return render_template("form.html", rain = rain, humd = humd, temp = temp)


@app.route('/recommend',methods=['POST'])
def recommend():
    if request.method=='POST':
        N=request.form.get("N")
        P=request.form.get("P")
        K=request.form.get("K")
        temperature=request.form.get("Temp")
        humidity=request.form.get("Humd")
        PH=request.form.get("Ph")
        rainfall=request.form.get("rnfall")
        #print(N,P,K,temperature,humidity,PH,rainfall)
        new_input=[[N,P,K,temperature,humidity,PH,rainfall]]
        model = pickle.load(open('model/model.pkl','rb'))
        new_input = np.asarray(new_input).astype(np.float32)
        new_output=model.predict(new_input)
        crop=int(new_output[0])
        crop_idx={20:'RICE',11:'MAIZE',3:'CHICKPEA',9:'KIDNEYBEANS',18:'PIGEONPEAS',13:'MOTHBEANS',14:'MUNGBEAN',2:'BLACKGRAM',10:'LENTIL',19:'POMEGRANATE'
                 ,1:'BANANA',12:'MANGO',7:'GRAPES',21:'WATERMELON',15:'MUSKMELON',0:'APPLE',16:'ORANGE',17:'PAPAYA',4:'COCONUT',6:'COTTON',8:'JUTE',5:'COFFEE'}
        crop=crop_idx[crop]
        filename = "static/images/" + crop + ".png"
        crop1 = crop.lower()
        a = eval(crop1)
        description = a["DESCRIPTION"]
        types = a["TYPE"]
        disease = a["DISEASES"]
        companion = a["COMPANION"]
        pests = a["PESTS"]
        fertilizer = a["FERTILIZER"]
        tips = a["TIPS"]
        spacing = a["SPACING"]
        watering = a["WATERING"]
        storage = a["STORAGE"]
        return render_template("output.html",crop=crop,filename=filename, description=description,types=types,disease=disease,
        companion=companion,pests=pests,fertilizer=fertilizer,tips=tips,spacing=spacing,watering=watering,storage=storage)
    else:
        return render_template("landing.html")

@app.route('/home')
def retry():
    return render_template('landing.html')

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)

