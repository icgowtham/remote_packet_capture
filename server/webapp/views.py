# -*- coding: utf-8 -*-
"""View handler for the application."""
import logging

import requests
from core.logger import get_logger
from flask import abort, flash, has_request_context, render_template, request
from webapp import app, config

LOGGER = get_logger()


class RequestFormatter(logging.Formatter):
    """Custom request formatter for logging."""

    def format(self, record):
        """Overridden method."""
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)


formatter = RequestFormatter(
    '[%(asctime)s]: %(remote_addr)s requested %(url)s\n'
    '%(name)s: %(levelname)s: %(message)s : %(filename)s#%(lineno)d %(funcName)s'
)
LOGGER.handlers[0].setFormatter(formatter)


@app.route('/', methods=['GET', 'POST'])
def main_handler():
    """
    Main route handler.

    :param: None
    :return: object
        Redirect to the appropriate page.
    """
    nodes = ['']
    nodes.extend(config['nodes'])
    if request.method == 'POST':
        # client_ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
        node = request.form.get('nodeIp')
        interface = request.form.get('interface')
        capture_time = request.form.get('captureTime')
        url = ''.join(['http://', node, ':8998/v1/start_capture/?',
                       'interface={itf}'.format(itf=interface),
                       '&time={tm}'.format(tm=capture_time)])
        response = requests.get(url=url, verify=False)
        LOGGER.info(response.text)
        response.raise_for_status()
        if response.status_code == 200:
            flash('Successfully started packet capture!', 'success')
    return render_template('index.html', nodes=nodes)


@app.route('/v1/interfaces')
def get_interfaces():
    """
    Get list of interfaces from the remote node.

    :param: None
    :return: object
    """
    node = request.args.get('node')
    if node:
        url = ''.join(['http://', node, ':8998/v1/interfaces'])
        response = requests.get(url=url, verify=False)
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
    return abort(404)
