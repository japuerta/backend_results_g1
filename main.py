import json

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from waitress import serve

if __name__ == '__main__':
    print("hola G1")
    """
    data_config = load_file_config()
    print("Server runing: http://"+data_config.get('url-backend')+":"+str(data_config.get('port')))
    serve(app, host=data_config.get('url-backend'), port=data_config.get('port'))
    """

