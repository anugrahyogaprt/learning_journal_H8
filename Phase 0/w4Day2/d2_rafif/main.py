import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="H8-Streamlit",
    page_icon="😼",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.google.com',
        'Report a bug': "https://www.github.com/rafifaditio",
        'About': "My first app using Streamlit"
    }
)

# ################ UPLOAD IMAGE #################################
# img = Image.open('2-4.jpg')

# st.header('Eiffel Tower')
# st.image(img, caption='Eiffel Tower', width=400, use_column_width=True)

# ############# COLUMNS USING WITH NOTATION ########################
# st.header('Columns partitioning')
# col1, col2, col3 = st.columns(3)

# with col1:
#     st.write('kolom pertama')
#     st.image(img)

# with col2:
#     st.write('kolom ke-2')

# with col3:
#     st.write('kolom ke-3')
#     st.image('https://static.streamlit.io/examples/owl.jpg')

# ############# COLUMNS USING VARIABLE ########################
# st.header('Columns using ratio partitioning')
# col1, col2 = st.columns([3, 1])
# data = np.random.randn(10, 1)

# col1.subheader("A wide column with a chart")
# col1.line_chart(data)

# col2.subheader("A narrow column with the data")
# col2.write(data)

# ################# CONTAINER USING WITH NOTATION #################
# st.subheader('container using with notation')

# with st.container():
#   st.write("This is inside the container")

#   # You can call any Streamlit command, including custom components:
#   st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")

# st.subheader('container using variable')
# cont = st.container()
# cont.write('This is inide container')

# st.write('This is outside container')

# cont.write('This is inside container 2')

# ################### EXPANDER #########################
# st.subheader('Expander')

# st.line_chart({"data": [1, 5, 2, 6, 2, 1]})

# with st.expander("See explanation"):
#   st.write("""
#      The chart above shows some numbers I picked for you.
#      I rolled actual dice for these, so they're *guaranteed* to
#      be random.
#   """)

#   st.image("https://static.streamlit.io/examples/dice.jpg")

selected = st.sidebar.selectbox('Page: ', ['Data Visualization', 'Hypothesis Testing'])

if selected == 'Data Visualization':
    with st.container():
        st.write("This is inside the container")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

        st.write("This is outside the container")

else:
    st.write('Demo Page for Hypothesis Testing')