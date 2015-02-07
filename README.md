# raspberry-pi-gpio-control-panel
A simple way to control the GPIOs on the raspberry pi through a web browser.
This is made for a Raspberry Pi B+ but would work with a regular Raspberry Pi B also (just don't use the extra GPIOs).
The file server.py (included in this project in the python folder) must be running on your raspberry pi.
In order to do that download server.py to your pi.  
Then from a terminal on your pi cd to the directoy where server.py is located.
Then type: sudo python server.py
Now launch the index.html file on any computer (with the supporting directories included in this project).
You may need to edit the IP address that we have provided as a default.
To do this open up the main.js file and find this line:
var host = "ws://192.168.1.133:8765/";
Change the IP address to the ip address that matches your Raspberry Pi's IP address.  Be sure to leave the port 8765.
