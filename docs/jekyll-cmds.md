# ------------------------------
# ONE-SHOT JEKYLL CLEAN + BUILD
# ------------------------------

1️⃣ Stop any running Jekyll server (just in case)
Ctrl+C in the terminal running jekyll serve.

2️⃣ Remove the generated site folder
rm -rf _site

3️⃣ Remove Jekyll cache
rm -rf .jekyll-cache

4️⃣ Optional: Remove any temporary gem cache (sometimes helps)
rm -rf .bundle

5️⃣ Search for any old include references (e.g., hero.html)
echo "🔍 Searching for old includes..."
grep -r "hero.html" _layouts _includes || echo "No references found."

6️⃣ Rebuild site cleanly
echo "🔄 Rebuilding site..."
bundle exec jekyll build --clean

7️⃣ Serve the site with live reload
echo "🚀 Serving site..."
bundle exec jekyll serve --livereload

