import requests
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
    
@app.route('/discussion/<path:key>')
def get_discussion(key):
    discussion_uri = 'http://discussionapi.guardian.co.uk/discussion-api/discussion//' + key +'?displayThreaded=true'
    response = requests.get(discussion_uri)
    facebook_uri='https://graph.facebook.com/comments/?ids=http://gu.com/' + key
    return render_template('discussion.html', response=response.json)

if __name__ == '__main__':
    app.run(debug=True)