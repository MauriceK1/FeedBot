#!/usr/bin/env bash

workon cv
python3 i2c.py | python3 detect.py | python3 send.py