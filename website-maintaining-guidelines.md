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
| `content/research/_index.md`     | Research page text and topics                   |
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
git clone https://github.com/<github-username>/<repository-name>.git
cd <repository-name>
```

Replace `<github-username>` and `<repository-name>` with the actual values.

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

| File type | Example | Resulting URL |
|---|---|---|
| Downloadable PDFs | `static/papers/smith2024.pdf` | `yoursite.com/papers/smith2024.pdf` |
| Custom domain config | `static/CNAME` | Used by GitHub Pages, not visible to visitors |
| Downloadable data files | `static/data/dataset.csv` | `yoursite.com/data/dataset.csv` |
| Custom `robots.txt` | `static/robots.txt` | `yoursite.com/robots.txt` |

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
1. Open `content/authors/<name>/_index.md`
2. Change their `role:` field to `Alumni` (or `Former PhD Student`, etc.)
3. In `content/people/index.md`, check whether your people page has a separate alumni group — if so, update the `user_groups:` line in their profile to match

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

### Change the site's colour scheme

The colour theme is controlled in two places:

1. **Switch to a built-in theme:** Open `config/_default/params.yaml`, find the `appearance:` section, and change `theme_day:` and `theme_night:` to any of the built-in HugoBlox theme names (e.g. `ocean`, `forest`, `rose`, `minimal`).

2. **Create a custom theme:** Add a new YAML file in `data/themes/` (e.g. `data/themes/seppala.yaml`) following the format of the existing file there. Then set `theme_day: seppala` in `params.yaml`.

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

## Quick reference for common tasks

| Task | Recommended method | File to edit |
|---|---|---|
| Update a team member's bio | Either | `content/authors/<name>/_index.md` |
| Add a new team member | Local (easier for photos) | Copy `content/authors/pi-template/`, rename, edit |
| Mark a team member as alumni | Either | `content/authors/<name>/_index.md` — update `role:` and `user_groups:` |
| Add a news post | Either | Copy `content/post/example-news/`, rename, edit |
| Add a publication | Either | Copy `content/publication/example-paper/`, rename, edit |
| Hide a post or publication | Either | Set `draft: true` in the content file |
| Update research text | Either | `content/research/_index.md` |
| Change navigation order | Either | `config/_default/menus.yaml` — adjust `weight:` values |
| Update contact info | Either | `config/_default/params.yaml` |
| Add a PDF download | Either | Place file in `static/`, link in content |
| Change colour scheme | Either | `config/_default/params.yaml` — update `theme_day:` |
| Replace site logo or favicon | Local preferred | Replace files in `assets/media/` |
| Set up a custom domain | Local preferred | Add `static/CNAME`, update `baseURL` in `hugo.yaml` |
