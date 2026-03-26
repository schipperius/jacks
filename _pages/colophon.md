---
layout: page
title: "Colophon"
permalink: /colophon/

text: 
  description: > 
    The book of jack was initially conceived as a ‘Coffee Table’ book. It was September 1994, the Internet was still in its infancy. 
  description-two: >
    Connection was through a 56K modem, with speeds noticeably slower than 56 that. Web pages consisted of static HTML tables and there were only about 10,000 websites worldwide.
  lead:
  excerpt:

image:
  path: /assets/images/pages/tavernier-jean-mielot.jpg
  alt: An author portrait of Jean Miélot writing his compilation of the Miracles of Our Lady, one of his many popular works. The setting is probably the Ducal Library. Bibliothèque Nationale de France, Paris. # Alternative text provides a text description of an image for screen readers ensuring compliance with accessibility standards
  caption: An author portrait of Jean Miélot writing his compilation of the Miracles of Our Lady, one of his many popular works. The setting is probably the Ducal Library. Bibliothèque Nationale de France, Paris. # A custom variable used to store descriptive text for an image, video or table
  credit: # Owner of image
  source: # A link to the original archive or museum page
  width: # Constrained width
  height: # Constrained height
  license: # Usage rights

seo:
  type: article
  keywords: [Chicago, candy]

categories: []
tags: []

map: 
  coordinates: [41.8781, -87.6298]
  modern-name: # The name: might be "Constantinople," but it's helpful to have a variable for the current city name ("Istanbul") for searchability
  display:
    region: # Useful for grouping by continent or ancient territory (e.g., Mesopotamia, Mediterranean)
    type: # What is this point? (e.g., battlefield, settlement, monument, trade-route)
    era: # To help the map show only points relevant to a specific time period (e.g., Bronze Age, Industrial Revolution)
    marker-color: # You could use hex codes (e.g., #ff5733) to color-code different civilizations
    zoom-level: # If the specific location is a tiny city, you might want the map to zoom in closer (15) than if it’s a vast empire (4)
    location-accuracy: # In history, we don't always know exactly where something happened. You could use values like precise, approximate, or legendary

timeline: 
  sort-year: -1780
  display:
    year: "1780 BCE"
    circa: true # Indicates approximate dates

Footnotes:
  url: https://wiki.ubc.ca/Course:LIBR548F/2012WT1/Colophon#:~:text=Colophon-,Definition,excommunication%20to%20unauthorized%20copiers.%22%20(

---

## The Digital Craft: Tech Stack & Architecture

*The Book of Jack* is built using a "Static Site" philosophy, prioritizing speed, longevity, and structural transparency. The project represents a synthesis of traditional narrative writing and modern software engineering.

### The Writing Layer
The narrative was composed and structured in **Scrivener**, utilizing a "Season/Episode" framework to manage the expansive history of the project. This allows for complex story-arc management while maintaining the granular detail required for archaeological accuracy.

### The Logic & Data Layer
The project’s "brain" is **Jekyll**, a Ruby-based static site generator. 
* **YAML (Yet Another Markup Language):** Used as the project's DNA to store structured research data, including the Master Evidence Vault and AI Prompt Library.
* **Liquid:** The templating language that acts as the connective tissue, dynamically retrieving data from YAML files and injecting it into the narrative chapters.
* **Markdown:** Used for prose to ensure the content remains "future-proof" and decoupled from any specific software.

### The Presentation Layer
* **Bootstrap 5:** The structural framework used for responsive layout, including the tabbed research centers and collapsible evidence drawers.
* **HTML5 & CSS3:** Custom-coded to provide a "digital anthology" aesthetic that balances modern legibility with academic tradition.

### Infrastructure & Tooling
* **GitHub Pages:** Provides secure, version-controlled hosting and automated deployment.
* **VS Code:** The primary environment for engineering the site's logic and design.
* **iTerm2:** Used for local development, providing a command-line interface to the Jekyll engine.


Markdown (The Ink): It’s the closest thing we have to "plain text," meaning your book will still be readable 50 years from now.

YAML (The Filing Cabinet): It allows you to separate your data (the facts) from your writing. This is why you can update a citation in one file and have it fix itself everywhere on the site.

Liquid (The Librarian): It’s the hardest one to learn because it’s logic-based (if/else, for-loops), but it’s what makes the site "smart."

CSS (The Lighting/Decor): It’s what allowed us to fix that "hover" issue. It controls the mood of the project.

Suggestions for the Colophon

Depth: The level of depth provided above is perfect. It’s technical enough for a developer to respect, but clear enough for a layperson to understand that a lot of work went into the "printing" of this digital book.

Personal Touch: You might add a sentence about the "Digital Archaeology" of the site itself—mentioning that the code is as much a part of the reconstruction as the images are.