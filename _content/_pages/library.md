---
layout: default
title: Library
permalink: /Library/
---

<div class="alert alert-warning">
  <strong>System Audit:</strong><br>
  Scholar Object exists: {% if site.scholar %} YES {% else %} NO {% endif %}<br>
  Bibliography Count (site.bibliography): {{ site.bibliography | size }}<br>
  Scholar Bib Count (site.scholar.bibliography): {{ site.scholar.bibliography | size }}<br>
  References Count (site.references): {{ site.references | size }}
</div>

### Project Resources
{% bibliography %}


{% assign visual_count = site.data.plates | size %}
<div class="container mt-5">
  <div class="my-4">
    <h4>Library Index</h4>
    <p class="text-secondary small my-4">
      <i class="bi bi-info-circle"></i> Currently indexing <strong>The Book of Jack</strong> Evidence Vault 
      <span class="mx-2">|</span> 
      <span id="stat-academic">0</span> Academic <span class="mx-1">•</span> 
      <span id="stat-narrative">0</span> Narrative <span class="mx-1">•</span> 
      {{ visual_count }} Visual
    </p>
  </div>

  <p class="lead text-body">A consolidated index of all academic, supplemental, and visual evidence.</p>
  
  <div class="mb-5">
    <input type="text" id="vaultSearch" class="form-control form-control-lg border-2 shadow-sm" placeholder="Search by author, title, chapter, or keyword...">
  </div>

  <ul class="nav nav-tabs mb-4 border-bottom-0" id="libraryTabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active fw-bold" id="academic-tab" data-bs-toggle="tab" data-bs-target="#academic-pane" type="button" role="tab">
        Academic <span id="count-academic" class="badge rounded-pill bg-secondary ms-1 small">0</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link fw-bold" id="narrative-tab" data-bs-toggle="tab" data-bs-target="#narrative-pane" type="button" role="tab">
        Narrative <span id="count-narrative" class="badge rounded-pill bg-secondary ms-1 small">0</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link fw-bold" id="visual-tab" data-bs-toggle="tab" data-bs-target="#visual-pane" type="button" role="tab">
        Visual <span id="count-visual" class="badge rounded-pill bg-secondary ms-1 small">{{ visual_count }}</span>
      </button>
    </li>
  </ul>

  <div class="tab-content" id="libraryTabContent">
    <div class="tab-pane fade show active" id="academic-pane" role="tabpanel">
      <div class="no-results-msg d-none py-5 text-center">
        <i class="bi bi-search text-secondary display-6"></i>
        <p class="text-secondary mt-3">No matches found.</p>
      </div>
<div class="list-group list-group-flush border-top">
  {% for entry in site.bibliography %}
    {% if entry.keywords contains "academic" %}
      {% include citation.html %}
    {% endif %}
  {% endfor %}
</div>
    </div>
    <div class="tab-pane fade" id="narrative-pane" role="tabpanel">
      <div class="no-results-msg d-none py-5 text-center">
        <i class="bi bi-search text-secondary display-6"></i>
        <p class="text-secondary mt-3">No matches found.</p>
      </div>
<div class="list-group list-group-flush border-top">
  {% for entry in site.bibliography %}
    {% if entry.keywords contains "narrative" %}
      {% include citation.html %}
    {% endif %}
  {% endfor %}
</div>
    </div>
    <div class="tab-pane fade" id="visual-pane" role="tabpanel">
      <div class="no-results-msg d-none py-5 text-center">
        <i class="bi bi-search text-secondary display-6"></i>
        <p class="text-secondary mt-3">No matches found.</p>
      </div>
      <div class="row row-cols-1 row-cols-md-2 g-4 mt-1">
        {% for item in site.data.plates %}
          <div class="col evidence-row">
            <div class="card h-100 border-0 bg-body-tertiary shadow-sm position-relative">
              <div class="row g-0 h-100">
                <div class="col-4">
                  <img src="{{ item.thumbnail }}" 
                       class="img-fluid rounded-start h-100 object-fit-cover" 
                       alt="{{ item.title }}" 
                       style="min-height: 120px;">
                </div>
                <div class="col-8">
                  <div class="card-body p-3">
                    <h6 class="card-title mb-1 text-body fw-bold">{{ item.title }}</h6>
                    <p class="card-text small text-secondary mb-2">{{ item.attribution }}</p>                   
                    {% if item.chapters %}
                    <div class="d-flex flex-wrap gap-1" style="z-index: 2; position: relative;">
                      {% assign plate_chaps = item.chapters | split: "," %}
                      {% for chap in plate_chaps %}
                        <span class="badge rounded-pill bg-warning-subtle text-warning-emphasis border border-warning-subtle small">{{ chap | strip }}</span>
                      {% endfor %}
                    </div>
                    {% endif %}                   
                    {% if item.url %}<a href="{{ item.url }}" target="_blank" class="stretched-link"></a>{% endif %}
                  </div>
                </div>
              </div>
            </div>
          </div>
        {% endfor %}
      </div>
    </div>

  </div>
</div>

<script>
function updateCounts() {
  const panes = ['academic', 'narrative', 'visual'];
  const filter = document.getElementById('vaultSearch').value.toLowerCase();
  
  panes.forEach(paneId => {
    const pane = document.getElementById(`${paneId}-pane`);
    const items = pane.querySelectorAll('.evidence-row');
    const noResultsMsg = pane.querySelector('.no-results-msg');
    let matchCount = 0;

    items.forEach(item => {
      const text = item.innerText.toLowerCase();
      if (text.includes(filter)) {
        item.classList.remove('d-none');
        matchCount++;
      } else {
        item.classList.add('d-none');
      }
    });

    document.getElementById(`count-${paneId}`).innerText = matchCount;
    
    // Also update the top index stats for academic and narrative on first load
    if (filter === "") {
        const statEl = document.getElementById(`stat-${paneId}`);
        if (statEl) statEl.innerText = matchCount;
    }

    if (matchCount === 0 && filter !== "") {
      noResultsMsg.classList.remove('d-none');
    } else {
      noResultsMsg.classList.add('d-none');
    }
  });
}

document.getElementById('vaultSearch').addEventListener('keyup', updateCounts);
window.addEventListener('DOMContentLoaded', updateCounts);
</script>