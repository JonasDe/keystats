# keystats
Small script to log keystrokes for statistical reasons. Uses a redis to store pressed key frequency. No character sequences are stored, just the count of keypresses for various keys.

## Dependencies

* Docker
* requirements.txt

## Quickstart

1. Set up redis server with docker: `docker run --name=redis-devel --publish=6379:6379 --hostname=redis --restart=on-failure --detach redis:latest`
2. Run script `python3 log.py`


