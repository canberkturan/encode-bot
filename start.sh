#!/bin/sh
docker build -t encode-bot . && docker run encode-bot &
