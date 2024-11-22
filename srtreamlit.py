import streamlit as st
import math

# Function to calculate R0 and X0
def Tran_Eff(V0, I0, W0):
    NPF = W0 / (V0 * I0)
    I_mu = I0 * math.sqrt(1 - NPF**2)
    I_w = I0 * NPF
    R0 = V0 / I_w
    X0 = V0 / I_mu
    return R0, X0

# Streamlit Web App
st.title("230521L24-PS7: Transformer Open Circuit Test Calculator")

# Input fields
V0 = st.number_input("Enter V0 (Volts)", min_value=0.0, format="%.2f")
I0 = st.number_input("Enter I0 (Amps)", min_value=0.0, format="%.2f")
W0_kW = st.number_input("Enter W0 (Power in kW)", min_value=0.0, format="%.2f")

# Convert power from kW to W
W0 = W0_kW * 1000

# Calculate and display results
if st.button("Compute"):
    if V0 > 0 and I0 > 0 and W0 > 0:
        R0, X0 = Tran_Eff(V0, I0, W0)
        st.success(f"R0 (Resistance): {R0:.2f} Ω")
        st.success(f"X0 (Reactance): {X0:.2f} Ω")
    else:
        st.error("Please enter valid positive values for all inputs!")
