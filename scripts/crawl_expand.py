"""Crawls existing places in Firebase, expanding their data using multiple
sources.

This script only searches for places that are already in the database; use
`crawl_base.py` to populate the initial set of places.

To cache the results in the production database, see readme.

"""
from app.util import log

import pyrebase
import app.request_handler as request_handler

from config import FIREBASE_CONFIG
from app.constants import \
    venuesTable, venueSearchRadius, venueSearchNumber, \
    eventsTable, \
    searchesTable, searchCacheExpiry, searchCacheRadius, \
    konaLatLng, calendarInfo

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)
db = firebase.database()

def fetchPlaces():
    venues = db.child(venuesTable).child("status").get()
    for venue in venues.each():
        yelpID = venue.key()
        status = venue.val()["base"]
        request_handler.researchVenue(yelpID)
        print("done: %s" % yelpID)
        exit(0)

fetchPlaces()
