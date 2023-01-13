# Remote Packet Capture (RPCap)
* A Python3 based application to start packet capture on specific interfaces on remote machines.

### Introduction
* `RPCap` is a Python3 based application to start packet capture on specific interfaces on remote machines.
* The application has two components: `server` and `agent`.
* The `agent` is a REST API server running on the remote machine.
* The `server` application acts as a master.
* It is developed mainly using Python3.
* The `server` is developed using Flask. Bootstrap along with some JQuery is used as part of rendering the HTML.
* The `agent` is developed using Sanic (Fast API).
* Both `server` and `agent` contain a config file which needs to updated appropriately before starting.

### Technology
`RPCap` is developed using Python 3 and makes use of:
* `Flask` - A Python based micro web framework. 
* `Bootstrap` - For rendering the components of the HTML page.
* `Sanic` - A Fast API, Python 3.7+ web server and web framework that's written to go fast.
* `JQuery` - To control some HTML rendition.

### Sample usage:
* On one terminal first run the server application:
```bash
$ cd remote_packet_capture/server
$ make setup-env
$ source .venv/bin/activate
$ python run.py
```
* Open a web browser and check http://<your machine's ip>:7581.
* For e.g., if the machine IP is x.x.x.x, then type http://x.x.x.x:7581
    * NOTE: Ingress and Egress traffic on port 7581 (or the configured port) should be enabled to view the application.
* On another machine run the agent application:
```bash
$ cd remote_packet_capture/agent
$ make setup-env
$ source .venv/bin/activate
$ python agent_rest_server.py
```


### Development
Clone the Git repo and follow the steps below on any linux machine.

    git clone https://github.com/icgowtham/remote_packet_capture.git

Server:

    cd remote_packet_capture/server
    make setup-env
    source .venv/bin/activate
    python run.py
    

Agent: 

    cd remote_packet_capture/agent
    make setup-env
    source .venv/bin/activate
    python agent_rest_server.py


### TODO
- Provide an option to fetch the captured PCAP file from the agent.
- Provide an option to show packet capture progress on the UI.



### Compliance

To validate compliance, complexity and coverage:

    cd server
    make compliance <code_path>

