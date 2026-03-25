---
layout: default
title: "Chapters"
permalink: /chapters/
---

<div class="container my-5">
  {% assign all_chapters = site.chapters | sort: 'chapter_number' %}
  
  {% for chapter_item in all_chapters %}
    {% include chapter-card.html chapter=chapter_item %}
  {% endfor %}
</div>

