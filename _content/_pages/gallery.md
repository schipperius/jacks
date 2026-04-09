---
layout: default
title: Gallery
permalink: /gallery/
---

<div class="container my-5">
  <div class="row row-cols-1 row-cols-md-2 row-cols-lg-3 g-4">
    {% for item in site.data.plates %}
    <div class="col-md-6 col-lg-4"> 
      <figure class="image-node border-gold h-100 p-3 mb-0 d-flex flex-column">
        <div class="image-wrapper mb-3">
          <a href="{{ '/plate/' | append: item.image_id | relative_url }}">
            <div class="ratio ratio-{{ item.image_aspect_ratio }}">
              <img src="{{ item.image_path | relative_url }}" 
                  class="rounded shadow-sm archive-img object-fit-cover" 
                  alt="{{ item.image_alt }}">
            </div>
          </a>
        </div>
        <figcaption class="d-flex flex-column flex-grow-1">
          <div class="meta-row d-flex justify-content-between mb-2">
            <span class="badge badge-date">
              {% if item.circa == "true" %}<em>c.</em> {% endif %}{{ item.display_year }}
            </span>
            <span class="geo-tag small">
              <i class="fas fa-map-marker-alt"></i> {{ item.label_past }}
            </span>
          </div>
          <h5 class="archival-font mb-1">{{ item.image_title }}</h5>
          <p class="caption-text small text-muted flex-grow-1">
            {{ item.image_caption }}
          </p>
        </figcaption>
      </figure>
    </div>
    {% endfor %}
  </div>
</div>

