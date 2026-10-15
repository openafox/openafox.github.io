---
layout: page
title: Summer in Japan 2017
permalink: /japan-2017/
---

![Tokyo at sunset from the SkyTree](/resources/img/japan-2017/img_20170701_184236.jpg)

In summer 2017 I spent a couple of months in Japan on the EAPSI / JSPS Summer Program, doing
research in Funakubo-sensei's lab at Tokyo Tech.

- **Orientation week** at the Shonan Village Center with about 115 other fellows: language
  classes, a trip to Kamakura, and a weekend homestay (where I ended up fixing an e-bike).
- **In the lab** on the Suzukakedai campus: bouncing x-rays off my materials while applying an
  electric field, to see how they change shape. Long days, a long commute, and a lot of data.
- **Weekends** in Tokyo: bike polo, Shibuya, the SkyTree, sentos, and the beach at Enoshima.

All the photos from the trip are in the
[full photo album](https://photos.google.com/share/AF1QipMXr8rcDhv4L3aj_NPTWJfbExZwVMOJw04pd9LUdBrCdCoK_hH3ihhQ3lr-ICLfXw?key=cXVrWjJib1pGbW1aNm5wa1REOC16dlM0RFRoSndn).

{% assign trip = site.posts | where: "series", "japan-2017" | reverse %}
{% for p in trip %}
- {{ p.date | date: "%b %-d" }} · [{{ p.title }}]({{ site.baseurl }}{{ p.url }})
{%- endfor %}
