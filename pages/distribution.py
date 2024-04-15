import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output


dash.register_page(__name__, path='/distribution', name="Target Distribution 📊")

# Define the data dictionary with multiple rows
data_dict = {
    'Label': ['1 Malicious', '0 Benign'],
    'Count': [196868, 1190978]
}

# Create a pandas DataFrame from the dictionary
cic_df = pd.DataFrame(data_dict)

####################### PIE CHART ################################
def create_pie_chart():
    fig = px.pie(cic_df, names='Label', values='Count', title='Class Distribution')
    return fig

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("🔎 Target Class : Binary"),
    html.B("0 : Benign"),
    html.Br(),
    html.Br(),
    html.B("1 : Malicious (DoS)"),
    html.Br(),
    html.Br(),
    dcc.Graph(id="pie_chart"),
])

####################### CALLBACKS ################################
@callback(Output("pie_chart", "figure"), [Input("pie_chart", "id")])
def update_pie_chart(selected_id):
    # Create pie chart based on selected column
    return create_pie_chart()
