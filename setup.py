#!/usr/bin/python3
import os
import fill_db
import initialize_db
import sys
from time import sleep

def main():
    try:
        docker_compose("up -d")
        init_db()
        load_db()
        sleep(100000)
    except Exception as e:
        print(e)
        docker_compose("down")

def docker_compose(command):
    print("running docker-compose " + command)
    os.system("docker-compose " + command)

def load_db():
    fill_db.main()

def init_db():
    initialize_db.main()

    

main()
