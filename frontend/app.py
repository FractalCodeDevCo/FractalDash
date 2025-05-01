import dash
from dash import dcc, html, Input, Output, State
import plotly.express as px
import pandas as pd
import base64
import io

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("FractalDash – Dashboard Interactivo Fractal 🌌", style={'textAlign': 'center'}),
    
    dcc.Upload(
        id='upload-data',
        children=html.Div(['📁 Arrastra o ', html.A('selecciona tu archivo')]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'borderRadius': '10px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),

    html.Div(id='output-graph'),
])

@app.callback(
    Output('output-graph', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_graph(contents, filename):
    if contents is None:
        return html.Div("Carga claramente un dataset para visualizar resultados.")
    
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        elif 'xls' in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return html.Div('Formato no soportado. Usa CSV o Excel.')
    except Exception as e:
        return html.Div(f'Error al leer el archivo: {str(e)}')

    fig = px.line(df, title=f'Dataset cargado: {filename}')
    return dcc.Graph(figure=fig)

if __name__ == '__main__':
    app.run(debug=True)  # <- Esta es la línea corregida claramente
