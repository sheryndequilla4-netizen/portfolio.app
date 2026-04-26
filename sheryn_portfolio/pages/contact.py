import streamlit as st

st.set_page_config(page_title="Contact", page_icon="📞", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
.main-header {font-family:'Poppins'; font-size:3rem; color:#000000; text-align:center;}
.sub-header {font-family:'Poppins'; color:#333333; text-align:center; font-size:1.4rem;}
.info-card {background:#ffffff; padding:2rem; border-radius:12px; box-shadow:0 5px 20px rgba(0,0,0,0.1); border-left:4px solid #000000; color:#000000; margin:1rem 0;}
.main .block-container {background-color:#ffffff;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">📞 Contact Me</h1>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#000000;">📧 Email</h3>
        <p style="font-size:1.3rem;">sheryndequilla4@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#000000;">📱 Phone</h3>
        <p style="font-size:1.3rem;">0907-488-7142</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h3 style="color:#000000;">📍 Location</h3>
        <p style="font-size:1.3rem;">Milagros, Masbate</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#666666;font-family:Poppins;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)