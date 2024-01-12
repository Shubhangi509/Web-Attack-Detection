# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 15:07:55 2023

@author: Shubh
"""
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


#Loading the model
url_model = pickle.load(open("C:/Users/Shubh/OneDrive/Desktop/My projects/web attack detection - mini project sem 5/files/URL/url_attack.sav", "rb"))

xss_model = pickle.load(open("C:/Users/Shubh/OneDrive/Desktop/My projects/web attack detection - mini project sem 5/files/XSS/xss_attack.sav", "rb"))

import pandas as pd
df = pd.read_excel("C:/Users/Shubh/OneDrive/Desktop/My projects/web attack detection - mini project sem 5/files/XSS/XSS_dataset.xlsx")
encoded_df = pd.read_csv("C:/Users/Shubh/OneDrive/Desktop/My projects/web attack detection - mini project sem 5/files/XSS/new.csv")

# from xss_attack import maps

#creating sidebars for navigation
with st.sidebar:
    
    selected = option_menu('Web Attack Detection System',
                           ['URL Attack', 'XSS Attack'],
                           default_index = 0)
   
#streamlit run "C:\Users\Shubh\OneDrive\Desktop\My projects\web attack detection - mini projestreamlit run "C:\Users\Shubh\OneDrive\Desktop\My projects\web attack detection - mini project sem 5\files\webAttack.py"ct sem 5\files\webAttack.py"

if(selected == 'URL Attack'):
    st.title("URL Attack detection")
    st.text("Please enter the following information for URL Attack Detection:")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        url_length = st.number_input('URL Length')
        number_special_characters = st.number_input('Number of special characters')
        content_length = st.number_input('Content length')
        tcp_conversation_exchange = st.number_input('TCP conversation exchange')
    with col2:
        dist_remote_tcp_port = st.number_input('Dist remote TCP port')
        remote_ips = st.number_input('remote ips')
        app_bytes = st.number_input('app bytes')

    with col3:
        source_app_packets = st.number_input('source_app_packets')
        remote_app_packets = st.number_input('remote_app_packets')
        source_app_bytes = st.number_input('source_app_bytes')
    with col4:
        remote_app_bytes = st.number_input('remote_app_bytes')
        app_packets = st.number_input('app_packets')
        dns_query_times = st.number_input('dns_query_times')

    url_pred = ''
    
    if st.button('URL Attack?'):
        #format necessary for scikit-learn
        pred = url_model.predict([[url_length, number_special_characters, content_length, tcp_conversation_exchange, dist_remote_tcp_port, remote_ips, app_bytes, source_app_packets, remote_app_packets, source_app_bytes, remote_app_bytes, app_packets, dns_query_times]])
        
        if pred[0] == 0.0:
            url_pred = 'Url attack on the website.'
        else:
            url_pred = 'No Url attack on the website.'
    
    st.success(url_pred)

       
   
if(selected == 'XSS Attack'):
    st.title("XSS Attack detection")

    st.text("Please enter the following information for XSS Attack Detection:")
    
    col1, col2, col3 = st.columns(3)
        
    
    with col1:
        app_name = st.text_input('App Names')
        website_name = st.text_input('Website Name')

    with col2:
        permission = st.text_input('Permissions')
        IP_address = st.text_input('IP')

    with col3:
        api_name = st.text_input('API Name')
        location = st.text_input('Location')

    ip_data = [app_name, permission, api_name, website_name, IP_address, location]
    ip_col = ['App Names', 'Permissions', 'API Name', 'Website Name', 'IP', 'Location']
    
    encoded_data = []
    i = 0
    for data in ip_data:
        col = ip_col[i]
        #val = maps[i][data]
        rows = df.index[df[col] == data].tolist()
        row = 0
        if(len(rows) != 0):
            row = rows[0]
        val = encoded_df.loc[row, col]
        encoded_data.append(val)
        i = i + 1
    
    
    xss_pred = ''
    
    if st.button('XSS Attack?'):
        #format necessary for scikit-learn
        pred = xss_model.predict([encoded_data])
        
        if pred[0] == 0.0:
            xss_pred = 'XSS attack on the website.'
        else:
            xss_pred = 'No XSS attack on the website.'
    
    st.success(xss_pred)

