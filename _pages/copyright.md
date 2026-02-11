---
layout: default
title: Copyright
permalink: /copyright/
---
<div class="container">
  <h2 class="mt-4">Two columns with two nested columns</h2>
  <p>
    Per the documentation, nesting is easy—just put a row of columns
    within an existing column. This gives you two columns
    <strong>starting at desktops and scaling to large desktops</strong>,
    with another two (equal widths) within the larger column.
  </p>
  <p>
    At mobile device sizes, tablets and down, these columns and their
    nested columns will stack.
  </p>
  <div class="row mb-3 text-start">
    <div class="col-md-4 themed-grid-col">.col-md-4
    <h4>Front Matter</h4>
  <ul class="navbar-nav">
    <li class="nav-item">
    <a href="{{ '/jack-origins/' | relative_url }}"
        class="nav-link {% if page.url contains '/jack-origins' %}active{% endif %} px-2">
      Origins
    </a>
    </li>
    <li class="nav-item">
    <a href="{{ '/about/' | relative_url }}"
        class="nav-link {% if page.url contains '/about' %}active{% endif %} px-2">
      About
    </a>
    </li>
    <li class="nav-item">
    <a href="{{ '/copyright/' | relative_url }}"
        class="nav-link {% if page.url contains '/copyright' %}active{% endif %} px-2">
      Copyright
    </a>
    </li>
  </ul>
    <h4>Food and Drink</h4>
  <ul class="navbar-nav">
    <li class="nav-item">
    <a href="{{ '/cracker-jack/' | relative_url }}"
        class="nav-link {% if page.url contains '/cracker-jack' %}active{% endif %} px-2">
      Cracker Jack
    </a>
    </li></ul></div>
    <div class="col-md-8 themed-grid-col">
      <div class="pb-3">.col-md-8</div>
      <div class="row">
        <div class="col-md-6 themed-grid-col">.col-md-6</div>
        <div class="col-md-6 themed-grid-col">.col-md-6</div>
      </div>
    </div>
  </div>
  <hr class="my-4" />
</div> <!-- end container -->
