import streamlit as st
import plotly.graph_objects as go

# App title
st.title("Yield Farming Calculator")


# Create three columns for input fields
col1, col2, col3 = st.columns(3)

# Input fields side-by-side
with col1:
    totaltvl = st.number_input("Total TVL (in $):", min_value=0.0, format="%.2f")

with col2:
    myfarm = st.number_input("Your Farm (in $):", min_value=0.0, format="%.2f")

with col3:
    myfees = st.number_input("Your Fees (in $):", min_value=0.0, format="%.2f")

# Perform the calculation
fees_kept = 0.75 * myfees
additional_earnings = 150000 * myfarm / totaltvl if totaltvl > 0 else 0

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
