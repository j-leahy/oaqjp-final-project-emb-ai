import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=obj, headers=header)
    formatted = json.loads(response.text)
    emotions = formatted['emotionPredictions'][0]['emotion']

    anger_score =   emotions['anger']
    disgust_score = emotions['disgust']
    fear_score =    emotions['fear']
    joy_score =     emotions['joy']
    sadness_score = emotions['sadness']

    dominant_emotion = ''
    top_score = 0
    for item in emotions.items():
        if item[1] > top_score:
            top_score = item[1]
            dominant_emotion = item[0]

    result={
    'anger':   anger_score,
    'disgust': disgust_score,
    'fear':    fear_score,
    'joy':     joy_score,
    'sadness': sadness_score,
    "dominant_emotion": dominant_emotion
    }

    return result