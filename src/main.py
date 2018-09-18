from flask import *

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop


app = Flask(__name__)


def collect(resolution):
    pass


@app.route('/')
def index():
    return send_file("static/form.html")


@app.route('/api', methods=["POST"])
def process():
    print request.form.get("size")
    # todo logic here
    return redirect("/thanks")


@app.route('/favicon.ico')
def icon():
    return send_file("static/favicon.ico")


@app.route('/thanks')
def thanks():
    return send_file("static/thanks.html")


'''app.run(
    port=80,
    # debug=True
)'''

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()
