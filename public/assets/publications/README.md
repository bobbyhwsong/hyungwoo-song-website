# Publication images

Put representative paper images in this folder, then reference them from `src/data/publications.ts`.

Recommended format:

- 16:9 or 4:3 image
- `.webp`, `.jpg`, or `.png`
- Around 1200px wide is enough
- Use lowercase filenames, for example:
  - `medibridge.webp`
  - `emobridge.webp`
  - `sigir-shopping-agent.webp`

Example publication entry:

```ts
{
  y: '2026',
  t: 'Paper title',
  a: 'Hyungwoo Song, ...',
  v: "CHI ’26",
  theme: 'Healthcare',
  url: 'https://doi.org/...',
  sel: true,
  n: 'Short note.',
  kind: 'Full Paper',
  award: 'Best Paper Honorable Mention',
  image: '/assets/publications/medibridge.webp'
}
```

Fields:

- `kind`: publication type, e.g. `Full Paper`, `Extended Abstract`, `Demo / Adjunct`, `Companion Paper`.
- `award`: optional award text. If present, the site shows a black/star award badge.
- `image`: optional representative image path. If absent, the publication renders as a clean text row.
