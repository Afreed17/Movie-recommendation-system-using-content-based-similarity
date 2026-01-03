#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 00:46:45 2026

@author: latheefkummath
"""

import pandas as pd 
import joblib 



# Importing Necessary DataFrames and Model dumps from the dumps folder 

data = pd.read_csv('/Users/latheefkummath/Desktop/DATASCIENCE PROJECTS/Project3  - Movie Recomendation System/Object_dumps/movie_data_for_app.csv')
data_frame = pd.read_csv('/Users/latheefkummath/Desktop/DATASCIENCE PROJECTS/Project3  - Movie Recomendation System/Object_dumps/movie_dataFrame_for_app.csv')

tfv = joblib.load('/Users/latheefkummath/Desktop/DATASCIENCE PROJECTS/Project3  - Movie Recomendation System/Object_dumps/tfidf_vectorizer.pkl')
sig = joblib.load('/Users/latheefkummath/Desktop/DATASCIENCE PROJECTS/Project3  - Movie Recomendation System/Object_dumps/sigmoid_kernel.pkl')


def give_recommendation(data ,dataFrame , movie_title , model ):
    
    indices = pd.Series( data = data.index , index = data['original_title'] )
    idx = indices[movie_title]

    model_scores = list(enumerate(model[idx]))
    model_score_sorted = sorted(model_scores , key = lambda x : x[1] ,reverse = True)

    model_score_10 = model_score_sorted[1:11]

    movie_indices_10 = [i[0]for i in model_score_10]
    
    return dataFrame['original_title'][movie_indices_10]



#Creating Frontend using Streamlit

import streamlit as st

st.set_page_config(page_title = 'Simple Movie Reccomender ' , layout = 'centered')
st.title('🎬 Simple Movie Reccomender ')
st.write('Find movies similar to your fav one !')

movie_list = data['original_title'].sort_values().tolist()
selected_movie = st.selectbox('Select a Movie :' , movie_list)

if st.button('Get Recommendations'):
    if selected_movie:
        recomendations = give_recommendation(data, data_frame, selected_movie , sig)
        
        st.subheader('Movies similar to ' + selected_movie)
        for index , movie in enumerate(recomendations) : 
            st.write(str(index + 1) + '.' + movie)
            
st.markdown('------')
st.markdown('This app uses content based filtering.')
        















