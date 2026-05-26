import os
import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load TF-IDF files and dataframe
tfidf_matrix = pickle.load(open("tfidf_matrix.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))
df = pd.read_pickle("df.pkl")

def ask_gita(question, top_k=3):
    q_embedding = tfidf.transform([question])

    similarities = cosine_similarity(
        q_embedding,
        tfidf_matrix
    ).flatten()

    top_indices = similarities.argsort()[
        -top_k:
    ][::-1]

    answers = []

    for idx in top_indices:
        row = df.iloc[idx]

        answers.append({
            "Chapter": int(row["Chapter"]),
            "Verse": int(row["Verse"]),
            "Meaning": row["EngMeaning"],
            "Score": float(similarities[idx])
        })

    return answers

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["GET"])
def ask():
    question = request.args.get("question", "").strip()
    if not question:
        return jsonify({"error": "Question cannot be empty"}), 400
    
    try:
        answers = ask_gita(question)
        return jsonify({"answers": answers})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
