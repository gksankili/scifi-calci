from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        expr = request.form.get('expression', '')
        try:
            result = eval(expr, {"__builtins__": None}, math.__dict__)
        except Exception as e:
            result = f"Error: {str(e)}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5011)