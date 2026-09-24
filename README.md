# INNO-SCREW — project website

Static bilingual (DE/EN) website for the INNO-SCREW research project
(RIF Institut für Forschung und Transfer e.V. · IPS, TU Dortmund).

## Publishing on GitHub Pages

1. Upload the contents of this folder to the repository root (not the folder itself).
2. Repository → **Settings → Pages** → Source: *Deploy from a branch* → Branch `main`, folder `/ (root)`.
3. The site appears at `https://<user>.github.io/<repo>/` after a minute or two.

No build step is required. Everything is plain HTML, CSS and JavaScript.

## Structure

```
index.html              Home — project status, research approach, latest news
project.html            Project — funding, work packages, team, institutions
infrastructure.html     Research infrastructure — five screwdriving systems (tabbed)
station-ass.html        Automatic screwdriving station (ASS)
station-rss.html        Robot-based screwdriving station (RSS)
station-mss.html        Manual screwdriving station (MSS)
station-dss.html        Dual-spindle screwdriving station (DSS)
station-kss.html        Cordless screwdriving systems (KSS)
data.html               Research data — dataset metadata, status, terminology
publications.html       INNO-SCREW publications · related research · software
news.html               Chronological news with category filter
contact.html            Contacts, funding details, legal notice, privacy
assets/style.css        All styling
assets/main.js          Language toggle, theme toggle, mobile nav, tabs, news filter
assets/*.png/.jpg/.webp Logo, BMWE logo, team photos, system photos
```

Old URLs (`about.html`, `stations.html`, `station-s1.html` … `station-s5.html`,
`demo.html`, `ap01.html` … `ap04.html`) are kept as redirect stubs so existing
links do not break. Delete them once nothing points at them any more.

## Identifier scheme

Three levels are kept strictly separate across the whole site:

| Level | Example | Meaning |
| --- | --- | --- |
| Screwdriving system | `ASS`, `RSS`, `MSS`, `DSS`, `KSS` | Physical station in the research infrastructure |
| Experimental scenario | `S01` … `S06` | A defined series of trials with its own set of process deviations |
| Dataset | `DS-2025-01`, `DS-2026-01` | A dataset or measurement campaign with its own version, licence and DOI |

"Domain" is reserved for machine-learning contexts (source/target domain,
domain adaptation) and is **not** used for physical stations.

## Terminology conventions

- **OK / NOK** throughout — *IO/NIO* is no longer used.
- *Schraubprozesse* / *Schraubvorgänge*, not *Verschraubungsvorgänge* or *Schraubbeobachtungen*.
- *statistische Prozessüberwachung* (SPC).
- Deviation types: **Cross-threading**, **Thread deformation**,
  **Increased tightening torque** / *Erhöhtes Anziehdrehmoment*.
- Neutral, descriptive wording — no promotional claims.

## Editing content

Pages are generated from `tools/build.py` (run it from inside `tools/`). You can
edit the HTML directly instead; if you prefer to regenerate, the content lives
in these structures inside `build.py`:

- `SYSTEMS` — the five screwdriving systems, their specifications and photos
- `SCENARIOS` — S01–S06 with station, sample count and class count
- `DATASETS` — dataset metadata blocks on `data.html`
- `PUBS` — publication list and BibTeX entries
- `NEWS` — news entries, each with a category from `CATS`
- `PROJECT_STATUS` — the status board shown on `index.html` and `project.html`

### Adding a news entry

Append an `<article class="nentry" id="…" data-cat="…">` block at the top of the
list in `news.html`. Valid `data-cat` values: `update`, `dataset`, `publication`,
`conference`, `transfer`, `infrastructure`. The filter buttons pick it up
automatically.

### Updating the project status

Edit the `.status-grid` cells in `index.html` and `project.html` (both pages
carry the same block), and update the "Letzte Aktualisierung / Last update"
cell each time.

## Language and theme

Both toggles live in the navigation bar and store their state in
`localStorage`, so the choice persists across pages.

- Elements with `data-de` / `data-en` attributes swap their text content.
- Elements with class `de-block` / `en-block` are shown or hidden as blocks —
  use these for whole paragraphs.

## Notes

- Fonts load from Google Fonts; this is disclosed in the privacy notice on
  `contact.html`.
- No cookies, no analytics, no form submission.
