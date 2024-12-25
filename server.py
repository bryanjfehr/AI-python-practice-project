''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
import flask from Flask
from flask import requests, render_template
from sentiment_analysis import sentiment_analyzer
#Initiate the flask app : TODO

@app.route("/sentimentAnalyzer", methods="POST")
def sent_analyzer(text_for_analysis):
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''#TODO

