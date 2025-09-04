from flask import Flask, request, jsonify
from app import summarize_text, extract_text_from_file, answer_question
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploaded_files'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
        
    text = data.get('text', "")
    if not text:
        return jsonify({"error": "Text is required"}), 400
        
    style = data.get('style', "general")
    length = data.get('length', "medium")
    character = data.get('character', "neutral")
    
    result = summarize_text(text, length, style, character)
    return jsonify({"summary": result})



@app.route('/analyze', methods=['POST'])
def analyze_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    question = request.form.get('question')
    if not question:
        return jsonify({"error": "Question is required"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    content = extract_text_from_file(file_path)
    if "error" in content:
        return jsonify({"error": content}), 500
    
    answer = answer_question(content, question)
    
    return jsonify({
        "filename": file.filename,
        "question": question,
        "answer": answer
    })

if __name__ == '__main__':
    app.run(debug=True)