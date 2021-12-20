import streamlit as st
import random
st.title('Lets find out what you will eat today!')
list1=['aloo tamatar','chuda matar','aloo gobhi','panner ka paratha','paneer ki sabzi']
dish=random.sample(list1,k=1)
for i in dish:
    val=i
st.header('You are eating : '+val+' tonight!')
st.header('-------------------Bon Apetite!-------------------')
st.header('----------Reload for another choice------------')

