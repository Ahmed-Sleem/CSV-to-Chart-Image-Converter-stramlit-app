import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os



# Function to load CSV files
def load_csv_files(uploaded_files):
    data = {}
    for uploaded_file in uploaded_files:
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            data[uploaded_file.name] = df
    return data

# Function to display line charts using Matplotlib
def display_line_charts(data):
    num_files = len(data)
    for i, (filename, df) in enumerate(data.items(), start=1):
        df['Date'] = pd.to_datetime(df['Date'])

        fig, ax = plt.subplots()
        ax.plot(df['Date'], df['Close'], color='blue')
        ax.axis('off')  # Turn off axis labels
        ax.set_title(f" ", color='white')
        ax.set_facecolor('black')  # Set background color
        fig.patch.set_facecolor('black')  # Set figure background color
        st.pyplot(fig)

# Function to save line charts as images
def save_line_charts_as_images(data):
    for filename, df in data.items():
        df['Date'] = pd.to_datetime(df['Date'])
        
        fig, ax = plt.subplots()
        ax.plot(df['Date'], df['Close'], color='blue')
        ax.axis('off')  # Turn off axis labels
        ax.set_facecolor('black')  # Set background color
        plt.savefig(f"{filename}_line_chart.png", bbox_inches='tight', pad_inches=0, facecolor=fig.get_facecolor())
        plt.close()

# Function to display data tables
def display_data_tables(data):
    for filename, df in data.items():
        st.subheader(f"Data table for {filename}")
        st.write(df)

# Main function
def main():
    
    
                
    # Sidebar
    st.sidebar.title("Options : ")
    
    upload_files = st.sidebar.file_uploader("Upload CSV files", accept_multiple_files=True)
    
    
    if not upload_files :
        st.warning("there in no charts uploaded !")
        
        
    if upload_files:
        data = load_csv_files(upload_files)
        num = len(data)
        st.title("Graphs : ")
        st.warning(f"number of charts : {num}")
        
        display_option = st.sidebar.radio("Display Option : ", ("Preview Graph", "Preview Table"))
        
        
        if st.sidebar.button("Download All Graphs Images"):
            save_line_charts_as_images(data)
            st.sidebar.success("All graphs downloaded successfully!")

        if display_option == "Preview Graph":
            display_line_charts(data)
        elif display_option == "Preview Table":
            display_data_tables(data)

if __name__ == "__main__":
    main()
    