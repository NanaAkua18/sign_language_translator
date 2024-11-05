# Import the Flask class from the flask module to create the web application.
from flask import Flask, render_template, Response

# Import the generate_frames function from the datatesting module.
# This function is assumed to generate frames from a video source (e.g., a webcam).
from datatesting import generate_frames

# Create an instance of the Flask class. The app variable will be our WSGI application.
app = Flask(__name__)

# Define the route for the homepage ('/'). When a user visits the root URL, 
# the index function will be called to handle the request.
@app.route('/')
def index():
    # Render and return the 'index.html' template when the root URL is accessed.
    return render_template('index.html')

# Define the route for the video feed ('/video_feed'). When a user visits this URL,
# the video_feed function will be called to handle the request.
@app.route('/video_feed')
def video_feed():
    # Return the response generated by the generate_frames function.
    # The response is streamed to the client as a multipart MIME type, which is necessary for 
    # displaying video streams in the browser.
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# If this script is executed directly (as the main program), the Flask application will start.
# The debug=True flag enables debug mode, which provides useful error messages and auto-reloads the server
# when code changes are made.
if __name__ == '__main__':
    app.run(debug=True)