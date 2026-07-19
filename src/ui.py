import streamlit as st


def setup_page(title, icon="🌍"):
    st.set_page_config(
        page_title=title,
        page_icon=icon,
        layout="wide",
        initial_sidebar_state="expanded"
    )


def dashboard_header(title, subtitle):
    st.title(title)

    st.markdown(
        f"""
        <p style="
        font-size:18px;
        color:gray;
        ">
        {subtitle}
        </p>
        """,
        unsafe_allow_html=True
    )


def metric_card(title, value, subtitle="", icon="📊", color="#3B82F6"):

    st.markdown(
        f"""
        <div style="
        background-color:#1E293B;
        padding:20px;
        border-radius:15px;
        text-align:center;
        ">

        <div style="font-size:40px;">
        {icon}
        </div>

        <h3 style="color:white;">
        {title}
        </h3>

        <h1 style="color:{color};">
        {value}
        </h1>

        <p style="color:#CBD5E1;">
        {subtitle}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )
    
def create_sidebar():

    with st.sidebar:

        st.title("🌍 Global Economic Intelligence")

        st.divider()

        st.markdown("### 📌 Dashboard")

        st.info(
            """
Explore global economic data
using the World Bank Open Data API.
"""
        )

        st.markdown("### 📂 Pages")

        st.write("🏠 Home")
        st.write("🌍 Global Overview")
        st.write("🇮🇳 India Analysis")
        st.write("🌎 Country Comparison")
        st.write("🤖 Economic Insights")
        st.write("🗺️ World Map")

        st.divider()

        st.caption("📡 Data Source")
        st.caption("World Bank Open Data API")

        st.caption("⚙ Built With")
        st.caption("Python • Pandas • Plotly • Streamlit")