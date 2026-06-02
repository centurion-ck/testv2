import joblib
import os

MODEL_PATH = "/app/model.pkl"
ENCODER_PATH = "/app/encoder.pkl"

model = joblib.load(MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

def predict_threat(process_name, cpu, memory):

    try:
        process_encoded = encoder.transform(
            [process_name]
        )[0]

    except:
        process_encoded = 0

    prediction = model.predict(
        [[
            process_encoded,
            cpu,
            memory
        ]]
    )[0]

    score = model.predict_proba(
        [[
            process_encoded,
            cpu,
            memory
        ]]
    )[0]

    if prediction == 1:

        return {
            "prediction":"malicious",
            "score":round(max(score),2)
        }

    return {
        "prediction":"normal",
        "score":round(max(score),2)
    }
