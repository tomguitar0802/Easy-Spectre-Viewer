import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Easy Spectre Viewer')
Path=st.file_uploader('Excelファイル')

def get_spectre(Sheet_name,i):
    df=pd.read_excel(Data,sheet_name=Sheet_name,skiprows=skip_rows)
    df=pd.DataFrame({x:df[x],y:df[y]/max(df[y])*100})
    ax[i].bar(df[x],df[y])

if Path is not None:
    Data=pd.ExcelFile(Path)
    Sheet_names=Data.sheet_names
    num_page=len(Sheet_names)
    defotate=2.0*num_page
    skip_rows=7
    x='Mass'
    y='Intensity'

    fig,ax=plt.subplots(len(Sheet_names),1,figsize=(8.0,defotate),sharex=True,sharey=True)

    for Sheet_name,i in zip(Sheet_names,range(len(Sheet_names))):
        get_spectre(Sheet_name,i)
    
    plt.xlabel("m/z")
    plt.ticklabel_format(useOffset=False,useMathText=True)
    st.pyplot(fig)
else:
    st.write("The spectre will be displayed when you upload Excel file.")
