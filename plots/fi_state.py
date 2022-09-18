import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st

from misc.helpers import load_data

def fi_state_ph():
# Write the title
    st.title(
        "This is the current state of FI in the Philippines."
    )

    # Load data
    data = load_data()

    # Fetch Philippine data
    philippine_data = data[
        data['economy'] == 'Philippines'
        ]

    # Create another column for debit card ownership
    philippine_data['has_debit_card'] = philippine_data['fin2'].apply(
        lambda x: 1 if x == 1 else 0
    )

    # Compute overall debit card ownership
    percent_debit_card_ownership = philippine_data['has_debit_card'].sum() * 100.0 / philippine_data[
        'wpid_random'].count()

    # Partition the page into 2
    col1, col2 = st.columns(2)

    # Display text in column 1
    col1.markdown(
        "In the Philippines, there is still an opportunity to expand access to financial services: "
    )

    # Display metric in column 2
    col2.metric(
        label='% of Population with Debit Card',
        value=percent_debit_card_ownership
    )

    # Display text
    st.markdown("In terms of gender breakdown:")

    # Create another column for gender
    philippine_data['gender'] = philippine_data['female'].apply(
        lambda x: 'male' if x == 1 else 'female'
    )

    # Compute breakdown of access to debit card by gender
    debit_by_gender = philippine_data.groupby('gender').agg(
        total_debit_card_owners=('has_debit_card', 'sum'),
        total_population=('wpid_random', 'count')
    ).reset_index()

    # Compute % debit card ownership
    debit_by_gender['% debit card ownership'] = debit_by_gender['total_debit_card_owners'] * 100.0 / debit_by_gender[
        'total_population']

    # Plot the data
    fig, ax = plt.subplots(figsize=(6, 3), dpi=200)
    ax.bar(
        debit_by_gender["gender"],
        debit_by_gender["% debit card ownership"],
    )
    ax.set_xlabel("Gender")
    ax.set_ylabel("% Debit Card Ownership")

    # Show the data
    st.pyplot(fig)

def fi_state_worldwide():
    # Write the title and the subheader
    st.title(
        "This is the current state of FI worldwide."
    )
    st.markdown(
        "**Here is a bubble map presenting the % of debit card ownership per country:**"
    )

    # Load data
    data = load_data()

    # Create another column for debit card ownership
    data['has_debit_card'] = data['fin2'].apply(
        lambda x: 1 if x == 1 else 0
    )

    # Group the data and apply aggregations
    grouped_data = data.groupby(['economy', 'economycode', 'regionwb']).agg(
        total_debit_card_owners=('has_debit_card', 'sum'),
        total_population=('wpid_random', 'count')
    ).reset_index()

    # Compute debit card ownership in %
    grouped_data['% of population with debit card'] = grouped_data['total_debit_card_owners'] * 100.0 / grouped_data[
        'total_population']

    # Build the bubble map
    fig = px.scatter_geo(
        grouped_data,
        locations="economycode",
        color="regionwb",
        hover_name="economy",
        size="% of population with debit card",
        projection="natural earth"
    )

    # Show the figure
    st.plotly_chart(fig)
