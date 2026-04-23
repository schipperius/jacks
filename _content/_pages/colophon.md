---
layout: default
title: Colophon
permalink: /colophon/
image_id: col-da-vinci-bottega
---

{% comment %} 
  1. Index everything using the new naming convention
{% endcomment %}
{% assign manifest_map = site.data.manifest    | group_by: "image_id" %}
{% assign loc_map      = site.data.location    | group_by: "image_id" %}
{% assign attr_map     = site.data.attribution | group_by: "image_id" %}
{% assign plate_map    = site.plates           | group_by: "image_id" %}

{% comment %} 
  2. Perform lookups for the specific image_id defined in front matter
{% endcomment %}
{% assign target_id = page.image_id | append: "" | strip %}

{% assign manifest = manifest_map | where: "name", target_id | map: "items" | first | first %}
{% assign loc      = loc_map      | where: "name", target_id | map: "items" | first | first %}
{% assign attr     = attr_map     | where: "name", target_id | map: "items" | first | first %}
{% assign plate    = plate_map    | where: "name", target_id | map: "items" | first | first %}

<article class="container-fluid px-lg-0 my-5">
  <div class="row g-5">
    <div class="col-lg-8">

      {% if manifest %}
        <div class="hero-plate-frame p-2 shadow-lg mb-2">
          <a href="{{ manifest.image_path | relative_url }}" class="lightbox-trigger">
            <img src="{{ manifest.image_path | relative_url }}" class="img-fluid w-100" alt="{{ manifest.image_title }}">
          </a>
        </div>

        <div class="d-flex justify-content-between align-items-center px-2 my-2">
          <p class="mb-0 text-muted small">
            {% if loc.place_city %}
              {{ loc.place_city }}{% if loc.place_region %}, {{ loc.place_region }}{% endif %} | 
            {% endif %}
            {{ loc.super_period }} | {{ loc.display_year }}      
          </p>
        </div>

        <div class="px-2 mt-4">
          <h3 class="display-6">{{ manifest.image_title }}</h3>
          
          {% comment %} Fallback: Plate caption > Manifest caption > Manifest Title {% endcomment %}
          <p class="lead">
            {{ plate.image_caption | default: manifest.image_caption | default: manifest.image_title }}
          </p>
          
          {% comment %} This displays Markdown text from your _plates/ file {% endcomment %}
          <div class="mt-4">
            {{ plate.content | strip_html | truncatewords: 75 }}
          </div>
        </div>

      {% else %}
        <div class="alert alert-warning">
          Data for ID <strong>{{ target_id }}</strong> not found in master manifest.
        </div>
      {% endif %}
    </div>

    <div class="col-lg-4">
      <div class="mb-4">
        <p class="lead text-body-secondary">The Book of Jack was initially conceived as a coffee table book. Today, it's a digital anthology.</p>
        <p>The history of writing and publishing is marked by diverse spaces, from sacred "Houses of Life" to industrial print shops, each reflecting the technology and culture of its era...</p>
      </div>

      <div class="mt-4">
        {% comment %} Using status from the attribution or manifest file {% endcomment %}
        {% if attr.status == "verified" or manifest.status == "verified" %}
          <span class="badge bg-success">Museum Verified</span>
        {% else %}
          <span class="badge border text-secondary">Research in Progress</span>
        {% endif %}
      </div>
    </div>
  </div>
  <hr class="border-bottom my-2">
</article>

### The Technology Stack & Architecture for the Book of Jack Project

* Building a website has a number of similarities to [*building a house*](https://www.linkedin.com/pulse/building-website-lot-like-house-lori-highby-xnjac) with the data resembling [*the kitchen and dining room*](https://www.kimballgroup.com/2004/01/data-warehouse-dining-experience/) experience. 

#### The Framework
* [*Jekyll*](https://jekyllrb.com) provides a structured framework to build, manage and deploy the Book of Jack project. 

#### The Presentation Layer
* [*Markdown*](https://www.markdownguide.org), [*HTML5 & CSS3*](https://www.w3schools.com/htmlcss/default.asp), [*Sass*](https://sass-lang.com) and [*Bootstrap 5*](https://getbootstrap.com) are used to format text, build the static pages, control the presentation and visual style, and provide mobile first responsiveness.  

#### The Data Layer
* [*Zotero*](https://www.zotero.org) is used to collect, organize, annotate and cite research. The [*Better BibTeX*](https://retorque.re/zotero-better-bibtex/) extension is used to manage, customize and prepare the bibliographic data for export. [*YAML*](https://yaml.org) keeps the structured data such as references, images and navigation separate from the presentation layer. 

#### The Logic Layer
* [*Liquid*](https://shopify.github.io/liquid/) acts as the 'glue' that connects the presentation and data layers creating the seemless design patterns across multiple pages and entire websites.

#### Infrastructure & Tooling
* For local development, [*iTerm2*](https://iterm2.com/index.html) provides a command-line interface to the Jekyll engine and [*VS Code*](https://code.visualstudio.com) is the primary development editor. 

* [*GitHub*](github.com) provides cloud storage for Git repositories, version control, issue tracking and project management tools. [*GitHub Pages*](*.github.io) provides secure hosting and automated deployment and [*GitHub Actions*](https://github.com/features/actions) is used to automate development workflows thorugh continuous integration and delivery.

#### Writing & Editing
* [*Scrivener*](https://www.literatureandlatte.com) is widely regarded as one of the best integrated writing environments designed specifically for writers, combining editing, file management, outlining and research tools into one user-friendly interface.
