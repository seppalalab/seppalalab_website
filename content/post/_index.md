---
title: News
date: 2024-01-01
type: landing

sections:
  - block: markdown
    content:
      title: News
      text: ''
    design:
      columns: '1'

  - block: collection
    content:
      title: Latest News
      text: ''
      filters:
        folders:
          - post
        featured_only: true
      archive:
        enable: false
    design:
      view: article
      columns: '1'
      css_class: section-subheading-sm

  - block: collection
    content:
      title: Read more news
      text: ''
      count: 9
      filters:
        folders:
          - post
        exclude_featured: true
      archive:
        enable: false
    design:
      view: card
      columns: '3'
      css_class: section-subheading-sm
---
