---
layout: default
title: Library
permalink: /Library/
---

{% assign visual_count = site.plates | size %}
<section class="container mt-5">
  <div class="my-3">
    <h1 class="fw-light">Library Index</h1>
    <p class="text-secondary my-4">
      <i class="bi bi-info-circle"></i> Currently indexing <strong>The Book of Jack</strong> Evidence Vault 
      <span class="mx-2">|</span> 
      <span id="stat-academic">0</span> Academic <span class="mx-1">•</span> 
      <span id="stat-narrative">0</span> Narrative <span class="mx-1">•</span> 
      {{ visual_count }} Visual
    </p>
  </div>

  <p class="lead text-body">A consolidated index of all primary, supplemental, and visual evidence.</p>
  
  <div class="mb-5">
    <input type="text" id="vaultSearch" class="form-control form-control-lg border-2 shadow-sm" placeholder="Search by author, title, chapter, or keyword...">
  </div>

  <ul class="nav nav-tabs mb-4 border-bottom-0" id="libraryTabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active fw-light" id="academic-tab" data-bs-toggle="tab" data-bs-target="#academic-pane" type="button" role="tab">
        Main Source <span id="count-academic" class="badge rounded-pill bg-secondary ms-1 small">0</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link fw-light" id="narrative-tab" data-bs-toggle="tab" data-bs-target="#narrative-pane" type="button" role="tab">
        Supplemental <span id="count-narrative" class="badge rounded-pill bg-secondary ms-1 small">0</span>
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link fw-light" id="visual-tab" data-bs-toggle="tab" data-bs-target="#visual-pane" type="button" role="tab">
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
        {% for entry in site.data.academic.references %}
          <div class="evidence-row">
            {% include citation.html %}
          </div>
        {% endfor %}
      </div>
    </div>
    <div class="tab-pane fade" id="narrative-pane" role="tabpanel">
      <div class="no-results-msg d-none py-5 text-center">
        <i class="bi bi-search text-secondary display-6"></i>
        <p class="text-secondary mt-3">No matches found.</p>
      </div>
      <div class="list-group list-group-flush border-top">
        {% for entry in site.data.narrative.references %}
          <div class="evidence-row">
            {% include citation.html %}
          </div>
        {% endfor %}
      </div>
    </div>
    <div class="tab-pane fade" id="visual-pane" role="tabpanel">
      <div class="no-results-msg d-none py-5 text-center">
        <i class="bi bi-search text-secondary display-6"></i>
        <p class="text-secondary mt-3">No matches found.</p>
      </div>
      <div class="row row-cols-1 row-cols-md-2 g-4 mt-1">
        {% for plate_file in site.plates %}
          {% comment %}
            We convert both IDs to strings to ensure the match works 
          {% endcomment %}
          {% assign current_id = plate_file.image_id | append: "" %}
          {% assign metadata = site.data.plates | where: "image_id", current_id | first %}
          <div class="col evidence-row">
            <!-- Hidden bank for search: includes prompt from MD and fields from CSV -->
            <div class="d-none">{{ plate_file.image_prompt }} {{ metadata.place_city }} {{ metadata.era }}</div>
            <div class="card h-100 border-0 bg-body-tertiary shadow-sm position-relative">
              <div class="row g-0 h-100">
                <div class="col-4">
                  <!-- Using image_path from your CSV -->
                  <img src="{{ metadata.image_path | relative_url }}" 
                      class="img-fluid rounded-start h-100 object-fit-cover" 
                      alt="{{ plate_file.title }}"
                      style="min-height: 100px; width: 100%;">
                </div>
                <div class="col-8">
                  <div class="card-body p-3">
                    <h6 class="card-title mb-1 text-body fw-light">{{ plate_file.title }}</h6>
                    <!-- Attribution using your specific CSV headers -->
                    <p class="card-text small text-secondary mb-2">
                      {{ metadata.attr_image_credit }} 
                      {% if metadata.display_year %}
                        ({{ metadata.display_year }})
                      {% endif %}
                    </p>
                    <!-- Chapter Badge using chapter_number or era from CSV -->
                    {% if metadata.era %}
                      <div class="d-flex flex-wrap gap-1" style="z-index: 5; position: relative;">
                        <span class="badge rounded-pill bg-warning-subtle text-warning-emphasis border border-warning-subtle small filter-badge" 
                              style="cursor: pointer;" 
                              onclick="filterByTag('{{ metadata.era | strip }}')">
                          {{ metadata.era }}
                        </span>
                      </div>
                    {% endif %}
                    <a href="{{ plate_file.url | relative_url }}" class="stretched-link"></a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        {% endfor %}
      </div>
    </div>

  </div>
</section>

<script>
  /**
   * Clickable Badge Filter
   * Triggered when a user clicks a chapter badge on a card.
   */
  function filterByTag(tagName) {
    const searchInput = document.getElementById('vaultSearch');
    
    // Set the search input to the tag name
    searchInput.value = tagName;
    
    // Run the update counts and filter logic
    updateCounts();
    
    // Smooth scroll back to the search bar so the user sees the result
    window.scrollTo({
      top: searchInput.offsetTop - 100,
      behavior: 'smooth'
    });
  }

  /**
   * Main Search and Count Logic
   * Filters Academic, Narrative, and Visual panes simultaneously.
   */
  function updateCounts() {
    const panes = ['academic', 'narrative', 'visual'];
    const filter = document.getElementById('vaultSearch').value.toLowerCase();
    
    panes.forEach(paneId => {
      const pane = document.getElementById(`${paneId}-pane`);
      // Ensure this looks for your .evidence-row class
      const items = pane.querySelectorAll('.evidence-row');
      const noResultsMsg = pane.querySelector('.no-results-msg');
      let matchCount = 0;

      items.forEach(item => {
        // Searches all text inside the card (Title, Author, Tags, Prompts)
        const text = item.innerText.toLowerCase();
        if (text.includes(filter)) {
          item.classList.remove('d-none');
          matchCount++;
        } else {
          item.classList.add('d-none');
        }
      });

      // Update the badge count in the Tabs
      const countBadge = document.getElementById(`count-${paneId}`);
      if (countBadge) {
        countBadge.innerText = matchCount;
      }
      
      // Update the "Index" stats at the top only when search is empty
      if (filter === "") {
          const statEl = document.getElementById(`stat-${paneId}`);
          if (statEl) statEl.innerText = matchCount;
      }

      // Toggle the "No Results" message
      if (matchCount === 0 && filter !== "") {
        noResultsMsg.classList.remove('d-none');
      } else {
        noResultsMsg.classList.add('d-none');
      }
    });
  }

  // Listen for typing in the search box
  document.getElementById('vaultSearch').addEventListener('keyup', updateCounts);

  // Run on page load to set initial counts
  window.addEventListener('DOMContentLoaded', updateCounts);
</script>


