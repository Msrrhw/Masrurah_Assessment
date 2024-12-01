from flask import Flask, jsonify, request
import requests

app = Flask(__name__, template_folder='../Masrurah_Assessment')

def generate_pascals_triangle(num_rows):
    triangle = []
    for i in range(num_rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

@app.route('/fetch', methods=['GET'])
def fetch_data():
    get_api = "https://assessment.takafulbrunei.com/v1/question/1" 
    try:
        response = requests.get(get_api)
        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return jsonify({"error": f"GET request failed with status code {response.status_code}"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/submit', methods=['POST'])
def submit_data():
   
    post_api = "https://assessment.takafulbrunei.com/v1/question/1"

    get_api = "https://assessment.takafulbrunei.com/v1/question/1"
    try:
        
        response = requests.get(get_api)
        if response.status_code != 200:
            return jsonify({"error": f"GET request failed with status code {response.status_code}"}), response.status_code
        data = response.json()
    except Exception as e:
        return jsonify({"error": f"Error fetching data from GET API: {str(e)}"}), 500

    id = data.get("id")
    num_row_list = data.get("numRowList")
    if not id or not isinstance(num_row_list, int):
        return jsonify({"error": "Invalid data format from GET API"}), 400

    pascals_triangle = generate_pascals_triangle(num_row_list)

    payload = {
        "id": id,
        "answer": pascals_triangle
    }
    try:
        post_response = requests.post(post_api, json=payload)
        if post_response.status_code == 200:
            return jsonify(post_response.json())
        else:
            return jsonify({"error": f"POST request failed {post_response.status_code}"}), post_response.status_code
    except Exception as e:
        return jsonify({"error": f"Error sending data to POST API: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
