"""This server hosts the emotional detector application
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    """Takes in some text and returns an emotion analysis on it
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    output = f"For the given statement, the system response is 'anger': {response['anger']}, "
    output2 = f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
    output3 = f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
    return output + output2 + output3 + f"The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """Renders the app UI at the home page
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
