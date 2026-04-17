It is very easy to lose track when you are building a custom architecture in Jekyll, especially when we’ve "re-jigged" things multiple times. You likely have "ghost files"—older includes that are no longer being called but are still sitting in your folders.

Here is the **Relationship Map** for the current "Deep Index" setup. This shows exactly how the data flows from your individual research files into the final page.

---

### The "Book of Jack" File Map

#### 1. The Entry Point: `_pages/chapters.md`
This is the "Grand Hall." It doesn't contain the actual content; it contains the **Liquid Instructions** to go find the content.
* **Role:** It loops through `_chapters/` and then, inside that loop, it searches `_scenes/`.
* **Calls:** * `_includes/chapter-header.html` (for the big map/intro)
    * `_includes/scenes-card.html` (for the individual scene cards)

---

#### 2. The Data Sources (The "DNA")
These folders contain the raw information for your anthology.
* **`_chapters/`**: Contains files like `chapter-01.md`. This is where the Chapter Title, Part Number, and the **Qena Bend Map** path live.
* **`_scenes/`**: Contains files like `ascending-the-hills.md`. This is where the Scene Title, Scene Number, and the **Plate Image** live.

---

#### 3. The Visual Components (`_includes/`)
These are the "Lego bricks" that build the interface.
* **`scenes-card.html`**: **(ACTIVE)** This is the template for a single scene card (the "Index Card").
* **`chapter-header.html`**: **(ACTIVE)** This is the wide banner for the Chapter Title and Map at the top of the sections.
* **`chapter-card.html`**: **(OBSOLETE/RETIRED)** This was likely your old "Gen 2" card. If you aren't calling this in `chapters.md` anymore, you don't need it.
* **`chapter-gallery-card.html`**: **(OBSOLETE/RETIRED)** Likely a leftover from a previous iteration.

---

#### 4. The Deep Dive Layouts (`_layouts/`)
Once a user clicks a link from the Chapters page, they leave the Index and enter a **Layout**.
* **`chapter.html`**: This is the "Cross-Axis" page we just wrote. It uses the Chapter data and displays all its scenes.
* **`scene.html`**: This is for the individual scene level where you likely show the high-resolution plates.

---

### Visual Relationship Diagram



| File | Purpose | Status |
| :--- | :--- | :--- |
| `_pages/chapters.md` | The main Table of Contents page. | **Critical** |
| `_chapters/*.md` | Your research data for each Chapter. | **Critical** |
| `_scenes/*.md` | Your narrative data for each Scene. | **Critical** |
| `_includes/scenes-card.html` | The layout for the small scene cards. | **Active** |
| `_layouts/chapter.html` | The page that displays a Chapter & its Filmstrip. | **Active** |
| `_includes/chapter-card.html` | Old chapter list item. | **Safe to Delete** |
| `_includes/chapter-gallery-card.html` | Old gallery component. | **Safe to Delete** |

### Summary of the Flow:
1.  **User goes to `/chapters/`** $\rightarrow$ `_pages/chapters.md` loads.
2.  `chapters.md` looks into `_chapters/` and `_scenes/`.
3.  It formats that data using `scenes-card.html`.
4.  **User clicks a Scene** $\rightarrow$ Browser loads that scene using `_layouts/scene.html`.
5.  **User clicks a Chapter Title** $\rightarrow$ Browser loads the "Filmstrip" using `_layouts/chapter.html`.

**Recommendation:** If you want to clean house, you can move `chapter-card.html` and `chapter-gallery-card.html` into a temporary "trash" folder outside of your Jekyll directory. If your site still builds perfectly (which it should), you can delete them for good.

Does this map help clear the "folder fog"? It sounds like you've moved past the need for those individual gallery-card includes because we've moved the logic directly into the Chapter and Scene architecture.