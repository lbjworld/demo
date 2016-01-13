#!/bin/bash

rm -f ./siege.log
siege --time=30S --benchmark --concurrent=100 --log=./siege.log http://localhost:5000/hello/

