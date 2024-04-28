from flask import Flask, request, render_template
import json

def read_json(json_path: str) -> dict:
	with open(json_path, 'r') as file:
		data = file.read()
		result = json.loads(data)
	return result


def write_json(json_path, data):
	json_data = json.dumps(data)
	with open(json_path, 'w') as file:
		file.write(json_data)


app = Flask(__name__)

admin_accaunt = { "login" : "admin", "password" : "cyninc0201"}
@app.route('/', methods=['GET', 'POST'])
def index():
	answer = "Log in"	
	if request.method == 'GET':
		
		return render_template('index.html', answer=answer), 200

	if request.method == 'POST':
		if admin_accaunt["login"] == request.form["login"] and admin_accaunt["password"] == request.form["password"]:
			answer = "You are logged in."
		else:
			answer = "You are fucked up."
		return render_template('index.html', answer=answer), 200

if __name__ == '__main__':
	app.run(debug=True)