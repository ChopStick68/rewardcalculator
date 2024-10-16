import streamlit as st

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

