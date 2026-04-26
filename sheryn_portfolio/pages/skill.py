import streamlit as st

st.set_page_config(page_title="Skills", page_icon="💻", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
.main-header {font-family:'Poppins'; font-size:3rem; color:#000000; text-align:center;}
.sub-header {font-family:'Poppins'; color:#333333; text-align:center; font-size:1.4rem;}
.info-card {background:#ffffff; padding:2rem; border-radius:12px; box-shadow:0 5px 20px rgba(0,0,0,0.1); border-left:4px solid #000000; color:#000000; margin:1rem 0;}
.skill-bar {background:#f5f5f5; padding:1rem; border-radius:8px; margin:0.5rem 0;}
.main .block-container {background-color:#ffffff;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">💻 My Skills</h1>', unsafe_allow_html=True)

st.markdown('<h2 class="sub-header">🛠️ Programming Languages</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="skill-bar">
        <strong>🐍 Python</strong> <span style="float:right;">85%</span><br>
        <div style="background:#e0e0e0; height:12px; border-radius:6px;">
            <div style="background:#000000; width:85%; height:100%; border-radius:6px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="skill-bar">
        <strong>🌐 JavaScript</strong> <span style="float:right;">70%</span><br>
        <div style="background:#e0e0e0; height:12px; border-radius:6px;">
            <div style="background:#000000; width:70%; height:100%; border-radius:6px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="skill-bar">
        <strong>📄 HTML/CSS</strong> <span style="float:right;">80%</span><br>
        <div style="background:#e0e0e0; height:12px; border-radius:6px;">
            <div style="background:#000000; width:80%; height:100%; border-radius:6px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<h2 class="sub-header">🛠️ Tools & Frameworks</h2>', unsafe_allow_html=True)
st.markdown("""
<div class="info-card">
    <strong>📊 Streamlit</strong> • <strong>⚛️ React</strong> • <strong>🐦 Django</strong><br>
    <strong>💅 Bootstrap</strong> • <strong>🐘 Git/GitHub</strong> • <strong>🔧 VS Code</strong>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center;color:#666666;font-family:Poppins;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)