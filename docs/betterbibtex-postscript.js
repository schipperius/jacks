if (Translator.BetterCSLYAML) {
  // 1. Flatten Authors to "First Last, First Last"
  if (item.creators && item.creators.length > 0) {
    reference.author_list = item.creators
      .map(c => `${c.firstName} ${c.lastName}`.trim())
      .join(', ');
  }

  // 2. Flatten Date
  if (item.date) reference.date = item.date;

  // 3. Flatten Publication
  if (item.publicationTitle) reference.publication = item.publicationTitle;

  // 4. Flatten Tags
  if (item.tags && item.tags.length > 0) {
    reference.tags = item.tags.map(t => t.tag).join(', ');
  }

  // 5. Extract Chapters (Keeping Note)
  if (item.extra) {
    const match = item.extra.match(/^chapters:\s*(.+)/m);
    if (match) reference.chapters = match[1];
  }
}
