from flask import Flask, request, jsonify, render_template
app= Flask(__name__)


@app.route("/")
def show_form():
    return render_template('index.html')

@app.route("/check_password", methods=["POST"]) # its a wrapper class that uses URL to wrap a python function 
def check_password(): # it depends on us what we want to do with the acquired data
    name=request.form.get("username") # the function should use the id mentioned in the html otherwise it wont work
    password=request.form.get("password") # these  will get the password and username submited in the form
    print(name, password)
    return "username and password received"

if __name__== "__main__":
    app.run(host="0.0.0.0",port=8000)
