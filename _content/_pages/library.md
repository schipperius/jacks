---
layout: default
title: Library
permalink: /Library/
---

{% assign academic_count = site.data.citations | size %}
{% assign narrative_count = site.data.bibliography | size %}
{% assign visual_count = site.data.images | size %}
{% assign total_records = academic_count | plus: narrative_count | plus: visual_count %}

<div class="container mt-5">
  <div class="my-4">
    <h4>Library Index</h4>
    <p class="text-secondary small my-4">
      <i class="bi bi-info-circle"></i> Currently indexing <strong>{{ total_records }}</strong> total records 
      <span class="mx-2">|</span> 
      {{ academic_count }} Academic <span class="mx-1">•</span> 
      {{ narrative_count }} Narrative <span class="mx-1">•</span> 
      {{ visual_count }} Visual
    </p>
  </div>

  <p class="lead text-body">A consolidated index of all academic, supplemental, and visual evidence used in The Book of Jack project.</p>
  
  <div class="mb-5">
    <input type="text" id="vaultSearch" class="form-control form-control-lg border-2 shadow-sm" placeholder="Search by author, title, chapter, or keyword...">
  </div>

  <ul class="nav nav-tabs mb-4 border-bottom-0" id="libraryTabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active fw-bold" id="academic-tab" data-bs-toggle="tab" data-bs-target="#academic-pane" type="button" role="tab">
        Academic <span id="count-academic" class="badge rounded-pill bg-secondary ms-1 small">{{ academic_count }}</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link fw-bold" id="narrative-tab" data-bs-toggle="tab" data-bs-target="#narrative-pane" type="button" role="tab">
        Narrative <span id="count-narrative" class="badge rounded-pill bg-secondary ms-1 small">{{ narrative_count }}</span>
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
        <p class="text-secondary mt-3">No matches found in this category.</p>
      </div>
      <div class="list-group list-group-flush border-top">
        {% for item in site.data.citations %}
        <div class="list-group-item list-group-item-action py-3 position-relative evidence-row">
          <div class="d-flex w-100 justify-content-between align-items-center">
            <div>
              <h6 class="mb-1 text-body fw-bold">{{ item.title }}</h6>
              <p class="mb-2 text-secondary small">{{ item.authors }} ({{ item.year }})</p>             
              {% if item.chapters %}
              <div class="d-flex gap-1" style="z-index: 2; position: relative;">
                {% for chap in item.chapters %}
                  <span class="badge rounded-pill bg-primary-subtle text-primary-emphasis border border-primary-subtle small">{{ chap }}</span>
                {% endfor %}
              </div>
              {% endif %}
            </div>
            <i class="bi bi-chevron-right text-secondary ms-3"></i>
          </div>
          <a href="{{ item.url }}" target="_blank" class="stretched-link"></a>
        </div>
        {% endfor %}
      </div>
    </div>
    <div class="tab-pane fade" id="narrative-pane" role="tabpanel">
      <div class="no-results-msg d-none py-5 text-center">
        <i class="bi bi-search text-secondary display-6"></i>
        <p class="text-secondary mt-3">No matches found in this category.</p>
      </div>
      <div class="list-group list-group-flush border-top">
        {% for item in site.data.bibliography %}
        <div class="list-group-item list-group-item-action py-3 position-relative evidence-row">
          <div class="d-flex w-100 justify-content-between align-items-center">
            <div class="text-body">
              {{ item.citation | markdownify | remove: '<p>' | remove: '</p>' }}
              {% if item.chapters %}
              <div class="d-flex gap-1 mt-2" style="z-index: 2; position: relative;">
                {% for chap in item.chapters %}
                  <span class="badge rounded-pill bg-secondary-subtle text-secondary-emphasis border border-secondary-subtle small">{{ chap }}</span>
                {% endfor %}
              </div>
              {% endif %}
            </div>
            <i class="bi bi-chevron-right text-secondary ms-3"></i>
          </div>
          {% if item.url %}<a href="{{ item.url }}" target="_blank" class="stretched-link"></a>{% endif %}
        </div>
        {% endfor %}
      </div>
    </div>
    <div class="tab-pane fade" id="visual-pane" role="tabpanel">
      <div class="no-results-msg d-none py-5 text-center">
        <i class="bi bi-search text-secondary display-6"></i>
        <p class="text-secondary mt-3">No matches found in this category.</p>
      </div>
      <div class="row row-cols-1 row-cols-md-2 g-4 mt-1">
        {% for item in site.data.images %}
          {% assign prompt = site.data.prompts | where: "id", item.id | first %}
          <div class="col evidence-row">
            <div class="card h-100 border-0 bg-body-tertiary shadow-sm position-relative">
              <div class="row g-0 h-100">
                <div class="col-4">
                  <img src="{{ item.thumbnail | default: '/assets/img/placeholder-thumb.jpg' }}" 
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
                      {% for chap in item.chapters %}
                        <span class="badge rounded-pill bg-warning-subtle text-warning-emphasis border border-warning-subtle small">{{ chap }}</span>
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
document.getElementById('vaultSearch').addEventListener('keyup', function() {
  const filter = this.value.toLowerCase();
  const panes = ['academic', 'narrative', 'visual'];
  
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

    // Update the tab badge count
    document.getElementById(`count-${paneId}`).innerText = matchCount;

    // Show/Hide the "No Results" message
    if (matchCount === 0 && filter !== "") {
      noResultsMsg.classList.remove('d-none');
    } else {
      noResultsMsg.classList.add('d-none');
    }
  });
});
</script>