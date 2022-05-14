from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    # once app launched to production environment, MUST set 'debug=False'

"""
To set up virtual environment, type this in terminal:

# Create virtual environment, which name is "env"
virtualenv env
# Activate "env"
source env\\Scripts\\activate.bat
# Provide environment variables
export FLASK_APP=application.py
export FLASK_DEBUG=1
# Run application
flask run
"""