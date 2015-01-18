# bigaspicam
Raspberry pi b+ hand held camera

This will be a raspberry pi b+ based portable camera with safe shutdown button, 
camera capture button, and hardware reset button.
It will use the standard RPi camera module.
The camera will run on batteries. 

I have chosen to puchase the PNG PowerPack BD7800.
It has 7800 mAh capacity, It has 5V 1A/2.4A usb ports(Max 2.4A) , a built in power switch, digital battery level display
and comes with a micro usb cable. Plug and play.
Its dimentions are a decent fit with the Rpi 

the camera will run two python scripts at start up from rc.local
TECshutdownpi.py for the safe shutdown button 
StandardCamLoopVersion.py for controls via a capture button and saving the captured file

Future possibilitys include a touch screen with icons to run different capture modes easly and see preview ,
flash, night vision, support for different camera modules, who knows?...
