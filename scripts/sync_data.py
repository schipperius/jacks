import pandas as pd
import os

# Paths (Update these if you moved files to _data/anthology/)
master_file = '_data/manifest.csv'
satellite_files = [
    '_data/attribution.csv', 
    '_data/location.csv'
]

def sync_data():
    master_df = pd.read_csv(master_file)
    master_order = master_df['image_slug'].tolist()
    
    for file_path in satellite_files:
        try:
            if not os.path.exists(file_path):
                pd.DataFrame(columns=['image_id', 'image_slug']).to_csv(file_path, index=False)
            
            sat_df = pd.read_csv(file_path)
            
            # --- THE FIX: WARNING MODE ---
            # Identify slugs in satellite file that are NOT in the Master hub
            orphans = sat_df[~sat_df['image_slug'].isin(master_order)]['image_slug'].tolist()
            
            if orphans:
                print(f"⚠️  WARNING: Found {len(orphans)} orphaned rows in {file_path} that are missing from Master:")
                for slug in orphans:
                    print(f"   - {slug}")
                print("   (These rows were NOT deleted. You should check if they need to be removed manually.)")

            # 1. Add missing rows from Master to Satellite
            new_rows = master_df[~master_df['image_slug'].isin(sat_df['image_slug'])].copy()
            if not new_rows.empty:
                to_add = new_rows[['image_id', 'image_slug']]
                sat_df = pd.concat([sat_df, to_add], ignore_index=True)
            
            # 2. Update IDs to match Master (Only for slugs that actually exist in Master)
            id_map = master_df.set_index('image_slug')['image_id']
            sat_df['image_id'] = sat_df['image_slug'].map(id_map)
            
            # 3. Re-order (Only sorts rows that have a match in Master; orphans stay at the bottom)
            sat_df['image_slug_cat'] = pd.Categorical(sat_df['image_slug'], categories=master_order, ordered=True)
            sat_df = sat_df.sort_values('image_slug_cat').drop(columns=['image_slug_cat']).reset_index(drop=True)
            
            # 4. Save
            sat_df.to_csv(file_path, index=False)
            print(f"✅ Synced: {file_path}")
            
        except Exception as e:
            print(f"❌ Error with {file_path}: {e}")

if __name__ == "__main__":
    sync_data()
