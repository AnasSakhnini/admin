import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

navbar = html.Nav([
    dcc.Link('Home', href='/'),
    dcc.Link('About', href='/about'),
    dcc.Link('Signin', href='/signin'),
    dcc.Link('Megamenu', href='/megamenu')
])

app.layout = html.Div([
    navbar,
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return html.Div([html.H1('Home Page')])
    elif pathname == '/about':
        return html.Div([html.H1('About Page')])
    elif pathname == '/signin':
        return html.Div([html.H1('Signin Page')])
    elif pathname == '/megamenu':
        return html.Div([html.H1('Megamenu Page')])
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)

