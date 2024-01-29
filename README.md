# Badge-generator
Badge generator
Description

The Badge Generator is a simple web application that allows users to create badges by uploading a 512 x 512 image. The uploaded image is then processed to be displayed as a circular badge with cheerful colors. This project utilizes Flask for the backend, Pillow for image adjustments, UUID is used to provide each browser session with a unique identifier and a combination of HTML and CSS for the front-end design.

Features

Image Processing: Converts the uploaded image into a circular shape.
Colorful Design: Adds happy colors to enhance the visual appeal of the badge.
User-Friendly: Simple and intuitive web interface for easy badge creation.


Requirements

Python 3.x
Flask
Pillow
UUID

Installation

First, pip must be installed in order for flask, pillow, and uuid to be installed using pip.
The tutorial for how PIP can be installed is provided through this link that provides a step by step process.
For Windows: https://phoenixnap.com/kb/install-pip-windows
For Mac: https://phoenixnap.com/kb/install-pip-mac
Next, in order to install flask and pillow both the links below provide the commands to install them both using pip.
PILLOW: https://pypi.org/project/pillow/
FLASK: https://pypi.org/project/Flask/
To install the UUID the command used is pip install uuid.
Finally after configuring everything, the github project should be installed and must be compiled using a pyhton compiler.
Then, using the terminal to configure the project these commands must be used in the same order as below.
 export FLASK_APP=main,
 export FLASK_ENV=development,
 flask run.
After running a link will be generated, click on it and the usage of how to use the website is down below. 

Usage

Open the web application in your browser.
Upload a 512 x 512 image.
Click on the "Upload Avatar" button.
Now your newly generated avatar will appear.
Each user will have a unique identifier for their browser session using UUID.


Credits

Developed by Ismail ElDahshan
Inspired by the joy of creating cheerful badges!
