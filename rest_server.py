from flask import Flask, request
from flask_cors import CORS
import main

api = Flask(__name__)
CORS(api)

@api.route('/', methods=['GET'])
def home():
  return "Home Page"

@api.route('/', methods=['POST'])
def get_inferencia():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    json_request = [
      request.json["query_variable"],
      request.json["query_evidence"]
    ]

    try:
      json_response = backend.gerar_inferencia(json_request)

      return json_response
    except Exception as ex:
      return ex
  else:
    return 'Content-Type not supported!'

if __name__ == '__main__':
    api.run()
