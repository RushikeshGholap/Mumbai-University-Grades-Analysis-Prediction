import streamlit as st

st.title('Mumbai University Engineering Project')

import inspect
import textwrap
from collections import OrderedDict

import streamlit as st
from streamlit.logger import get_logger
import ft

LOGGER = get_logger(__name__)

# Dictionary of
# demo_name -> (demo_ft, demo_description)  
ft = OrderedDict(
    [
        ("About", (ft.about,None)),
        (
            "Prediction",
            (
                ft.prediction,
               
            ),
        ),
        (
            "Analyse/Compare/Insights",
            (
                ft.analysis,
                
            ),
        ),
       
        (
            "Contribute",
            (
                ft.contribute,
               
            ),
        ),
        (
            "Suggestion",
            (
                ft.suggestion,
            )
        ),
        # (
        #     "How it works ?",
        #     (
        #         ft.working,
        #     )
        # )
    ]
)


def run():
      
    st.markdown(
        """ <p style="color:red">
         <b>Note</b>- The site is in progress. Some glitches and minor changes need to be fixed. Ignore them for now.
        </p>


        """,unsafe_allow_html=True

    )
    demo_name = st.sidebar.selectbox("Choose from Menu 👇 ", list(ft.keys()), 0)
    demo = ft[demo_name][0]

    demo()

    
    st.write('##### -<a href="https://www.linkedin.com/in/rushikeshgholap/" target="_blank"> Rushikesh Gholap </a>',unsafe_allow_html=True)
    

if __name__ == "__main__":
    run()