# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
application = Flask(__name__)
application.debug=True
application.secret_key = 'AKIASKWOKSTJBTF526PE'
# use decorators to link the function to a url
@application.route('/')
@application.route('/index')
def home():
    return render_template('welcome.html')



# start the server with the 'run()' method
if __name__ == '__main__':
    application.run(host='0.0.0.0')
