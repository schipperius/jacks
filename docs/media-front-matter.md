In the context of **Jekyll**, "media" isn't a native, hard-coded keyword in the core engine. Instead, it is almost always a **custom variable** defined in your Front Matter to help organize your assets.

Depending on which theme you’re using (like Chirpy, Minimal Mistakes, or Al-Jabr), the `media` key is typically used as a container for metadata related to external or internal files.

---

### Common Subcategories in Jekyll Front Matter

When developers use a `media` block, they usually break it down into these functional subcategories:

| Subcategory | Purpose | Example Usage |
| --- | --- | --- |
| **`image`** | The primary visual for the post (og-image or header). | `image: /assets/img/hero.jpg` |
| **`video`** | Links to YouTube, Vimeo, or local mp4 files. | `video: https://youtu.be/xyz` |
| **`audio`** | Links to podcasts or SoundCloud embeds. | `audio: /assets/audio/podcast-ep1.mp3` |
| **`thumbnail`** | A smaller version of the image for index pages. | `thumbnail: /assets/img/thumb.png` |
| **`caption`** | Text descriptions or credits for the media. | `caption: "Photo by John Doe"` |

---

### How it Looks in Your File

In your `.md` or `.html` file, you would structure it like this:

```yaml
---
layout: post
title: "My Awesome Adventure"
media:
  type: image
  link: "/assets/posts/adventure.jpg"
  caption: "The summit of the mountain"
  alt: "A snowy mountain peak"
---

```

### Why Use These Subcategories?

Since Jekyll uses **Liquid**, defining these subcategories allows you to create "smart" layouts. For example, you can write a conditional statement in your `_layouts/post.html`:

> "If this post has a `media.type` of 'video', render an iframe; if it's an 'image', render an `<img>` tag."

### Is there a "Standard"?

If you are using **Jekyll Admin** or a specific **CMS (like Netlify CMS/Decap)**, "media" might simply refer to your `assets/` folder. However, for Front Matter specifically, it is an **arbitrary map**. You can name the subcategories whatever you want, as long as your HTML templates are coded to look for those specific names.

---

**Would you like me to write a Liquid snippet that shows you how to display these different media types on your actual website?**