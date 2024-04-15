import pandas as pd
import dash
from dash import html, dash_table, dcc
import plotly.graph_objects as go

dash.register_page(__name__, path='/dataset', name="Dataset 📋")

####################### LOAD DATASET #############################
cic_df = pd.read_csv("pages/dataset.py/sample_ft_dos.csv")


# Take the first 10 rows of the DataFrame
a = cic_df.head(10)

# Define the layout for the Dash app
layout = html.Div(children=[
    html.Br(),
    html.H2("💾 CSE-CIC-IDS2018 dataset"),
    html.Br(),
    html.B("🗹 captures a variety of contemporary network attacks"),
    html.Br(),
    html.Br(),
    html.B("🗹 the dataset is meticulously labelled, making it ideal for supervised learning methods"),

    html.Br(),
    html.Br(),

    # Display DataTable for the subset of DataFrame `a`
    html.P("🔎 Subset of DataFrame:", style={"fontSize": "16px", "fontWeight": "bold"}),
    dash_table.DataTable(
        # Pass the data as list of dictionaries (records)
        data=a.to_dict('records'),
        # Set the page size for pagination
        page_size=10,  # Adjusted to display fewer rows per page for better visibility
        # Style for cells in the table
        style_cell={
            "backgroundColor": "white",
            "color": "black",
            "fontSize": "14px",
            "textAlign": "left",
            "whiteSpace": "normal",
            "height": "auto",
        },
        # Style for headers
        style_header={
            "backgroundColor": "dodgerblue",
            "fontWeight": "bold",
            "color": "white",
            "padding": "10px",
            "fontSize": "16px",
        },
        # Define columns based on DataFrame columns
        columns=[{"name": col, "id": col} for col in a.columns],
    ),
])
