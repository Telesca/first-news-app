from flask import Flask
from flask import render_template
app = Flask(__name__)

#decorator follows. route is a function inside the function we created. 

@app.route('/')

def index():
	template = 'index.html'
	return render_template(template)
	
#template is a variable. index.html is a string
#return is the result of the function 


if __name__ == '__main__':
    # Fire up the Flask test server
    app.run(debug=True, use_reloader=True)

