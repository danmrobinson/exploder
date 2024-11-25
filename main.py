import streamlit as st
import pandas as pd
import io

st.image(
    "https://images.emojiterra.com/google/noto-emoji/unicode-16.0/color/svg/1f9e8.svg",
    width=100,
)

# Streamlit App: The Exploder
st.title("The Exploder")

# Step 1: Upload CSV File
st.header("Upload a CSV File")
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Load the uploaded CSV file
    df = pd.read_csv(uploaded_file)
    st.subheader("Uploaded Data")
    st.write(df)

    # Step 2: Select Column to Explode
    st.header("Select a Column to Explode")
    column_to_explode = st.selectbox(
        "Choose the column to explode",
        df.columns,
        help="Select the column containing lists or values to split into rows.",
    )

    # Check if selected column is valid for explode
    if column_to_explode:
        # Step 3: Explode the DataFrame
        try:
            # Assuming the column is a delimited string (e.g., comma-separated)
            if df[column_to_explode].dtype == object:
                df[column_to_explode] = df[column_to_explode].str.split(',')
            
            exploded_df = df.explode(column_to_explode)

            st.subheader("Exploded Data")
            st.write(exploded_df)

            # Step 4: Download Exploded Data
            st.header("Download Exploded Data")
            csv_buffer = io.StringIO()
            exploded_df.to_csv(csv_buffer, index=False)
            csv_data = csv_buffer.getvalue()
            st.download_button(
                label="Download as CSV",
                data=csv_data,
                file_name="exploded_data.csv",
                mime="text/csv",
            )
        except Exception as e:
            st.error(f"Error while exploding the column: {e}")
else:
    st.info("Upload a CSV file to get started.")
