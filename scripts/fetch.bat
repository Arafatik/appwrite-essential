@echo off
if exist .\temp rmdir .\temp /s /q
mkdir .\temp
cd .\temp
call appwrite init project
call appwrite init collection
call appwrite init bucket
