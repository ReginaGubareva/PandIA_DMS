Firstly, set venv. For the Pycharm go to the File -> Settings -> in search line put "Interpreter" ->
open interpreter settings -> add interpreter -> add local -> Virtualenv Environment

Then install requirements.txt: 
`pip install requirements.txt`

Dash framework version is in scripts/dash_app.py file
To test it, just uncomment this code and run this file.

To launch Flask app use the following command: 
`flask --app app run`


The files divided by the part of analysis:
base analysis
exploratory analysis
clusters

All analysis includes Braganca and whole Portugal. If the function works with Braganca
datasets, it has prefix br. If the function works with portugal it has prefix pt.
All functions have the comment what chart you should get: table, heatmap, line or geo.
