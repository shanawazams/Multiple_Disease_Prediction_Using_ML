# -*- coding: utf-8 -*-
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import json
import requests
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time

# loading the saved models
diabetes_model = pickle.load(open('/Users/ahmedbinnayeem/Desktop/MultipleDiseasePredictionUsingStreamlit/saved models/diabetes_model.sav', 'rb'))



heart_disease_model = pickle.load(open('/Users/ahmedbinnayeem/Desktop/MultipleDiseasePredictionUsingStreamlit/saved models/heart_disease_model.sav','rb'))


brain_stroke_model = pickle.load(open('/Users/ahmedbinnayeem/Desktop/MultipleDiseasePredictionUsingStreamlit/saved models/stroke_model.sav', 'rb'))


kidney_model = pickle.load(open('/Users/ahmedbinnayeem/Desktop/MultipleDiseasePredictionUsingStreamlit/saved models/kidney_model.sav', 'rb'))



liver_model = pickle.load(open('/Users/ahmedbinnayeem/Desktop/MultipleDiseasePredictionUsingStreamlit/saved models/liver_model.sav', 'rb'))



parkinsons_model = pickle.load(open('/Users/ahmedbinnayeem/Desktop/MultipleDiseasePredictionUsingStreamlit/saved models/parkinsons_model.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction using Machine Learning',
                          
                          [   'Introduction',  
                              'Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Brain Stroke Prediction',
                           'Kidney Disease Prediction',
                           'Liver Disease Prediction', 
                           "Parkinson's Disease Prediction"],
                          icons=['','activity','heart','activity','person','activity','person'],
                          default_index= 0 )
 
st.sidebar.success("Select any diseases above for Prediction ")



# Introduction Page

if(selected == 'Introduction'):
    
    #page title
    st.title("Welcome to Multiple Disease Prediction System")
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url_hello = "https://assets1.lottiefiles.com/packages/lf20_ibbakwps.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, key="hello")



# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction')
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url_hello = "https://assets2.lottiefiles.com/packages/lf20_W6U9Osg3Pb.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, speed=1, reverse = False, loop = True, height = 250, width = 1000)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
    st.success(diab_diagnosis)
    
 
    
 
    
 
    
    
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Classification')
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url_hello = "https://assets2.lottiefiles.com/packages/lf20_txlsmlkc.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, speed=1, reverse = False, loop = True, height = 222, width = 1000)
    
    col1,col2,col3, col4 = st.columns(4)
    

    with col1:
        age = st.text_input('Age')
        
    with col2:    
        sex = st.text_input('Sex')
        
    with col3:    
        cp = st.text_input('Chest Pain types')
        
    with col4:    
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col1:    
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col2:    
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col3:    
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col4:    
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col1:    
        exang = st.text_input('Exercise Induced Angina')
        
    with col2:    
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col3:    
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col4:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    




# Brain Stroke Prediction Page
if (selected == 'Brain Stroke Prediction'):
    
    # page title
    st.title('Brain Stroke Prediction')
    
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_33asonmr.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, speed=1, reverse = False, loop = True, height = 222, width = 1000)
    
    
    col1,col2,col3, col4 = st.columns(4)
    
    
    with col1:
        gender = st.text_input('gender: "Male:0", "Female:1" or "Other:2"')
        
    with col2:
        age = st.text_input('Age')
    
    with col3:
        hypertension = st.text_input('hypertension -> 1 if the patient possess it & 0, if does not')
    
    with col4:    
        heart_disease = st.text_input('heart_disease-> 1 if heart disease & 0, if not')
    
    with col1:     
        ever_married = st.text_input('ever_married->Yes if 1, No if 0')
    
    with col2:    
        work_type = st.text_input('work_type->Private: 0, Self-employed:1, Govt_job:2, children:3, Never_worked:4')
        
    with col3:
        Residence_type = st.text_input('Residence_type-> Rural: 0, Urban:1')
        
    with col4:    
        avg_glucose_level = st.text_input('avg_glucose_level-> average glucose level in blood')
    
    with col1:       
        bmi = st.text_input('Body Mass Index')
        
    with col2:    
        smoking_status = st.text_input('smoking_status-> formerly smoked:0, never smoked:1, smokes:2 , Unknown:3')
    
 
    # code for Prediction
    stroke_diagnosis = ''

    # creating a button for Prediction

    if st.button('Brain Stroke Prediction Test Result'):
        stroke_prediction = brain_stroke_model.predict([[gender, age, hypertension, heart_disease, ever_married, work_type,Residence_type,avg_glucose_level,bmi,smoking_status]])                          
    
        if (stroke_prediction[0] == 1):
            stroke_diagnosis = 'The person is prone to brain stroke'
        else:
            stroke_diagnosis = 'The person is not prone to brain stroke'
    
    st.success(stroke_diagnosis)
    








# Kidney Disease Prediction Page
if (selected == 'Kidney Disease Prediction'):
    
    # page title
    st.title('Kidney Disease Prediction')
    
    
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url_hello = "https://assets10.lottiefiles.com/packages/lf20_xP3xRYyhLs.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, speed=1, reverse = False, loop = True, height = 208, width = 1100)
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        age = st.text_input('Age')
    
    with col2:
        blood_pressure = st.text_input('blood_pressure')
       
    with col3:    
        specific_gravity = st.text_input('specific_gravity')
        
    with col4:    
        albumin = st.text_input('albumin')    
        
    with col5:    
        sugar = st.text_input('sugar')
        
    with col6:    
        red_blood_cells = st.text_input('red_blood_cells')
        
    with col1:    
        pus_cell = st.text_input('pus_cell')
     
    with col2:    
        pus_cell_clumps = st.text_input('pus_cell_clumps')
        
    with col3:    
        bacteria = st.text_input('bacteria')
    
    with col4:    
        blood_glucose_random = st.text_input('blood_glucose_random')
        
    with col5:
        blood_urea = st.text_input('blood_urea')
        
    with col6:
        serum_creatinine = st.text_input('serum_creatinine')
        
    with col1:    
        sodium = st.text_input('sodium')
        
    with col2:    
        potassium = st.text_input('potassium')
        
    with col3:    
        haemoglobin = st.text_input('haemoglobin')
        
    with col4:    
        packed_cell_volume = st.text_input('packed_cell_volume')
        
    with col5:    
        white_blood_cell_count = st.text_input('white_blood_cell_count')
        
    with col6:    
        red_blood_cell_count = st.text_input('red_blood_cell_count')
        
    with col1:    
        hypertension = st.text_input('hypertension')
        
    with col2:    
        diabetes_mellitus = st.text_input('diabetes_mellitus')
        
    with col3:    
        coronary_artery_disease = st.text_input('coronary_artery_disease')
        
    with col4:    
        appetite = st.text_input('appetite')
       
    with col5:    
        peda_edema = st.text_input('peda_edema')
        
    with col6:    
        aanemia = st.text_input('aanemia')
 
 
    # code for Prediction
    kidney_diagnosis = ''

    # creating a button for Prediction

    if st.button('Kidney Disease Prediction Test Result'):
        kidney_prediction = kidney_model.predict([[age, blood_pressure, specific_gravity, albumin, sugar, red_blood_cells, pus_cell,
             pus_cell_clumps, bacteria, blood_glucose_random, blood_urea, serum_creatinine, sodium,
             potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count,
             hypertension, diabetes_mellitus, coronary_artery_disease, appetite, peda_edema,
             aanemia]])                          
    
        if (kidney_prediction[0] == 1):
            kidney_diagnosis = 'The person is diagnosed with kidney disease'
        else:
            kidney_diagnosis = 'The person is not diagnosed with kidney disease'
    
    st.success(kidney_diagnosis)









    
    
# Liver Disease Prediction Page
if (selected == 'Liver Disease Prediction'):
    
    # page title
    st.title('Liver Disease Prediction') 
    
    
        
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url_hello = "https://assets5.lottiefiles.com/packages/lf20_rsral8z3.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, speed=1.5, reverse = False, loop = True, height = 222, width = 1100)
    
    
        
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Age = st.text_input('Age')
        
    with col2:
        Gender = st.text_input('Gender')
    
    with col3:
        Total_Bilirubin = st.text_input('Total_Bilirubin')
    
    with col1:
        Direct_Bilirubin = st.text_input('Direct_Bilirubin')
    
    with col2:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')
    
    with col3:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')
    
    with col1:
        Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')
    
    with col2:
        Total_Protiens = st.text_input('Total_Protiens')
    
    with col3:
        Albumin = st.text_input('Albumin')
    
    with col1:
        Albumin_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')
    

    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Liver Test Result'):
        liver_prediction = liver_model.predict([[Age, Gender, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase, Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_Globulin_Ratio]])
        
        if (liver_prediction[0] == 1):
          liver_diagnosis = 'The person is suffering from liver disease'
        else:
          liver_diagnosis = 'The person is not suffering from liver disease'
        
    st.success(liver_diagnosis)










# Parkinsons Prediction Page
if (selected == "Parkinson's Disease Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction")  
    
            
    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    lottie_url_hello = "https://assets1.lottiefiles.com/packages/lf20_2ZKqKUm2Jm.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, speed=1.5, reverse = False, loop = True, height = 222, width = 1100)
    
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)  

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    
    with col6:
        RAP = st.text_input('MDVP:RAP')
    
    with col7:
        PPQ = st.text_input('MDVP:PPQ')
    
    with col1:
        DDP = st.text_input('Jitter:DDP')
    
    with col2:
        Shimmer = st.text_input('MDVP:Shimmer')
    
    with col3:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    with col4:
        APQ3 = st.text_input('Shimmer:APQ3')
    
    with col5:
        APQ5 = st.text_input('Shimmer:APQ5')
    
    with col6:
        APQ = st.text_input('MDVP:APQ')
    
    with col7:
        DDA = st.text_input('Shimmer:DDA')
    
    with col1:
        NHR = st.text_input('NHR')
    
    with col2:
        HNR = st.text_input('HNR')
    
    with col3:
        RPDE = st.text_input('RPDE')
        
    with col4:
        DFA = st.text_input('DFA')
    
    with col5:
        spread1 = st.text_input('spread1')
    
    with col6:
        spread2 = st.text_input('spread2')
    
    with col7:
        D2 = st.text_input('D2')
    
    with col1:
        PPE = st.text_input('PPE')
    


    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
    
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    
    st.success(parkinsons_diagnosis)
    