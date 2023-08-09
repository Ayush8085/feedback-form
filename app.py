from flask import Flask, request, jsonify, render_template
import sqlite3

app=Flask(__name__)

# Creating sqlite
conn = sqlite3.connect('feedback.sqlite')
cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        subject TEXT NOT NULL,
        message TEXT NOT NULL
    )
''')
conn.commit()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/api/create-feedback', methods=['POST'])
def createFeedback():
    data = request.json
    if 'name' not in data or 'email' not in data or 'subject' not in data or 'message' not in data:
        return jsonify({'error': 'Please provide all the info.'}), 400
    
    name = data['name']
    email = data['email']
    subject = data['subject']
    message = data['message']

    if name=='' or email=='' or subject=='' or message=='':
        return jsonify({'error': 'Please fill all the fields!!'}), 400
    
    # Connect to DB
    conn = sqlite3.connect('feedback.sqlite')
    cur = conn.cursor()
    # Save in sqlite
    cur.execute('INSERT INTO feedback (name, email, subject, message) VALUES (?, ?, ?, ?)',
              (name, email, subject, message))
    conn.commit()
    
    feedback_info = {
        'name': name,
        'email': email,
        'subject': subject,
        'message': message
    }

    return jsonify(feedback_info)

if __name__=='__main__':
    app.run(debug=True)