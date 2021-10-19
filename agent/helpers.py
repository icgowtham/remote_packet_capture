# -*- coding: utf-8 -*-
"""Helper functions."""
import subprocess

from logger import get_logger

LOGGER = get_logger()


def execute_shell_cmd(cmd):
    """
    Function to run a command on the current shell.

    :param cmd: str
        The command to run.
    :return: str
        Output of the executed command.
    """
    try:
        out = subprocess.run(cmd, check=True, shell=True, universal_newlines=True,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return out.stdout
    except subprocess.CalledProcessError as cpe:
        err_msg = cpe.output or cpe.stdout or cpe.stderr
        LOGGER.error(err_msg)
        return cpe.returncode, err_msg
    except Exception:  # pylint: disable=broad-except
        LOGGER.exception('Unknown Exception. Could NOT run command {cmd}. %s'.format(cmd=cmd))
