source "https://rubygems.org"

gem "jekyll", "~> 4.3" 

# Standard plugins group (Jekyll automatically requires these)
group :jekyll_plugins do
  gem "jekyll-scholar"
  gem "jekyll-feed"
  # gem "jekyll-autoprefixer" # To many build issues 2026-03-31
  gem "jekyll-sitemap", "~> 1.4"
  gem "jekyll-seo-tag", "~> 2.8"
end

# Dependencies & Tools
gem "webrick"       # Necessary for Ruby 3.0+ 'jekyll serve'
gem "faraday-retry" # Helper for faraday (often used by scholar)
gem "execjs"        # JavaScript execution (required by jekyll-autoprefixer)
gem 'html-proofer'  # link checker

gem "csv"
gem "base64"
gem "bigdecimal"
gem "mutex_m"