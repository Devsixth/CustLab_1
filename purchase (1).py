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

def calculate(): 
    # finding values
    mi=df[column].min()
    mx=df[column].max()
    z=df[column][df[column ]== 0].count()
    nz=df[column][df[column ]!= 0].count()
    # creating tuple
    d=mi,mx,z,nz
    #creating tuple into dataframe
    t=pd.DataFrame(list(d),columns=[column], index=['Minimum', 'Maximum', 'Zeros', 'Non_Zeros'])
    st.dataframe(t,use_container_width=True)
    
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
    column=["Product viewed", "Added to cart", "Checkout made", "Purchased"]
    #finding values
    mi=df[column].min().rename('Minimum')
    mx=df[column].max().rename('Maximum')
    z=df[column][df[column ]== 0].count().rename('Zeros')
    nz=df[column][df[column ]!= 0].count().rename('Non_Zeros')
    #creating datframe
    a=pd.DataFrame(mi)
    b=pd.DataFrame(mx)
    c=pd.DataFrame(z)
    d=pd.DataFrame(nz)
    #merging dataframe
    result=pd.concat([a,b,c,d], axis=1, join='inner')
    st.dataframe(result,use_container_width=True)
    