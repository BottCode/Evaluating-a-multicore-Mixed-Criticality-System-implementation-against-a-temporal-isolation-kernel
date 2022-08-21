#!/bin/sh

pip3 install -r requirements.txt

git submodule update --init --recursive

git submodule update --recursive --remote
