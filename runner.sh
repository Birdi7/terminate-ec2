#!/usr/bin/env bash

cd $PROJECT_PATH
$(pwd)/.venv/bin/python3 main.py &> /tmp/auto_terminate_ec2.log.2