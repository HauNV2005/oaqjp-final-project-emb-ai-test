
"use strict";

/**
 * Send user input to Flask and display the emotion result.
 */
function RunSentimentAnalysis() {
    const input = document.getElementById("textToAnalyze");

    const resultElement = document.getElementById(
        "system_response"
    );

    const text = input.value;

    if (!text.trim()) {
        resultElement.textContent =
            "Invalid text! Please try again!";
        return;
    }

    fetch(
        "/emotionDetector?textToAnalyze=" +
        encodeURIComponent(text)
    )
        .then(async function (response) {
            const result = await response.text();

            if (!response.ok) {
                throw new Error(result);
            }

            return result;
        })
        .then(function (result) {
            resultElement.textContent = result;
        })
        .catch(function (error) {
            resultElement.textContent = error.message;
        });
}
