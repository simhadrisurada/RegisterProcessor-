from flask import Flask, render_template_string, request, jsonify
import json
import os
import shutil

app = Flask(__name__)

DATA_FILE = 'events_db.json'
EVENTS_DIR = 'hosted_events'


if not os.path.exists(EVENTS_DIR):
    os.makedirs(EVENTS_DIR)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def index():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            return render_template_string(f.read())
    except FileNotFoundError:
        return "Error: index.html not found. Please ensure it is in the same folder."

@app.route('/api/save_event', methods=['POST'])
def save_event():
    event_data = request.json
    event_name = event_data['name']
    
    db = load_data()
    db[event_name] = event_data
    save_data(db)
    
    path = os.path.join(EVENTS_DIR, event_name)
    if not os.path.exists(path):
        os.makedirs(path)
        
    return jsonify({"status": "success"})

@app.route('/api/delete_event', methods=['POST'])
def delete_event():
    data = request.json
    event_name = data.get('name')
    
    
    db = load_data()
    if event_name in db:
        del db[event_name]
        save_data(db)
    
    
    path = os.path.join(EVENTS_DIR, event_name)
    if os.path.exists(path):
        shutil.rmtree(path) 
        
    return jsonify({"status": "success"})

@app.route('/api/register_user', methods=['POST'])
def register_user():
    reg_data = request.json
    event_name = reg_data['event']
    name = reg_data['name']
    email = reg_data['email']
    phone = reg_data['phone']
    
    event_path = os.path.join(EVENTS_DIR, event_name)
    if not os.path.exists(event_path):
        os.makedirs(event_path)
    
    for filename in os.listdir(event_path):
        file_path = os.path.join(event_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if f"Email: {email}" in content:
                    return jsonify({"status": "error", "message": "Email already registered!"}), 400
                if f"Phone: {phone}" in content:
                    return jsonify({"status": "error", "message": "Phone number already registered!"}), 400

    safe_email = email.replace('@', '_at_').replace('.', '_')
    file_name = f"{safe_email}.txt"
    with open(os.path.join(event_path, file_name), 'w', encoding='utf-8') as f:
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Phone: {phone}\n")

    return jsonify({"status": "success"})

@app.route('/api/get_events', methods=['GET'])
def get_events():
    return jsonify(load_data())

if __name__ == '__main__':
    print("Server running at http://127.0.0.1:5000")

    app.run(debug=True, port=5000)
