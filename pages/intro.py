import dash
from dash import html
from PIL import Image

pil_image = Image.open("experimental_design.png")

dash.register_page(__name__, path='/', name="Introduction 😃")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("✅ Objective"),
        html.Br(),
        html.B("1️⃣ Check the vulnerability of ML-based NIDS to adversarial attacks"),
        html.Br(),
        html.Br(),
        html.B("2️⃣ increase the robustness of ML-based NIDS through adversarial training"),
        
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("✅ Procedure"),
        html.B("1.Preprocessing dataset"),
        html.Br(),
        html.Br(),
        html.B("2.Feature Selection"), 
        html.Br(),
        html.Br(),
        html.B("3.Build Machine Learning Models and Evaluation "),
        html.Br(),
        html.Br(),
        html.B("------------ the purpose of Adversarial attacks and Adversarial training-----------"),
        html.Br(),
        html.Br(),
        html.B("4.Build WCGAN-GP Model"),
        html.Br(),
        html.Br(),
        html.B("5.Adaptive Perturbation Pattern Method (A2PM)"),
        html.Br(),
        html.Br(),
        html.B("6.The result"),
        html.Br(),
    ]),

    html.Div(children=[
        html.Br(),
        html.H2("✅ Experimental Design"),
        html.Img(src=pil_image,  # Specify the path to your image
             style={'width': '80%', 'height': 'auto'})  # Adjust width and height as needed

    ]),
], className="bg-light p-4 m-2")