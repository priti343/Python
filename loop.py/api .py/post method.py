
from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
@app.route('/api/post_example', methods=['POST'])

def post_example():

    try:

        # Get data from the POST request

        data = request.get_json()
 
        # Assuming the POST request contains a 'number' field

        if 'number' in data:

            user_input = data['number']

            result = 18 + user_input
 
            # Perform additional operations (subtract, multiply, divide) if needed

            result = result - 5

            result = result * 2

            result = result / 3
 
            # Return the result in JSON format

            return jsonify({'result': result})
 
        else:

            return jsonify({'error': 'Missing or invalid input'})
 
    except Exception as e:

        return jsonify({'error': str(e)})
 
if __name__ == '__main__':

    app.run(debug=True)
from flask import Flask, request, jsonify
 
app = Flask(__name__)
 
# Assume a variable to store data

stored_data = None
 
@app.route('/api/put_example', methods=['PUT'])

def put_example():

    try:

        # Get data from the PUT request

        data = request.get_json()
 
        # Assuming the PUT request contains a 'value' field

        if 'value' in data:

            global stored_data

            stored_data = data['value']
 
            # You can perform additional operations on stored_data if needed
 
            return jsonify({'message': 'Data updated successfully'})
 
        else:

            return jsonify({'error': 'Missing or invalid input'})
 
    except Exception as e:

        return jsonify({'error': str(e)})
 
@app.route('/api/get_data', methods=['GET'])

def get_data():

    global stored_data

    return jsonify({'data': stored_data})
 
if __name__ == '__main__':

    app.run(debug=True)
