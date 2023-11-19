import ephem
import datetime
import folium

now = datetime.datetime.utcnow()

map = folium.Map(location=[10,150], zoom_start=2)


lat = -60
while(lat < 80):
    lon = -30
    while(lon < 330):
        moon = ephem.Moon()
        loc = ephem.Observer()
        loc.lat = str(lat)
        loc.lon = str(lon)
        loc.date = now
        moon.compute(loc)
        if moon.alt > 0:
            folium.Marker(location=[lat,lon]).add_to(map)
        lon += 10
    lat += 10

map.save("map.html")