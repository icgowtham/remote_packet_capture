# -*- coding: utf-8 -*-
"""Webapp entry-point."""

import os

from webapp import app, config

if __name__ == '__main__':
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    os.environ['basedir'] = BASE_DIR
    app.run(host=config.get('server_host', '0.0.0.0'),
            port=config.get('server_port', 8080),
            debug=True)
