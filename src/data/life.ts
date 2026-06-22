export type LifePost = {
  slug: string;
  date: string;
  image?: string;
  tags: string[];
  title: { en: string; ko: string };
  excerpt: { en: string; ko: string };
  body: { en: string[]; ko: string[] };
  quote?: { en: string; ko: string };
};

export const lifePosts: LifePost[] = [
  {
    slug: 'nirvana-the-band-and-the-pleasure-of-trying',
    date: '2026-06-22',
    tags: ['film', 'comedy', 'trying'],
    title: { en: 'Nirvanna the Band and the pleasure of trying', ko: '너바나 더밴드와 애쓰는 사람들의 우스움' },
    excerpt: {
      en: 'What stayed with me was not success, but the strange dignity of people who keep making a plan anyway.',
      ko: '남은 건 성공이 아니라, 그래도 계속 계획을 세우는 사람들의 이상한 품위였습니다.'
    },
    body: {
      en: [
        'What I liked about Nirvanna the Band was the texture of trying. The characters are ridiculous, but not because they want too much. They are ridiculous because they keep turning wanting into a plan, and a plan into another failure, and failure into the next performance.',
        'That rhythm feels close to research, or maybe to being young in general. You prepare a stage that may not open. You rehearse a story that may not land. Still, the attempt itself leaves a trace. It makes a life slightly more authored than it would have been otherwise.',
        'I think I am drawn to works that do not mock failure from far away. They stay close enough to show that foolishness and sincerity often share the same body.'
      ],
      ko: [
        '최근에 본 「너바나 더밴드」에서 좋았던 건 “애씀”의 질감이었습니다. 인물들은 우스운데, 그 우스움은 너무 큰 욕망 때문이라기보다 욕망을 계속 계획으로 만들고, 계획을 실패로 만들고, 실패를 다시 다음 공연으로 바꾸기 때문에 생깁니다.',
        '그 리듬이 연구와도 조금 닮아 있다고 느꼈습니다. 혹은 그냥 젊다는 것과 닮아 있을지도 모르겠습니다. 열리지 않을 수도 있는 무대를 준비하고, 통하지 않을 수도 있는 이야기를 연습합니다. 그래도 시도는 흔적을 남깁니다. 삶을 조금은 더 자기 것으로 만듭니다.',
        '저는 실패를 멀리서 비웃지 않는 작품에 끌리는 것 같습니다. 충분히 가까이 붙어서, 우스움과 진심이 사실은 같은 몸에 들어 있다는 걸 보여주는 작품들 말입니다.'
      ]
    },
    quote: {
      en: 'Trying can be comic, but it is also one of the few ways a life becomes authored.',
      ko: '애쓰는 일은 우스울 수 있지만, 삶이 자기 것이 되는 몇 안 되는 방식이기도 합니다.'
    }
  },
  {
    slug: 'han-byung-chul-and-the-crisis-of-narrative',
    date: '2026-06-22',
    tags: ['Byung-Chul Han', 'narrative', 'attention'],
    title: { en: 'Reading The Crisis of Narration', ko: '한병철, 『서사의 위기』를 읽으며' },
    excerpt: {
      en: 'A life without narrative does not lack events; it lacks the slow work of binding them together.',
      ko: '서사가 없는 삶은 사건이 부족한 삶이 아니라, 사건을 묶어내는 느린 작업이 부족한 삶일 수 있습니다.'
    },
    body: {
      en: [
        'What I take from Han Byung-Chul’s The Crisis of Narration is not simply nostalgia for stories. It is a warning about a life made only of updates. There can be many events, many records, many posts, and still no narrative strong enough to hold them together.',
        'This matters to me because research also risks becoming an update machine: papers, deadlines, prototypes, outputs. Field Notes are partly a small resistance to that. They are a way to ask what thread connects the fragments, not just how many fragments have accumulated.',
        'Narrative is not decoration after life happens. It is one of the ways a person becomes able to stay with what happened.'
      ],
      ko: [
        '한병철의 『서사의 위기』에서 제가 가져가고 싶은 것은 단순히 “이야기가 좋다”는 nostalgia는 아닙니다. 오히려 업데이트만 남은 삶에 대한 경고에 가깝습니다. 사건은 많고, 기록도 많고, 게시물도 많은데, 그것들을 붙잡아줄 만큼 느린 서사는 없는 상태 말입니다.',
        '이 말이 연구하는 삶에도 꽤 닿아 있다고 느꼈습니다. 연구도 자칫하면 업데이트 기계가 됩니다. 논문, 마감, 프로토타입, 산출물. 필드노트를 만들고 싶은 이유도 조금은 여기에 있습니다. 조각이 얼마나 쌓였는지가 아니라, 그 조각들을 어떤 실로 묶을 수 있는지를 묻고 싶기 때문입니다.',
        '서사는 삶이 끝난 뒤 붙는 장식이 아닙니다. 어떤 일이 나에게 일어났는지 오래 붙들 수 있게 해주는 형식입니다.'
      ]
    },
    quote: {
      en: 'Narrative is not decoration after life; it is a way of remaining with experience.',
      ko: '서사는 삶 이후의 장식이 아니라, 경험 곁에 머무는 방식입니다.'
    }
  }
];
