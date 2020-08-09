
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
        ("Intro ", (ft.intro())),
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
            "Analyse",
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
            "Compare",
            (
                ft.compare,
                """
This demo shows how to use
[`st.deck_gl_chart`](https://docs.streamlit.io/en/latest/api.html#streamlit.deck_gl_chart)
to display geospatial data.
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
    demo_name = st.sidebar.selectbox("Choose from ft", list(ft.keys()), 0)
    demo = ft[demo_name][0]

    if demo_name == "intro":
        
        st.write("# Welcome to Streamlit! 👋")
    else:
        
        st.markdown("# %s" % demo_name)
        description = ft[demo_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        for i in range(10):
            st.empty()

    demo()

   
    st.write("#### -Rushikesh Gholap")


if __name__ == "__main__":
    run()