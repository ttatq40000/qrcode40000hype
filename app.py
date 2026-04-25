from flask import Flask, render_template_string, request, render_template
from flask_qrcode import QRcode


app = Flask(__name__)
QRcode(app)

#адреса страниц
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/qr-generator', methods=['GET', 'POST'])
def qr_generator():
    qr_data = None
    if request.method == 'POST':
        qr_data = request.form['data']
    return render_template('qr_generator.html', qr_data=qr_data)

@app.route("/history")
def history():
    return render_template('history.html')

@app.route("/types")
def types():
    return render_template('types.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/gen")
def gen():
    return render_template('gen.html')

if __name__=='__main__':
    app.run(debug=True)