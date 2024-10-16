import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

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
    fig1, ax1 = plt.subplots()
    sizes = [myfarm, totaltvl - myfarm]
    labels = ['My Farm', 'Rest of TVL']
    colors = ['#ff9999','#66b3ff']
    explode = (0.1, 0)  # explode the 1st slice (my farm)

    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', colors=colors, shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    
    st.write("### Visual 1: My Farm as a Part of Total TVL")
    st.pyplot(fig1)
else:
    st.write("Total TVL should be greater than 0 to display the pie chart.")

# --- Add Visual 2: Bar Chart for Fees ---
if myfees > 0:
    fig2, ax2 = plt.subplots()

    labels = ['Usual Fees', 'Fees Kept on Yeve', 'Additional Earnings on Yeve']
    values = [myfees, fees_kept, additional_earnings]
    colors = ['#ff9999', '#66b3ff', '#99ff99']

    ax2.bar(labels, values, color=colors)
    ax2.set_ylabel('Amount in Dollars')

    st.write("### Visual 2: Fees Comparison")
    st.pyplot(fig2)
else:
    st.write("Usual fees should be greater than 0 to display the bar chart.")
