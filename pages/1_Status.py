import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import os




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
            color: #f4fbfb;
            font-family: serif;
            primaryColor=#7b2828;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ... Your existing code ...

# Custom CSS for styling
custom_css = """
<style>
/* Add your custom CSS styles here */

/* Example styles for the sidebar */
.sidebar .sidebar-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.sidebar img {
    margin-bottom: 10px; /* Add margin to the bottom of the image */
    border-radius: 50%;
}

/* Example styles for the tables */
table {
    border-collapse: collapse;
    width: 100%;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}

th {
    background-color: #5C5E62;
    color: white;
}

/* Add more styles as needed */

</style>
"""




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

st.title("Schedule Production Work Order")

# Change the title color to blue
st.markdown('<style>h1{color: #6498C1;}</style>', unsafe_allow_html=True)


def main():
    # Define a list of robots
    robot_options = ["Robot1", "Robot2", "Robot3", "Robot4"]

    # Create a single line for selecting a robot and date range
    selected_robot, start_date, end_date = st.columns([1, 1, 1])

    # Dropdown menu to select a robot
    selected_robot_value = selected_robot.selectbox("Select a Robot", robot_options, key='selected_robot')

    # Date range input fields for start and end dates with pink background color
    default_end_date = datetime.now().date()
    default_start_date = default_end_date - timedelta(days=7)  # Default to a 7-day range

    # Input field for start date with pink background color
    start_date_value = start_date.date_input("Start Date", default_start_date, key='start_date')

    # Input field for end date with pink background color
    end_date_value = end_date.date_input("End Date", default_end_date, key='end_date')

    # Apply pink background color to the date input fields using CSS
    st.markdown(
        """
        <style>
            .css-2trqyj {
                background-color: pink !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display the selected robot and date range
    #st.write(f"You selected: {selected_robot_value}, Start Date: {start_date_value}, End Date: {end_date_value}")

if __name__ == "__main__":
    main()




data2 = {
    'Order Id ': ['1', '2'],
    'Part Name<br>(Father)': ['PICKUP FRAME', 'V6_Gate_Tail'],
    'Weekly Quantity': ['50', '50'],
    'Completion Status': ['43%','60%'],
}

# Second dataframe
df2 = pd.DataFrame(data2)

styled_df2 = df2.style.hide(axis="index").set_table_styles([
    {'selector': '', 'props': [('background-color', '#BBBFC3'), ('color', 'black'), ('text-align', 'center')]},
    {'selector': 'th', 'props': [('background-color', '#BBBFC3'), ('color', 'black')]},
])

# Convert the styled DataFrame to HTML
html_code = styled_df2.to_html(escape=False)

print(html_code)


print(html_code)

    # Manipulate the HTML string to include the width property
html_code = html_code.replace('<table', '<table style="width:1300px; height:150px; "')


st.markdown(html_code, unsafe_allow_html=True)

    # Add a horizontal rule with black color
st.markdown("<hr style='border: 2px solid #FFFEFE;'>", unsafe_allow_html=True)

data2 = {
        'Order Id ': ['1', '1', '1'],
        'Child Component<br> Name)': ['FANCANTINE-A40-ST1', 'COCLE-A-40-ST1', 'RACCOGLITORE_V6_DX-K56790'],
        'Quantity to be<br> produced': ['20', '30', '35'],
        'Quantity  Produced': ['30', '20', '15'],
    }

df2 = pd.DataFrame(data2)

styled_df2 = df2.style.hide(axis="index").set_table_styles([
        {'selector': '', 'props': [('background-color', '#BBBFC3'), ('color', 'black')]},
        {'selector': 'th', 'props': [('background-color', '#BBBFC3'), ('color', 'black')]},
    ])
    

# Convert the styled DataFrame to HTML
html_code = styled_df2.to_html(escape=False)

    # Manipulate the HTML string to include the width property
html_code = html_code.replace('<table', '<table style="width:900px; margin-left:150px;"')

st.markdown(html_code, unsafe_allow_html=True)
     

