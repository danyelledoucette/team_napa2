"""
Routes and views for the flask application.
"""
import json
import urllib.request
import os

from datetime import datetime
from flask import render_template, request, redirect
from FlaskAppAML import app
#testing
from FlaskAppAML.forms import SubmissionForm

#API Key from AZURE ML after Web Service is deployed
QMLKEY_RED=os.environ.get('API_KEY', "q3EOLRefFR97PJ9Vew877BFx1gy5PIcqlUtfs3dKKPCUPoUJXe2+pWYuAdwGzmROjajreDredWsgzydhH+4Iig==")
QMLURL_RED = os.environ.get('URL', " https://ussouthcentral.services.azureml.net/workspaces/9abe4feec820456f9b9ac830f4fe67c6/servic[…]b7b6130fd10049/execute?api-version=2.0&details=true")
QMLHEADERS_RED = {'Content-Type':'application/json', 'Authorization':('Bearer '+ QMLKEY_RED)}

QMLKEY_WHITE=os.environ.get('API_KEY', "Szy1uEq4V2an8f3BU8ulQcsClY7VslC+vUbMFkrR3Lyhjo/j9A0Iy6Nix1vM4DHps1YsqV86dxlzkUrCSBc7UQ==")
QMLURL_WHITE = os.environ.get('URL', "https://ussouthcentral.services.azureml.net/workspaces/9abe4feec820456f9b9ac830f4fe67c6/servic[…]59cfbafff50224/execute?api-version=2.0&details=true")
QMLHEADERS_WHITE = {'Content-Type':'application/json', 'Authorization':('Bearer '+ QMLKEY_WHITE)}

@app.route('/', methods=['GET', 'POST'])
@app.route('/qml', methods=['GET', 'POST'])
def qml():
    """Renders the home page which is the CNS of the web app currently, nothing pretty."""
    form = SubmissionForm(request.form)
    if request.method == 'POST' and form.validate():
        reddata =  {
              "Inputs": {
                "input1": {
                  "ColumnNames": ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"],
                  "Values": [ [
                      10.2,
                      0,
                      # <0.24-0.61>,
                      0.5,
                      1.9,
                      0.1,
                      16.2,
                      40.2,
                      1.0,
                      3.2,
                      0,
                      # <0.63-0.87>,
                      # <8.4-8.7>,
                      0,
                      5.2
                    ]
                  ]
                }
              },
              "GlobalParameters": {}
            }
        whitedata =  {
              "Inputs": {
                "input1": {
                  "ColumnNames": ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density", "pH", "sulphates", "alcohol", "quality"],
                  "Values": [ [
                      7.2,
                      #<0.2-0.3>
                      0,
                      0.3,
                      9.2,
                      0.052,
                      #<14-47>
                      0,
                      154.2,
                      1.0,
                      3.2,
                      0.4,
                      #<8.8-10.1>
                      0,
                      6.0
                    ]
                  ]
                }
              },
              "GlobalParameters": {}
            }
        # Serialize the input data into json string
        redbody = str.encode(json.dumps(reddata))
        whitebody = str.encode(json.dumps(whitedata))
        # Formulate the request
        #req = urllib.request.Request(URL, body, HEADERS)
        req = urllib.request.Request(BRAIN_URL, body, HEADERS)
        # Send this request to the AML service and render the results on page
        try:
            response = urllib.request.urlopen(req)
            respdata = response.read()
            result = json.loads(str(respdata, 'utf-8'))
            return render_template(
                'result.html',
                title="This is the result from AzureML running our example Student Brain Weight Prediction:",
                result=result)

        # An HTTP error
        except urllib.error.HTTPError as err:
            result="The request failed with status code: " + str(err.code)
            return render_template(
                'result.html',
                title='There was an error',
                result=result)
            #print(err)

    # Just serve up the input form
    return render_template(
        'form.html',
        form=form,
        title='Run App',
        year=datetime.now().year,
        message='Demonstrating a website using Azure ML Api')



@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
