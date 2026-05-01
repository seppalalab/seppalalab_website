# Seppälä Lab Website — Claude Context

## Project overview
Static research group website built with **Hugo + HugoBlox (bootstrap v5 module)**, deployed via **GitHub Pages**. Non-coders manage content by editing Markdown files — no coding knowledge required.

## Tech stack
| Layer | Technology |
|-------|-----------|
| Static site generator | Hugo v0.161+ (extended) |
| Theme / framework | HugoBlox blox-bootstrap v5 (Hugo module) |
| Config format | YAML (all under `config/_default/`) |
| Deployment | GitHub Pages via GitHub Actions |
| Hosting | `<org>.github.io/<repo>` → custom domain in Phase 2 |

## Prerequisites (local development)
- Hugo extended: `brew install hugo`
- Go (for Hugo modules): `brew install go`
- Run site locally: `hugo server --buildDrafts` → opens at `http://localhost:1313`
- Build production: `hugo --minify` → output in `public/`

## Folder structure
```
seppalalab_website/
├── config/_default/         # All site config (edit here, not in content)
│   ├── hugo.yaml            # Site title, baseURL, build settings
│   ├── params.yaml          # Appearance, analytics, contact info, features
│   ├── menus.yaml           # Navigation bar links and order
│   ├── languages.yaml       # Language settings
│   └── module.yaml          # Hugo module imports (theme)
├── content/                 # ALL WEBSITE CONTENT LIVES HERE
│   ├── _index.md            # Homepage — edit sections/blocks here
│   ├── research/_index.md   # Research page
│   ├── people/index.md      # Team page (auto-populated from authors/)
│   ├── post/                # News posts (one folder per post)
│   ├── publication/         # Publications (one folder per paper)
│   ├── authors/             # Team member profiles (one folder per person)
│   └── contact/index.md     # Contact page
├── assets/media/            # Images (hero photo, team avatars go here)
├── static/                  # Files served as-is (PDFs, downloads)
├── layouts/                 # Custom HTML overrides (advanced, rarely needed)
├── go.mod / go.sum          # Hugo module dependencies (do not edit manually)
└── public/                  # Generated site output (git-ignored)
```

## Content editing guide (for non-coders)

### Add a team member
1. Copy `content/authors/pi-template/` → rename folder to `firstname-lastname` (lowercase)
2. Edit `_index.md` — fill in name, role, bio, social links
3. Add photo named `avatar.jpg` to that folder
4. Set `superuser: true` only for the PI

### Add a news post
1. Copy `content/post/example-news/` → rename to `YYYY-topic` (e.g. `2024-new-grant`)
2. Edit `index.md` — set title, date, tags, write content in Markdown
3. Set `draft: false` to publish
4. Optional: add `featured.jpg` for a thumbnail

### Add a publication
1. Copy `content/publication/example-paper/` → rename to `lastname-year-keyword`
2. Edit `index.md` — fill in authors, journal, abstract, links
3. Set `draft: false` to publish
4. Optional: add `paper.pdf` to the folder for direct PDF download

### Update research topics
- Edit `content/research/_index.md` directly — use Markdown headings (`###`) for each topic

### Update site info / contact
- Edit `config/_default/params.yaml` — find the `contact:` section

### Change navigation order
- Edit `config/_default/menus.yaml` — lower `weight` = appears first/left

## Deployment phases

### Phase 1 (current) — GitHub Pages, no custom domain
- Push to `main` branch → GitHub Actions builds and deploys automatically
- Site lives at: `https://<github-username>.github.io/seppalalab_website/`
- Set `baseURL` in `config/_default/hugo.yaml` to match this URL before first deploy

### Phase 2 — Custom domain
1. Update `baseURL` in `config/_default/hugo.yaml` to `https://your-domain.com/`
2. Add a file `static/CNAME` containing just `your-domain.com`
3. In GitHub repo Settings → Pages → Custom domain, enter the domain
4. Add DNS records at your registrar pointing to GitHub Pages IPs

## GitHub Actions deploy workflow
The file `.github/workflows/deploy.yml` (to be created) handles automated builds.
Standard Hugo GitHub Pages workflow — uses `peaceiris/actions-hugo` and `peaceiris/actions-gh-pages`.

## Key HugoBlox docs
- Page building blocks: https://docs.hugoblox.com/blocks/
- Author/team profiles: https://docs.hugoblox.com/content/authors/
- Publications: https://docs.hugoblox.com/content/publications/
- Appearance/themes: https://docs.hugoblox.com/getting-started/customize/

## What NOT to edit
- `go.mod` / `go.sum` — managed by `hugo mod get`
- `public/` — auto-generated, git-ignored
- `resources/` — build cache, git-ignored
