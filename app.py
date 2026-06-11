from flask import Flask, render_template, request
from shopping_engine import get_recommendations

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    no_results = False
    query = ""

    if request.method == "POST":

        query = request.form["query"]

        recommendations = get_recommendations(query)

        if len(recommendations) == 0:
            no_results = True

    return render_template(
        "index.html",
        recommendations=recommendations,
        no_results=no_results,
        query=query
    )

if __name__ == "__main__":
    app.run(debug=True)