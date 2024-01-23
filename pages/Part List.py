import streamlit as st
import pandas as pd

# Set page config to change background color
st.set_page_config(
    page_title="Your App Title",
    page_icon=":robot:",
    layout="wide",
    initial_sidebar_state="expanded",
)
st.markdown(
    """
    <style>
        body {
            background-color: #080707;
            color: white;
            font-family: serif;
            primaryColor=#7b2828;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# Add custom CSS for styling
custom_css = """
    <style>
        body {
            background-color: white;
            color: white;
        }
        .sidebar .sidebar-content {
            background-color: gray;
        }
        .stTable {
            color: white;
            margin-bottom: 10px; /* Add margin between table rows */
        }
        /* Style anchor tag for yashkawa schedule */
        .sidebar a[href="#yashkawa-schedule"] {
            color: white;
            text-decoration: none;
        }
        .sidebar .css-15ziabu {
            margin: 0 !important;
            padding: 0 !important;
        }
    </style>
"""


st.markdown(custom_css, unsafe_allow_html=True)


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
# Use HTML and CSS to style the subheader with a blue color
def main():
    # Display a subheader with blue text color
    st.markdown("<h3 style='color:#6498C1;'>Part List</h3>", unsafe_allow_html=True)

    # The rest of your Streamlit app goes here

if __name__ == "__main__":
    main()

import streamlit as st

# Sample data structure to store Master and Part Components
master_components = []

# Function to create Master Component
def create_master_component(name):
    # Logic to save the Master Component with the entered information
    master_components.append({"name": name, "part_components": []})

# Function to associate Part Components with a Master Component
def associate_part_components(master_name, part_name, quantity):
    # Logic to associate Part Components with the selected Master Component
    for master_component in master_components:
        if master_component["name"] == master_name:
            master_component["part_components"].append({"name": part_name, "quantity": quantity})

# Name input field
part_name = st.text_input("Name: Enter the name of the Master Component", key="master_name")
# Quantity input field
quantity = st.number_input("2. Quantity: Specify the quantity if applicable", min_value=0)

# Dropdown to select Master Component
selected_master = st.selectbox("3. Select Master Component (father)", ["Select a Master Component"] + [master["name"] for master in master_components])

# Button to submit the form
if st.button("Create Part Component"):
    if selected_master == "Select a Master Component":
        st.warning("Please select a Master Component.")
    else:
        # Logic to save the Part Component with the entered information
        # Display success message or handle errors
        associate_part_components(selected_master, part_name, quantity)
        st.success(f"Part Component '{part_name}' created successfully and associated with '{selected_master}'!")

# View Master Components and their associated Part Components Table
st.header("View Master Components and Associated Part Components Table")

# Display Master Components and their associated Part Components in a table
table_data = []
for master_component in master_components:
    for part_component in master_component["part_components"]:
        table_data.append({"Master Component": master_component["name"], "Part Component": part_component["name"], "Quantity": part_component["quantity"]})

if table_data:
    st.table(table_data)
else:
    st.info("No Part Components associated yet.")





