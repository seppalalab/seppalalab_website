# seppalalab GitHub Organization — Management Guide

This guide is for the organization owner (tseppalalab@gmail.com). It covers day-to-day management of members and repository permissions.

---

## Organization roles

| Role | What they can do |
|---|---|
| **Owner** | Full control: add/remove members, change settings, delete repos |
| **Member** | Access repos they are added to; cannot create repos by default |

Keep the number of Owners minimal (1–2 people). All lab members are Members.

---

## Adding a member

1. Go to [github.com/seppalalab](https://github.com/seppalalab)
2. Click **People** tab → **Invite member**
3. Enter their GitHub username or email → **Send invitation**
4. They must accept the email invitation before access is granted

---

## Removing a member

When someone leaves the lab:

1. **People** tab → find the person → click the three dots (⋯) → **Remove from organization**
2. They immediately lose access to all private repositories
3. Their contributions (commits, issues) remain in the repositories

---

## Repository permission levels

When adding someone as a collaborator on a specific repository, choose the appropriate level:

| Level | Use case |
|---|---|
| **Read** | Can view and clone — for external collaborators or read-only access |
| **Write** | Can push changes — standard for active contributors |
| **Maintain** | Can manage issues, PRs, and releases — for repo leads |
| **Admin** | Full repo control — only for owners or trusted senior members |

### Adding a collaborator to a repository

1. Go to the repository → **Settings** → **Collaborators and teams**
2. Click **Add people** → enter GitHub username → select permission level → **Add**

---

## Default member permissions (org-wide setting)

Controls what members can do across the entire organization:

1. Go to [github.com/organizations/seppalalab/settings/member_privileges](https://github.com/organizations/tseppalalab/settings/member_privileges)
2. Recommended settings for a small research lab:

| Setting | Recommended value |
|---|---|
| Base permissions | **Read** (members see public repos; Write is granted per repo) |
| Repository creation | **Disabled** (Emmi creates repos, avoids accidental public repos) |
| Repository forking | **Enabled** |

---

## Creating a new repository

1. Go to [github.com/seppalalab](https://github.com/seppalalab) → **New repository**
2. Name: use `lastname-year-keyword` for research repos (e.g. `hokkanen-2026-mlh1-code`)
3. Visibility: **Public** for research outputs, **Private** for work-in-progress
4. Check **Add a README file**
5. After creation, go to **Settings → Collaborators** and add the relevant lab member with **Write** access

---

## Quick reference

| Task | Where |
|---|---|
| Invite member | github.com/seppalalab → People → Invite member |
| Remove member | github.com/seppalalab → People → ⋯ → Remove |
| Add collaborator to repo | Repo → Settings → Collaborators and teams |
| Change org-wide permissions | github.com/organizations/seppalalab/settings/member_privileges |
| Transfer repo ownership | Repo → Settings → Danger Zone → Transfer ownership |

---

## When a lab member leaves

1. Remove from organization (People tab)
2. Check if they are listed as a maintainer on any Zenodo deposits — update the contact person if needed
3. Update their profile on the lab website (`content/authors/<name>/_index.md`) — change role to Alumni or remove

---

## Questions / issues

Contact GitHub support at [support.github.com](https://support.github.com) or check the GitHub Organizations documentation at [docs.github.com/organizations](https://docs.github.com/en/organizations).
