# dash-app-domino

### This repo provides a workaround to get the Dash app working in the Domino workspace.
### Configure path for dependencies. This is required for Domino. 
### There are two options for routing path which may vary depending on how to use the app.
### The first option is to publish app in domino project and the second option is to publish the app in the workspace.
### Learn more about Dash on Domino https://blog.dominodatalab.com/building-domino-web-app-dash/  

This repo contains one python file and two jupyter notebook files
1. dash-app-doc-inst.py
2. dash-app-workspace-min-change.ipynb
3. dash-app-workspace-max-change.ipynb

The 1. dash-app-doc-inst.py is based on our documentation which works completely fine for domino dash app.
The 2. and 3. jupyter files are the ways that dash app can be installed and used within Domino workspace.

The 2. has the minimum changes routing changes that can help to get the application working.
The 3. has more changes to get the routing working properly.



- With dockerfile instruction
```
USER root
RUN pip install flask==0.12 \
                dash==0.21.0 \
                dash-core-components==0.21.1\
                dash-html-components==0.9.0\
                dash-renderer==0.12.1\
                dash-table-experiments==0.6.0
USER ubuntu
```

- Without docker instruction examples are in the no-docker-instruction-dash-app
