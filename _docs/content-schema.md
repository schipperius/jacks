---
layout: page
title: Content Schema
---

# Template Structure
# Global Block
layout: lead-section # The foundation that wraps content in a specific template to ensure consistent design structure
title: "Cracker Jack" # The identity that can be used to generate heading and title tags

seo:
  type: article
  keywords: [Chicago, candy]

# Taxonomies / Navigation Block
categories: []
tags: []

text: # Text Block
  description: >  
    A mixture of molasses-flavored candy-coated popcorn and peanuts that was sold for the first time at the World's Columbian Exposition in 1893.
  lead:
  excerpt:

media:
image: # Image Block
  path: /assets/img/stories/cracker-jack.jpg
  alt: # Alternative text provides a text description of an image for screen readers ensuring compliance with accessibility standards
  caption: # A custom variable used to store descriptive text for an image, video or table
  credit: # Owner of image
  source: # A link to the original archive or museum page
  width: # Constrained width
  height: # Constrained height
  license: # Usage rights

timeline: # Timeline Block
  sort-year: -1780
  display:
    year: "1780 BCE"
    circa: true # Indicates approximate dates

map: # Map Block
    coordinates: [41.8781, -87.6298]
    modern-name: # The name: might be "Constantinople," but it's helpful to have a variable for the current city name ("Istanbul") for searchability
  display:
    region: # Useful for grouping by continent or ancient territory (e.g., Mesopotamia, Mediterranean)
    type: # What is this point? (e.g., battlefield, settlement, monument, trade-route)
    era: # To help the map show only points relevant to a specific time period (e.g., Bronze Age, Industrial Revolution)
    marker-color: # You could use hex codes (e.g., #ff5733) to color-code different civilizations
    zoom-level: # If the specific location is a tiny city, you might want the map to zoom in closer (15) than if it’s a vast empire (4)
    location-accuracy: # In history, we don't always know exactly where something happened. You could use values like precise, approximate, or legendary

