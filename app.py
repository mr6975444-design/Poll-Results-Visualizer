
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Poll Results Visualizer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Poll Results Visualizer")
st.write("Explore survey responses through interactive data visualizations.")

# Load data
df = pd.read_csv("data/processed/cleaned_poll_data.csv")

# Sidebar filters
st.sidebar.header("Filter Options")

age_groups = st.sidebar.multiselect(
    "Select Age Groups",
    options=df["Age Group"].unique(),
    default=df["Age Group"].unique()
)

filtered_df = df[df["Age Group"].isin(age_groups)]

# Key metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Responses", len(filtered_df))
col2.metric(
    "Most Popular Tool",
    filtered_df["Preferred Tool"].mode()[0]
    if not filtered_df.empty else "N/A"
)
col3.metric(
    "Average Satisfaction",
    round(filtered_df["Satisfaction"].mean(), 2)
    if not filtered_df.empty else "N/A"
)

st.divider()

# Preferred tool chart
st.subheader("Preferred Programming Tools")

fig, ax = plt.subplots(figsize=(9, 4))
sns.countplot(
    data=filtered_df,
    x="Preferred Tool",
    order=filtered_df["Preferred Tool"].value_counts().index,
    ax=ax
)
ax.set_xlabel("Programming Tool")
ax.set_ylabel("Votes")
st.pyplot(fig)
plt.close(fig)

# Age group chart
st.subheader("Age Group Distribution")

if not filtered_df.empty:
    age_counts = filtered_df["Age Group"].value_counts()
    st.bar_chart(age_counts)
else:
    st.info("Select at least one age group to view charts.")

# Satisfaction chart
st.subheader("Satisfaction Ratings")

if not filtered_df.empty:
    satisfaction_counts = filtered_df["Satisfaction"].value_counts().sort_index()
    st.bar_chart(satisfaction_counts)

# Raw data
with st.expander("View Survey Data"):
    st.dataframe(filtered_df, use_container_width=True)

st.success("Dashboard loaded successfully!")
