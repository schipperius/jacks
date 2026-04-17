1408x768 
It is the default resolution used by Google's generative models
For modern web design in 2026, you shouldn't rely on a single image size like 1408x768. 
Use Responsive Image techniques to serve different versions of the same image based on the user's device. 

1. Recommended Breakpoints for 2026
Most modern websites use three to four strategic "breakpoints" where the layout and image size change: 
Mobile (320px – 480px): Focus on vertical/square images and large touch targets. 
Tablet (768px – 1024px): A balance between mobile and desktop; often uses 2-column layouts. 
Desktop (1280px – 1440px): Standard widescreen layouts; 1440x900 is considered optimal for many laptops. 
Large Desktop (1920px+): High-resolution monitors; images here should be high-quality (Full HD). 

2. Best Practices for Web Images
Use srcset and sizes: Instead of one 1408x768 image, provide a "set" of different sizes. This allows the browser to automatically download the smallest image that will still look sharp on that specific screen. 

Desktop: 16:9 or 3:2 (landscape) for banners and hero images.
Mobile: 9:16 or 1:1 (vertical/square) to fill the screen better.
File Formats: Use WebP or AVIF for the best balance of quality and small file size. 
Content-Based Breakpoints: Don't just design for specific phones; add a breakpoint whenever your layout starts to look "broken" or awkward as you resize your browser. 

To use your 1408x768 image effectively in web design, you should implement the srcset attribute. This allows you to serve the high-quality 1408px version to large screens while providing smaller versions for mobile to save data and improve loading speed. 

Responsive Image Code Snippet
<img 
  srcset="image-mobile-480w.jpg 480w,
          image-tablet-800w.jpg 800w,
          image-original-1408w.jpg 1408w"
  sizes="(max-width: 600px) 480px,
         (max-width: 1024px) 800px,
         1408px"
  src="image-original-1408w.jpg" 
  alt="Descriptive text for your image"
  style="width: 100%; height: auto;">

Breakdown of the Code:
srcset: Lists your available image files and their actual widths in pixels (using the w descriptor). 
sizes: Tells the browser how much space the image will take up at different screen widths. For example, (max-width: 600px) 480px tells the browser that on small screens, the image will be displayed at 480px wide. 
src: The fallback image used by older browsers that don't support responsive attributes. 
style="width: 100%; height: auto;": Essential CSS to ensure the image scales fluidly to fit its container without distorting. 

To get the best result in web design, you should create three separate image files. 
1. "Resolution Switching" (Scaling)
This is what the srcset code I gave you does. It tells the browser: "Here are three different sizes of the same image. Pick the one that fits the screen best so the user doesn't waste data downloading a huge file on a tiny phone". 

Pro Tip: You can use free tools like Responsive Breakpoints to automatically generate all these different sizes and crops at once. 

How do I convert .jpg and .png to WebP or AVIF ?
1. Online Browser Tools (No Install)
These are ideal for quick, one-off conversions. 
Squoosh.app: A powerful tool by Google that allows you to drag-and-drop an image and see a real-time side-by-side comparison of different compression levels for WebP and AVIF. 
Cloudinary: Best for bulk-converting multiple JPGs to WebP at once. 
AnyWebP: A specialized browser tool for batch processing hundreds of images without uploading them to a server (processing happens locally in your browser). 

2. Desktop Software (Offline)
For security or large batches of files, offline tools are often faster.
XnConvert: A free, cross-platform utility that supports bulk conversion for almost every format, including AVIF and WebP. 

3. Professional Design Tools
GIMP: This free open-source editor supports both WebP and AVIF natively via File > Export As. 

4. Command Line (For Developers) 
Use Google's official libraries for the fastest batch processing.
WebP: Use the cwebp command: cwebp -q 80 input.jpg -o output.webp.
AVIF: Use avifenc (part of libavif): avifenc input.jpg output.avif. 

Quick Tip: AVIF generally offers 20–30% better compression than WebP, but WebP has slightly better browser compatibility for very old devices. 

cwebp is a command-line tool used to compress images to the WebP format, supporting input formats like PNG, JPEG, 

For the best results, you should use AVIF as your primary format with WebP as a fallback. This ensures you get the maximum performance benefits of the newest technology while maintaining compatibility for 100% of your users. 

Compression	Best. Typically 20–30% smaller than WebP for the same quality.	Good. 25–34% smaller than JPEG, but larger than AVIF.
Image Quality	Superior. Supports 10/12-bit HDR and wider color gamuts; fewer artifacts.	Standard. Mostly 8-bit color; can show "blockiness" at high compression.
Device Support	~93-95% of modern browsers/devices.	~96-97% (nearly universal since 2020).
Loading Speed	Faster initial download due to tiny file size.	Faster decoding (requires less CPU power to "unzip" and show).

Why AVIF is Better for 2026
Mobile Performance: Since mobile users often have slower or capped data, AVIF’s smaller file size makes pages load significantly faster on phones. 
High-End Displays: AVIF supports HDR (High Dynamic Range), making your images look more vibrant on modern laptop and tablet screens that support high brightness and color depth. 
Progressive Rendering: Unlike WebP, AVIF can show a blurry version of the image while it’s still downloading, which improves "perceived" speed for the user. 
When to Stick with WebP
Animations: WebP remains the better choice for animated images (replacing GIFs) as it has more mature browser and tool support for moving pictures. 
Simple Graphics: For basic logos or icons, the file size difference between WebP and AVIF is often negligible. 

The Recommended "Future-Proof" Code
Use the HTML <picture> tag to let the browser choose the best format itself. It will try AVIF first, then WebP, and finally a standard JPG: 

html
<picture>
  <source srcset="image.avif" type="image/avif">
  <source srcset="image.webp" type="image/webp">
  <img src="image.jpg" alt="Description" loading="lazy">
</picture>

Here is the summary of the "gold standard" workflow for 2026:
1. Three Image Sizes
Mobile: 480px wide (Portrait/Square crop is best).
Tablet: 800px – 1024px wide.
Desktop: 1408px – 1920px wide (Widescreen).
2. Tools for Formatting
For Conversion: Use Squoosh.app (manual) or XnConvert (bulk) to handle files.
For Generation: Use Responsive Breakpoints to automate the creation of all three sizes from one master file.
3. Best File Types
Primary: AVIF (smallest file size, highest quality, HDR support).
Fallback: WebP (universal compatibility for older devices).
4. Code to Display
Use the <picture> tag combined with srcset for the ultimate "future-proof" setup:
html
<picture>
  <!-- Mobile Version (AVIF then WebP) -->
  <source media="(max-width: 600px)" srcset="img-480.avif" type="image/avif">
  <source media="(max-width: 600px)" srcset="img-480.webp" type="image/webp">
  
  <!-- Desktop Version (AVIF then WebP) -->
  <source srcset="img-1408.avif" type="image/avif">
  <source srcset="img-1408.webp" type="image/webp">
  
  <!-- Fallback for old browsers -->
  <img src="img-1408.jpg" alt="Description" loading="lazy" style="width:100%; height:auto;">
</picture>

loading="lazy": Always add this attribute to images below the "fold" (not visible immediately) to speed up your initial page load.
Aspect Ratio Box: To prevent the page from "jumping" while images load, ensure your CSS or HTML attributes define the aspect-ratio so the browser reserves the correct space.

To prevent Cumulative Layout Shift (CLS)—that annoying "jump" where text moves around while an image is loading—you need to tell the browser the aspect ratio before the image file arrives.

In 2026, the aspect-ratio property is the cleanest way to do this.
The CSS Snippet
Add this to your stylesheet to handle your 1408x768 (roughly 11:6 or 1.83:1) images:
css
/* Responsive Image Container */
img {
  width: 100%;
  height: auto;
  display: block;
  /* Reserves the space based on your 1408x768 dimensions */
  aspect-ratio: 1408 / 768; 
  /* Ensures the image covers the area without stretching */
  object-fit: cover;
  /* Smoothly fades in once loaded */
  background-color: #f0f0f0; 
}

/* Optional: Different ratio for Mobile if you use a square crop */
@media (max-width: 600px) {
  img {
    aspect-ratio: 1 / 1; 
  }
}

Why this is a "must-have":
Browser Reservation: The browser calculates the height based on the width of the user's screen immediately, even if the image takes 2 seconds to download.
Object-Fit: Using object-fit: cover is a lifesaver. If your image is slightly off-ratio, it will intelligently crop to fill the space rather than squishing or stretching your content.
Background Color: The background-color acts as a "placeholder" box so the user knows an image is coming.
One final check
In your HTML, always include the original width and height attributes. Modern browsers use these to calculate the aspect ratio automatically before the CSS even loads:
html
<img src="image.avif" width="1408" height="768" alt="..." loading="lazy">

To wrap this up, here is your final checklist for the perfect standalone image implementation:
Alt Text: Since there’s no surrounding text, ensure your alt="..." attribute is highly descriptive for accessibility and SEO.
Corner Styling: Modern standalone images often look better with a slight rounding to match UI trends. Add border-radius: 8px; (or similar) to your CSS snippet.
Shadows/Depth: If the image is on a flat white background, a subtle box-shadow: 0 4px 12px rgba(0,0,0,0.1); can help it "pop."
Lightbox/Zoom: If the image contains fine detail, consider adding a simple script so users can click to view the full 1408x768 original in a larger "lightbox" view.

Here is everything you need to fully automate your responsive image workflow for 2026.
1. Test Instantly: Dynamic Placeholder Images
You can test your <picture> tag and CSS right now by using a dynamic service like Placehold.co. These URLs generate an image on-the-fly in the exact sizes we discussed: 
Mobile (480px): https://placehold.co
Tablet (800px): https://placehold.co
Desktop (1408px): https://placehold.co 
2. Automation Script (Node.js + Sharp)
The professional way to automate this is using the Sharp library in Node.js. It is significantly faster than other tools and supports AVIF and WebP natively. 
Steps to setup:
Initialize your project: npm init -y
Install Sharp: npm install sharp
Create a file named process-images.js and paste this script:
javascript
const sharp = require('sharp');
const fs = require('fs');
const sizes = [
  { width: 480, name: 'mobile' },
  { width: 800, name: 'tablet' },
  { width: 1408, name: 'desktop' }
];
// Process all files in an 'input' folder
fs.readdirSync('./input').forEach(file => {
  if (file.match(/\.(jpg|jpeg|png)$/i)) {
    sizes.forEach(async (size) => {
      const baseName = file.split('.')[0];
      
      // Generate AVIF version
      await sharp(`./input/${file}`)
        .resize(size.width)
        .toFormat('avif', { quality: 50 })
        .toFile(`./output/${baseName}-${size.name}.avif`);
      // Generate WebP version
      await sharp(`./input/${file}`)
        .resize(size.width)
        .toFormat('webp', { quality: 75 })
        .toFile(`./output/${baseName}-${size.name}.webp`);
        
      console.log(`Generated ${size.name} versions for ${file}`);
    });
  }
});

3. Summary Checklist
Sizes: 480px (Mobile), 800px (Tablet), 1408px (Desktop).
Tool: Sharp for automated batch processing. 
File Types: AVIF for quality, WebP for compatibility. 
Code: Use the <picture> tag with srcset and loading="lazy".

To integrate your image processing script into a GitHub Action, you can create a workflow that triggers every time you push new images to your repository. This workflow will run your Node.js script and automatically commit the resized AVIF and WebP versions back to your project. 
1. Prerequisites
Ensure your repository has a package.json file that includes sharp as a dependency. You will also need the process-images.js script we created earlier. 
2. Create the Workflow File 
Create a new file at .github/workflows/optimize-images.yml in your repository and paste the following configuration: 
yaml
name: Auto Optimize Images
on:
  push:
    paths:
      - 'input/**' # Only runs when files in the 'input' folder change
jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write # Allows the action to commit files back to your repo
    steps:
      - name: Checkout Repository
        uses: actions/checkout@v4
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm' # Speeds up subsequent runs
      - name: Install Dependencies
        run: npm install
      - name: Run Image Processing Script
        run: node process-images.js
      - name: Commit and Push Changes
        uses: stefanzweifel/git-auto-commit-action@v5
        with:
          commit_message: "Automated: Optimized images (AVIF/WebP)"
          file_pattern: 'output/**' # Commits only the new optimized images

3. How it Works
Trigger: The workflow waits for a push to the input/ folder. 
Environment: It spins up a fresh Ubuntu runner, installs Node.js, and pulls your code. 
Processing: It executes your script, which reads from input/ and writes the three sizes (Mobile, Tablet, Desktop) to output/. 
Auto-Commit: The Git Auto Commit Action detects the new files in the output/ folder and pushes them back to your branch automatically. 
4. Marketplace Alternative
If you prefer a "no-code" solution, you can use the Image Actions marketplace tool. It automatically optimizes images in Pull Requests and commits them back for you. 
Tip: To prevent an infinite loop where the "Auto-Commit" triggers the action again, the paths filter in the on: section ensures the script only runs when the original images in the input folder are changed, not when the optimized images are added to output. 

To keep your project clean and professional, you should follow the "Source vs. Build" pattern. This ensures you never accidentally delete your high-quality originals and keeps your web-ready files organized for your code to find.

The Ideal Folder Structure
my-web-project/
├── images-src/             <-- "The Source" (Input)
│   ├── hero-banner.jpg     (Your original 1408x768 file)
│   └── profile-pic.png
├── images-web/             <-- "The Build" (Output)
│   ├── hero-banner-mobile.avif
│   ├── hero-banner-mobile.webp
│   ├── hero-banner-tablet.avif
│   ├── hero-banner-tablet.webp
│   ├── hero-banner-desktop.avif
│   └── hero-banner-desktop.webp
├── process-images.js       (The automation script)
├── package.json            (Dependencies like 'sharp')
└── index.html              (Where you use the <picture> tags)

Why this structure works:
Safety: Your high-resolution master images are in images-src. If you ever need to change the compression level or size in the future, you still have the uncompressed originals.
Cleanliness: Your HTML code only ever looks inside images-web. This keeps your deployment folder free of "junk" or massive RAW files.
Git Ignore: You can choose to add images-src/ to your .gitignore file if you store your master assets in the cloud (like Google Drive) to keep your repository size small.
Final "Pro" Tip: Naming Conventions
Always use kebab-case (lowercase with hyphens) for image names.
Good: autumn-forest-desktop.avif
Bad: Autumn Forest Desktop.avif (Spaces cause broken links in browsers).
Your 2026 Web Image Master Plan:
Drop a 1408x768 JPG into /images-src.
Run your script (manually or via GitHub Action).
Link to the six generated files in /images-web using the <picture> tag.
Enjoy a lightning-fast, high-quality website!
Do you have any questions about how to link these specific folder paths in your HTML code?
Are you suggesting that I can add one 1408x768 jpg file and automagically all of those image options will become available for parsing on various devices?
Yes, exactly! That is the power of the automation script and the GitHub Action we discussed.
Here is the "magic" workflow in action:
You Upload One File: You drop your 1408x768 .jpg into the images-src/ folder and push it to GitHub.
The "Machine" Takes Over: GitHub Actions sees the new file. It runs the Sharp script, which instantly creates 6 new files (3 sizes in AVIF, 3 sizes in WebP) and puts them in the images-web/ folder.
The Code Handles the Rest: Because your HTML <picture> tag is already written to look for those specific filenames (e.g., hero-mobile.avif, hero-desktop.webp), the browser "automagically" picks the perfect version for the user's device.
The "Parsing" Secret
The browser doesn't actually "parse" the images to decide; it simply reads your srcset instructions. It's like a menu: you've provided the options, and the browser picks the "meal" that fits the user's "appetite" (screen size).
Your Final HTML Mapping
For a file named hero.jpg, your HTML would look like this to match your automated folders:
html
<picture>
  <!-- Mobile Options -->
  <source media="(max-width: 600px)" srcset="images-web/hero-mobile.avif" type="image/avif">
  <source media="(max-width: 600px)" srcset="images-web/hero-mobile.webp" type="image/webp">
  
  <!-- Desktop Options -->
  <source srcset="images-web/hero-desktop.avif" type="image/avif">
  <source srcset="images-web/hero-desktop.webp" type="image/webp">
  
  <!-- The Fallback -->
  <img src="images-web/hero-desktop.jpg" alt="Hero Banner" loading="lazy" width="1408" height="768">
</picture>

Manual-Automation Hybrid: Continue using tools such as Squoosh.app or XnConvert. It is important to hand-check the images to ensure details look correct in AVIF.
Use a Jekyll "Include": Create a reusable snippet instead of typing the long <picture> code for every image.
Create a file in the Jekyll folder: _includes/responsive-image.html.
Paste the <picture> code there.
In blog posts, write: {% include responsive-image.html name="roman-temple" alt="3D reconstruction of a Roman temple" %}
No-Crop Advantage: Since images are standalone historical reconstructions without text, cropping them for mobile is not required. However, historical details can get lost on a small phone screen.

Quick Tip for Historical Images:
Historical reconstructions often have fine lines. AVIF keeps tiny details sharp without the "fuzzy" artifacts seen in old JPEGs.

Here is your Master Step-by-Step Roadmap from the very top:

Phase 1: The Setup (Do this once)
Organize your GitHub Folders: Create two folders in your Jekyll project: images-src/ (for your 1408x768 originals) and images-web/ (for the final optimized files).
Add the "Brain": Create the process-images.js file and the .github/workflows/optimize-images.yml file using the code we discussed earlier.
Create the Jekyll Shortcut: Create _includes/responsive-image.html so you don't have to write long code every time.

Phase 2: The Daily Workflow (Your routine)
Create your historical reconstruction image.
Save that 1408x768 .jpg into your images-src/ folder (e.g., roman-forum.jpg).
Upload (Push) your changes to your GitHub repository.
The following will happen:
GitHub Actions detects the new file.
It runs the Sharp script.
It creates roman-forum-mobile.avif, roman-forum-desktop.webp, etc., and puts them in images-web/.
It automatically commits these new files back to your repo.

Phase 3: Displaying on Your Site
Use one line of code inside your Jekyll blog post or page:
markdown
{% include responsive-image.html name="roman-forum" alt="Reconstruction of the Roman Forum in 80 AD" %}

Benefits for a Research Project:
Accuracy: AVIF will keep the textures (marble, wood, stone) looking realistic even at small file sizes.
Longevity: The site will load quickly on any device.
Focus: Once the setup is done, the focus can be 100% on historical research.
Check: Does your Jekyll theme currently use a specific folder for images, or are you starting with a fresh "images-src" folder as planned?

Since you already have a structured path (_assets/img/stories/), we just need to tweak your folders and script slightly to fit the Jekyll way of doing things.

Here is your tailored setup guide:
1. New Folder Strategy
Keep the source (the 1408x768 originals) separate from the processed web files so Jekyll does not get confused:
Source: _assets/img/stories-src/. Place the Gemini-generated JPGs here.
Web-Ready: assets/img/stories/. The script will automatically put the AVIF/WebP files here.

2. Tweak the Automation Script
In the process-images.js file, update the paths to match the project:
javascript
// Change these lines in your script:
const inputFolder = './_assets/img/stories-src';
const outputFolder = './assets/img/stories';
Use code with caution.

3. The Jekyll "Magic" Snippet
Because Jekyll is being used, create a file at _includes/historical-image.html. This allows inserting these complex images with a single line of text:
html
<!-- _includes/historical-image.html -->
<picture>
  <!-- Mobile AVIF -->
  <source media="(max-width: 600px)" 
          srcset="{{ site.baseurl }}/assets/img/stories/{{ include.name }}-mobile.avif" type="image/avif">
  <!-- Desktop AVIF -->
  <source srcset="{{ site.baseurl }}/assets/img/stories/{{ include.name }}-desktop.avif" type="image/avif">
  
  <!-- Fallback to WebP for slightly older phones -->
  <source srcset="{{ site.baseurl }}/assets/img/stories/{{ include.name }}-desktop.webp" type="image/webp">
  
  <!-- The final fallback (The Original JPG) -->
  <img src="{{ site.baseurl }}/assets/img/stories/{{ include.name }}-desktop.jpg" 
       alt="{{ include.alt }}" 
       loading="lazy" 
       class="historical-reconstruction">
</picture>

4. How to Use it in the Stories
When writing a new historical post in Markdown, type this:
{% include historical-image.html name="pompeii-reconstruction" alt="A reconstructed street view of Pompeii" %}

Next Step
To get this "automagically" working, run npm install sharp in the project folder once.

Would you like information on how to update CSS to make these historical images look "museum-quality" (centered with a nice caption) on the Jekyll site?

To achieve a "museum-quality" look for your historical reconstructions on Jekyll, you should wrap your images in the semantic HTML <figure> tag. This naturally pairs the image with a <figcaption> that is centered and styled with refined typography. [1, 2] 
1. The "Museum" CSS Snippet
Add this to your main CSS or SCSS file (usually in assets/css/style.scss). It uses a "card" style with subtle shadows to make your reconstructions stand out. [3] 
/* Museum Gallery Style */
.historical-figure {
  margin: 2rem auto;
  max-width: 1408px; /* Matches your Gemini output size */
  text-align: center;
  background: #fff;
  padding: 15px;
  border: 1px solid #e0e0e0;
  box-shadow: 0 4px 20px rgba(0,0,0,0.08); /* Subtle depth */
}
.historical-figure img {
  display: block;
  width: 100%;
  height: auto;
  border-bottom: 1px solid #eee; /* Divider between image and text */
  margin-bottom: 12px;
}
.historical-caption {
  font-family: "Georgia", serif; /* Classic academic feel */
  font-size: 0.95rem;
  line-height: 1.5;
  color: #444;
  padding: 10px 20px;
  font-style: italic;
}
.historical-caption strong {
  display: block;
  font-style: normal;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.8rem;
  color: #888;
  margin-bottom: 5px;
}
2. Update Your Jekyll Include
Modify your _includes/historical-image.html to use these new classes and the <figure> structure. [4, 5] 
<figure class="historical-figure">
  <picture>
    <source media="(max-width: 600px)" srcset="{{ site.baseurl }}/assets/img/stories/{{ include.name }}-mobile.avif" type="image/avif">
    <source srcset="{{ site.baseurl }}/assets/img/stories/{{ include.name }}-desktop.avif" type="image/avif">
    <img src="{{ site.baseurl }}/assets/img/stories/{{ include.name }}-desktop.jpg" alt="{{ include.alt }}" loading="lazy">
  </picture>
  
  <figcaption class="historical-caption">
    <strong>Historical Reconstruction</strong>
    {{ include.caption }}
  </figcaption>
</figure>
3. Usage in Your Story
Now, when you write your post, you can include the specific historical context for that reconstruction: [6] 
{% include historical-image.html name="pompeii-gate" alt="The Herculaneum Gate" caption="A 3D reconstruction of the Herculaneum Gate in Pompeii, showing the original marble finish before the eruption of 79 AD." %}
Why this is "Museum-Quality":
* Contextual Captions: Unlike alt text (which describes what is literally in the image), the figcaption provides the historical significance and research context. [7, 8] 
* Visual Focus: The border and shadow create a "frame" effect, signaling to the reader that this is a key artifact of your research. [3] 
* Accessibility: Using <figure> and <figcaption> tells screen readers exactly which description belongs to which image. [9, 10] 
Would you like to know how to add a "Zoom" or "Fullscreen" feature so researchers can inspect the fine details of your reconstructions?

To allow your readers to inspect the fine details of your historical reconstructions without leaving the page, the most "museum-quality" approach is a Lightbox.
Since you are using Jekyll and GitHub Pages, we will use a "Vanilla JavaScript" method. This is lightweight, doesn't require complex plugins, and works perfectly with your existing folder structure.
1. The "Click to Enlarge" CSS
Add this to your stylesheet. It creates a dark overlay (the "modal") that appears when an image is clicked.
/* Lightbox Overlay */
.lightbox-modal {
  display: none;
  position: fixed;
  z-index: 9999;
  padding-top: 50px;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: rgba(0,0,0,0.9);
  cursor: zoom-out;
}
/* The Zoomed Image */
.lightbox-content {
  margin: auto;
  display: block;
  max-width: 90%;
  max-height: 80vh;
  box-shadow: 0 0 20px rgba(255,255,255,0.2);
}
/* The Caption in Lightbox */
#lightbox-caption {
  margin: auto;
  display: block;
  width: 80%;
  text-align: center;
  color: #ccc;
  padding: 20px 0;
  font-family: serif;
}
/* Hover effect on your main images */
.historical-figure img {
  cursor: zoom-in;
  transition: opacity 0.3s;
}
.historical-figure img:hover {
  opacity: 0.9;
}
2. The Interactive JavaScript
Place this at the very bottom of your layout file (usually _layouts/default.html), just before the </body> tag.
<div id="myLightbox" class="lightbox-modal" onclick="this.style.display='none'">
  <img class="lightbox-content" id="img01">
  <div id="lightbox-caption"></div></div>
<script>
document.querySelectorAll('.historical-figure img').forEach(image => {
  image.onclick = function() {
    document.getElementById("myLightbox").style.display = "block";
    document.getElementById("img01").src = this.src; // Uses the high-res desktop version
    document.getElementById("lightbox-caption").innerHTML = this.alt;
  }
});</script>
To allow your readers to inspect the fine details of your historical reconstructions without leaving the page, the most "museum-quality" approach is a Lightbox.
Since you are using Jekyll and GitHub Pages, we will use a "Vanilla JavaScript" method. This is lightweight, doesn't require complex plugins, and works perfectly with your existing folder structure.
1. The "Click to Enlarge" CSS
Add this to your stylesheet. It creates a dark overlay (the "modal") that appears when an image is clicked.
/* Lightbox Overlay */
.lightbox-modal {
  display: none;
  position: fixed;
  z-index: 9999;
  padding-top: 50px;
  left: 0; top: 0;
  width: 100%; height: 100%;
  background-color: rgba(0,0,0,0.9);
  cursor: zoom-out;
}
/* The Zoomed Image */
.lightbox-content {
  margin: auto;
  display: block;
  max-width: 90%;
  max-height: 80vh;
  box-shadow: 0 0 20px rgba(255,255,255,0.2);
}
/* The Caption in Lightbox */
#lightbox-caption {
  margin: auto;
  display: block;
  width: 80%;
  text-align: center;
  color: #ccc;
  padding: 20px 0;
  font-family: serif;
}
/* Hover effect on your main images */
.historical-figure img {
  cursor: zoom-in;
  transition: opacity 0.3s;
}
.historical-figure img:hover {
  opacity: 0.9;
}
2. The Interactive JavaScript
Place this at the very bottom of your layout file (usually _layouts/default.html), just before the </body> tag.
<div id="myLightbox" class="lightbox-modal" onclick="this.style.display='none'">
  <img class="lightbox-content" id="img01">
  <div id="lightbox-caption"></div>
</div>
<script>
document.querySelectorAll('.historical-figure img').forEach(image => {
  image.onclick = function() {
    document.getElementById("myLightbox").style.display = "block";
    document.getElementById("img01").src = this.src; // Uses the high-res desktop version
    document.getElementById("lightbox-caption").innerHTML = this.alt;
  }
});
</script>
3. How this helps Research:
* Inspection: Researchers can see specific brushstrokes or architectural details.
* Focus: The user's focus is on the reconstruction by dimming the rest of the website.
* No Extra Files: It uses the same 1408x768 image, so it doesn't slow the site by downloading "extra" high-res files unless clicked.
Final Summary Checklist:
   1. Image Source: 1408x768 JPG in _assets/img/stories-src/.
   2. Automation: GitHub Action creates AVIF/WebP in assets/img/stories/.
   3. Jekyll Include: Use the historical-image.html tag in your markdown.
   4. Presentation: CSS handles the "Museum Frame" and "Lightbox Zoom."

