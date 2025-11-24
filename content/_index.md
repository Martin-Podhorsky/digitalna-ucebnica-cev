---
title: 'Domov'
date: 2023-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: hero
    content:
      title: Cestné Vozidlá
      text: Prehľadná učebnica Cestných vozidiel dostupná kedykoľvek a kdekoľvek!
      primary_action:
        text: Otvoriť
        url: /ucebnica/
        icon: book-open
    design:
      spacing:
        padding: [0, 0, 0, 0]
        margin: [0, 0, 0, 0]
      # For full-screen, add `min-h-screen` below
      css_class: "text-white-block text-center"
      background:
        color: ""
        image:
          filename: "hero-background.jpg"
  - block: features
    id: features
    content:
      title: Prečo ju používať?
      items:
        - name: Prehľadná
          icon: magnifying-glass
          description: Navigačné sidebary a taktiež funkcia vyhľadávania.
        - name: Praktická
          icon: bolt
          description: Nemusíte so sebou vláčiť 4 knihy; stačí mobil, tablet, alebo notebook.
        - name: Up-to-date
          icon: calendar-days
          description: Učebnica bola vytvorená v roku 2026 a dá sa ľahko aktualizovať, na rozdiel od papierových učebníc z roku 2002.
        - name: Elegantná
          icon: sparkles
          description: Jednoduchý, prehľadný, dobre-sa-naň-pozerajúci dizajn.
  - block: cta-card
    content:
      title: "Začni sa učiť s Digitálnou učebnicou Cestných vozidiel už dnes!"
      button:
        text: Otvoriť učebnicu
        url: /ucebnica/
    design:
      card:
        # Card background color (CSS class)
        css_class: "bg-primary-700"
        css_style: ""
---
