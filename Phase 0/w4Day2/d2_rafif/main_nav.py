import data_viz, hypotest, home_page
import streamlit as st

PAGES = {'Data Visualization': data_viz,
         'Hypothesis Testing': hypotest,
         'Home': home_page
         }

selected = st.sidebar.selectbox('Pages: ', list(PAGES.keys()))

page = PAGES[selected]

page.app()