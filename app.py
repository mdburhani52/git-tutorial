from flask import Flask, request, redirect, render_template
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client.todoDB
collection = db.items

@app.route('/')
def home():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')

    if item_name and item_desc:
        collection.insert_one({
            'name': item_name,
            'description': item_desc
        })
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
