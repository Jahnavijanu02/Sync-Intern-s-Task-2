from flask import Flask, render_template, request

app = Flask(__name__)

candidates = {}  # Dictionary to store candidates and their votes


@app.route('/')
def index():
    return render_template('index.html', candidates=candidates)


@app.route('/register', methods=['POST'])
def register():
    candidate_name = request.form.get('candidate_name')
    
    if candidate_name:
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
            return render_template('success.html', message=f"{candidate_name} registered successfully!")
        else:
            return render_template('error.html', message=f"{candidate_name} is already registered.")
    else:
        return render_template('error.html', message="Invalid candidate name.")


@app.route('/vote', methods=['POST'])
def vote():
    candidate_name = request.form.get('candidate_name')
    
    if candidate_name:
        if candidate_name in candidates:
            candidates[candidate_name] += 1
            return render_template('success.html', message=f"Vote for {candidate_name} recorded successfully!")
        else:
            return render_template('error.html', message=f"{candidate_name} is not a valid candidate.")
    else:
        return render_template('error.html', message="Invalid candidate name.")


if __name__ == '__main__':
    app.run(debug=True)
