from flask import Flask, jsonify, request
app = Flask (__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        input_json = request.get_json()
        print(input_json)
        return jsonify({"input_json": input_json}), 201
    else:
        return jsonify({"application": "JRE Flask App 01"})

if __name__ == '__main__':
    app.run(debug=True)
