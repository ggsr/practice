# practice

Couple of things you'll need/want. 

First first, clone the repository. ( git clone https://etc-etc

First, is python. https://www.python.org/downloads/
I'm using the old 2.7.0 here. Doesn't particularly matter, but 3 is a little less stable I think.

Second, is PIP, which will let you install things easily in python. https://dev.to/el_joft/installing-pip-on-windows

Finally, is virtualenv, this'll let you develop a little quicker without loading your computer up with dozens of tiny programs, and flask, what we're using to deploy the app itself.
http://flask.pocoo.org/docs/0.12/installation/ should walk you through it just fine. I did everything on a MAC, so I dunno exactly how difficult it will be.
I've done some of these things on Windows but not all.

Anyway, once you've got everything installed, navigate down into whichever project you want to look at. 
For RnR: practice/rnr/venv/rnr 
Then activate your virtual environment, if it isn't already: venv\Scripts\activate

Then run ( python app.py ) or you can run ( export FLASK_APP=app.py ) and then run ( flask run )
