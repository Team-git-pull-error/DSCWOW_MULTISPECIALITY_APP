# Import the required packages and libraries
from flask import Flask, render_template, url_for, request, redirect
import os
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


# To navigate the user to skin cancer predictor results web page
@app.route("/skin-cancer-predictor-results")
def skin_cancer_predictor_results():
    return render_template("skin-cancer-predictor-results.html")


# To upload the image and start machine learning techniques to determine the result
@app.route("/upload_skin_cancer_image", methods=['POST'])
def upload_skin_cancer_image():
    my_test_image = request.files['image']
    image_name = my_test_image.filename
    if my_test_image is not None:
        my_path = os.path.join("multi speciality app/static/uploads/images/temp/", str(image_name))
        my_test_image.save(my_path)
        ###########################
        #   WRITE AI CODE HERE    #
        ###########################
        return redirect("/skin-cancer-predictor-results")

# To start the flask application
if __name__ == "__main__":
    # NOTE: The application is in debug mode
    app.run(debug=True)