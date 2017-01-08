---
layout: default
title: Home
---

# Welcome!
{: style="text-align: center;"}
  <div class="tags-expo-list" style="text-align: center;">
    {% for tag in site.categories %}
    <a href="/blog/categories#{{ tag[0] | slugify }}" class="post-tag">{{ tag[0] }}</a>
    {% endfor %}
  </div>
  <br>
<figure style="width:350px; margin: auto; text-align: center;">
  <img src="/resources/img/Sunset.jpg" alt="Uncle Charlie riding into the sunset" width="350">
  <figcaption>Uncle Charlie riding into the sunset on our only 100 mile day (2012-Tour).</figcaption>
</figure>
