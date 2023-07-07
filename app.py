from flask import Flask, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def run_ui():
    result = subprocess.run(['python', 'ui.py'], capture_output=True, text=True)
    output = result.stdout  # Fetch the output of the script
    return render_template('output.html', output=output)

if __name__ == '__main__':
    app.run()
