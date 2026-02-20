---
layout: default
title: "Wadi el-Hol"
permalink: /wadi-el-hol/
node: wadi-el-hol

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

{% include hero.html
   image=item.image
   alt=item.alt
   caption=item.caption
   title=item.title
   description=item.description
   links=item.links
%}
<!-- end hero section -->

