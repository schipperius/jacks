---
layout: default
title: Map
permalink: /map/
---
<section id="map" class="my-4" style="height: 80vh; border-radius: 12px;">
</section>

<script>
  window.storyLocations = [
    {% for story in site.stories %}
      {% if story.lat and story.lng %}
        {
          id: "{{ story.id }}",
          name: "{{ story.name | escape }}",
          lat: {{ story.lat }},
          lng: {{ story.lng }},
          category: "{{ story.category }}",
          description: "{{ story.description | escape }}",
          url: "{{ story.url | relative_url }}"
        },
      {% endif %}
    {% endfor %}
  ];
</script>
<script src="{{ '/assets/js/map.js' | relative_url }}" defer></script>