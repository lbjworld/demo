#!/bin/bash

# input: tcp_addr, tcp_port
wait_tcp_dependency()
{
    local tcp_addr=$1;
    local tcp_port=$2;
    local testing_url="tcp://${tcp_addr}:${tcp_port}"

    # assign fd automatically
    # refer to http://stackoverflow.com/questions/8295908/how-to-use-a-variable-to-indicate-a-file-descriptor-in-bash
    while ! exec {id}<>/dev/tcp/${tcp_addr}/${tcp_port}; do
        echo "$(date) - trying to connect to ${testing_url}"
        sleep 1
    done   
}

echo "connecting to db ..."
wait_tcp_dependency ${DB_PORT_3306_TCP_ADDR} ${DB_PORT_3306_TCP_PORT}

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
