#!/bin/bash
# a Bash script that takes in,  sends a request to that URL and displays response size
curl -sI $1 | grep "Content-Length:" | cut -d " " -f 2
