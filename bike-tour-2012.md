---
layout: page
title: Circle America Bike Tour
permalink: /bike-tour-2012/
---

Archive of my old bike tour blog (originally at foxbiketour.blogspot.com): gear prep and
DIY panniers in 2011, then daily posts from the ride with my Uncle Charlie, March to June 2012.

A few photos from each day of the ride are in the posts; all 837 are in the
[full photo album](https://photos.app.goo.gl/t4o6poa1jkSrdL2WA).

<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css">
<div id="tour-map" style="height:380px;margin:1.5rem 0;border-radius:4px"></div>
<p style="font-size:.85rem;color:#777;margin-top:-1rem">Overnight stops by town, from the posts. Dashed = by van. Click a stop for that day's post.</p>
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script>
  (function () {
    var stops = {{ site.data.bike_tour_stops | jsonify }};
    var map = L.map('tour-map', { scrollWheelZoom: false });
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 12, attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
    var ride = [], van = [];
    stops.forEach(function (s, i) {
      (s.van ? van : ride).push([s.lat, s.lon]);
      if (s.van && i > 0 && !stops[i - 1].van) van.unshift([stops[i - 1].lat, stops[i - 1].lon]);
      L.circleMarker([s.lat, s.lon], { radius: 4, color: '#2a7ae2', weight: 2, fillOpacity: .9 })
        .addTo(map).bindPopup('<b>' + s.place + '</b><br><a href="{{ site.baseurl }}' + s.url + '">' + s.title + '</a>');
    });
    L.polyline(ride, { color: '#2a7ae2', weight: 3 }).addTo(map);
    L.polyline(van, { color: '#2a7ae2', weight: 3, dashArray: '6 6' }).addTo(map);
    map.fitBounds(L.latLngBounds(ride.concat(van)), { padding: [20, 20] });
  })();
</script>

{% assign tour = site.posts | where: "series", "bike-tour-2012" | reverse %}
{% assign years = tour | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for y in years %}
## {% if y.name == "2011" %}Getting ready (2011){% else %}On the road (2012){% endif %}
{% for p in y.items %}
- {{ p.date | date: "%b %-d" }} · [{{ p.title }}]({{ site.baseurl }}{{ p.url }})
{%- endfor %}
{% endfor %}
