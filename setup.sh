sudo apt update && sudo apt dist-upgrade -y
sudo apt install -y nano vim python-is-python3 python3-venv python3-pip
python -m venv .venv && source .venv/bin/activate
echo -e "" > hello.py
