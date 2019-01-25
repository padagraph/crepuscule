import os
from _datetime import datetime
from .crepes import Paragraphe

from flask import Flask, render_template, request, jsonify, g, redirect, url_for, flash, abort


def create_app(test_config=None):

    print("starting crepuscule app")
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        ES_ADDRESS="localhost",
        HOST = "raindrop.re", # "http://localhost:5000",
    )

    conf_py = app.root_path + '/config.py'

    if os.path.exists(conf_py):
        app.logger.info ("reading config %s" % conf_py)
        app.config.from_pyfile(conf_py)

    if test_config is not None:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from flask_wtf.csrf import CSRFProtect
    app.config["WTF_CSRF_CHECK_DEFAULT"] = False
    csrf = CSRFProtect(app)
    csrf. init_app(app)

    from . import crepes
    crepes.init_app(app)


    @app.route('/')
    def index():
        data = {'a':1, 'b': 2}
        return render_template('index.xhtml', title="ceci est un titre", data=data)

    @app.route('/search/<string:q>', methods=['GET'])
    def test_query(q=None):
        limit = 50
        print("searching for %s" % q)
        if q:
            data = [p for p in Paragraphe.simple_search(q, 0, limit)]
            return jsonify(data)
        else:
            return jsonify([])

    return app
