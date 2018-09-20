from flask import Flask
from flask import send_file
from flask import redirect
from flask import request

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()


app = Flask(__name__)

selquery = "SELECT size FROM data WHERE size = ?"
oldquery = "UPDATE data SET count = count + 1 WHERE size = ?"
newquery = "INSERT INTO data VALUES (?,?)"


def collect(resolution):
    c = cursor.execute(selquery, (resolution,))
    result = c.fetchall()
    if result == []:
        print "New stuff!!!"
        c = cursor.execute(newquery,(resolution,1,))
    else:
        print "Old stuff!!!"
        c = cursor.execute(oldquery,(resolution,))
    connection.commit()


@app.route('/')
def index():
    return send_file("static/form.html")


@app.errorhandler(500)
def page_not_found(e):
    return redirect("/500")


@app.route('/api', methods=["POST"])
def process():
    resolution = request.form.get("size")
    collect(resolution)
    # todo logic here
    return redirect("/thanks")


@app.route('/404')
def notfound():
    return send_file("static/404.html")


@app.route('/<path:path>')
def statics(path):
    try:
        return send_file("static/"+path)
    except IOError:
        try:
            return send_file("static/"+path+".html")
        except IOError:
            return redirect("/404")


#develop server
'''app.run(
    port=80,
    debug=True
)'''

def main():
    try:
        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(5000)
        IOLoop.instance().start()
    except Exception:
        main()
        print("restart!")

main()