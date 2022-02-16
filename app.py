import altair as alt
from dash import Dash, html, Input, Output, dcc
from gapminder import gapminder


def plot_altair(xmax):
    chart = alt.Chart(gapminder[gapminder['lifeExp'] < xmax]).mark_point().encode(
        x='lifeExp',
        y='pop',
        tooltip='country').interactive()
    return chart.to_html()

app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            srcDoc=plot_altair(xmax=0),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        dcc.Slider(id='xslider', min=25, max=100)])
        
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xslider', 'value'))
def update_output(xmax):
    return plot_altair(xmax)

if __name__ == '__main__':
    app.run_server(debug=True)