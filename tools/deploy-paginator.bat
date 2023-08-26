@echo off
call appwrite functions createDeployment --functionId=64e9cd0497e2f9810861 --entrypoint='index.py' --code=.\functions\paginator --activate=true
