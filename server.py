
"""Flask server for the Emotion Detector application."""

import requests
from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    """Analyze the emotion of the submitted text."""

    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    try:
        result = emotion_detector(text_to_analyze)

        if result["dominant_emotion"] is None:
            return "Invalid text! Please try again!", 400

        return (
            "For the given statement, the system response is "
            f"{result}. The dominant emotion is "
            f"{result['dominant_emotion']}."
        )

    except requests.exceptions.RequestException:
        return (
            "Cannot connect to IBM Watson Emotion Detection API. "
            "Please try again later.",
            503
        )

    except (ValueError, KeyError, IndexError):
        return "Unable to analyze the text.", 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
