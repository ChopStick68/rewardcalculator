import streamlit as st
import plotly.graph_objects as go

# App title
st.title("Yield Farming Calculator")

# Instructions
st.write("Fill in the blanks to see your potential farming outcome:")

# User input fields
totaltvl = st.number_input("Total TVL on the platform (in dollars):", min_value=0.0, format="%.2f")
myfarm = st.number_input("Amount you're planning to farm with (in dollars):", min_value=0.0, format="%.2f")
myfees = st.number_input("Your usual fees (in dollars):", min_value=0.0, format="%.2f")

# Perform the calculation
fees_kept = 0.75 * myfees
additional_earnings = 150000 * myfarm / totaltvl if totaltvl > 0 else 0

# Display results in the same format as requested
st.write(f"We assume that there is a total TVL of {totaltvl:.2f} on the platform and you are planning to farm with {myfarm:.2f} yourself.")
st.write(f"You usually make {myfees:.2f}.")
st.write(f"On yeve you will keep 0.75 * {myfees:.2f} = {fees_kept:.2f}")
st.write(f"Additionally, you will get 150000 * {myfarm:.2f} / {totaltvl:.2f} = {additional_earnings:.2f}")

# --- Add Visual 1: Pie Chart for TVL and Farm ---
if totaltvl > 0:
    labels = ['My Farm', 'Rest of TVL']
    values = [myfarm, totaltvl - myfarm]

    fig1 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    st.write("### Visual 1: My Farm as a Part of Total TVL")
    st.plotly_chart(fig1)
else:
    st.write("Total TVL should be greater than 0 to display the pie chart.")

# --- Add Visual 2: Bar Chart for Fees ---
if myfees > 0:
    fig2 = go.Figure(data=[
        go.Bar(name='Usual Fees', x=['Fees'], y=[myfees], marker_color='#ff9999'),
        go.Bar(name='Fees Kept on Yeve', x=['Fees'], y=[fees_kept], marker_color='#66b3ff'),
        go.Bar(name='Additional Earnings on Yeve', x=['Fees'], y=[additional_earnings], marker_color='#99ff99')
    ])

    fig2.update_layout(barmode='group', yaxis_title='Amount in Dollars')
    st.write("### Visual 2: Fees Comparison")
    st.plotly_chart(fig2)
else:
    st.write("Usual fees should be greater than 0 to display the bar chart.")
