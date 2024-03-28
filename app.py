from flask import Flask, render_template, request
from utils.import_functions import import_cars_by_brand


# initiate a Flask instance
app = Flask(__name__)


# add the inital route
@app.route('/')
def index():
    return render_template("index.html")


# route for getting cars by brand
@app.route('/get_cars_brand', methods=['GET', 'POST'])
def get_cars_brand():

    # check the type of request
    if request.method == 'POST':

        # get the car
        selected_brand = request.form.get("brand")
        cars_list = import_cars_by_brand(selected_brand)
    
        return render_template("cars_brands.html", 
                               cars_list=cars_list,
                               selected_brand=selected_brand)

    return render_template("cars_brands.html")

# run the application
if __name__ == "__main__":
    app.run()