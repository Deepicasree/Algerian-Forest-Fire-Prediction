from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Model and Scaler
model = pickle.load(open("ridge.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:
        Temperature = float(request.form["Temperature"])
        RH = float(request.form["RH"])
        Ws = float(request.form["Ws"])
        Rain = float(request.form["Rain"])
        FFMC = float(request.form["FFMC"])
        DMC = float(request.form["DMC"])
        ISI = float(request.form["ISI"])
        Classes = float(request.form["Classes"])
        Region = float(request.form["Region"])

        data = np.array([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])

        scaled_data = scaler.transform(data)

        prediction = model.predict(scaled_data)

        return render_template("home.html",prediction_text=f"Predicted FWI : {prediction[0]:.2f}")

    except Exception as e:
        return render_template(
            "home.html",
            prediction_text=f"Error: {e}"
        )


if __name__ == "__main__":
    app.run(debug=True)