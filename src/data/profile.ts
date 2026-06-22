export const profile = {
  name: 'Hyungwoo Song',
  affiliation: 'Seoul National University',
  email: 'rotto95@snu.ac.kr',
  scholar: 'https://scholar.google.com/citations?user=g7s2hrAAAAAJ',
  orcid: 'https://orcid.org/0009-0008-6649-9453',
  linkedin: 'https://www.linkedin.com/in/hyungwoosong',
  github: 'https://github.com/bobbyhwsong',
  cv: '/assets/Hyungwoo_Song_CV.pdf',
  portrait: '/assets/hyungwoo-song-portrait.jpg'
};

export const ui = {
  en: {
    nav: { research: 'Research', publications: 'Publications', notes: 'Field Notes', life: 'Life', about: 'About', cv: 'CV', otherLang: '한국어' },
    langPrefix: '',
    otherLangHref: '/ko/'
  },
  ko: {
    nav: { research: '연구', publications: '논문', notes: '필드노트', life: '삶', about: '소개', cv: 'CV', otherLang: 'English' },
    langPrefix: '/ko',
    otherLangHref: '/'
  }
} as const;

export type Lang = keyof typeof ui;
