def emotion_detector(text_to_analyze):

    if "happy" in text_to_analyze.lower():
        return {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.90,
            "sadness": 0.04,
            "dominant_emotion": "joy"
        }

    if "hate" in text_to_analyze.lower():
        return {
            "anger": 0.90,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.01,
            "sadness": 0.04,
            "dominant_emotion": "anger"
        }

    return {
        "anger": 0.10,
        "disgust": 0.10,
        "fear": 0.10,
        "joy": 0.10,
        "sadness": 0.10,
        "dominant_emotion": "joy"
    }
