Start up the timelapse.py python script, then run node app.js. 

The python script starts capturing images through the Raspberry Pi's camera every x seconds. 

The NodeJS application runs an Express server, providing an endpoint to view the latest captured image through a browser b visiting '/picture' at the Pi's ip address.
