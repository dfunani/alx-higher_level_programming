#!/bin/bash
# curls to arg1 url
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
