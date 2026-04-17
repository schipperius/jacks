Best practices for retrieving and storing images with proper citation involve a hybrid approach: 
storing images in a dedicated file system (or cloud storage) while keeping citation metadata in a database. 
This ensures performance, scalability, and ethical, legal compliance (e.g., copyright protection) by maintaining a permanent, traceable link to the original source. 

I. Best Practices for Retrieving & Documenting (Citation)
Identify the Original Source: Do not cite search engines like Google Images; click through to find the original website, photographer, or artist.
Collect Minimum Metadata: Always record the creator (photographer/artist), title of the work, date of creation, source URL, and date of access.
Check Licensing & Permissions: Look for Creative Commons (CC) licenses or public domain markers. If no license is specified, assume it is protected by copyright and seek permission.
Use Specialized Search Tools: Use resources that provide licensing info, such as Wikimedia Commons, Flickr (filtered by license), or reverse image searches (TinEye, Google) to locate the source.
Create a Citation Log: Maintain a log or spreadsheet for each image, documenting the steps taken to verify its usage rights. 

II. Best Practices for Storing Images
File System/Cloud Storage: Store actual image files in a dedicated file system, Amazon S3, or similar object storage.
Database References: Save only the file path (URL or directory path) in your relational database (e.g., PostgreSQL, MySQL). This prevents "database bloat" and improves performance.
Unique File Naming: Use UUIDs or hashes for filenames to avoid conflicts.
Metadata Storage: Embed metadata (copyright info, author, title) directly into the image files using formats like EXIF or XMP, allowing the metadata to travel with the photo. 

III. Citation Formats and Display
In-Text/Caption: Place the citation immediately below the image (e.g., "Figure 1: [Title] by [Creator]. [Source URL] [License]").
Citation Examples:
Creative Commons: "Mermaid Cove Sunrise" by Jerry Meadon is licensed under CC BY-NC-SA 2.0.
Online Image: Creator Last Name, First Name. "Title of Work." Website Name, Date, URL (Accessed Date).
Digital Asset Management (DAM): Use a system that allows for tagging and storing descriptive metadata alongside the image file. 
Massachusetts Institute of Technology

IV. Ethical & Legal Compliance
AI-Generated Images: Acknowledge the AI tool used (e.g., "Image generated using [Tool Name] [Date]").
Respect "All Rights Reserved": Do not use copyrighted images without explicit permission, even if you cite them.
Modification: If you alter an image, note "Adapted from" in the citation. 

By adhering to these practices, you ensure that your image usage is both legally compliant and academically/professionally sound.