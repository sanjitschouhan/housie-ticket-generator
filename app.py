from flask import Flask, request

from tambola import get_board

app = Flask(__name__)


@app.route('/')
def hello_world():
    username = request.args.get('username', None)
    if not username:
        return "Required param: username"
    username = username.split("@")[0].lower()
    print(f"Generating board for {username}")
    return get_board(username)


if __name__ == '__main__':
    app.run()
