# bible_api
Bible API written in python using FastAPI to return, books, chapters or verses in three different versions.


To run, just enter the root of the directory and run 'docker-compose -f docker-compose.yml up'.

The API is configured to run on port 8000.

At the root we have a file called docs in it we have all the abbreviations of the books and the versions of bibles available.

In the requisitions it is necessary to inform the version of the bible to be used and the abbreviation of the book.

FastAPI has standard documentation using Swagger, just access:

http: // localhost: 8000 / docs
