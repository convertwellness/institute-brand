/**
 * Every string on the site that is not page body copy.
 *
 * Voice rules, from the brand specification:
 *   Lead with the question, then the mechanism.
 *   Treat the system as real and describable.
 *   Reverence without incense — awe from scale and precision, not mystery.
 *   Every term is one of Michael's own. Never vibration, frequency, or quantum.
 *   Never: countdown timers, seat scarcity, before-and-after testimonials.
 *
 * Capitalisation is a rule, not a style. Capital: Concept, Pattern, Concept
 * Family, Concept Weave, Pattern Weave, School, Foundation Course, Human
 * Operating System. Lowercase when used ordinarily — a pattern in a carpet is
 * not a Pattern.
 */

export const BRAND = {
  /** Never shortened, never an acronym. Always three lines, broken exactly here. */
  fullName: ["The Institute of", "The Spiritual Science", "of Human Patterns"],
  shortName: "The Institute",
  promise: "There is a structure underneath, and it can be seen.",
  /** Michael's own reassurance line. Use it wherever a visitor might feel behind. */
  reassurance: "You do not have to understand everything before you begin.",
} as const;

export const HOME = {
  hero: {
    eyebrow: "The Institute of The Spiritual Science of Human Patterns",
    heading: "There is a structure underneath, and it can be seen.",
    body: "The Institute studies the Concepts and Patterns that shape how we think, choose, relate and respond — and teaches you to recognise them operating in your own life.",
    primaryCta: { label: "Start the free course", href: "/courses/five-laws" },
    secondaryCta: { label: "See the system", href: "/human-operating-system" },
    footnote: "You do not have to understand everything before you begin.",
  },

  operatingSystem: {
    eyebrow: "The Human Operating System",
    heading: "Why can we consciously want one thing and repeatedly create something different?",
    /** His other two opening questions — rotate or stack them */
    alternateHeadings: [
      "Why do we become who we become?",
      "Why do certain experiences continue to repeat?",
    ],
    body: "Institute teachings examine the relationship between what we hold as true and what our lives keep producing. Not as a metaphor — as a sequence that can be drawn, followed, and interrupted.",
    aside: "Learn to recognise what is operating beneath the visible circumstances of your life, and change the internal cause rather than the external result.",
    chain: ["Concept", "Belief", "Pattern", "Emotion", "Behavior", "Life Result"],
    chainCaption: "Always this order, always with arrows",
    cta: { label: "Explore the Human Operating System", href: "/human-operating-system" },
  },

  begin: {
    heading: "Begin where you are",
    body: "Some students begin with the free course. Others enter through a Concept they already recognise.",
  },

  path: {
    eyebrow: "How the education fits together",
    steps: [
      { tier: "Free introduction", detail: "The Five Laws of Manifestation" },
      { tier: "Recognition", detail: "Foundation Course — thirty Patterns of Behavior" },
      { tier: "Focused study", detail: "Concepts, Families, Weaves" },
      { tier: "Deeper understanding", detail: "Extended Foundation, the Human Operating System" },
      { tier: "Comprehensive education", detail: "The Schools of the Institute" },
    ],
    note: "The Foundation Course opens everything that follows. Every study stays readable and purchasable before then — the sequence governs when you begin, not what you can see.",
  },

  explore: {
    heading: "Explore the Institute",
    body: "Start where you are, explore what speaks to you, and allow your understanding to deepen as you continue.",
  },

  readingSurface: {
    eyebrow: "Inside a Concept Study",
    heading: "The cosmos is the frame. The page is where the work happens.",
    body: "Students sit with a Course for a long time. The shell stays dark and the reading moves onto a page laid under it.",
  },

  schools: {
    heading: "The Schools of the Institute",
    body: "The most comprehensive areas of continuing education. Each School holds multiple Courses devoted to one area of human understanding.",
  },

  membership: {
    eyebrow: "Membership",
    heading: "You are not being asked to believe anything.",
    body: "You are being asked to look at what is already operating, and to decide for yourself whether you recognise it. Members receive preferred pricing on qualifying Courses, books and materials.",
    primaryCta: { label: "Become a member", href: "/membership" },
    secondaryCta: { label: "Start free", href: "/courses/five-laws" },
  },
} as const;

/* ── Courses ─────────────────────────────────────────────────── */

export const COURSES = [
  {
    slug: "five-laws",
    title: "The Five Laws of Manifestation",
    kicker: "Free",
    summary:
      "An introduction to several of the fundamental principles upon which the Institute's teachings are built.",
    body: "This course provides an opportunity to experience the Institute's approach before deciding whether to continue into more extensive study.",
    cta: "Start the free course",
    gated: false,
    includes: [] as string[],
    needsMichael: "Final course title, and the title of each of the Five Laws.",
  },
  {
    slug: "foundation",
    title: "Foundation — Introduction to Human Patterns",
    kicker: "Ten weeks · thirty Patterns",
    summary:
      "The Foundation Course is a ten-week journey of recognition and personal discovery. Each week introduces three Patterns of Behavior that may influence how we think, choose, relate, and respond to life.",
    body: "The purpose is not to judge or label, but to develop awareness of the patterns operating beneath familiar reactions. Through presentations, reflection, and personal recognition exercises, students explore thirty Patterns of Behavior and begin making more conscious choices. The Foundation Course prepares students for the deeper Concept and Pattern Studies that follow.",
    cta: "Explore the Foundation Course",
    gated: false,
    includes: [
      "Ten weeks of study",
      "Thirty Patterns of Behavior",
      "Three Pattern presentations each week",
      "Weekly reflection",
      "Pattern-recognition exercises",
      "Supporting workbook and materials",
    ],
  },
  {
    slug: "extended-foundation",
    title: "Extended Foundation — Depth Two",
    kicker: "Opens after the Foundation",
    summary:
      "For students ready to move beyond introductory recognition, Depth Two provides a more comprehensive examination of the principles introduced in the Foundation Course.",
    body: "Students move from simply recognising Patterns toward understanding more deeply what creates them, why they continue, and how conscious change becomes possible.",
    cta: "Continue to Depth Two",
    gated: true,
    includes: [] as string[],
    needsMichael: "Complete curriculum description, from existing Institute material.",
  },
  {
    slug: "awakening-of-consciousness",
    title: "Awakening of Consciousness",
    kicker: "Opens after the Foundation",
    summary: "",
    body: "",
    cta: "Explore the Course",
    gated: true,
    includes: [] as string[],
    needsMichael: "Everything. Named on his sketch; no description exists yet.",
  },
  {
    slug: "tj",
    title: "T.J.",
    kicker: "",
    summary: "",
    body: "",
    cta: "Explore the Course",
    gated: true,
    includes: [] as string[],
    needsMichael: "Everything, including what T.J. stands for. It appears in both the Courses row and the Books row of his sketch.",
  },
] as const;

/** Every Course ships in two editions. His sketch brackets both across the row. */
export const COURSE_FORMATS = ["Audio edition", "Video edition"] as const;

/* ── Concepts ────────────────────────────────────────────────── */

export const CONCEPTS = {
  heading: "Concept Studies",
  lead: "Everything begins with Concept.",
  body: "Concept Studies allow students to explore the individual Concepts that influence beliefs, expectations, patterns, choices, and life experiences. Students may select the Concepts most relevant to their present lives rather than following a predetermined sequence.",
  counts: [
    { n: 24, label: "Individual Concepts" },
    { n: 12, label: "Concept Weaves" },
    { n: 8, label: "Concept Families" },
  ],
  /** Michael's own examples. The launch twenty-four are not yet chosen. */
  examples: [
    "Acceptance", "Approval", "Rejection", "Unworthiness", "Abandonment", "Fear",
    "Control", "Guilt", "Success and Failure", "Victimhood", "Validation", "Worth",
  ],
  needsMichael: "Which twenty-four of the roughly fifty ship first. Longest lead item on the list.",

  /** Section order for every Concept page. One to six are his own headings. */
  pageSections: [
    "The Concept",
    "How the Concept influences perception",
    "Associated beliefs and expectations",
    "Three or six primary Patterns",
    "Recognition of the Patterns in everyday life",
    "Opportunities for conscious change",
    "The Family it belongs to, and the Weaves it appears in",
    "The written edition, where one exists",
    "Price, and its state",
  ],
} as const;

export const FAMILIES = {
  heading: "Concept Families",
  lead: "Individual Concepts frequently belong to a larger family of related Concepts.",
  body: "Concept Family Studies allow students to explore a central area of human experience and recognise the different Concepts and Patterns that may develop within it. Each Family Study may contain approximately ten to twelve significant Patterns.",
  /** His fifteen. Eight ship at launch; which eight is not decided. */
  all: [
    "Acceptance", "Freedom", "Control", "Emotional Expression", "Belonging",
    "Achievement", "Safety and Protection", "Responsibility", "Relationship",
    "Love", "Identity", "Worth", "Trust", "Truth and Communication",
    "Spiritual Connection",
  ],
  needsMichael: "Which eight Families ship as standalone courses.",
} as const;

export const WEAVES = {
  heading: "Concept Weaves",
  lead: "Concepts rarely operate completely independently.",
  body: "One Concept may become connected with several others until they form a Concept Weave. A person may recognise one Concept without realising that several related Concepts have become interconnected within their Human Operating System. The emphasis is on understanding the relationship among the Concepts, rather than an extensive study of all the Patterns associated with each.",
  example: ["Sacrifice", "Deprivation", "Denial"],
  exampleCaption: "One rarely arrives alone.",
  needsMichael: "The twelve Weaves that ship at launch.",
} as const;

export const PATTERN_WEAVES = {
  heading: "Pattern Weaves",
  lead: "Just as Concepts can become interconnected, Patterns can operate together.",
  body: "One familiar Pattern may activate or reinforce several others, creating a repeating Pattern Weave. Pattern Weave Studies help students move beyond recognising a single behaviour and begin seeing the larger system operating beneath repeated experiences. Each study explores approximately three to six interconnected Institute Patterns.",
  status: "Phase two. Described in his 19 Aug architecture, absent from his navigation sketch.",
} as const;

/* ── Schools ─────────────────────────────────────────────────── */

export const SCHOOLS = [
  { slug: "human-consciousness", name: "School of Human Consciousness", short: "Human Consciousness",
    summary: "Courses examine awareness, attention, perception, interpretation, meaning, choice, internal communication, and conscious participation." },
  { slug: "concepts-and-beliefs", name: "School of Concepts and Beliefs", short: "Concepts and Beliefs",
    summary: "Courses examine the formation and operation of Concepts, their relationship to beliefs and expectations, and how the internal Concept structure influences life experience." },
  { slug: "human-patterns", name: "School of Human Patterns", short: "Human Patterns",
    summary: "Courses examine Pattern formation, recognition, repetition, purpose, interruption, replacement, transition, and Pattern mastery." },
  { slug: "identity", name: "School of Identity", short: "Identity",
    summary: "Courses examine identity formation, acceptance, approval and rejection, self-image, roles, masks, the mother relationship, the father relationship, expectations, self-worth, identity change, and authentic identity." },
  { slug: "relationships", name: "School of Relationships", short: "Relationships",
    summary: "Studies include expectations, relationship Patterns, boundaries, trust, forgiveness, communication, the Four Selves in relationships, and Two Human Operating Systems interacting with one another.",
    principle: "Relationships do not create the Concepts within us. They reveal the Concepts that already exist." },
  { slug: "symbolic-body", name: "School of the Symbolic Body", short: "The Symbolic Body",
    summary: "Courses examine the body as messenger, the symbolic meaning of the body, body systems, the Five Senses, symptoms, accidents, and learning to recognise the language through which the body communicates." },
] as const;

export const SCHOOLS_INTRO = {
  heading: "The Schools of the Institute",
  lead: "The Schools provide the Institute's most comprehensive areas of continuing education.",
  body: "Rather than examining only a single Concept or Pattern, each School contains multiple Courses devoted to a major area of human understanding.",
  needsMichael: "Final School names, their sequence, and the complete Course list inside each. He notes there is considerably more School material already developed than the outline shows.",
} as const;

/* ── Books, workbooks, video ─────────────────────────────────── */

export const BOOKS = {
  heading: "Books & Study Editions",
  lead: "Students learn differently.",
  body: "Some prefer audiovisual presentations. Others want to read, underline, return to passages, and study at their own pace. Where appropriate, Institute Courses, Concept Studies and Pattern Studies have corresponding written editions. Books may be purchased separately from audiovisual Courses.",
  titles: [
    { slug: "awakening", title: "Awakening" },
    { slug: "human-operating-system", title: "The Human Operating System" },
    { slug: "body-symbology", title: "Body Symbology" },
    { slug: "tj", title: "T.J.", needsMichael: true },
  ],
  needsMichael: "One title is marked FREE on his sketch — an arrow points at the row without clearly indicating which.",
} as const;

export const WORKBOOKS = {
  heading: "Workbooks & Awakening Portfolios",
  lead: "Learning becomes more meaningful when information becomes personal recognition.",
  body: "Selected Institute Courses include workbooks, reflection exercises, Pattern-recognition exercises, self-assessments, and Awakening Portfolios designed to help students apply what they are learning to their own lives.",
  note: "These materials are not tests of right or wrong. Their purpose is to encourage observation, recognition, and conscious participation.",
} as const;

export const VIDEO_STUDIES = {
  heading: "Video Studies & Special Topics",
  lead: "The Institute's educational library extends beyond formal Courses.",
  body: "Special video series provide shorter studies in areas drawn from the Institute's existing body of work.",
  collections: [
    { name: "Spiritual Teachings", detail: "Including studies such as the Eightfold Path and other universal teachings examined through the Institute's perspective." },
    { name: "The Symbolic Body", detail: "Individual presentations exploring the body's symbolic language and what physical experiences may reveal." },
    { name: "Conscious Living", detail: "Short teachings applying Institute principles to recognisable experiences of everyday life." },
    { name: "Special Topics", detail: "Focused presentations drawn from the Institute's growing educational library." },
  ],
  status: "Phase two. No titles named yet.",
} as const;

/* ── Live events ─────────────────────────────────────────────── */

export const EVENTS = {
  heading: "Live Events & Seminars",
  lead: "Live sessions on Zoom, organised by subject.",
  body: "Each seminar applies the Institute's principles to a single area of experience.",
  named: ["Arthritis", "Cancer"],
  needsMichael: "His sketch shows roughly seven subjects; two are named. Also unresolved: whether seminars are recorded and sold afterwards, which decides whether an Event page outlives its date.",
} as const;

/* ── Membership & commerce ───────────────────────────────────── */

export const MEMBERSHIP = {
  heading: "Membership",
  lead: "You are not being asked to believe anything.",
  body: "You are being asked to look at what is already operating, and to decide for yourself whether you recognise it.",
  tiers: [
    { name: "Public Price", detail: "Available to anyone wishing to purchase individual Institute materials." },
    { name: "Member Price", detail: "Institute members receive preferred pricing on qualifying Courses, books, and educational materials." },
  ],
  needsMichael: "Whether membership is a discount, a subscription, or an access tier. It changes the checkout.",
} as const;

/* ── Gating — the Foundation Course opens everything ─────────── */

export const GATING = {
  /** The gate stops study. It never stops browsing or buying. */
  states: {
    open: { label: "Available now", help: "" },
    locked: {
      label: "Opens after the Foundation",
      help: "This study opens once you have finished the Foundation Course, where the vocabulary comes from. You can read the whole description, and buy it now to keep on your shelf.",
    },
    inProgress: { label: "In progress", help: "Resume where you left off." },
    complete: { label: "Complete", help: "Revisit any lesson. Your workbook stays available." },
  },
  /** Never: countdowns, seat scarcity, or anything implying the visitor is behind. */
  neverSay: ["Enrol before", "Only N seats", "You're falling behind", "Limited time"],
} as const;

/* ── Interface microcopy ─────────────────────────────────────── */

export const UI = {
  skipToContent: "Skip to content",
  menuOpen: "Open menu",
  menuClose: "Close menu",
  searchPlaceholder: "Search Concepts, Courses and Patterns",
  searchEmpty: "Nothing matched that. Try a Concept name — Acceptance, Control, Worth.",
  cartEmpty: "Nothing in your cart yet.",
  addToCart: "Add to cart",
  buyNow: "Buy now",
  viewAll: "View all",
  readMore: "Read more",
  back: "Back",
  loading: "Loading",
  formRequired: "This one is required.",
  formEmail: "That email address does not look right.",
  newsletterHeading: "Occasional letters from the Institute",
  newsletterBody: "New Concepts, new Courses, and seminar dates. No more than monthly.",
  newsletterCta: "Subscribe",
  error404Heading: "That page is not here.",
  error404Body: "The link may be old, or the study may have moved. Everything is reachable from the five doors above.",
  error500Heading: "Something went wrong on our side.",
  error500Body: "Try again in a moment. If it keeps happening, tell us and we will look.",
} as const;

export const PAGE_TITLES: Record<string, string> = {
  "/": "The Institute of The Spiritual Science of Human Patterns",
  "/begin": "Begin Here",
  "/begin/the-path": "How the education fits together",
  "/concepts": "Concept Studies",
  "/concepts/families": "Concept Families",
  "/concepts/weaves": "Concept Weaves",
  "/concepts/pattern-weaves": "Pattern Weaves",
  "/courses": "Courses",
  "/schools": "The Schools of the Institute",
  "/human-operating-system": "The Human Operating System",
  "/books": "Books & Study Editions",
  "/books/workbooks": "Workbooks & Awakening Portfolios",
  "/books/video-studies": "Video Studies & Special Topics",
  "/events": "Live Events & Seminars",
  "/membership": "Membership",
  "/about": "About the Institute",
  "/michael": "Michael Schwartz",
  "/contact": "Contact",
  "/account": "My studies",
  "/search": "Search",
};
