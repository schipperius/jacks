---
layout: default
title: Chapters
permalink: /chapters/
---

<div class="container my-5">
  {% assign chapters = site.chapters | sort: 'chapter_number' %}
  
  {% for chapter in chapters %}
    <section class="chapter-group mb-5">
      {% include chapter-header.html chapter=chapter %}
      <div class="row g-4 mb-5">
        {% assign current_scenes = site.scenes | where: "chapter_number", chapter.chapter_number | sort: "scene_number" %}
        {% for scene in current_scenes %}
          <div class="col-md-4 col-lg-3">
            {% include scene-card.html scene=scene %}
          </div>
        {% endfor %}
      </div>
      <hr class="my-5 opacity-25">
    </section>
  {% endfor %}
</div>