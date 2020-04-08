#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template
from person import Person

app = Flask(__name__, static_url_path="/static")
pers = Person('usama')
course = "Objektorienterad Python"

@app.route("/")
def main():
    """ Main route """
    return (render_template("index.html", name=pers.name, img=pers.get_dp(),
                            age=pers.age(), course=course))


@app.route("/redovisning")
def redovisning():
    """ Redovisning route """
    return render_template("redovisning.html", course=course)


@app.route("/about")
def about():
    """ About route """
    return render_template("about.html", img=pers.get_dp(), course=course)


@app.errorhandler(404)
def page_not_found(e):
    """
    Handler for page not found 404
    """
    #pylint: disable=unused-argument
    return "Flask 404 here, but not the page you requested."


@app.errorhandler(500)
def internal_server_error(e):
    """
    Handler for internal server error 500
    """
    #pylint: disable=unused-argument
    import traceback
    return "<p>Flask 500<pre>" + traceback.format_exc()


if __name__ == "__main__":
    pers = Person('usama')

    app.run()
