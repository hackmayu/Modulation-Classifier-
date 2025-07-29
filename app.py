import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import joblib

# Load model
model = joblib.load("best_rf_model.pkl")  # Ensure this file is saved from Colab
mod_classes = ['BPSK', 'QPSK', '8PSK', '16QAM', '64QAM', '4ASK', 'FSK']  # Update based on your model

# Feature extractor
def extract_features(sig):
    I = np.real(sig)
    Q = np.imag(sig)
    return [
        I.mean(), I.std(), skew(I), kurtosis(I),
        Q.mean(), Q.std(), skew(Q), kurtosis(Q)
    ]

# Streamlit UI
st.title("📡 Modulation Classifier")
st.write("Upload a `.npy` file containing a complex baseband signal:")

uploaded_file = st.file_uploader("Choose a .npy signal file", type=["npy"])

if uploaded_file is not None:
    try:
        import io
        sig = np.load(io.BytesIO(uploaded_file.read()), allow_pickle=True)

        if not np.iscomplexobj(sig):
            st.error("Uploaded signal must be complex-valued!")
        else:
            st.success("Signal loaded successfully.")
            st.write("Signal length:", len(sig))

            # Show signal plot
            fig, ax = plt.subplots()
            ax.plot(np.real(sig), label="In-phase (I)")
            ax.plot(np.imag(sig), label="Quadrature (Q)")
            ax.legend()
            ax.set_title("Signal Plot")
            st.pyplot(fig)

            # Extract features & predict
            feats = np.array(extract_features(sig)).reshape(1, -1)
            pred = model.predict(feats)[0]
            st.subheader(f"🔍 Predicted Modulation: **{pred}**")
    except Exception as e:
        st.error(f"Error: {e}")
