import csv
from flask import Flask
from flask import render_template
app = Flask(__name__)


def get_csv():
	csv_path = './static/la-riots-deaths.csv'
	csv_file = open(csv_path, 'r')
	csv_obj = csv.DictReader(csv_file)
	csv_list = list(csv_obj)
	return csv_list
	
	
# CSV list coverts to a list	
# You use DictReader when you have a file of headers. 
# Each row will be a list and each item will be a dictionary 
# Where the keys are the headers and the values in that row. 
# r is read	
# .= start where you currently are
# decorator is @app.route('/') route is a function inside the function we created. 

@app.route('/')
def index():
	template = 'index.html'
	object_list = get_csv()
 	return render_template(template, object_list=object_list)	
 	
#template is a variable. index.html is a string
#return is the result of the function 


if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)

