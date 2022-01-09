Once you are in terminal/command line, access the database/collection you want to use as follows:

show dbs
use <db name>
show collections
choose your collection and type the following to see all contents of that collection:

db.collectionName.find()
More info here on the MongoDB Quick Reference Guide. http://docs.mongodb.org/manual/reference/mongo-shell/

docker exec -it baleen_app_1 bin/baleen export /baleen/info --scheme=html