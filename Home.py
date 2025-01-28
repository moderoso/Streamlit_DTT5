# Importação das bibliotecas
import streamlit as st
import pandas as pd

import altair as alt
from plotly.colors import n_colors
import plotly.express as px
import plotly.graph_objects as go
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title= 'ONG - Passos Mágicos', layout='wide', page_icon='📊')

# Título da página
st.title('ONG - Passos Mágicos :woman-woman-girl-boy:')


#with st.sidebar:
 #   selected = option_menu("Menu", ["Home", 'Settings'], 
 #       icons=['house', 'gear'], default_index=0)

#if selected == "Home":
#    st.write("home is where the heart is")
#else:
#    st.write("settings is my bettings")
	
	
from streamlit_navigation_bar import st_navbar

page = st_navbar(["Home", "Documentation", "Examples", "Community", "Sobre"])

st.write(page)

