#! /bin/sh
# to start the server
echo "\x1B[05mStart of the AMP back\x1B[0m"
uvicorn app.main:app --reload
