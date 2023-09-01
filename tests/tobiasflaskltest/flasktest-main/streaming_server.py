from flask import Flask, render_template, Response
import stream
import test
from stream_test_lib import *


app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    stream.start_stream()
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def hello_world():
    return render_template('test.html')
    #return test.hello_world()
    

"""
@app.route('/stream', methods=['GET','POST'])
def start_stream():
    return render_template('owlcam_stream.html')
"""
@app.route('/stream', methods=['GET', 'POST'])
def generate_frames():
    return Response(stream.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=FRAME')

if __name__ == "__main__":
    app.run()