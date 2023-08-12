from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/waktusolat/')
def waktusolat():

    #Shah Alam API Endpoint
    URL = 'https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=today&zone=sgr01'

    # A GET request to the API
    response = requests.get(URL)

    # Print the response
    response_json = response.json()
    print(response_json)
    print()
    return(response_json)


@app.route('/waktusolatklsac/')
def waktusolatklsac():


    URL = ['https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=today&zone=sgr01',
           'https://www.e-solat.gov.my/index.php?r=esolatApi/takwimsolat&period=today&zone=wly01']

    data = []

    for i in URL:
        data.append(requests.get(i).json())

    print(data)
    return (data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

