import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Sheryn Portfolio", page_icon="👩‍💻", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
.main-header {font-family:'Poppins'; font-size:3rem; color:#000000; text-align:center;}
.sub-header {font-family:'Poppins'; color:#333333; text-align:center; font-size:1.4rem;}
.metric-card {background:#000000; color:#ffffff; padding:2rem; border-radius:15px; text-align:center;}
.info-card {background:#ffffff; padding:1.8rem; border-radius:12px; box-shadow:0 5px 20px rgba(0,0,0,0.1); border-left:4px solid #000000; color:#000000;}
.stButton > button {background:#000000; color:#ffffff !important; border-radius:25px; font-weight:600;}
.main .block-container {background-color:#ffffff;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">👋 Welcome to My Portfolio</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Sheryn A Dequilla<br>3rd Year BSCS DEBESMSCAT Student</p>', unsafe_allow_html=True)

# Stats Cards
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="metric-card"><h2 style="font-size:2.8rem;margin:0;">21</h2><p>Years Old</p></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="metric-card"><h2 style="font-size:2.8rem;margin:0;">3rd</h2><p>Year BSCS</p></div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="metric-card"><h2 style="font-size:2.8rem;margin:0;">🎓</h2><p>DEBESMSCAT</p></div>', unsafe_allow_html=True)

# Contact Info
st.markdown("---")
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#000000;">📍 Address</h3>
        <p><strong>Milagros</strong><br>Masbate</p>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#000000;">📧 Contact</h3>
        <p><strong>sheryndequilla4@gmail.com</strong><br><strong>0907-488-7142</strong></p>
    </div>
    """, unsafe_allow_html=True)

# Birthday Counter
st.markdown("---")
today = datetime.now()
next_bday = datetime(today.year + 1, 3, 21) if today.month > 3 or (today.month == 3 and today.day >= 21) else datetime(today.year, 3, 21)
days_left = (next_bday - today).days
st.subheader("🎂 Days Until Birthday")
st.metric("Days Left", f"{days_left} days", f"March 21, {next_bday.year}")

st.markdown("<p style='text-align:center;color:#666666;font-family:Poppins;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)