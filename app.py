from flask import Flask, redirect
import os

app = Flask(__name__)
client_id = os.environ['client_id']


@app.route('/')
def hello_world():
    return redirect('https://accounts.spotify.com/en/authorize?'
                    'client_id=' + client_id +
                    '&response_type=token&redirect_uri=https:%2F%2Fgoogle.com')


if __name__ == '__main__':
    app.run()
