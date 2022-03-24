#import subprocess
 
#def index():
#    subprocess.call("sudo pip install -r requirements_apps.txt", shell=True)
 
#index()

import dash
from dash import Dash
import dash_table
import pandas as pd
import os







portID = '8888'


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.update({'requests_pathname_prefix': '/{}/{}/r/notebookSession/{}/'.format(
  os.environ.get("DOMINO_PROJECT_OWNER"),
  os.environ.get("DOMINO_PROJECT_NAME"),
  os.environ.get("DOMINO_RUN_ID"))})



"""
runID = os.environ['DOMINO_RUN_ID']
user = os.environ['DOMINO_PROJECT_OWNER']
project = os.environ['DOMINO_PROJECT_NAME']
assets_path = '<Domino url>'+ user + '/' + project +'/notebookSession/' + runID + '/proxy/' + portID + '/assets/'

#set the external path to the assets folder
app = dash.Dash(assets_external_path = assets_path)
#app = dash.Dash()

app.scripts.config.serve_locally = True
app.css.config.serve_locally = True    
app = dash.Dash()
 
app.scripts.config.serve_locally = True
# app.css.config.serve_locally = True
 
################################################################
# Configure path for dependencies. This is required for Domino.
#Learn more about Dash on Domino https://blog.dominodatalab.com/building-domino-web-app-dash/

# For Dash >= 0.18.3
# app.config.update({
# #### as the proxy server may remove the prefix
# 'routes_pathname_prefix': ''+portID+'/',

# #### the front-end will prefix this string to the requests
# #### that are made to the proxy server
# 'routes_pathname_prefix': ''+portID+'/'
# })

# For Dash < 0.18.3
app.config.routes_pathname_prefix=''+portID+'/'
app.config.requests_pathname_prefix=''+portID+'/'
#################################################################

"""







    
    
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
app.layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])
 
 
if __name__ == '__main__':
    app.run_server(port=int(portID), host='0.0.0.0', debug=True) # Domino hosts all apps at 0.0.0.0:8888