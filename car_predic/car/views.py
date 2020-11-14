from django.shortcuts import render
import jsonify
import requests
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
import joblib


from django.shortcuts import render 
model=joblib.load('./models/model_joblib')
  
# Create your views here. 
def Home(request):
    return render(request, 'index.html')



# model = pickle.load(open('random_forest_regression_model2.pkl', 'rb'))

def Home(request):  
    return render(request, "index.html") 

standard_to = StandardScaler()

def predict(request):
    Fuel_Type_Diesel=0
    if request.method == 'POST':
     
        Year=int(request.POST.get('Year'))
        Present_Price=float(request.POST.get('Present_Price'))
        Kms_Driven=int(request.POST.get('Kms_Driven'))
        Kms_Driven2=np.log(Kms_Driven)
        Owner=int(request.POST.get('Owner'))
        Fuel_Type_Petrol=request.POST.get('Fuel_Type_Petrol')
        if(Fuel_Type_Petrol=='Petrol'):
                Fuel_Type_Petrol=1
                Fuel_Type_Diesel=0
        else:
            Fuel_Type_Petrol=0
            Fuel_Type_Diesel=1
        Year=2020-Year
        Seller_Type_Individual=request.POST.get('Seller_Type_Individual')
        if(Seller_Type_Individual=='Individual'):
            Seller_Type_Individual=1
        else:
            Seller_Type_Individual=0	
        Transmission_Mannual=request.POST.get('Transmission_Mannual')
        if(Transmission_Mannual=='Mannual'):
            Transmission_Mannual=1
        else:
            Transmission_Mannual=0
        prediction=model.predict([[Present_Price,Kms_Driven2,Owner,Year,Fuel_Type_Diesel,Fuel_Type_Petrol,Seller_Type_Individual,Transmission_Mannual]])
        output=round(prediction[0],2)

        if output<0:
            context={'prediction_texts':"Sorry you cannot sell this car"}
            return render(request,'result.html',context=context)
        else:
            context={'prediction_texts':"You Can Sell The Car at {}".format(output)}

            return render(request,'result.html',context=context)
    else:
        return render('index.html')




    