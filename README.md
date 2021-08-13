# HTTP_File_Storage

A daemon that will provide an HTTP API for uploading, downloading and deleting files.

## User's manual

To start the server, you need to run **rest_api.py**

***Upload:***

The file is uploaded to the server according to the settings from **constants.py** (UPLOAD_FOLDER and ALLOWED_EXTENSIONS)

- having received a file from the client, the daemon returns the hash of the uploaded file
- the daemon saves the file to disk in the following directory structure:

      UPLOAD_FOLDER/ab/abcdef12345...
      
  where "abcdef12345..." is a file name that matches its hash.
  
  /ab/ - subdirectory consisting of the first two characters of the file hash.


***Download:***

Download request: the client passes the parameter - the hash of the file. The daemon searches the local storage for the file and gives it back if it finds it.

      http://127.0.0.1:5000/download/abcdef12345...

***Delete:***

Delete request: the client passes the parameter - the hash of the file. The daemon looks for the file in local storage and deletes it if it finds it.

      http://127.0.0.1:5000/delete/abcdef12345...
