import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="CampusLink Uganda",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_FILE = Path(__file__).parent / "data" / "listings.xlsx"

@st.cache_data
def load_data():
    return {
        "Hostels": pd.read_excel(DATA_FILE, sheet_name="Hostels"),
        "Jobs": pd.read_excel(DATA_FILE, sheet_name="Jobs"),
        "Scholarships": pd.read_excel(DATA_FILE, sheet_name="Scholarships"),
    }

data = load_data()

st.markdown("""
<style>
.main-title {font-size: 2.4rem; font-weight: 800; margin-bottom: 0.2rem;}
.subtitle {font-size: 1.05rem; color: #666;}
.card {
    padding: 1rem 1.2rem;
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    margin-bottom: 0.8rem;
    background: white;
}
.small {color:#666; font-size:0.9rem;}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 CampusLink Uganda</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A student hub for hostels, jobs and scholarships.</div>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.header("Explore")
    section = st.radio("Choose a service", ["🏠 Hostels", "💼 Jobs Board", "🎓 Scholarships"])
    st.divider()
    st.caption("Content is maintained through the Excel workbook in the Git repository.")

def search_box(df, columns):
    q = st.text_input("🔎 Search", placeholder="Search by name, location, field, provider...")
    if q:
        mask = pd.Series(False, index=df.index)
        for col in columns:
            if col in df.columns:
                mask = mask | df[col].fillna("").astype(str).str.contains(q, case=False, regex=False)
        return df[mask]
    return df

if section == "🏠 Hostels":
    st.header("🏠 Student Hostels")
    df = data["Hostels"].copy()
    df = search_box(df, ["Name", "Location", "Gender", "Amenities"])

    c1, c2 = st.columns(2)
    with c1:
        locations = ["All"] + sorted(df["Location"].dropna().astype(str).unique().tolist())
        loc = st.selectbox("Location", locations)
    with c2:
        genders = ["All"] + sorted(df["Gender"].dropna().astype(str).unique().tolist())
        gender = st.selectbox("Gender", genders)

    if loc != "All":
        df = df[df["Location"].astype(str) == loc]
    if gender != "All":
        df = df[df["Gender"].astype(str) == gender]

    st.info(f"{len(df)} hostel listing(s) found.")
    for _, row in df.iterrows():
        st.markdown(f"""
        <div class="card">
            <h3>{row.get('Name','')}</h3>
            <b>📍 {row.get('Location','')}</b><br>
            <b>💰 {row.get('Price','')}</b> &nbsp; | &nbsp; <b>👥 {row.get('Gender','')}</b><br>
            <span class="small">Amenities: {row.get('Amenities','')}</span><br>
            <span class="small">Contact: {row.get('Contact','')}</span>
        </div>
        """, unsafe_allow_html=True)
        if pd.notna(row.get("Link")):
            st.link_button("View hostel / contact", str(row["Link"]))

elif section == "💼 Jobs Board":
    st.header("💼 Student Jobs & Internships")
    df = data["Jobs"].copy()
    df = search_box(df, ["Title", "Organization", "Location", "Type", "Description"])

    types = ["All"] + sorted(df["Type"].dropna().astype(str).unique().tolist())
    job_type = st.selectbox("Job type", types)
    if job_type != "All":
        df = df[df["Type"].astype(str) == job_type]

    st.info(f"{len(df)} job listing(s) found.")
    for _, row in df.iterrows():
        st.markdown(f"""
        <div class="card">
            <h3>{row.get('Title','')}</h3>
            <b>🏢 {row.get('Organization','')}</b><br>
            📍 {row.get('Location','')} &nbsp; | &nbsp; 💼 {row.get('Type','')}<br>
            ⏰ Deadline: {row.get('Deadline','')}<br>
            <span class="small">{row.get('Description','')}</span>
        </div>
        """, unsafe_allow_html=True)
        if pd.notna(row.get("Link")):
            st.link_button("Apply / view details", str(row["Link"]))

else:
    st.header("🎓 Scholarships")
    df = data["Scholarships"].copy()
    df = search_box(df, ["Scholarship", "Provider", "Study Level", "Field", "Country/Region", "Description"])

    c1, c2 = st.columns(2)
    with c1:
        levels = ["All"] + sorted(df["Study Level"].dropna().astype(str).unique().tolist())
        level = st.selectbox("Study level", levels)
    with c2:
        fields = ["All"] + sorted(df["Field"].dropna().astype(str).unique().tolist())
        field = st.selectbox("Field", fields)

    if level != "All":
        df = df[df["Study Level"].astype(str) == level]
    if field != "All":
        df = df[df["Field"].astype(str) == field]

    st.info(f"{len(df)} scholarship listing(s) found.")
    for _, row in df.iterrows():
        st.markdown(f"""
        <div class="card">
            <h3>{row.get('Scholarship','')}</h3>
            <b>🏛️ {row.get('Provider','')}</b><br>
            🎓 {row.get('Study Level','')} &nbsp; | &nbsp; 📚 {row.get('Field','')}<br>
            🌍 {row.get('Country/Region','')} &nbsp; | &nbsp; ⏰ Deadline: {row.get('Deadline','')}<br>
            <span class="small">{row.get('Description','')}</span>
        </div>
        """, unsafe_allow_html=True)
        if pd.notna(row.get("Link")):
            st.link_button("View scholarship / apply", str(row["Link"]))

st.divider()
st.caption("CampusLink Uganda • Update listings by editing data/listings.xlsx and pushing the changes to GitHub.")