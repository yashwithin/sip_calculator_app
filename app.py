
import streamlit as st
from datetime import datetime
from modules.calculator import calculate_sip_with_step_up
from modules.plotting import plot_sip

st.title("SIP Growth Calculator with Annual Increase")

monthly = st.number_input("Monthly SIP Amount (₹)", value=5000,step=500)
years = st.slider("Investment Duration (Years)", 1, 40, 10,step=1)
rate = st.slider("Expected Annual Return (%)", 10.0, 30.0, 12.0,step=0.5)
step_up = st.slider("Annual SIP Increase (%)", 0, 20, 10,step=1)
lump_sum = st.number_input("Lump Sum Investment (Optional)", value=0)
start_date = st.date_input("SIP Start Date", datetime.today())

if st.button("Calculate"):
    st.write("You Selected start Date:",start_date.strftime("%d-%m-%y"))
    monthly_df,yearly_df = calculate_sip_with_step_up(monthly, years, rate, step_up, lump_sum, start_date)
    
    
    plot_sip(monthly_df)

    st.subheader("Yearly Summary")
    st.write(yearly_df)
    
with st.sidebar:
    st.markdown("### Developed by Yash")
    st.markdown("[GitHub](https://github.com/yashwithin)")
    st.markdown("[Connect On LinkedIN](https://www.linkedin.com/in/yash-pareek-ml/)")

