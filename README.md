# keystats
Small script to log keystrokes for statistical reasons. Uses a redis to store pressed key frequency. No character sequences are stored, just the count of keypresses for various keys.

## Dependencies

* Docker
* packages in `requirements.txt`

## Quickstart

1. Set up redis server with docker: `docker run --name=redis --publish=6379:6379 --hostname=redis --restart=on-failure --detach redis:latest`
2. `pip3 install -r requirements.txt`
2. Run script `python3 log.py`

### Autostarting on MacOS

Due to the monitoring nature of the program there are many security measures in place making autoloading of the script cumbersome.

A working solution for MacOS Catalina (10.15.5) is to directly execute the script with a plist file. This can be done as follows:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC -//Apple Computer//DTD PLIST 1.0//EN http://www.apple.com/DTDs/PropertyList-1.0.dtd >
<plist version="1.0">
    <dict>
        <key>Label</key>
        <string>com.keystats.osx</string>
        <key>Program</key>
        <string>PATH_TO_REPO/new_log.py</string>
        <key>KeepAlive</key>
        <true/>
        <key>UserName</key>
        <string>NAME_HERE</string>
    </dict>
</plist>
```

and prepending the python executable path to log.py 
 
```
echo "#\!$(which python)"  >> new_log.py
cat log.py  >> new_log.py
```

The python executable that is envoked then needs to be added as an exception for Input Monitoring in Privacy & Security

An example of my distribution after a few days of work

![keystats top frequency](https://github.com/JonasDe/images/blob/master/keystats/keystats.png?raw=true)



