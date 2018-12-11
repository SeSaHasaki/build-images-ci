#!/usr/bin/env bash
export CHANGE_DIR=`git log -1 --name-only -- ../images/ | grep Dockerfile | awk -F "/" '{print$2}'`