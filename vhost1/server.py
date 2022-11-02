
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        return current_time

if __name__ == '__main__':

	app.run(debug=True, host='0.0.0.0', port=80)


