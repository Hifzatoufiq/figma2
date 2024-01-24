import streamlit as st
import pandas as pd

st.set_page_config(
  
    page_title="Your App Title",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url('https://res.cloudinary.com/asadullahkhan/image/upload/c_pad,b_auto:predominant,fl_preserve_transparency/v1705583102/RE-removebg-preview_kp4ymg.jpg?_s=public-apps');

                background-repeat: no-repeat;
                background-size: 120px;
                padding-top: 120px;
                background-position: 20px 20px;
                
            }
               [data-testid="stSidebarNav"]::before {
                content: "Work Orders";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 20px;
                position: relative;
                top: 100px;
                font-weight: bold;
            }
             
           
           
        </style>
        """,
        unsafe_allow_html=True,
    )
# Function to create or get SessionState
def get_session():
    if "session" not in st.session_state:
        st.session_state.session = SessionState()
    return st.session_state.session

# SessionState class for persisting session state
class SessionState:
    def __init__(self):
        self.master_components = []

# Sample data structure to store Master and Part Components
session = get_session()

# Function to create Master Component
def create_master_component(name):
    # Logic to save the Master Component with the entered information
    session.master_components.append({"name": name, "part_components": []})

# Add custom CSS for styling
st.markdown(
    """
    <style>
        .st-eb {
            max-width: 40px !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit app
def main():
    # Display a subheader with blue text color
    st.markdown("<h3 style='color:#6498C1;'>Master Part</h3>", unsafe_allow_html=True)

    # The rest of your Streamlit app goes here

if __name__ == "__main__":
    main()

# Form to create Master Component
master_name = st.text_input("Name: Enter the name of the Master Component", key="master_name")
if st.button("Create Master Component"):
    create_master_component(master_name)
    st.success(f"Master Component '{master_name}' created successfully!")

# View Master Components
#st.header("View Master Components and Associated Part Components Table")

# Display Master Components and their associated Part Components in a table

st.subheader("Child Table")


# Add custom CSS for styling
st.markdown(
    """
    <style>
        .st-eb {
            max-width: 50px !important;
            background-color: #BBBFC3 !important;
            color: black !important;
        }
        .st-eb option {
            background-color: #BBBFC3 !important;
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Rest of your Streamlit app code...

# Dropdown to select Master Component
selected_master = st.selectbox(
    "Select Master Component",
    ["Select a Master Component"] + [master["name"] for master in session.master_components],
    key="selected_master",
    format_func=lambda x: 'Select a Master Component' if x == 'Select a Master Component' else x  # To display the placeholder text properly
)
# Button to open the form for associating Part Components
if selected_master != "Select a Master Component":
    st.subheader(f"Master Component Details: {selected_master}")

    # Display details of the selected Master Component in a table
    details_table_data = []
    for master_component in session.master_components:
        if master_component["name"] == selected_master:
            details_table_data.append({"Attribute": "Name", "Value": master_component["name"]})
            details_table_data.append({"Attribute": "Associated Part Components", "Value": ", ".join(part["name"] for part in master_component["part_components"])})

    st.table(details_table_data if details_table_data else "No details available.")

    # Display existing Part Components
    existing_part_components = [part["name"] for master_component in session.master_components if master_component["name"] == selected_master for part in master_component["part_components"]]





