import pickle
import streamlit as st
import numpy as np
import json

# Load the trained model
with open('decision_tree_model.sav', 'rb') as model_file:
    common_model = pickle.load(model_file)

# Load the list of symptoms from the file
with open('Symptoms.txt', 'r') as symptoms_file:
    symptoms_list = json.load(symptoms_file)

# Set the layout of the Streamlit page
st.set_page_config(layout='wide')

# Sidebar for navigation
with st.sidebar:
    selected = st.selectbox('Multiple Disease Prediction System',
                            ['Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Parkinsons Prediction',
                             'Common diseases Prediction'])

# Common diseases prediction
if selected == 'Common diseases Prediction':
    st.title('Common Disease Prediction using ML')
    
    # Create input fields for symptoms dynamically
    symptoms_inputs = []
    for symptom in symptoms_list:
        symptom_input = st.checkbox(symptom)
        symptoms_inputs.append(symptom_input)

    common_diagnostics = ''

    if st.button('Common Disease Prediction'):
        # Create the input vector for the model
        ipt = [1 if symptom_checked else 0 for symptom_checked in symptoms_inputs]
        ipt = np.array([ipt])
        
        # Make predictions
        pred = common_model.predict(ipt)[0]
        prob = common_model.predict_proba(ipt)
        
        if any(ipt[0]):
            common_diagnostics = f"Person is predicted to have: {pred}"
        else:
            common_diagnostics = "Persons diseases cannot be classified by the model, please provide appropriate symptoms."

    st.success(common_diagnostics)
