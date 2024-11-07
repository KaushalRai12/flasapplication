# Import necessary modules from Flask framework
from flask import Flask, render_template

# Create a Flask application instance
app = Flask(__name__)

# Define route for the root URL ('/')
@app.route('/')
def index():
    # Render and return the index.html template
    return render_template('index.html')

# Only run the app if this file is run directly (not imported)
if __name__ == '__main__':
    # Start the Flask development server with debug mode enabled
    app.run(debug=True)
