The short answer is **yes, absolutely.** Jekyll is quite flexible when it comes to reusing code across different collections.

Since `_pages` and `_stories` are both collections (or one is the default `pages` and the other is a custom collection), they can both access the same files located in your `_includes/` directory.

### How to Implement It

To make a single include work for both, you just need to ensure the logic inside the include file is **context-aware**. Jekyll's `include` tag allows you to pass variables, or you can rely on the `page` object which updates based on which document is being rendered.

**1. Create your include (e.g., `_includes/content-header.html`)**
You can write code that adapts to whichever collection is calling it:

```html
<header class="post-header">
  <h1>{{ page.title }}</h1>
  
  {% if page.collection == 'stories' %}
    <span class="story-meta">Story Category: {{ page.genre }}</span>
  {% endif %}
  
  <p class="date">Published on: {{ page.date | date_to_string }}</p>
</header>

```

**2. Call it in your layouts**
Whether you are in `_layouts/page.html` or `_layouts/story.html`, the call remains the same:

```liquid
{% include content-header.html %}

```

---

### Best Practices for Shared Includes

| Strategy | When to Use |
| --- | --- |
| **Direct Variable Passing** | Use this if you want the include to look different based on a specific setting: `{% include hero.html title=page.title color="blue" %}`. |
| **Conditional Logic** | Use `{% if page.collection == 'stories' %}` inside the include to toggle specific features (like reading time or author bios) that only apply to stories. |
| **Front Matter Defaults** | Set different defaults in your `_config.yml` for each collection so the include always has the data it needs without manual entry. |

### Common Gotcha: URL Paths

If your `_includes` contain images or links, remember that `_pages` often live at the root `/` while `_stories` might live at `/stories/`. Always use the `relative_url` or `absolute_url` filters to ensure your shared assets don't break:

`<img src="{{ '/assets/img/logo.png' | relative_url }}">`

---

**Would you like me to help you write a specific conditional loop to list your latest stories on one of your pages?**