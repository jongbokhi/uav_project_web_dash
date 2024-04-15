import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output


dash.register_page(__name__, path='/distribution', name="Target Distribution 📊")

####################### LOAD DATASET #############################
cic_df = pd.read_csv("C:\\Users\\jongb\\Desktop\\multipage_dash_dashboard-main\\extracted_ft_dos.csv")

####################### HISTOGRAM ###############################
def create_pie_chart():
    label_counts = cic_df['Label'].value_counts()
    fig = px.pie(names=label_counts.index, values=label_counts.values, title='Class Distribution')
    return fig

####################### WIDGETS ################################
columns = ['Label']
dd = dcc.Dropdown(id="dist_column", options=columns, value='Label', clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.H2("🔎 Target Class : Binary"),
    html.B("0 : Benign "),
    html.Br(),
    html.Br(),
    html.B("1 : Malicious(DoS)"),
    html.Br(),
    html.Br(),
    dcc.Dropdown(id="dist_column", options=[{'label': col, 'value': col} for col in columns], value='Label', clearable=False),
    dcc.Graph(id="pie_chart"),
])

####################### CALLBACKS ################################
@callback(Output("pie_chart", "figure"), [Input("dist_column", "value")])
def update_pie_chart(selected_column):
    # Create pie chart based on selected column
    return create_pie_chart()

