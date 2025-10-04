from flask import Flask, request, abort

app = Flask(__name__)

@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST'
    return response

@app.route('/', methods=['POST'])
def rec():
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)
    print(body)
    return "OK"

if __name__ == '__main__':
    app.run(port=5000)
