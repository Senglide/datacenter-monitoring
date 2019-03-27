# Test running and accessing an AIOHTTP API

# Imports
import configparser
import urllib.parse
import pymongo

from pymongo import MongoClient
from aiohttp import web
from bson.json_util import dumps

# Get db credentials from config file
dbconfig = configparser.ConfigParser()
dbconfig.sections()
dbconfig.read('/etc/monitoring/dbconfig.ini')
dbuser = dbconfig['configuration']['username']
dbpass = dbconfig['configuration']['password']
dbhost = dbconfig['configuration']['host']
dbport = dbconfig['configuration']['port']
dbauth = dbconfig['configuration']['auth']
dbmech = dbconfig['configuration']['mech']

# Connect to db
client = MongoClient('mongodb://%s:%s@%s:%s/%s?authMechanism=%s' % (dbuser, dbpass, dbhost, dbport, dbauth, dbmech))
db = client['monitoring']

# Setup API request handler
async def getReadings(request):
    cursor = db.dashboard_rack_1.find()
    readinglist = list(cursor)
    readings = dumps(readinglist)

    return web.json_response(readings)

# Setup API with routes
app = web.Application()
app.add_routes([web.get('/readings', getReadings)])

# Run API
web.run_app(app)