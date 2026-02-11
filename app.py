from flask import Flask, render_template, request
import numpy as np
import joblib
import warnings

warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load trained model
model = joblib.load("best_model.pkl")


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        try:
            study_hours = float(request.form["study_hours"])
            attendance = float(request.form["attendance"])
            mental_health = int(request.form["mental_health"])
            sleep_hours = float(request.form["sleep_hours"])
            part_time_job = request.form["part_time_job"]

            ptj_encoded = 1 if part_time_job == "Yes" else 0

            input_data = np.array([[study_hours, attendance, mental_health, sleep_hours, ptj_encoded]])

            prediction = model.predict(input_data)[0]
            prediction = max(0, min(100, prediction))
            prediction = round(prediction, 1)

        except:
            prediction = "Error in input values"

    return render_template("index.html", prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
