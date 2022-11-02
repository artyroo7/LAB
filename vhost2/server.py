
from flask import Flask, request
import ftplib
from urllib.request import urlopen
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def home():
    if(request.method == 'GET'):
        response = urlopen('https://api.meteo.lt/v1/places/kaunas/forecasts/long-term')
        return json.loads(response.read())

@app.route('/backup', methods = ['GET'])
def backup():
    with open('/tmp/backup.json', 'a') as f1:
        f1.write(str(home()))
    
    with open('/opt/backup/backup.json', 'w+') as f2:
        f2.write(str(home()))
        return 'OK1OK2'

@app.route('/push', methods = ['GET'])
def push():
    session = ftplib.FTP('vhost3', 'ftp', 'ftp')
    file = open('/tmp/backup.json','rb')
    session.storbinary('STOR backup.json', file)
    file.close()
    session.quit()
    return str(session)

if __name__ == '__main__':

	app.run(debug=True, host='0.0.0.0', port=80)


