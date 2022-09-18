import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

from plots.fi_state import *
from misc.helpers import *

def introduction():
    # Write the title and the subheader
    st.title(
        "Towards Financial Inclusion (FI): using survey data to assess FI status of the Philippines"
    )
    st.subheader(
        """
        In line with the National Strategy for Financial Inclusion (NSFI) 2022-2028 by Bangko Sentral ng Pilipinas (BSP), this sprint aims to:
        1. Profile financial inclusion (FI) metrics in the Philippines using survey data from World Bank.
        2. Formulate policy recommendations to further improve access to financial services particularly to vulnerable sectors.
        """
    )

    # Load photo
    st.image("streamlit-photo-1.jpeg")

    # Load data
    data = load_data()

    # Display data
    st.markdown("**The Data**")
    st.dataframe(data)
    st.markdown("Source: Global Findex 2017 from World Bank.")


def recommendations():
    # Write the title
    st.title(
        "What We Can Do"
    )


def the_team():
    # Write the title
    st.title(
        "The Team"
    )


list_of_pages = [
    "Towards Financial Inclusion",
    "FI Status of the Philippines",
    "FI Status Worldwide",
    "What We Can Do",
    "The Team"
]

st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Towards Financial Inclusion":
    introduction()

elif selection == "FI Status of the Philippines":
    fi_state_ph()

elif selection == "FI Status Worldwide":
    fi_state_worldwide()

elif selection == "What We Can Do":
    recommendations()

elif selection == "The Team":
    the_team()
