# Deployment Guide

Recommended first deployment: **Vercel**.

This Astro site is static. Build command and output directory:

- Framework: Astro
- Install command: `npm install`
- Build command: `npm run build`
- Output directory: `dist`
- Node.js: `22.x` or any version satisfying `>=22.12.0`

## Current local project

```bash
cd /Users/bro_wma1/personal-website-astro
npm run build
```

## Option A — Vercel, recommended

1. Create a GitHub repository, for example `hyungwoo-song-website`.
2. Push this folder to the repository.
3. Go to <https://vercel.com/new>.
4. Import the GitHub repository.
5. Vercel should auto-detect Astro. If it asks:
   - Build command: `npm run build`
   - Output directory: `dist`
6. Deploy.
7. After deploy, add custom domain later:
   - `hyungwoosong.com`
   - Optional: `www.hyungwoosong.com`

## Option B — Netlify

1. Push to GitHub.
2. Go to <https://app.netlify.com/start>.
3. Import the repository.
4. Set:
   - Build command: `npm run build`
   - Publish directory: `dist`
5. Deploy.

## Option C — GitHub Pages

Possible, but less convenient for this project because it needs GitHub Actions setup and custom-domain handling. Use Vercel/Netlify first unless there is a strong reason to keep hosting on GitHub Pages.

## Local Git setup

If the folder is not a git repository yet:

```bash
cd /Users/bro_wma1/personal-website-astro
git init
git add .
git commit -m "Initial Astro personal website"
```

Then create a GitHub repo and push:

```bash
git branch -M main
git remote add origin git@github.com:<GITHUB_USERNAME>/hyungwoo-song-website.git
git push -u origin main
```

If using HTTPS instead of SSH:

```bash
git remote add origin https://github.com/<GITHUB_USERNAME>/hyungwoo-song-website.git
```

## Domain later

When the domain is purchased, connect it in Vercel/Netlify first. The platform will show DNS records. Usually:

- Apex domain `hyungwoosong.com`: `A` record or platform-specific record
- `www.hyungwoosong.com`: `CNAME` record

Do not edit DNS until the deployment platform gives exact records.
