from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return send_file("static/form.html")

@app.route('/api',methods=["POST"])
def process():
    print request.form.get("size")
    #todo logic here
    return redirect("/thanks")

@app.route('/favicon.ico')
def icon():
    return send_file("static/favicon.ico")

@app.route('/thanks')
def thanks():
    return send_file("static/thanks.html")

app.run(
    port=80,
    debug=True
)
