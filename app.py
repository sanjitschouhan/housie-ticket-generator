from flask import Flask, request, render_template

from housie import get_ticket
from presenter import get_matrix, add_value

app = Flask(__name__)


@app.route('/generate_ticket')
def generate_ticket(username):
    if not username:
        username = request.args.get('username', None)
    if not username:
        return "Required param: username"
    username = username.split("@")[0].lower()
    print(f"Generating board for {username}")
    return get_ticket(username)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/send_ticket', methods=['post'])
def send_ticket():
    username = request.form.get('username', None)
    ticket = generate_ticket(username)
    return ticket


@app.route('/present/<code>', methods=['get', 'post'])
def presenter(code):
    current = "--"
    if request.method == 'POST':
        number = int(request.form.get("number", None))
        if number and 1 <= number <= 90:
            current = number
            add_value(code, number)
    matrix = get_matrix(code)
    return render_template("presenter.html", matrix=matrix, current=current)


if __name__ == '__main__':
    app.run()
