#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 14:20:49 2020

@author: kavish
"""

import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

pickle_in = open("model.pkl","rb")
regressor=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_score(study_hours):
    
    """Let's predict the score. 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: study_hours
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output value
        
    """
   
    prediction=regressor.predict([[study_hours]])
    print(prediction)
    return prediction

def main():
    st.title("Score Predictor")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    study_hours = st.text_input("Study_hours","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_score(study_hours)
    st.success('The score is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()