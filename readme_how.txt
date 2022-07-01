This is a docmument to explain how the project was made.

FrameWorks:

Flask as the web Application 

Pymongo To Access The database as ORM

Passlib for hashing of information


Other Python liblaries.

Running The App.
The App requires a running MongoDb client which in this case runs in the local machine 
and exposes the port 27017  , this can be modified depending on parameters.

The port in which the app runs is on the application setting on the last line incase it should it
be run with docker or other WSGI application durring a production or tresting environment

