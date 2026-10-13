---
layout: page
title: Circle America Bike Tour
permalink: /bike-tour-2012/
---

Archive of my old bike tour blog (originally at foxbiketour.blogspot.com): gear prep and
DIY panniers in 2011, then daily posts from the ride with my Uncle Charlie, March to June 2012.

Photos from the 2012 ride lived in Picasa albums that Google has since shut down; I'm working on
recovering them.

{% assign tour = site.posts | where: "series", "bike-tour-2012" | reverse %}
{% assign years = tour | group_by_exp: "p", "p.date | date: '%Y'" %}
{% for y in years %}
## {% if y.name == "2011" %}Getting ready (2011){% else %}On the road (2012){% endif %}
{% for p in y.items %}
- {{ p.date | date: "%b %-d" }} · [{{ p.title }}]({{ site.baseurl }}{{ p.url }})
{%- endfor %}
{% endfor %}
