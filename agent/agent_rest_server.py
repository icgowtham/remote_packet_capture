# -*- coding: utf-8 -*-
"""REST based agent API server."""
import os
from datetime import datetime

from sanic import Sanic, exceptions, response
from yaml import safe_load

from helpers import execute_shell_cmd
from logger import get_logger

__author__ = 'Ishwarachandra Gowtham'
__email__ = 'ic.gowtham@gmail.com'

LOGGER = get_logger()
app = Sanic(__name__)


@app.route('/v1/interfaces', methods=['GET'])
async def get_interfaces(request):
    """API endpoint handler to return active network interfaces."""
    cmd = ' | '.join(["ifconfig",
                      "grep 'UP'",
                      "awk '{print $1}'",
                      "grep ':'",
                      "tr -d ':'",
                      "grep -v lo"])
    cmd_out = execute_shell_cmd(cmd)
    if isinstance(cmd_out, tuple):
        LOGGER.error(str(cmd_out))
        raise exceptions.ServerError
    interfaces = list(filter(None, cmd_out.split('\n')))
    return response.json(
        {'interfaces': interfaces}
    )


@app.route('/v1/start_capture', methods=['GET'])
async def start_packet_capture(request):
    """API endpoint handler to start packet capture on a particular interface."""
    intf = request.args.get('interface')
    capture_time = request.args.get('time')
    base_dir = os.path.abspath(os.path.dirname(__file__))
    pcap_file = os.path.join(base_dir, '{itf}_{tm}.pcap'.format(
        itf=intf, tm=datetime.now().strftime('%d_%m_%y_%H_%M_%S')))
    cmd = ' '.join(['nohup',
                   'timeout {tm}'.format(tm=capture_time),
                   '{tool}'.format(tool=CONFIG.get('packet_capture_tool', 'tcpdump')),
                    '-i {itf}'.format(itf=intf),
                    '-w {fl}'.format(fl=pcap_file),
                    '&'
                   ])
    cmd_out = execute_shell_cmd(cmd)
    if isinstance(cmd_out, tuple):
        LOGGER.error(str(cmd_out))
        raise exceptions.ServerError
    return response.json(
        {'status': 'Packet capture started', 'file_name': pcap_file}
    )


@app.route('/v1/files/pcap', methods=['GET'])
async def get_captured_pcap(request):
    """API endpoint handler to send back captured PCAP file."""
    pcap_file_name = request.args.get('file_name')
    if not os.path.isfile(pcap_file_name):
        msg = 'File "{fl}" does not exist.'.format(fl=pcap_file_name)
        exceptions.FileNotFound(message=msg, path='.',
                                relative_url='/v1/files/pcap')
    return await response.file_stream(pcap_file_name)


if __name__ == '__main__':
    with open('config.yaml') as stream:
        CONFIG = safe_load(stream)
    app.run(host='0.0.0.0',
            port=int(CONFIG.get('port', 8998)),
            debug=True)
