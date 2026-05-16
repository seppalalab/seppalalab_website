---
title: Publications
date: 2024-01-01
type: landing

sections:
  - block: collection
    content:
      title: Highlighted Publications
      text: ''
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: showcase
      columns: '1'
      flip_alt_rows: true

  - block: collection
    content:
      title: Recent Publications
      text: ''
      count: 5
      filters:
        folders:
          - publication
        exclude_featured: true
      buttons: []
    design:
      view: citation
      columns: '1'
      sort_by: Date
      sort_ascending: false

  - block: markdown
    content:
      title: ''
      text: |
        **[View all publications on PubMed →](https://pubmed.ncbi.nlm.nih.gov/?term=Seppala+TT%5BAuthor%5D&sort=date)**
    design:
      columns: '1'
---
