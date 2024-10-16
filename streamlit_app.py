import streamlit as st
import plotly.graph_objects as go
import numpy as np

# App title
st.title("Typical numbers on Yeve")

# Inputs for Token Price and Redemption Rate
st.write("### Emissions")
col1, col2 = st.columns(2)

with col1:
    token_price = st.number_input("Token Price (in $):", min_value=0.0, value=1.0, format="%.2f")

with col2:
    redemption_rate = st.number_input("Redemption Rate (as a fraction):", min_value=0.0, max_value=1.0, value=1.0, format="%.2f")

# --- Add Emissions Plot and Adjusted Emissions Plot ---

# Generate the data for the emissions plot
i_values = np.arange(1, 51)  # Values from 1 to 50
emissions_values = 2000000 * (0.99 ** i_values)  # Emissions function
adjusted_emissions_values = emissions_values * token_price * redemption_rate  # Adjusted emissions with token price and redemption rate

# Create a line plot for the original emissions
emissions_fig = go.Figure(data=go.Scatter(x=i_values, y=emissions_values, mode='lines+markers', name="Emissions"))
emissions_fig.update_layout(
    title="Emissions Over Time",
    xaxis_title="Epoch (i)",
    yaxis_title="Token Emissions",
    yaxis=dict(range=[0, 2000000])  # Set y-axis range for better visualization
)

# Create a second plot for adjusted emissions
adjusted_emissions_fig = go.Figure(data=go.Scatter(x=i_values, y=adjusted_emissions_values, mode='lines+markers', name="Adjusted Emissions"))
adjusted_emissions_fig.update_layout(
    title="Adjusted Emissions Over Time",
    xaxis_title="Epoch (i)",
    yaxis_title="Dollar Emissions",
    yaxis=dict(range=[0, 2000000 * token_price * redemption_rate])  # Set y-axis range dynamically
)

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(emissions_fig)

with col2:
    st.plotly_chart(adjusted_emissions_fig)

# Instructions for yield farming calculator
st.write("Fill in the blanks to see your potential farming outcome:")

# Create four columns for input fields
col1, col2, col3, col4 = st.columns(4)

# Input fields side-by-side
with col1:
    totaltvl = st.number_input("Total TVL (in $):", min_value=0.0, format="%.2f")

with col2:
    myfarm = st.number_input("Your Farm (in $):", min_value=0.0, format="%.2f")

with col3:
    myfees = st.number_input("Your Fees (in $):", min_value=0.0, format="%.2f")

with col4:
    emissions_per_epoch = st.number_input("Emissions per Epoch", min_value=0.0, value=150000.0, format="%.2f")

# Perform the calculation
fees_kept = 0.75 * myfees
additional_earnings = emissions_per_epoch * myfarm / totaltvl if totaltvl > 0 else 0

# Create two columns for side-by-side visuals
col1, col2 = st.columns(2)

# --- Add Visual 1: Pie Chart for TVL and Farm ---
with col1:
    if totaltvl > 0:
        labels = ['My Farm', 'Rest of TVL']
        values = [myfarm, totaltvl - myfarm]

        fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
        st.write("### My Farm as a Part of Total TVL")
        st.plotly_chart(fig1)
    else:
        st.write("Total TVL should be greater than 0 to display the pie chart.")

# --- Add Visual 2: Bar Chart for Fees ---
with col2:
    if myfees > 0:
        fig2 = go.Figure(data=[
            go.Bar(name='Usual Fees', x=['Fees'], y=[myfees], marker_color='#ff9999'),
            go.Bar(name='Fees Kept on Yeve', x=['Fees'], y=[fees_kept], marker_color='#66b3ff'),
            go.Bar(name='Additional Earnings on Yeve', x=['Fees'], y=[additional_earnings], marker_color='#99ff99')
        ])

        fig2.update_layout(barmode='group', yaxis_title='Amount in Dollars')
        st.write("### Fees Comparison")
        st.plotly_chart(fig2)
    else:
        st.write("Usual fees should be greater than 0 to display the bar chart.")
