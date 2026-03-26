---
layout: page
title: "The Master Evidence Vault"
permalink: /research-index/
---

{% assign academic_count = site.data.citations | size %}
{% assign narrative_count = site.data.bibliography | size %}
{% assign visual_count = site.data.images | size %}
{% assign total_records = academic_count | plus: narrative_count | plus: visual_count %}

<p class="text-muted small mb-4">
  <i class="bi bi-info-circle"></i> Currently indexing <strong>{{ total_records }}</strong> total records 
  <span class="mx-2">|</span> 
  {{ academic_count }} Academic <span class="mx-1">•</span> 
  {{ narrative_count }} Narrative <span class="mx-1">•</span> 
  {{ visual_count }} Visual Reconstructions
</p>

### Project Roadmap
* **Front Matter**
    * [Introduction](/intro/)
    * [Methodology & AI Transparency](/methodology/)
* **Season 01: The Ascent**
    {% assign season1 = site.chapters | where: "part_number", 1 | sort: "chapter_number" %}
    {% for chapter in season1 %}
    * [Chapter {{ chapter.chapter_number }}: {{ chapter.title }}]({{ chapter.url }})
    {% endfor %}
* **Season 02: The Deep Desert**
    * (In Research Phase)

<div class="container mt-5">
  <p class="lead">A consolidated index of all academic, supplemental, and visual evidence used in this project.</p>
  
  <div class="mb-4">
    <input type="text" id="vaultSearch" class="form-control" placeholder="Search by author, title, or keyword...">
  </div>

  <div class="table-responsive">
    <table class="table table-hover align-middle" id="evidenceTable">
      <thead class="table-dark">
        <tr>
          <th>Type</th>
          <th>Reference / Resource</th>
          <th>Status</th>
        </tr>
      </thead>
      <tbody>
        {% for item in site.data.citations %}
        <tr class="evidence-row" data-type="Academic">
          <td><span class="badge bg-primary">Academic</span></td>
          <td>
            <strong>{{ item.authors }} ({{ item.year }})</strong><br>
            <span class="small text-muted italic">{{ item.title }}</span>
          </td>
          <td><a href="{{ item.url }}" class="btn btn-sm btn-link">Link</a></td>
        </tr>
        {% endfor %}
        {% for item in site.data.bibliography %}
        <tr class="evidence-row" data-type="Narrative">
          <td><span class="badge bg-secondary">Narrative</span></td>
          <td>{{ item.citation | markdownify | remove: '<p>' | remove: '</p>' }}</td>
          <td><span class="text-muted small">Web</span></td>
        </tr>
        {% endfor %}
        {% for item in site.data.images %}
        {% assign prompt = site.data.prompts | where: "id", item.id | first %}
        <tr class="evidence-row" data-type="Visual">
          <td><span class="badge bg-warning text-dark">Visual</span></td>
          <td>
            <strong>{{ item.title }}</strong><br>
            <span class="small text-muted">{{ item.attribution }}</span>
            {% if prompt %}
              <div class="mt-1 small border-start ps-2 border-warning" style="font-family: monospace; font-size: 0.75rem;">
                PROMPT: {{ prompt.prompt | truncate: 100 }}
              </div>
            {% endif %}
          </td>
          <td><span class="text-muted small">AI-Gen</span></td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

<script>
document.getElementById('vaultSearch').addEventListener('keyup', function() {
  let filter = this.value.toLowerCase();
  let rows = document.querySelectorAll('.evidence-row');
  let visibleCount = 0;
  
  rows.forEach(row => {
    let text = row.innerText.toLowerCase();
    if (text.includes(filter)) {
      row.style.display = '';
      visibleCount++;
    } else {
      row.style.display = 'none';
    }
  });
  
  // Optional: Update a "showing X of Y" message if you want to get fancy!
});
</script>