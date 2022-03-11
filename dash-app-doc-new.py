import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import os

df = pd.read_csv(
    'https://raw.githubusercontent.com/plotly/'
    'datasets/master/gapminderDataFiveYear.csv')

app = dash.Dash()

# Configure Dash to recognize the URL of the container
user = os.environ.get("DOMINO_PROJECT_OWNER")
project = os.environ.get("DOMINO_PROJECT_NAME")
portID = '8887' #  # string port id                                                ##### <-------------be adde
runid = os.environ.get("DOMINO_RUN_ID")
runurl = '/' + user + '/' + project + '/r/notebookSession/'+ runid + '/'

## To publish the app using domino app feature. This feature expects portID: '8888' ##### <-------------be removed
#app.config.update({                                                                ##### <-------------be removed
#'routes_pathname_prefix': runurl,                                                  ##### <-------------be removed
#'requests_pathname_prefix': runurl                                                 ##### <-------------be removed
#})                                                                                 ##### <-------------be removed
################################################################                                ##### <-------------be added
# Configure path for dependencies. This is required for Domino.                                 ##### <-------------be added
#Learn more about Dash on Domino https://blog.dominodatalab.com/building-domino-web-app-dash/   ##### <-------------be added
app.config.routes_pathname_prefix=''+portID+'/'                                                   ##### <-------------be added
app.config.requests_pathname_prefix=''+portID+'/'                                                 ##### <-------------be added
#################################################################                               ##### <-------------be added

# Set layout
app.layout = html.Div(style={'paddingLeft': '40px', 'paddingRight': '40px'}, children=[
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        step=None,
        marks={str(year): str(year) for year in df['year'].unique()}
    )
])


@app.callback(
    dash.dependencies.Output('graph-with-slider', 'figure'),
    [dash.dependencies.Input('year-slider', 'value')])
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for i in filtered_df.continent.unique():
        df_by_continent = filtered_df[filtered_df['continent'] == i]
        traces.append(go.Scatter(
            x=df_by_continent['gdpPercap'],
            y=df_by_continent['lifeExp'],
            text=df_by_continent['country'],
            mode='markers',
            opacity=0.7,
            marker={
                'size': 15,
                'line': {'width': 0.5, 'color': 'white'}
            },
            name=i
        ))

    return {
        'data': traces,
        'layout': go.Layout(
            xaxis={'type': 'log', 'title': 'GDP Per Capita'},
            yaxis={'title': 'Life Expectancy', 'range': [20, 90]},
            margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
            legend={'x': 0, 'y': 1},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(port=int(portID), host='0.0.0.0', debug=True)