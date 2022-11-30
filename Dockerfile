from ubuntu:20.04
run apt-get update -y && apt install git curl wget -y
#run apt install software-properties-common -y
arg DEBIAN_FRONTEND=noninteractive
#run add-apt-repository ppa:deadsnakes/ppa
run apt install python3-pip  -y
run git clone https://github.com/kubemq-io/kubemq-Python.git
workdir kubemq-Python
expose 50000
expose 9090
expose 8080
env ADDR=0.0.0.0
run pip3 install kubemq
run pip3 install --upgrade pip setuptools wheel
run pip3 install .
run pip3 uninstall protobuf -y && pip3 install protobuf==3.20.0
env PYTHONUNBUFFERED=1
copy publisher.py .
entrypoint ["python3"]
cmd ["-u","publisher.py"]
