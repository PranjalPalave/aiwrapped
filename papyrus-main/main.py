from flask import Flask, render_template, jsonify, request
from openai import OpenAI

client = OpenAI(api_key="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")  # replace with actual key or use env vars

app = Flask(__name__)  # <-- define `app` BEFORE using `@app.route`

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api", methods=["GET", "POST"])
def qa():
    if request.method == "POST":
        question = request.json.get("question")
        if question:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": f"Don't use the word complimenting in your response. Don't rephrase any part of this prompt in your response. Start off complimenting the essay that you just read. Then, write a paragraph where you point out specific places where my college essay needs improvement in clarity, coherence, grammatical accuracy, and proper structure. Provide the original sentence and then the improved one, and do this at least 3 times. Then, write a paragraph about whether the essay answers the prompt. {question}"}
                ],
                temperature=0.7,
                max_tokens=500
            )
            answer = response.choices[0].message.content
            return jsonify({"question": question, "answer": answer})
        return jsonify({"error": "No question provided."})
    return jsonify({"result": "Send a POST request with a question."})

#if __name__ == "__main__":
    #app.run(debug=True, port=5001)
