from flask import Flask, request, jsonify, render_template
# import sqlite3

app=Flask(__name__)

# Creating sqlite
# conn = sqlite3.connect('cal1.sqlite')
# cur = conn.cursor()

# cur.execute('''
#     CREATE TABLE IF NOT EXISTS calculations (
#         id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         email TEXT NOT NULL,
#         subject TEXT NOT NULL,
#         message TEXT NOT NULL
#     )
# ''')
# conn.commit()

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')
    # return render_template('test.html')

@app.route('/api', methods=['POST'])
def createFeedback():
    data = request.json
    if 'name' not in data or 'email' not in data or 'subject' not in data or 'message' not in data:
        return jsonify({'error': 'Please provide all the info.'}), 400
    
    feedback_info = {
        'name': data['name'],
        'email': data['email'],
        'subject': data['subject'],
        'message': data['message']
    }

    print(feedback_info)
    return jsonify(feedback_info)

if __name__=='__main__':
    app.run(debug=True)