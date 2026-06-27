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
- Thoughts data: `src/data/notes.ts` and `src/data/life.ts` are combined by `src/data/thoughts.ts`
- Profile links: `src/data/profile.ts`
- Shared layout/nav: `src/layouts/BaseLayout.astro`
- Assets: `public/assets/`
- Global styles: `public/styles.css`

## Add a publication

Add one object to `src/data/publications.ts`:

```ts
{
  y: '2026',
  t: 'Title',
  a: 'Hyungwoo Song, ...',
  v: "CHI ’26",
  theme: 'Accessibility',
  url: 'https://doi.org/...',
  sel: false,
  n: 'Short note.',
  kind: 'Full Paper',
  award: 'Best Paper Honorable Mention', // optional
  image: '/assets/publications/example.webp' // optional
}
```

Set `sel: true` to show it on the homepage selected-work list.

Publication image files go in `public/assets/publications/`. If `award` is present, the publication card shows a star award badge. Use `kind` to distinguish `Full Paper`, `Extended Abstract`, `Demo / Adjunct`, `Companion Paper`, etc.

## Add a thought

Add research-adjacent notes to `src/data/notes.ts` or personal/free-form notes to `src/data/life.ts`. Both are merged automatically by `src/data/thoughts.ts` and generated at:

- English: `/thoughts/<slug>/`
- Korean: `/ko/thoughts/<slug>/`

The old `/field-notes/` and `/life/` paths point users toward Thoughts.

Put images under `public/assets/` and reference them as `/assets/file-name.jpg`.
