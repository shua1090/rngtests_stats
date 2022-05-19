sudo apt-get update
sudo apt-get install openjdk-11-jdk

sudo apt-get install python3-dev
pip3 install cython
git clone https://github.com/originell/jpype.git
cd jpype
sudo python3 setup.py install
cd ..
sudo rm -r jpype

pip3 install pycryptodome