#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:30:22 2020

@author: kavish
"""

#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pickle
import numpy as np
regressor=pickle.load(open('model.pkl','rb'))


def predict_marks(hours):
    input=np.array([[hours]]).astype(np.float64)
    prediction=regressor.predict(input)
    pred='{0:.{1}f}'.format(prediction[0][0], 2)
    return float(pred)

def main():
    st.title("Marks Obtained on the basis of hours studied")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Marks Obtained</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    hours = st.text_input("Hours Studied","Type Here")

    if st.button("Predict"):
        output=predict_marks(hours)
        st.success('The marks obtained are {}'.format(output))

if __name__=='__main__':
    main()


# In[ ]:



