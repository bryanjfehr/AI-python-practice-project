''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask
from flask import request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    """Sends text from the HTML form for analysis using the method in sentiment_analysis.py"""
    #Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    #Pass the text to the analyzer function
    response = sentiment_analyzer(text_to_analyze)

    #Extract the label and score from the response
    label = response['label']
    score = response['score']

    #Check if label is None, indicating err or invalid response
    if label is None:
        return "Invalid input ! Try again."
    #Return a formatted string with the outputs
    return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    """Renders the webpage for entering Strings and viewing results."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
