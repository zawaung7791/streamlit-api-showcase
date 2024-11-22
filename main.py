import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Streamlit API Showcase",
    page_icon="✨",
    layout="centered",
)

# Page Title
st.title("📚 Streamlit API Showcase")

# Sidebar for navigation
with st.sidebar:
    st.header("Navigate")
    page = st.radio(
        "Sections",
        ["Widgets", "Media", "Charts", "Layout", "DataFrames", "Utilities"]
    )
    st.info("Explore different Streamlit API features!")

# 1. Widgets Section
if page == "Widgets":
    st.header("🔘 Widgets")

    # Button
    if st.button("Click Me"):
        st.write("🎉 Button clicked!")

    # Checkbox
    agree = st.checkbox("I agree")
    if agree:
        st.write("✅ Thanks for agreeing!")

    # Radio
    choice = st.radio("Choose an option:", ["Option 1", "Option 2", "Option 3"])
    st.write(f"You selected: {choice}")

    # Selectbox
    option = st.selectbox("Select an item:", ["Item A", "Item B", "Item C"])
    st.write(f"You selected: {option}")

    # Multiselect
    items = st.multiselect("Select multiple items:", ["Item 1", "Item 2", "Item 3"])
    st.write(f"Selected items: {items}")

    # Slider
    value = st.slider("Select a value:", 0, 100, 50)
    st.write(f"Slider value: {value}")

    # Text input
    name = st.text_input("Enter your name:")
    st.write(f"Hello, {name}!")

    # Number input
    number = st.number_input("Enter a number:", 0, 100, 50)
    st.write(f"Number entered: {number}")

    # Date input
    date = st.date_input("Pick a date:", datetime.now())
    st.write(f"Selected date: {date}")

    # File uploader
    uploaded_file = st.file_uploader("Upload a file:")
    if uploaded_file:
        st.write("Uploaded file name:", uploaded_file.name)

# 2. Media Section
elif page == "Media":
    st.header("🎥 Media")

    # Display an image
    st.image("https://via.placeholder.com/400", caption="Sample Image", use_container_width=True)

    # Display an audio file
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

    # Display a video
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# 3. Charts Section
elif page == "Charts":
    st.header("📊 Charts")

    # Line chart
    st.subheader("Line Chart")
    data = pd.DataFrame(np.random.randn(50, 3), columns=["A", "B", "C"])
    st.line_chart(data)

    # Bar chart
    st.subheader("Bar Chart")
    st.bar_chart(data)

    # Area chart
    st.subheader("Area Chart")
    st.area_chart(data)

# 4. Layout Section
elif page == "Layout":
    st.header("📐 Layouts")

    # Columns
    st.subheader("Columns")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("Column 1")
    with col2:
        st.write("Column 2")
    with col3:
        st.write("Column 3")

    # Tabs
    st.subheader("Tabs")
    tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
    with tab1:
        st.write("Content for Tab 1")
    with tab2:
        st.write("Content for Tab 2")
    with tab3:
        st.write("Content for Tab 3")

    # Expander
    st.subheader("Expander")
    with st.expander("Click to expand"):
        st.write("Expanded content!")

# 5. DataFrames Section
elif page == "DataFrames":
    st.header("📋 DataFrames")

    # Display dataframe
    st.subheader("Static DataFrame")
    df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])
    st.dataframe(df)

    # Display table
    st.subheader("Static Table")
    st.table(df.head())

# 6. Utilities Section
elif page == "Utilities":
    st.header("🔧 Utilities")

    # Progress bar
    st.subheader("Progress Bar")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)

    # Balloons
    st.subheader("Balloons")
    if st.button("Celebrate!"):
        st.balloons()

    # Code display
    st.subheader("Code")
    st.code("import streamlit as st\nst.write('Hello, world!')", language="python")

    # JSON display
    st.subheader("JSON")
    st.json({"key": "value", "foo": "bar"})