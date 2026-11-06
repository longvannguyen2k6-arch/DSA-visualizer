from flask import Flask, render_template, request, jsonify
from  algorithms.sorting import bubble_sort,insertion_sort

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/sort", methods=["POST"])
def api_sort():
    data = request.get_json()
    arr = data.get("array", [5, 2, 8, 1, 9, 3])
    algo = data.get("algorithm", "bubble")

    if algo == "bubble_sort":
        steps = list(bubble_sort(arr))
    elif algo == "insertion_sort":
        steps = insertion_sort(arr)
    else:
        steps = []

    return jsonify({"steps": steps})

if __name__ == "__main__":
    app.run(debug=True)