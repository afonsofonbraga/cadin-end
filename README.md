# cadin-end
## requestData.py

This code will request all debris data that currently orbits the earth. (Data providded by space-track)
Some configuration is required:

Provide a config file in the same directory as this file, called SLTrack.ini, with this format (without the # signs)
```
[configuration]
username = XXX
password = YYY
````
where XXX and YYY are your www.space-track.org credentials (https://www.space-track.org/auth/createAccount for free account)

All data will be stored into an SQL-based database.

## treatData.py

This code will acess add data providded by requestData and convert information into geodetic coordinates (with astropy python library), obtaining latitude, longitude and height at a certain time.

The result will also be stored into the database.

## api.py

The api.py will act as a rest server providing a json file with the data prodidded by treatData.py.
Cadin-app will make a request and display all the information in a GUI.
