#!/bin/bash
###############################################################################
# monitor.sh - Script to check whether the REST based file server is running  #
# and run it in the background, if it is not already running.                 #
# The script runs as a cronjob every 30 minutes on all days.                  #
###############################################################################
if [ -z "$1" ]; then
  echo -e "\nUsage '$0 <app_name>'!\n"
  exit 1
fi

ROOT_DIR=/home/ishwarachandra_g/dpi/rest_file_server
export PYTHONPATH=$ROOT_DIR:$PYTHONPATH

VENV=venv3
PY3=/usr/local/bin/python3.8
FROM="igowtham@microsoft.com"
RECIPIENTS="igowtham@microsoft.com"
SUBJECT="Alert: REST File Server Monitor - $(date '+%d/%m/%y')"

create_env() {
  if [ ! -d ${VENV} ]; then
    printf "\nPython Virtual Environment is not present. Creating ... "
    ${PY3} -m venv ${VENV}
    printf "Done\n"
    install_req_pkgs
  fi
}

install_req_pkgs() {
  cd "${ROOT_DIR}" || exit
  source ${VENV}/bin/activate
  printf "\nInstalling project requirements ... "
  pip install -q --upgrade pip
  pip install -q -r requirements.txt
  printf "Done\n"
}

restart_app() {
  create_env
  cd "${ROOT_DIR}" || exit

  if [ -d __pycache__ ]; then
    /bin/rm -rf __pycache__
  fi

  printf "\nActivating virtual environment ... "
  source ${VENV}/bin/activate
  printf "Done\n"
  printf "\nAttempting to restart '%s' ... " "$1"
  /usr/bin/nohup python3 "$1" </dev/null >"${ROOT_DIR}"/app.log 2>&1 &
  printf "Done\n"
  /usr/sbin/sendmail "${RECIPIENTS}" <<EOF
subject:$SUBJECT
from:$FROM
REST file server was down. Restarted.
EOF
}

PID=$(/usr/bin/pgrep -f "python3 $1")
if [[ "$PID" == "" ]]; then
  printf "'%s' is not running.\n" "$1"
  restart_app "$@"
  printf "'%s' was restarted.\n" "$1"
fi
