import csv
import os
import frontmatter

# Configuration
csv_path = '_data/plates.csv'
output_dir = '_content/_plates'

def sync_plates():
    if not os.path.exists(csv_path):
        print(f"Error: {csv_path} not found.")
        return

    with open(csv_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # We use the image_id from the CSV to find the correct file
            image_id = row['image_id']
            filename = os.path.join(output_dir, f"{image_id}.md")
            
            # 1. Load existing file or create a blank slate
            if os.path.exists(filename):
                post = frontmatter.load(filename)
            else:
                # If the file is new, we start with empty content
                post = frontmatter.Post("")
            
            # 2. Sync ONLY the structural keys
            # Everything else already in the front matter (image_alt, etc.) is preserved
            post['layout'] = 'plate'
            post['image_id'] = image_id

            # 3. Save the file back to your _content/_plates/ directory
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'wb') as f:
                frontmatter.dump(post, f)

    print(f"Sync complete. Structural keys updated, research content preserved.")

if __name__ == "__main__":
    sync_plates()
