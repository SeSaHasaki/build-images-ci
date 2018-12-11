#!/usr/bin/env bash
git log -1 --name-only -- ../images/ | grep Dockerfile | awk -F "/" '{print$2}' >> CHANGE_DIR
echo "已执行sh脚本"