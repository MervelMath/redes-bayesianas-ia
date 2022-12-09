from flask import Flask, request
from flask_cors import CORS
import main
import json

api = Flask(__name__)
CORS(api)

@api.route('/', methods=['POST'])
def get_inferencia():
  content_type = request.headers.get('Content-Type')
  if (content_type == 'application/json'):
    json_request = [
      request.json["query_variable"],
      request.json["query_evidence"]
    ]

    try:
      inferencia = main.gerar_inferencia(json_request)

      json_response = {
        "inferencia": str(inferencia)
      }

      return json.dumps(json_response)
    except Exception as ex:
      return ex
  else:
    return 'Content-Type not supported!'

if __name__ == '__main__':
    api.run()