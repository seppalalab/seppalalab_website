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

  - block: collection
    content:
      title: Highlight
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
      title: Latest News
      text: ''
      count: 3
      offset: 0
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

  - block: collection
    content:
      title: Read More News
      text: ''
      count: 6
      offset: 3
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
