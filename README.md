# Hyungwoo Song Astro Website

Bilingual Astro version of the personal researcher website.

## Run

```bash
export PATH=/Users/bro_wma1/.local/nodejs/node-v22.23.0-darwin-arm64/bin:$PATH
cd /Users/bro_wma1/personal-website-astro
npm run dev -- --host 0.0.0.0 --port 4321
```

- English: `http://127.0.0.1:4321/`
- Korean: `http://127.0.0.1:4321/ko/`

## Manage content

- Publications: `src/data/publications.ts`
- Field notes: `src/data/notes.ts`
- Life posts: `src/data/life.ts`
- Profile links: `src/data/profile.ts`
- Shared layout/nav: `src/layouts/BaseLayout.astro`
- Assets: `public/assets/`
- Global styles: `public/styles.css`

## Add a publication

Add one object to `src/data/publications.ts`:

```ts
{ y: '2026', t: 'Title', a: 'Hyungwoo Song, ...', v: "CHI ’26", theme: 'Accessibility', url: 'https://doi.org/...', sel: false, n: 'Short note.' }
```

Set `sel: true` to show it on the homepage selected-work list.

## Add a field note

Add one object to `src/data/notes.ts`. The dynamic pages are generated automatically at:

- English: `/field-notes/<slug>/`
- Korean: `/ko/field-notes/<slug>/`

Put images under `public/assets/` and reference them as `/assets/file-name.jpg`.
