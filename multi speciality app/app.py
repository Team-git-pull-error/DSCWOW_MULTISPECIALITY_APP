# Import the required packages and libraries
from flask import Flask, render_template, url_for, request

# Initialise the flask app
app = Flask(__name__)

# To navigate the user to index page or main page
@app.route("/")
def main_page():
    return render_template("index.html")

# To navigate the user to skin cancer predictor web page
@app.route("/skin-cancer-predictor")
def skin_cancer_predictor():
    return render_template("skin-cancer-predictor.html")

# To upload the image and start machine learning techniques to determine the result
@app.route("/upload_skin_cancer_image", methods=['POST'])
def upload_skin_cancer_image():
    file_name = request.files['image']
    value = file_name.filename
    return value


# To start the flask application
if __name__ == "__main__":
    # NOTE: The application is in debug mode
    app.run(debug=True)
