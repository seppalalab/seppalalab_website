---
title: Team
date: 2024-01-01
type: landing

sections:
  - block: people
    content:
      title: Meet the Team
      user_groups:
        - Principal investigator
        - Lab Members
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: false
      show_role: true
      show_social: true
      columns: 3
      css_class: team-section

  - block: markdown
    content:
      title: Alumni
      text: |
        <br>

        <!-- Format: **Name**, degree — original role, original affiliation · *now* current role, current institution
             Drop the "· *now* …" clause when current info is unavailable. -->

        **Nesrin Dinc** — Erasmus Exchange Student

        **Kornelia Kuc** — MSc student, University of Helsinki · Research Assistant, Evotec

        **Siiri Kuusela** — Research Assistant and MSc student, University of Helsinki

        **Elina Välkesalmi** — MSc student, University of Helsinki · Doctoral Researcher, University of Helsinki

        **Samuli Rajala** — Research Assistant and BSc student, University of Helsinki
    design:
      columns: '1'
      css_class: team-section section-alumni

  - block: markdown
    content:
      title: Visitors
      text: |
        <br>

        **Katarina Andini**, Doctoral Researcher from University of Groningen
    design:
      columns: '1'
      css_class: team-section section-visitors
---
