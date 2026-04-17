---
layout: default
title: Colophon
permalink: /colophon/
image_id: craftsman-workshop # Foreign Key from plates.csv

---

{% comment %} 
  LOGIC: We look into our 'plates.csv' and find the row where 'image_id' 
  matches the 'image_id' in this page's front matter above. 
{% endcomment %}
{% assign d = site.data.plates | where: "image_id", page.image_id | first %}
<article class="container-fluid px-lg-0 my-5">
  <div class="row g-5">
    <div class="col-lg-8">
      {% comment %} 
        LOGIC: If 'd' (our CSV data) actually exists, show the image. 
        This prevents the page from looking 'broken' if a CSV row is missing.
      {% endcomment %}
      {% if d %}
      <div class="hero-plate-frame p-2 shadow-lg mb-2">
        <a href="{{ d.image_path | relative_url }}" class="lightbox-trigger">
          <img src="{{ d.image_path | relative_url }}" class="img-fluid w-100" alt="{{ d.image_prompt }}">
        </a>
      </div>
      <div class="d-flex justify-content-between align-items-center px-2 my-2">
        <p class="mb-0">
          {% comment %} Logic: Displaying the location/date string from the CSV {% endcomment %}
          {{ d.place_place }}, {{ d.place_provincial }} | {{ d.period }} | {{ d.display_year }}      
        </p>
      </div>
      {% endif %}
      <div class="px-2 mt-3">
        {% comment %} 
          Logic: 
          1. We look into 'site.plates' (your collection).
          2. We find the file where the 'image_id' matches this page's 'image_id'.
          3. We 'assign' that whole file to a new name: 'plate_file'.
        {% endcomment %}
        {% assign plate_file = site.plates | where: "image_id", page.image_id | first %}
        {% if plate_file %}
          {% comment %} 
            Now we use 'plate_file' instead of 'page' or 'item'. 
          {% endcomment %}
          <h1 class="display-5">{{ plate_file.image_title }}</h1>
          <p class="lead italic">{{ plate_file.image_caption }}</p>
        {% else %}
          {% comment %} Optional: A fallback if the file isn't found {% endcomment %}
          <h1 class="display-5">Plate Not Found</h1>
        {% endif %}
      </div>
      <!-- <div>{{ some_page.content | strip_html | truncatewords: 50 }}</div>
       Maybe add the first truncated paragraph that supports the image -->
    </div>
    <div class="col-lg-4">
      <div class="row">
      <h1 class="display-5 fw-light text-body-emphasis lh-1 mb-3">
        {{ page.title }}
      </h1>
      <p class="lead text-body-secondary">The Book of Jack was initially conceived as a coffee table book.</p>
      <p>This digital anthology retains the original purpose of a curated collection designed for an immersive experience.</p>
      </div>
      <div class="justify-content-between align-items-center">
        {% comment %} 
          Logic: You can check a 'status' column in your CSV. 
          If it's 'verified', show a gold badge. If not, show a 'work in progress' note.
        {% endcomment %}
        {% if d.status == "verified" %}
          <span class="badge bg-gold">Museum Verified</span>
        {% else %}
          <span class="badge bg-secondary">Research in Progress</span>
        {% endif %}
      </div>
    </div>
    <hr class="border-bottom my-1">
  </div>
</article>


### The Technology Stack & Architecture
* Building data-driven static site architecture has a number of similarities to [*building a house*](https://www.linkedin.com/pulse/building-website-lot-like-house-lori-highby-xnjac) with data management analagous to the [*restaurant dining experience*](https://www.kimballgroup.com/2004/01/data-warehouse-dining-experience/). 

#### The Framework
* [*Jekyll*](https://jekyllrb.com) provides a structured framework to build, manage and deploy the Book of Jack. 

#### The Presentation Layer
* [*Markdown*](https://www.markdownguide.org), [*HTML5 & CSS3*](https://www.w3schools.com/htmlcss/default.asp) and [*Bootstrap 5*](https://getbootstrap.com) are used to format text, build the static pages, control the presentation and visual style, and provide mobile first responsiveness.  

#### The Data Layer
* [*Zotero*](https://www.zotero.org) is used to collect, organize, annotate and cite research. The [*Better BibTeX*](https://retorque.re/zotero-better-bibtex/) extension is used to manage, customize and prepare the bibliographic data for export. And [*YAML*](https://yaml.org) keeps the structured data such as references, images and navigation separate from the presentation layer. 

#### The Logic Layer
* [*Liquid*](https://shopify.github.io/liquid/) acts as the 'glue' that connects the presentation and data layers creating a seemless design across multiple pages.

#### Infrastructure & Tooling
* For local development, [*iTerm2*](https://iterm2.com/index.html) provides a command-line interface to the Jekyll engine and [*VS Code*](https://code.visualstudio.com) is the primary development editor. 

* A web-based platform, [*GitHub*](github.com) provides cloud storage for Git repositories, version control, issue tracking, project management tools, and more. [*GitHub Pages*](*.github.io) provides secure, version-controlled hosting and automated deployment and [*GitHub Actions*](https://github.com/features/actions) is used to automate web development workflows thorugh cccontinuous integration and delivery.

#### Writing & Editing
* [*Scrivener*](https://www.literatureandlatte.com) combines editing, file management, outlining and research tools into one interface.

<br>
<!-- Paginaton-->
<div class="row mt-2 pt-3" style="border-color: var(--scribe-gold) !important;">
  <div class="col-12 d-flex align-items-center gap-1 gap-md-3">
    {% if page.previous %}
    <a href="{{ page.previous.url | relative_url }}" class="btn btn-outline-dark fw-light">&larr; Previous Page</a>
    {% else %}
    <span></span>
    {% endif %}
    {% if page.next %}
    <a href="{{ page.next.url | relative_url }}" class="btn btn-outline-dark fw-light">Next Page &rarr;</a>
    {% endif %}
  </div>
</div>
<br>

