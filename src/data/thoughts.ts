import { notes, type Note } from './notes';
import { lifePosts, type LifePost } from './life';

export type Thought = (Note | LifePost) & {
  source: 'field-note' | 'life';
  kind: { en: string; ko: string };
};

export const thoughts: Thought[] = [
  ...notes.map((note) => ({ ...note, source: 'field-note' as const, kind: { en: 'Research note', ko: '연구 노트' } })),
  ...lifePosts.map((post) => ({ ...post, source: 'life' as const, kind: { en: 'Personal note', ko: '개인 노트' } }))
].sort((a, b) => b.date.localeCompare(a.date));
