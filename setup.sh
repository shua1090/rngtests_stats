sudo apt-get update
sudo apt-get install openjdk-11-jdk

sudo apt-get install python3-dev
git clone https://github.com/originell/jpype.git
cd jpype
pip3 install cython
sudo python3 setup.py install
cd ..
sudo rm -r jpype

pip3 install pycryptodome