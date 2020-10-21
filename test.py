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
        ("-", (ft.about,None)),
        (
            "Prediction",
            (
                ft.prediction,
                """
This app shows how you can use Streamlit to build cool animations.
It displays an animated fractal based on the the Julia Set. Use the slider
to tune different parameters.
""",
            ),
        ),
        (
            "Analyse/Compare/Insights",
            (
                ft.analysis,
                """
This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
""",
            ),
        ),
       
        (
            "Contribute",
            (
                ft.contribute,
                """
This demo shows how to use `st.write` to visualize Pandas DataFrames.

(Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
""",
            ),
        ),
        (
            "Suggestion",
            (
                ft.suggestion,
            )
        ),
        (
            "How it works ?",
            (
                ft.working,
            )
        )
    ]
)


def run():
    demo_name = st.sidebar.selectbox("Choose from Menu 👇 ", list(ft.keys()), 0)
    demo = ft[demo_name][0]

    demo()

   
    st.write("##### -Rushikesh Gholap")


if __name__ == "__main__":
    run()