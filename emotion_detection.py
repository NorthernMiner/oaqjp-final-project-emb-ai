def emotion_detector(text_to_analyze):

    text = text_to_analyze.lower()

    if "happy" in text or "glad" in text or "love" in text:
        return {
            "anger": 0.01,
            "disgust": 0.02,
            "fear": 0.03,
            "joy": 0.90,
            "sadness": 0.04,
            "dominant_emotion": "joy"
        }

    if "hate" in text or "mad" in text:
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
        "joy": 0.60,
        "sadness": 0.10,
        "dominant_emotion": "joy"
    }
