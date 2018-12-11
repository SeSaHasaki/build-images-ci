#!/usr/bin/env bash
git log -1 --name-only -- ../ | grep Dockerfile | awk -F "/" '{print$2}' >> CHANGE_DIR