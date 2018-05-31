#!/bin/bash
INSTALL_DIR=/opt/trailblaze
git clone https://github.com/wpr101/AgileTrailblazers.git "$INSTALL_DIR"
cd "$INSTALL_DIR"
pyvenv .
source bin/activate
pip3 install flask
pip3 install gevent
cd "$INSTALL_DIR"
python3 Trailblaze.py
