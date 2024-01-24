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

# Streamlit app
st.header("Create Part Component")

# Name input field
part_name = st.text_input("1. Name: Enter the name of the Part Component")
if not part_name:
    st.warning("Please enter the name of the Part Component.")

# Quantity input field
quantity = st.number_input("2. Quantity: Specify the quantity if applicable", min_value=0)

# Dropdown to select Master Component
selected_master = st.selectbox("3. Select Master Component (father)", ["Select a Master Component"] + [master["name"] for master in master_components])

# Button to submit the form
if st.button("Create Part Component"):
    if selected_master == "Select a Master Component":
        st.warning("Please select a Master Component.")
    else:
        try:
            # Logic to save the Part Component with the entered information
            associate_part_components(selected_master, part_name, quantity)
            st.success(f"Part Component '{part_name}' created successfully and associated with '{selected_master}'!")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# View Master Components and their associated Part Components Table
st.header("Master Table")

# Display Master Components and their associated Part Components in a table
table_data = []
for master_component in master_components:
    for part_component in master_component["part_components"]:
        table_data.append({"Master Component": master_component["name"], "Part Component": part_component["name"], "Quantity": part_component["quantity"]})

if table_data:
    st.table(table_data)
else:
    st.info("No Part Components associated yet.")






