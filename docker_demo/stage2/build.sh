#!/bin/bash

set -ue

sudo docker --dns 208.67.220.220 --dns 208.67.222.222 build -t demo_stage2 .

