from flask import Flask  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<string:name>')
def name(name):
    return "Hi " + name


@app.route('/say/<string:name1>')
def name1(name1):
    return "Hi " + name1

@app.route('/repeat/hello/<int:num>')
def repeat(num):
    return f"Hello " * num

@app.route('/repeat/<int:integer>/<string:str>')
def bonus(integer, str):
    return f"Hello " + (integer * str)

@app.route('/repeat/<int:integer>/<string:str>')
def anyWrite(integer, str):
    integer = 5
    str = "mounir"
    return f"Hello " + (integer * str)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
