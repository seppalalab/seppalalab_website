# Contributing to Seppälä Lab GitHub

Welcome to the **tseppalalab** GitHub organization. This guide covers everything lab members need to know to contribute — whether you are editing the lab website or publishing research resources.

---

## What lives here

| Repository | Purpose |
|---|---|
| `seppalalab_website` | Lab website (Hugo static site, deployed to GitHub Pages) |
| Other repositories | Research resources: data, code, posters, supplementary materials |

---

## Part 1 — Contributing to the Website

The website is built with Hugo and deployed automatically to GitHub Pages whenever changes are pushed to the `main` branch. You do **not** need to know how to code — all content is written in Markdown.

For full instructions see **[website-maintaining-guidelines.md](website-maintaining-guidelines.md)** in the website repository. A quick summary:

### What you can safely edit

| Content | Location |
|---|---|
| Team member profiles | `content/authors/<your-name>/_index.md` |
| News posts | `content/post/<post-folder>/index.md` |
| Publications | `content/publication/<paper-folder>/index.md` |
| Research page text | `content/research/_index.md` |
| Contact info | `config/_default/params.yaml` |

<br>
<br>

### Two ways to make edits

**Option A — In the browser (no software needed, best for small edits)**
1. Go to the repository on GitHub
2. Navigate to the file you want to edit
3. Click the pencil icon → edit → scroll down → Commit changes
4. The site rebuilds and goes live within 1–2 minutes

**Option B — On your computer (best for adding images or larger edits)**
1. Clone the repo, install Hugo + Go (see the full guidelines for instructions)
2. Run `hugo server --buildDrafts` to preview at `http://localhost:1313`
3. Edit files, check the preview, then `git add . && git commit -m "your message" && git push`

### Getting write access

Ask the repository owner (Emmi) to add you as a collaborator:
- Repo **Settings → Collaborators → Add people** → enter your GitHub username
- You will receive an email invitation — accept it before making changes

---

## Part 2 — Publishing Research Resources

The tseppalalab GitHub organization can host supplementary materials for publications, posters, datasets, and code. Keeping these on GitHub (and archiving them to Zenodo for a permanent DOI) makes them citable, persistent, and easy to share.

### What belongs in a research repository

- **Code** associated with a publication (analysis scripts, pipelines, custom tools)
- **Data** that is small enough to store on GitHub (< 100 MB per file, < 1 GB total)
- **Posters** (PDF format)
- **Supplementary materials** (tables, figures, protocols)

> For large datasets (> 1 GB), use Zenodo directly for upload — GitHub is not designed for large binary files.

<br>
<br>

### How to create a research repository

1. Go to [github.com/tseppalalab](https://github.com/tseppalalab)
2. Click **New repository** (green button, top right)
3. Name it clearly: use the format `lastname-year-keyword` (e.g. `hokkanen-2026-mlh1-code`)
4. Set visibility to **Public** (required for Zenodo archiving and citability)
5. Check **Add a README file**
6. Click **Create repository**

### README template for a research repository

Every research repository should have a README that helps others understand and reuse the content. Use this template:

```markdown
# [Short descriptive title]

**Associated publication:** [Full citation or DOI link]

## Contents

| File / Folder | Description |
|---|---|
| `scripts/` | Analysis scripts |
| `data/` | Input data files |
| `figures/` | Generated figures |
| `poster.pdf` | Conference poster |

## Requirements

[List any software, languages, or dependencies needed to run the code]

## Usage

[Short instructions for reproducing the analysis or using the data]

## Citation

If you use this material, please cite:
> [Author et al. (Year). Title. Journal. DOI]

## License

[Choose one — see below]
```

### Choosing a license

Add a `LICENSE` file when creating the repository (GitHub offers a picker). Recommended choices:

| Material | Recommended license |
|---|---|
| Code / scripts | MIT License (permissive, allows reuse with attribution) |
| Data / figures | Creative Commons CC BY 4.0 (attribution required) |
| Unsure | Ask Emmi |

---

## Part 3 — Zenodo Integration

[Zenodo](https://zenodo.org) is a free, long-term research archive run by CERN. It assigns a permanent **DOI** to each deposit, making your research outputs citable for decades.

The **Seppälä Lab Zenodo community** is at:
`https://zenodo.org/communities/seppalalab`

All lab research outputs should be added to this community so they are discoverable in one place.

### Option A — Automatic archiving via GitHub (recommended for code and mixed repositories)

This links a GitHub repository to Zenodo so that every time you create a GitHub Release, Zenodo automatically archives a snapshot and assigns a DOI.

**One-time setup (done by the repository owner):**

1. Go to [zenodo.org](https://zenodo.org) and log in (create a free account if needed)
2. Click your name (top right) → **GitHub**
3. Find the repository in the list and toggle it **ON**
4. Return to GitHub and create a Release:
   - Go to the repository → **Releases** (right sidebar) → **Create a new release**
   - Set a tag (e.g. `v1.0`), add a title and description, click **Publish release**
5. Zenodo automatically creates a DOI within a few minutes
6. Go to [zenodo.org](https://zenodo.org) → find your upload → click **Edit** → add it to the **seppalalab** community → **Save**

**Getting the badge for your README:**

After the deposit is created, go to the Zenodo record page and copy the DOI badge Markdown. Add it to the top of your repository README:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
```

### Option B — Direct upload to Zenodo (for large datasets, posters, standalone files)

Use this when the material is too large for GitHub or is a single file (poster PDF, large dataset).

1. Go to [zenodo.org](https://zenodo.org) → log in → **+ New upload** (top right)
2. Drag and drop your files
3. Fill in the metadata: title, authors, publication date, description, license
4. Under **Communities**, search for `seppalalab` and select it
5. Click **Publish** — you will receive a DOI immediately
6. Share the DOI link in the associated paper or on the lab website

### Linking a Zenodo DOI on the lab website

In the publication's `index.md`, add the DOI to the `url_dataset:` or `url_code:` field:

```yaml
url_dataset: 'https://doi.org/10.5281/zenodo.XXXXXXX'
url_code: 'https://doi.org/10.5281/zenodo.XXXXXXX'
```

Or link it in the body of a news post using standard Markdown:

```markdown
Data and code are available on [Zenodo](https://doi.org/10.5281/zenodo.XXXXXXX).
```

---

<br>
<br>
<br>
<br>
<br>
<br>

## Quick reference

| Task | Where to do it |
|---|---|
| Edit website content | GitHub browser editor or local clone — see `website-maintaining-guidelines.md` |
| Get website write access | Ask Emmi to add you as collaborator |
| Publish code with a paper | Create a `lastname-year-keyword` repo, enable Zenodo, create a Release |
| Upload a poster or large dataset | Upload directly to Zenodo, add to seppalalab community |
| Add a DOI to the website | Edit the publication `index.md`, fill in `url_dataset:` or `url_code:` |
| Zenodo community | [zenodo.org/communities/seppalalab](https://zenodo.org/communities/seppalalab) |

---

## Questions?

Open an issue in the relevant repository or contact Emmi (tseppalalab@gmail.com).
