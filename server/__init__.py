# -*- coding: utf-8 -*-
# pylint: disable=wrong-import-position,wrong-import-order
"""Webapp module. Gateway to external apps."""

import os
from yaml import safe_load
from flask import Flask

__author__ = 'Ishwarachandra Gowtham'
__email__ = 'ic.gowtham@gmail.com'

parent_path = os.path.dirname(os.path.dirname(__file__))
config_file = os.path.join(parent_path, 'config.yaml')
with open(config_file) as stream:
    config = safe_load(stream)

app = Flask(__name__,
            template_folder='templates',
            static_folder='static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '0g1o2w3t4h5a6m'

from webapp import views  # noqa: F401
