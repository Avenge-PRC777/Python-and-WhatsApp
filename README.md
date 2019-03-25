# Python-and-WhatsApp
This repo will contain the code for controlling WhatsApp through Python, Selenium.

Make sure you do pip install selenium
The wp2.py file contains the code!

The following steps are ultra necessary for code to run:
i)You need to check the version of your Chrome browser and download the driver accordingly
from the internet.

ii)You need to put the absolute path of the driver, the syntax has been taken care of in
the code, just check and change the relevant directories.

AFTER THESE TWO STEPS YOU ARE "NOT" GOOD TO GO...
HE HE...
iii)You see a "class_name" variable in the code, you have to find it by going
to web.whatsapp->Inspect(or Ctrl+Shift+I)->then find the class name of the text
box, by opening up the "div"s. Change the class_name accordingly

iv)See the find_element_by_class_name method, it also has a class name of the button
that is to be clicked for sending the message. Find and change the class name similarly.

NOW YOU ARE GOOD TO GO:
Just run the script.

DEBUGGING:
i) Cache error- Try restarting the browser, check if you have correct version of
chrome and driver or not.
ii) Any other compilation error- Check that class names are correct and most importanlt
if the code says that a certain name does not exist then there might be issues in
connectivity.
