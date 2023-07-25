import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from streamlit_option_menu import option_menu

df=pd.read_csv('E:/Excel files/user_purchase_rating.csv')
st.title('Shopping Details:')

with st.sidebar:
    select = option_menu(
                    menu_title=None,
                    options=["Product viewed", "Added to cart", "Checkout made", "Purchased", "Summary"],
                    icons=["eye", "cart", "check", "bag", "list" ]#, orientation ="horizontal"  
                    )

if not select == "Summary":
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        mi=st.button("Minimum")
    with col2:
        mx=st.button("Maximum")
    with col3:
        z=st.button("Zeros")
    with col4:
        nz=st.button("Non_Zeros")
    with col5:   
        c=st.button("Counts") 

def calculate():
    if mi:
        st.subheader("The minimum value is:")
        st.subheader(df[column].min())
    elif mx:
        st.subheader("The maximum value is:")
        st.subheader(df[column].max())
    elif z:
        st.subheader("The Number of Zero value is:")
        st.subheader(df[column][df[column ]== 0].count())    
    elif nz:
        st.subheader("The Number of Non_Zero value is:")
        st.subheader(df[column][df[column ]!= 0].count())   
    elif c:
        col1,col2=st.columns(2)
        with col1:
            st.subheader("Each Value Counts:")
            st.write(df.groupby(column).size())
            #st.write(df[column].value_counts().sort_index())
        with col2: 
            st.subheader(f"Distribution Of {column}:")
            a=df[column].value_counts().sort_index()#.reset_index(name='counts')
            fig=px.bar(a,text_auto=True,
                      labels={'index':column, 'value': 'Counts'})
            fig.update_traces(width=1,textfont_size=14)
            st.plotly_chart(fig)    
            
if select == "Product viewed":
    column="Product viewed"
    calculate()
elif select == "Added to cart":
    column="Added to cart"
    calculate()
elif select == "Checkout made":
    column= "Checkout made"
    calculate()
elif select == "Purchased":
    column= "Purchased"
    calculate()  
elif select == "Summary":
    column=df[["Product viewed", "Added to cart", "Checkout made", "Purchased"]]
    st.subheader("The maximum values are:")
    st.dataframe(column.max(),width=1000)
    