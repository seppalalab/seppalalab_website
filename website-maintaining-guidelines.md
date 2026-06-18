# Website Maintaining Guidelines

## 1. Project Folder Overview

The project is split into three categories: **content you can freely edit**, **Hugo backend files you should not touch**, and **frontend/theme override files** that require HTML/CSS knowledge.

---

### Editable content folders

These folders contain all the website's text, images, and configuration. Most routine maintenance happens here.

| Folder / File                    | What it controls                                |
| -------------------------------- | ----------------------------------------------- |
| `content/authors/`               | Team member profiles, one sub-folder per person |
| `content/post/`                  | News and announcements, one sub-folder per post |
| `content/publication/`           | Publications, one sub-folder per paper          |
| `content/research/_index.md`     | Research page layout and intro text             |
| `content/people/index.md`        | Team page layout settings                       |
| `content/contact/index.md`       | Contact page settings                           |
| `content/_index.md`              | Homepage blocks and sections                    |
| `config/_default/hugo.yaml`      | Site title, base URL, build settings            |
| `config/_default/params.yaml`    | Appearance, contact info, features              |
| `config/_default/menus.yaml`     | Navigation bar links and order                  |
| `config/_default/languages.yaml` | Language settings                               |
| `assets/media/`                  | Shared images, site logo, favicon, hero photo   |
| `static/`                        | Files served as-is, PDFs and other downloads    |
| `data/themes/`                   | Custom colour theme definitions                 |
| `data/funders.yaml`              | Funding page — list of funders with name, URL, logo |
| `data/collaborators.yaml`        | Funding page — list of collaborators with name, institution, role |
| `data/research_topics.yaml`      | Research page — topic cards with title, text, image |

---

### Hugo backend — do not edit

These files are managed automatically by Hugo's module system. Editing them manually can break the build.

| Folder / File | Purpose                                              |
| ------------- | ---------------------------------------------------- |
| `go.mod`      | Declares which version of the HugoBlox theme is used |
| `go.sum`      | Cryptographic checksums for Hugo module dependencies |
| `public/`     | Auto-generated site output, recreated on every build |
| `resources/`  | Build cache, recreated automatically                 |

---

### Frontend / theme overrides — edit with care

These files override the default HugoBlox theme. Editing them requires knowledge of HTML, Go templating, or CSS.

| Folder / File | Purpose |
|---|---|
| `layouts/` | Custom HTML template overrides |
| `assets/jsconfig.json` | JavaScript configuration for asset processing |
| `i18n/` | Translation strings for multi-language support |
| `archetypes/` | Default front-matter templates for new content |

---

## 2. Making Changes on a Local Repository

Working locally lets you preview changes before they go live. This is the recommended approach for any non-trivial edits.

### Requirements

| Software                | Purpose                                      | Minimum version    |
| ----------------------- | -------------------------------------------- | ------------------ |
| Git                     | Version control, cloning and pushing changes | Any recent version |
| Hugo (extended edition) | Builds and previews the site locally         | v0.161 or newer    |
| Go                      | Required by Hugo's module system             | v1.21 or newer     |

### Step 1 - Install required software

#### macOS

Open the **Terminal** application and run:

```bash
# Install Homebrew (skip if already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Git
brew install git

# Install Hugo (extended edition)
brew install hugo

# Install Go
brew install go
```

Verify the installations:

```bash
git --version
hugo version    # should say "extended" in the output
go version
```

#### Windows

The recommended approach on Windows is to use **Winget** (built into Windows 10/11) from the **Command Prompt** or **PowerShell**. Open either application (search for it in the Start menu) and run:

```powershell
# Install Git
winget install --id Git.Git -e --source winget

# Install Hugo (extended edition)
winget install --id Hugo.Hugo.Extended -e --source winget

# Install Go
winget install --id GoLang.Go -e --source winget
```

**Close and reopen** your terminal after installing so the new commands are recognised, then verify:

```powershell
git --version
hugo version    # should say "extended" in the output
go version
```

> **Note:** If `winget` is not available on your machine, you can install each tool manually:
> - Git: download the installer from [git-scm.com/download/win](https://git-scm.com/download/win)
> - Hugo: download the **extended** edition `.zip` from the [Hugo releases page](https://github.com/gohugoio/hugo/releases), extract it, and add the folder to your system PATH
> - Go: download the installer from [go.dev/dl](https://go.dev/dl)

### Step 2 - Configure Git with your identity

This only needs to be done once per machine. Run in Terminal (macOS) or Command Prompt / PowerShell (Windows):

```bash
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### Step 3 - Clone the repository

```bash
git clone git@github.com:emsqqq/seppalalab_website.git
cd seppalalab_website
```

### Step 4 - Download theme dependencies

Run this once after cloning, and again if `go.mod` ever changes:

```bash
hugo mod get
```

### Step 5 - Start the local preview server

```bash
hugo server --buildDrafts
```

Open a browser and go to `http://localhost:1313`. The site reloads automatically as you save files.
Press `Ctrl + C` in the terminal / Command Prompt to stop the server.

### Step 6 - Make your edits

Edit files in the folders listed under **Editable content folders** above.
The browser preview updates within a few seconds of saving.

### Step 7 - Save and upload your changes

Once you are happy with the result:

```bash
# Stage all changed files
git add .

# Commit with a short description of what you changed
git commit -m "Update Jane Doe bio"

# Upload to GitHub
git push
```

GitHub Actions will automatically build and deploy the updated site within 1–2 minutes.

### Troubleshooting: `git push` asks for credentials or fails

This repository uses an **SSH key** for authentication — no password or token needed.

**Verify SSH is configured correctly (one-time check):**

```bash
ssh -T git@github.com
```

You should see: `Hi emsqqq! You've successfully authenticated…`

**Ensure the remote URL uses SSH (not HTTPS):**

```bash
git remote set-url origin git@github.com:emsqqq/seppalalab_website.git
```

After that, `git push` works silently with no prompts.

> **If you get `Permission denied (publickey)`:** your SSH key is not loaded. Run `ssh-add ~/.ssh/id_ed25519` and try again. If the key file does not exist, a new SSH key needs to be generated and added to GitHub (Settings → SSH keys).

---

## 3. Making Changes on the Remote Repository (GitHub Only)

This approach requires no software installation and works entirely in a web browser. It is best suited for small text edits. There is no preview so changes go live immediately after the build finishes.

### Requirements

- A GitHub account (free), register at [github.com](https://github.com)
- **Write access** to the repository, ask the repository owner to add you as a collaborator:
  - Repository owner goes to **Settings → Collaborators → Add people** and enters your GitHub username or email
  - You will receive an email invitation, accept it before you can make changes

### Step 1 - Navigate to the repository

Go to `https://github.com/<github-username>/<repository-name>` in your browser.

### Step 2 - Find the file to edit

Browse the folder structure to find the file you want to change (see the **Editable content folders** table above for guidance).
Click the file name to open it.

### Step 3 - Open the editor

Click the **pencil icon** (Edit this file) in the top-right corner of the file view.

### Step 4 - Make your edits

Edit the file directly in the browser. The file uses Markdown formatting:

- `**bold**` → **bold**
- `*italic*` → *italic*
- `# Heading 1`, `## Heading 2`, `### Heading 3`
- A blank line between paragraphs

### Step 5 - Commit the changes

Scroll to the bottom of the page to the **Commit changes** section:

1. Write a short description of your change in the first field (e.g. `Update research topics`)
2. Leave **Commit directly to the main branch** selected
3. Click **Commit changes**

### Step 6 - Confirm the build

Go to the **Actions** tab in the repository. You should see a workflow run triggered by your commit. A green checkmark means the site has been rebuilt and deployed successfully. A red cross means something went wrong, click the run to read the error log.

### Uploading images on GitHub (without local setup)

1. Navigate to the target folder (e.g. `content/authors/jane-doe/`)
2. Click **Add file → Upload files**
3. Drag and drop the image file (avatar photos must be named `avatar.jpg`)
4. Scroll down and click **Commit changes**

---

## 4. The `static/` Folder — What Goes There

The `static/` folder holds files that Hugo copies to the website as-is, without any processing. Anything placed here becomes directly accessible via a URL.

**When to use it:**

| File type               | Example                       | Resulting URL                                 |
| ----------------------- | ----------------------------- | --------------------------------------------- |
| Downloadable PDFs       | `static/papers/smith2024.pdf` | `yoursite.com/papers/smith2024.pdf`           |
| Custom domain config    | `static/CNAME`                | Used by GitHub Pages, not visible to visitors |
| Downloadable data files | `static/data/dataset.csv`     | `yoursite.com/data/dataset.csv`               |
| Custom `robots.txt`     | `static/robots.txt`           | `yoursite.com/robots.txt`                     |

**How to link to a file in `static/` from a content page:**

```markdown
[Download paper (PDF)](/papers/smith2024.pdf)
```

Note the leading `/` — the path starts from the root of the site, not the `static/` folder itself.

**What does NOT go here:**

- Team member avatars → go in `content/authors/<name>/avatar.jpg`
- Site logo or favicon → go in `assets/media/`
- Post or publication images → go in the same folder as the content file

---

## 5. Use-Case Scenarios

Short step-by-step guides for the most common maintenance situations.

### A team member has left the lab

**Option 1: Remove them entirely**
1. Delete their folder `content/authors/<name>/`
2. Remove their name from any publication `authors:` lists if you want to clean those up (not required — the name will just appear as plain text)

**Option 2: Keep them listed as alumni**

Alumni are listed as plain text at the bottom of the Team page. To add or update an alumni entry:

1. Open `content/people/_index.md`
2. Find the `Alumni` markdown block near the bottom of the file
3. Add a new line following this format:
   ```
   **First Name Last Name**, Degree — Role
   ```
   Examples:
   ```
   **Kornelia Kuc**, MSc — Student
   **Samuli Rajala**, MSc — Research Assistant
   **Katarina Andini** — Visiting Researcher
   ```
   - **Degree** = highest degree held or being pursued at the time (MSc, PhD, BSc) — omit if not applicable
   - **Role** = their position in the lab (Student, Research Assistant, Visiting Researcher, Erasmus Exchange Student)
4. Save and commit — the change appears on the Team page immediately after the next build

> No separate author folder is needed for alumni. Current affiliation is intentionally not listed as it changes over time.

### Add or update a visitor

Visitors are listed as plain text at the bottom of the Team page, below Alumni. To add or update a visitor entry:

1. Open `content/people/_index.md`
2. Find the `Visitors` markdown block at the bottom of the file
3. Add a new line following this format:
   ```
   **First Name Last Name**, Position from Affiliation
   ```
   Example:
   ```
   **Katarina Andini**, Doctoral Researcher from University of Groningen
   ```
   - **Position** = their role or degree status at the time of the visit (e.g. Doctoral Researcher, MSc Student, Postdoctoral Researcher)
   - **Affiliation** = their home institution
4. Save and commit — the change appears on the Team page after the next build

> When a visitor leaves the lab, move their entry from the Visitors block to the Alumni block and update the format to `**Name**, Degree — Role`.

### Add a downloadable PDF (e.g. a preprint or dataset)

1. Place the PDF in `static/` — for example `static/papers/smith2024.pdf`
2. In the relevant publication or post file, add a link in the body:
   ```markdown
   [Download PDF](/papers/smith2024.pdf)
   ```
   Or use the `url_pdf:` field in a publication's front matter:
   ```yaml
   url_pdf: '/papers/smith2024.pdf'
   ```

### Why HugoBlox was chosen

HugoBlox was selected because it is the easiest framework for non-coders to maintain. It provides ready-made templates for academic content types — publications, team member profiles, and news posts — which can be updated by editing simple text fields without any coding knowledge.

Switching to a different Hugo theme (non-HugoBlox) would require rewriting most of the site content and configuration, and would lose these built-in academic features. Switching to an entirely different platform (e.g. Jekyll, WordPress) would require a full site migration. Available HugoBlox colour themes are listed below — appearance can be changed without touching any other part of the site.

---

### Change the site's colour scheme

The colour theme is set in `config/_default/params.yaml` under the `appearance:` section:

```yaml
appearance:
  theme_day: seppala        # theme used in light mode
  theme_night: seppala-dark # theme used in dark mode (optional)
```

#### Built-in themes

These names can be used directly — no extra files needed. Only themes marked **Yes** in the `theme_day` column work as a day/light theme; the others are dark-only and must be used as `theme_night`.

| Name         | Feel                        | `theme_day` | `theme_night` |
| ------------ | --------------------------- | ----------- | ------------- |
| `minimal`    | Clean white, black accents  | Yes         | —             |
| `ocean`      | Blue tones                  | Yes         | —             |
| `forest`     | Green tones                 | Yes         | —             |
| `earth`      | Warm brown / terracotta     | Yes         | —             |
| `rose`       | Pink / rose                 | Yes         | —             |
| `coffee`     | Warm brown                  | Yes         | —             |
| `strawberry` | Red / pink                  | Yes         | —             |
| `1950s`      | Retro warm                  | Yes         | —             |
| `cyberpunk`  | High contrast neon           | Yes         | —             |
| `dark`       | Full dark                   | —           | Yes           |
| `apogee`     | Dark navy                   | —           | Yes           |
| `mr_robot`   | Dark hacker-style           | —           | Yes           |

#### Custom themes (this site)

Two custom themes are defined in `data/themes/`:

| File                       | Name           | Use as       |
| -------------------------- | -------------- | ------------ |
| `data/themes/seppala.toml` | Seppala        | `theme_day`  |
| `data/themes/seppala-dark.toml` | Seppala Dark | `theme_day` or `theme_night` |

Both use the lab colour palette: `#671927` (dark red) and `#979797` (dark gray). The `seppala-dark` variant uses a charcoal background with burgundy accents for a darker feel.

#### How to preview a theme without publishing

1. Open `config/_default/params.yaml` and change `theme_day:` to the theme name you want to try
2. Run `hugo server --buildDrafts` in the terminal
3. Open `http://localhost:1313` in a browser — it updates live as you change the value
4. Press `Ctrl + C` to stop. Revert the change in `params.yaml` if you don't want to keep it

#### Create a new custom theme

1. Create a new `.toml` file in `data/themes/` (e.g. `data/themes/mytheme.toml`)
2. Copy the contents of `data/themes/seppala.toml` as a starting point
3. Edit the colour hex values — the `[light]` section controls light mode, `[dark]` controls dark mode
4. Set `theme_day: mytheme` in `params.yaml` to activate it

> Changing the entire site framework (e.g. switching from HugoBlox to a completely different Hugo theme) is a major undertaking that requires rewriting most of the content front matter and configuration. It is not recommended unless there is a strong reason.

### Set up a custom domain

1. Update `baseURL` in `config/_default/hugo.yaml` to `https://your-domain.com/`
2. Create a file `static/CNAME` containing just your domain name (no `https://`):
   ```
   your-domain.com
   ```
3. In the GitHub repository, go to **Settings → Pages → Custom domain**, enter your domain, and save
4. At your domain registrar, add DNS A records pointing to GitHub Pages' IP addresses (GitHub lists the current IPs in their Pages documentation)
5. Wait up to 24 hours for DNS to propagate — GitHub will provision an SSL certificate automatically once it resolves

### Temporarily hide a post or publication without deleting it

Open the content file (`index.md`) and set:

```yaml
draft: true
```

The item disappears from the live site on the next build but remains in the repository. Set it back to `draft: false` to republish.

### Change the order of items in the navigation bar

Open `config/_default/menus.yaml`. Each menu item has a `weight:` value — **lower numbers appear first** (left-most in the nav bar).

Example — to move Research before People, give Research a lower weight:

```yaml
- name: Research
  weight: 20
- name: People
  weight: 30
```

### A build fails after a change (red cross in Actions)

1. Go to the **Actions** tab in the GitHub repository
2. Click the failed workflow run
3. Click the failing job to expand the log
4. Look for lines starting with `ERROR` — Hugo usually prints the file name and line number where the problem is
5. Common causes:
   - A YAML front matter field is indented incorrectly (YAML is sensitive to spacing)
   - A required field like `date:` is missing from a new post or publication
   - An image file is referenced in front matter but the file was not uploaded

Fix the problem in the file and commit again — a new build will start automatically.

### Add, remove, or edit a funder

Open `data/funders.yaml`. Each funder is one block:

```yaml
- name: Cancer Foundation Finland
  url: https://syopasaatio.fi/en/homepage/
  logo: cancer-foundation-finland.png
```

- **`name`** — display name shown below the logo
- **`url`** — link when clicking the funder name (use `''` if none)
- **`logo`** — filename of the logo image, must exist in `static/funders/`

To add a funder: upload the logo to `static/funders/` and add a new block at the bottom of the file.
To remove a funder: delete the entire `- name: ...` block for that funder.

---

### Add, remove, or edit a collaborator

Open `data/collaborators.yaml`. Each collaborator is one block:

```yaml
- name: Computational Biology
  group: Nykter Group
  institution: Tampere University
  role: Joint Lynch syndrome cohort
```

- **`name`** — lab or person name shown in bold
- **`group`** — group name shown in burgundy below the name (omit if not applicable)
- **`institution`** — university or organisation
- **`role`** — short description of the collaboration (omit or set to `""` if unknown)

To add a collaborator: add a new `- name:` block at the bottom.
To remove one: delete the entire block.

---

### Add, remove, or edit a research topic

Open `data/research_topics.yaml`. Each topic is one block:

```yaml
- title: Selecting Right Patients at the Right Time
  image: ""
  text: >
    Your topic description here...
```

- **`title`** — heading shown on the card
- **`image`** — filename of an image in `assets/media/` (leave as `""` for placeholder)
- **`text`** — body paragraph; use `>` for multi-line text (keep consistent indentation)

To add an image later: drop the file in `assets/media/` and set `image: your-filename.jpg`.
To add a topic: add a new `- title:` block. To remove: delete the entire block.

---

### Update the featured publications (with results figure)

The Publications page shows three highlighted papers at the top, each with a result figure, abstract, PDF link, and article link. To swap one out for another paper:

**Step 1 — Remove the old featured paper from the spotlight**

Open the old paper's `index.md` (e.g. `content/publication/lastname-year-keyword/index.md`) and change:

```yaml
featured: true
```
to:
```yaml
featured: false
```

Also clear the pdf field if it was set:
```yaml
url_pdf: ''
```

**Step 2 — Prepare the new paper's folder**

The new featured paper needs three files inside its folder (`content/publication/<folder>/`):

| File | What it is |
|---|---|
| `index.md` | Already exists — you will edit it |
| `featured.png` | The main result figure (PNG or JPG, named exactly `featured.png`) |
| `paper.pdf` | The PDF of the paper |

Upload `featured.png` and `paper.pdf` to the publication folder (GitHub: **Add file → Upload files**; local: copy files into the folder).

**Step 3 — Edit the new paper's `index.md`**

Set the following fields:

```yaml
featured: true

url_pdf: 'publication/<folder-name>/paper.pdf'
```

Replace `<folder-name>` with the actual folder name, for example:

```yaml
url_pdf: 'publication/hokkanen-2026-mlh1/paper.pdf'
```

Make sure `abstract:` is filled in — it appears below the figure on the page. If the paper has no formal abstract (e.g. a letter or perspective), write a short 2–3 sentence summary there.

**Step 4 — Commit and push**

Save and push the changes. The site will rebuild automatically within 1–2 minutes.

> **Note:** The Publications page displays **all** papers marked `featured: true`. If you have more than three, all will appear. If you want exactly three, ensure only three papers have `featured: true`.

---

### Update the selected recent publications list

The Publications page shows the five most recent non-featured papers in a citation list below the highlighted section. This list updates **automatically** based on each paper's `date:` field — no manual curation is needed for the normal case.

**To change how many recent papers are shown:**

Open `content/publication/_index.md` and change the `count:` value under the second `block: collection` section:

```yaml
count: 5   # change this number
```

**To exclude a specific paper from this list without deleting it:**

Mark it as featured (`featured: true`) — it will move to the highlighted section instead. Or set it to a draft (`draft: true`) to hide it entirely.

**To control which papers appear (manual curation):**

The list is sorted by `date:` descending. If you want a specific older paper to appear, update its `date:` field to a more recent date. If you want to push a paper down, set its date earlier.

> **Important:** The date field format is `'YYYY-MM-DD'`. Changing a date only affects display order — it does not affect the DOI or citation information.

---

### Write a plain-language summary for a publication

The `abstract:` field in each publication's `index.md` is shown on the Publications page. It should be written in plain language that a general audience can understand — not a copy of the scientific abstract from the journal.

> **Character limit: 750 characters maximum.** The Publications page displays the abstract in a fixed-height text area on highlighted publications. Summaries longer than 750 characters will be cut off. Aim for 3–4 concise sentences that fit within this limit.

#### Option 1 — Using Claude Code (if you have access)

Run the following slash command in the Claude Code terminal from the project root:

```
/summarize-publication <folder-name>
```

Example:
```
/summarize-publication hokkanen-2026-mlh1
```

Claude will read the publication, generate a 3–4 sentence plain-language summary within the 750-character limit, and update the `abstract:` field automatically. Review the before/after shown in the output before committing.

#### Option 2 — Using any AI tool (ChatGPT, Copilot, etc.)

1. Open the publication's `index.md` (e.g. `content/publication/hokkanen-2026-mlh1/index.md`)
2. Copy the entire contents of the `index.md` file
3. Paste the following prompt into your AI tool of choice, followed by the file contents:

---

> **Prompt to copy:**
>
> I need a plain-language summary of a scientific paper for a general public audience with no scientific background. Write 3–4 sentences. Use simple language — if a technical term is unavoidable, explain it in plain words. State what the research investigated, what was found, and why it matters for patients or society. Do not use bullet points. Do not start with "This study" or "This paper". Keep the summary under 750 characters total. Use all information in the file below to inform the summary.
>
> [PASTE THE FULL CONTENTS OF index.md HERE]

---

4. Copy the AI output
5. Open the publication's `index.md` and replace the `abstract:` value with the new text, keeping the single quotes:
   ```yaml
   abstract: 'Your new plain-language summary goes here.'
   ```
6. Save and commit

---

## Quick reference for common tasks

| Task | Recommended method | File to edit |
|---|---|---|
| Update a team member's bio | Either | `content/authors/<name>/_index.md` |
| Add a new team member | Local (easier for photos) | Copy `content/authors/pi-template/`, rename, edit |
| Mark a team member as alumni | Either | `content/authors/<name>/_index.md` — update `role:` and `user_groups:` |
| Add a news post | Either | Copy `content/post/example-news/`, rename, edit |
| Add a publication | Either | Copy `content/publication/example-paper/`, rename, edit |
| Hide a post or publication | Either | Set `draft: true` in the content file |
| Update research topic text or image | Either | `data/research_topics.yaml` |
| Add or remove a research topic | Either | `data/research_topics.yaml` — add or delete a `- title:` block |
| Add or remove a funder | Either | `data/funders.yaml` |
| Add or remove a collaborator | Either | `data/collaborators.yaml` |
| Change navigation order | Either | `config/_default/menus.yaml` — adjust `weight:` values |
| Update contact info | Either | `config/_default/params.yaml` |
| Add a PDF download | Either | Place file in `static/`, link in content |
| Swap a featured publication | Local preferred | Set `featured: true/false`, add `featured.png` + `paper.pdf`, set `url_pdf` |
| Change number of recent publications shown | Either | `content/publication/_index.md` — update `count:` |
| Change colour scheme | Either | `config/_default/params.yaml` — update `theme_day:` |
| Replace site logo or favicon | Local preferred | Replace files in `assets/media/` |
| Set up a custom domain | Local preferred | Add `static/CNAME`, update `baseURL` in `hugo.yaml` |
