from flask import Flask, request, render_template
import pickle


app = Flask(__name__)

with open('model.pkl','rb') as file:
    model = pickle.load(file)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        hours = float(request.form['hours'])
        pred = model.predict([[hours]])[0]

        return render_template('index.html',prediction_text=f'Predicted Score: {pred:.2f}')
    except ValueError:
        return render_template('index.html',predicition_text= "Please enter a valid number.")
if __name__=="__main__":
    app.run(debug=True)
