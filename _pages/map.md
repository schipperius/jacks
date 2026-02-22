---
layout: default
title: Geographic Archive
permalink: /map/
---

<div id="map" style="height: 80vh; border-radius: 12px;"></div>

<script>
document.addEventListener("DOMContentLoaded", function () {

  // 1. Create map
  var map = L.map('map').setView([20, 0], 2);

  // 2. Define base layers
  var flatLayer = L.tileLayer(
    'https://server.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}',
    { attribution: 'Tiles © Esri' }
  );

  var terrainLayer = L.tileLayer(
    'https://server.arcgisonline.com/ArcGIS/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}',
    { attribution: 'Tiles © Esri' }
  );

  var satelliteLayer = L.tileLayer(
    'https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    { attribution: 'Tiles © Esri' }
  );

  // 3. Add default layer to map
  flatLayer.addTo(map);

  // 4. Define layer control object
  var baseMaps = {
    "Flat / Topo": flatLayer,
    "Terrain": terrainLayer,
    "Satellite": satelliteLayer
  };

  L.control.layers(baseMaps, null, { position: 'topleft' }).addTo(map);

  // 5. Marker colors
  var categoryColors = {
    origins: "#e74c3c",
    medieval: "#3498db",
    modern: "#2ecc71",
    default: "#95a5a6"
  };

  // 6. Store bounds for auto-zoom
  var bounds = [];

  // 7. Add markers from Jekyll data
  {% for place in site.data.locations %}
    var color = categoryColors["{{ place.category }}"] || categoryColors.default;

    var marker = L.circleMarker(
      [{{ place.lat }}, {{ place.lng }}],
      {
        radius: 6,
        fillColor: color,
        color: color,
        weight: 1,
        opacity: 1,
        fillOpacity: 0.9
      }
    ).addTo(map);

    marker.bindPopup(
      `<strong>
        <a href="{{ place.link | relative_url }}">
          {{ place.name }}
        </a>
      </strong><br>{{ place.description }}`
    );

    bounds.push([{{ place.lat }}, {{ place.lng }}]);
  {% endfor %}

  // 8. Fit map to markers
  if (bounds.length > 0) {
    map.fitBounds(bounds, { padding: [50, 50] });
  }

});
</script>