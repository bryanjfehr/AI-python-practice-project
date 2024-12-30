import requests
import json  # Import the requests library to handle HTTP requests

def sentiment_analyzer(text_to_analyze):  # Define a function named sentiment_analyzer that takes a string input (text_to_analyse)
    """Sends text to the watson library for sentiment analysis, then formats the response as JSON and returns the score and label as a dictionary pair"""
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    
    response = requests.post(url, json=myobj, headers=header)  # Send a POST request to the API with the text and headers
    
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    
    #If the response code is 500, set label and score to "None"
    elif response.status_code == 500:
        label = None
        score = None

    #Return the label and score as a dictionary
    return {'label': label, 'score': score}