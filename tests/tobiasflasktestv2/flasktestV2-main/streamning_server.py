from flask import Flask, render_template, Response
from stream_test_lib import *
import stream

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/stream', methods=['GET', 'POST'])
def generate_frames():
    return Response(stream.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=FRAME')

if __name__ == "__main__":
    app.run()
