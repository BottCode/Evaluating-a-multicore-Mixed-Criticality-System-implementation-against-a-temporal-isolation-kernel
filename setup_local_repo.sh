#!/bin/sh

sudo apt install python3-tk -y
sudo apt-get install python3-pil python3-pil.imagetk -y
pip3 install -r requirements.txt

git submodule update --init --recursive

git submodule update --recursive --remote
