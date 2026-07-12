from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # host='0.0.0.0' permite que accedas desde tu móvil si está en el mismo WiFi
    app.run(debug=True)

