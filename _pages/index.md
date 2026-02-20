---
layout: default
title: the Book of Jack
permalink: /
node: the-book-of-jack

categories: [Origins, Anthologies]
tags:
  - etymology 
  - origin
  - location
  - time
  - narrative
---

<!-- start hero section -->
{% assign item = site.data.gallery | where: "id", node.id | first %}

{% include cover.html
   image=item.image
   alt=item.alt
   caption=item.caption
   title=item.title
   description=item.description
   links=item.links
%}
<!-- end hero section -->

