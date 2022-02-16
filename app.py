import altair as alt
from dash import Dash, html, Input, Output, dcc
from gapminder import gapminder




app = Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

server = app.server

app.layout = html.Div([
        html.Iframe(
            id='scatter',
            # srcDoc=plot_altair(xcol),
            style={'border-width': '0', 'width': '100%', 'height': '400px'}),
         dcc.Dropdown(
            id='xcol-widget',
            value='lifeExp',  # REQUIRED to show the plot on the first page load
            options=[{'label': col, 'value': col} for col in gapminder.columns])])
        
@app.callback(
    Output('scatter', 'srcDoc'),
    Input('xcol-widget', 'value'))
def plot_altair(xcol):
    chart = alt.Chart(gapminder).mark_point().encode(
        x=xcol,
        y='pop',
        tooltip='country').interactive()
    return chart.to_html()

if __name__ == '__main__':
    app.run_server(debug=True)