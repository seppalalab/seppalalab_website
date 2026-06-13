---
title: News
date: 2024-01-01
type: landing

sections:
  - block: markdown
    content:
      title: News
      text: '<p style="text-align:center; font-size:1.1rem;">Updates from the lab, recent publications, events, and scientific highlights.</p>'
    design:
      columns: '1'
      css_class: news-section

  - block: collection
    content:
      title: ''
      filters:
        folders:
          - post
        featured_only: true
      archive:
        enable: false
    design:
      view: article
      columns: '1'
      css_class: news-section

  - block: collection
    content:
      title: ''
      filters:
        folders:
          - post
        exclude_featured: true
      archive:
        enable: false
    design:
      view: card
      columns: '3'
      sort_by: Date
      sort_ascending: false
      css_class: news-section
---
