export type Note = {
  slug: string;
  date: string;
  image?: string;
  tags: string[];
  title: { en: string; ko: string };
  excerpt: { en: string; ko: string };
  body: { en: string[]; ko: string[] };
  quote?: { en: string; ko: string };
};

export const notes: Note[] = [
  {
    slug: 'relational-equality-and-ai',
    date: '2026-06-22',
    tags: ['AI', 'relational equality', 'voice'],
    title: { en: 'AI and relational equality', ko: 'AI와 관계적 평등' },
    excerpt: {
      en: 'The question is not only whether AI gives everyone the same tool, but whether it changes who has to adjust to whom.',
      ko: 'AI가 모두에게 같은 도구를 주는지가 아니라, 누가 누구에게 맞춰야 하는지를 바꾸는지가 더 중요할 수 있습니다.'
    },
    body: {
      en: [
        'I keep thinking that equality in AI is often discussed as access: who can use the tool, who gets a better model, who receives support. That matters. But relational equality asks a slightly different question. It asks whether people stand before one another as equals, or whether one side must keep translating themselves to be accepted.',
        'This feels especially important when AI helps people write, speak, complain, apologize, or present themselves. A writing assistant can make a person sound more professional. But it can also teach that their original anger, hesitation, accent, or uncertainty must be cleaned up before it can count as a legitimate voice.',
        'So the design question is not simply how to give people better expression. It is how to make AI support people without making adaptation one-sided. The goal is not to make everyone sound like the institution already wants them to sound. It is to help more kinds of voices arrive without having to disappear first.'
      ],
      ko: [
        'AI에서 평등을 말할 때 우리는 자주 접근성을 떠올립니다. 누가 도구를 쓸 수 있는지, 누가 더 좋은 모델을 갖는지, 누가 지원을 받는지. 물론 중요합니다. 그런데 관계적 평등은 조금 다른 질문을 던집니다. 사람들이 서로를 동등한 사람으로 마주하는가, 아니면 한쪽이 계속 자신을 번역하고 조정해야만 받아들여지는가.',
        '이 질문은 AI가 글쓰기, 말하기, 항의, 사과, 자기소개를 도울 때 특히 중요해집니다. 글쓰기 AI는 어떤 사람의 말을 더 전문적으로 들리게 해줄 수 있습니다. 하지만 동시에 그 사람의 분노, 망설임, 억양, 불확실성이 정당한 목소리로 인정받기 전에 먼저 정리되고 제거되어야 한다고 가르칠 수도 있습니다.',
        '그래서 제가 붙잡고 싶은 디자인 질문은 단순히 “표현을 더 잘하게 돕는 AI”가 아닙니다. AI가 사람을 돕되, 적응의 부담을 한쪽에게만 지우지 않게 하는 것입니다. 모두가 제도가 이미 듣기 좋아하는 말투로 변하는 것이 목표가 아니라, 더 다양한 목소리가 사라지지 않고 도착할 수 있게 하는 것이 목표여야 합니다.'
      ]
    },
    quote: {
      en: 'Relational equality asks whether support lets a voice arrive, or merely makes it acceptable after translation.',
      ko: '관계적 평등은 지원이 목소리를 도착하게 하는지, 아니면 번역된 뒤에야 받아들여지게 하는지를 묻습니다.'
    }
  },
  {
    slug: 'bourdieu-and-the-cost-of-sounding-natural',
    date: '2026-06-22',
    tags: ['Bourdieu', 'language', 'power'],
    title: { en: 'Bourdieu and the cost of sounding natural', ko: '부르디외와 자연스럽게 들리는 것의 비용' },
    excerpt: {
      en: 'Some voices sound natural because the field has already been built around them.',
      ko: '어떤 목소리가 자연스럽게 들리는 이유는, 이미 그 목소리에 맞춰 장이 구성되어 있기 때문일 수 있습니다.'
    },
    body: {
      en: [
        'Bourdieu is useful because he makes “naturalness” suspicious. In many settings, the voice that sounds calm, rational, concise, and professional is treated as if it simply communicates better. But that voice is not outside power. It has a history, a training process, and a field that rewards it.',
        'This matters for AI writing tools. When an LLM makes a complaint more polished, it is not only improving style. It may be converting a situated, risky, emotional utterance into the linguistic currency that an organization recognizes. The conversion can be useful. It can protect the speaker. But it also reveals the price of being heard.',
        'The question I want to keep open is this: when AI helps someone acquire legitimate language, does it redistribute linguistic capital, or does it quietly confirm that only capitalized language deserves uptake? Probably both. That tension is where the design problem begins.'
      ],
      ko: [
        '부르디외가 좋은 이유는 “자연스러움”을 의심하게 만들기 때문입니다. 어떤 장면에서 차분하고, 합리적이고, 간결하고, 전문적인 목소리는 그냥 더 잘 전달되는 말처럼 취급됩니다. 하지만 그 목소리는 권력 바깥에 있지 않습니다. 그것은 훈련의 결과이고, 특정한 장이 보상하는 언어 자본입니다.',
        '이 지점은 AI 글쓰기 도구를 볼 때 중요해집니다. LLM이 항의문을 더 매끄럽게 다듬을 때, 그것은 단지 문체를 개선하는 것이 아닐 수 있습니다. 위험하고 감정적이며 위치 지어진 발화를 조직이 알아들을 수 있는 언어 화폐로 바꾸는 일일 수 있습니다. 이 변환은 유용합니다. 말하는 사람을 보호할 수도 있습니다. 하지만 동시에 들리기 위해 치러야 하는 비용을 드러냅니다.',
        '제가 열어두고 싶은 질문은 이것입니다. AI가 누군가에게 정당한 언어를 획득하게 도울 때, 그것은 언어 자본을 재분배하는 것일까요? 아니면 자본화된 언어만이 응답받을 자격이 있다는 사실을 조용히 확인하는 것일까요? 아마 둘 다일 것입니다. 디자인의 문제는 바로 그 긴장에서 시작됩니다.'
      ]
    },
    quote: {
      en: 'AI may lend people legitimate language. But we should still ask why legitimacy had a price in the first place.',
      ko: 'AI는 사람에게 정당한 언어를 빌려줄 수 있습니다. 하지만 우리는 여전히 왜 정당성이 애초에 비용을 요구했는지 물어야 합니다.'
    }
  },
  {
    slug: 'what-counts-as-help',
    date: '2026-06-22',
    image: '/assets/field-note-example.svg',
    tags: ['AI', 'agency', 'design'],
    title: { en: 'What counts as “help”?', ko: '도움은 무엇인가?' },
    excerpt: {
      en: 'When a system summarizes, suggests, or acts, the boundary between scaffolding and substitution becomes a design question.',
      ko: '시스템이 요약하고 제안하고 행동할 때, 발판과 대체 사이의 경계가 디자인 문제가 됩니다.'
    },
    body: {
      en: [
        'I keep returning to the same uneasiness: when a system becomes very good at helping, it also becomes very good at deciding what help should mean.',
        'In many AI systems, help is measured by friction removed: fewer clicks, shorter summaries, faster decisions, less effort. That is not wrong. But it is incomplete. Some friction is just waste. Other friction is where interpretation, ownership, and care happen.',
        'So the question I want to keep open is not simply whether AI helps. It is: what kind of person does this help assume, and what kind of participation does it leave open?'
      ],
      ko: [
        '시스템이 아주 잘 도와주기 시작할 때, 그 시스템은 동시에 “도움”이 무엇인지 결정하기 시작합니다.',
        '많은 AI 시스템에서 도움은 마찰을 줄이는 것으로 측정됩니다. 클릭을 줄이고, 요약을 제공하고, 더 빠르게 결정하게 하는 것. 물론 그런 도움은 필요합니다. 하지만 모든 마찰이 나쁜 것은 아닙니다. 어떤 마찰은 낭비이지만, 어떤 마찰은 해석과 소유감과 돌봄이 생기는 자리입니다.',
        '그래서 제가 붙잡고 싶은 질문은 단순히 “AI가 도움이 되는가?”가 아닙니다. 이 도움은 어떤 사람을 상정하고, 어떤 참여 가능성을 남겨두는가? 입니다.'
      ]
    },
    quote: {
      en: 'Maybe good AI support is not the kind that disappears. Maybe it is the kind that leaves people more present after using it.',
      ko: '좋은 AI 지원은 사라지는 지원이 아니라, 사용 후 사람이 더 자기 자리에 남아 있게 만드는 지원일지도 모릅니다.'
    }
  },
  {
    slug: 'interfaces-have-manners',
    date: '2026-06-22',
    tags: ['interfaces', 'observation'],
    title: { en: 'Interfaces have manners.', ko: '인터페이스에는 태도가 있다.' },
    excerpt: {
      en: 'Every button, delay, and prompt tells people what kind of participation is expected of them.',
      ko: '버튼, 지연, 프롬프트는 모두 사용자에게 어떤 참여를 기대하는지 말합니다.'
    },
    body: {
      en: [
        'Every interface teaches a small etiquette: what can be asked, how fast to respond, when to trust, and when to stay silent.',
        'I want Field Notes to be a place for this kind of observation — not yet a paper, not necessarily polished, but worth keeping.'
      ],
      ko: [
        '모든 인터페이스는 작은 예절을 가르칩니다. 무엇을 물어볼 수 있는지, 얼마나 빨리 반응해야 하는지, 언제 믿고 언제 멈춰야 하는지.',
        '필드노트는 이런 관찰을 남기는 공간이면 좋겠습니다. 아직 논문은 아니고, 꼭 정리된 주장도 아니지만, 계속 들고 있고 싶은 생각들입니다.'
      ]
    }
  }
];
