from app.apis.weather import AWConnection

aw = AWConnection()
loc = aw.get_location_by_postal_code('02857')
print(loc)

