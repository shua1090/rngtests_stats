sudo apt-get update
sudo apt-get install openjdk-11-jdk

git clone https://github.com/originell/jpype.git
cd jpype
python setup.py install
sudo rm -r jpype

pip3 install pycryptodome