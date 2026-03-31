---
layout: default
title: "Chapters"
permalink: /chapters/
---

<div class="container my-5">
  <div class="row g-4"> {% assign all_chapters = site.chapters | sort: 'chapter_number' %}
    
    {% for chapter_item in all_chapters %}
      <div class="col-md-6 col-lg-4"> {% include chapter-gallery-card.html chapter=chapter_item %}
      </div>
    {% endfor %}
  </div>
</div>