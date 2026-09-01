/**
 * Navigation — the complete menu system.
 *
 * Five doors, from Michael's handwritten sketch of 23 Aug 2026, plus Membership
 * on the utility rail. His own instruction: keep the top level small, or a
 * first-time visitor faces "hundreds of individual choices."
 *
 * Anything marked NEEDS_MICHAEL has no confirmed content yet. Render the route,
 * ship the placeholder, do not invent the label.
 */

export type NavItem = {
  label: string;
  href: string;
  /** one line, used in mega-menu and mobile drawer */
  blurb?: string;
  badge?: "Free" | "Opens after the Foundation" | "Coming soon";
  children?: NavItem[];
  needsMichael?: boolean;
};

export const PRIMARY_NAV: NavItem[] = [
  {
    label: "Begin Here",
    href: "/begin",
    blurb: "Start with the free course, or see how the education fits together.",
    children: [
      { label: "The Five Laws of Manifestation", href: "/courses/five-laws", badge: "Free",
        blurb: "An introduction to the principles the teachings are built on." },
      { label: "The Human Operating System", href: "/human-operating-system",
        blurb: "Concept to Belief to Pattern to Emotion to Behavior to Life Result." },
      { label: "How the education fits together", href: "/begin/the-path",
        blurb: "The whole path, from the free course to the Schools." },
    ],
  },
  {
    label: "Concepts",
    href: "/concepts",
    blurb: "Everything begins with Concept.",
    children: [
      { label: "Individual Concepts", href: "/concepts", blurb: "Twenty-four Concepts, each with its Patterns." },
      { label: "Concept Families", href: "/concepts/families", blurb: "Eight Families. A central area of human experience." },
      { label: "Concept Weaves", href: "/concepts/weaves", blurb: "Twelve Weaves. Concepts rarely operate alone." },
      { label: "Pattern Weaves", href: "/concepts/pattern-weaves", badge: "Coming soon",
        blurb: "Patterns that activate and reinforce one another." },
    ],
  },
  {
    label: "Courses",
    href: "/courses",
    blurb: "Every Course in an audio and a video edition.",
    children: [
      { label: "The Five Laws of Manifestation", href: "/courses/five-laws", badge: "Free" },
      { label: "Foundation — Introduction to Human Patterns", href: "/courses/foundation",
        blurb: "Ten weeks. Thirty Patterns of Behavior." },
      { label: "Extended Foundation — Depth Two", href: "/courses/extended-foundation",
        badge: "Opens after the Foundation" },
      { label: "Awakening of Consciousness", href: "/courses/awakening-of-consciousness",
        badge: "Opens after the Foundation" },
      { label: "T.J.", href: "/courses/tj", needsMichael: true,
        blurb: "NEEDS_MICHAEL — appears in both the Courses row and the Books row of his sketch. Title unknown." },
      { label: "The Schools of the Institute", href: "/schools",
        blurb: "Six Schools. The most comprehensive areas of continuing education." },
    ],
  },
  {
    label: "Books",
    href: "/books",
    blurb: "Written editions, workbooks and study materials.",
    children: [
      { label: "Awakening", href: "/books/awakening" },
      { label: "The Human Operating System", href: "/books/human-operating-system" },
      { label: "Body Symbology", href: "/books/body-symbology" },
      { label: "T.J.", href: "/books/tj", needsMichael: true },
      { label: "Workbooks & Awakening Portfolios", href: "/books/workbooks" },
      { label: "Video Studies & Special Topics", href: "/books/video-studies", badge: "Coming soon" },
    ],
  },
  {
    label: "Live Events",
    href: "/events",
    blurb: "Seminars on Zoom, organised by subject.",
    children: [
      { label: "Arthritis", href: "/events/arthritis" },
      { label: "Cancer", href: "/events/cancer" },
      { label: "All seminars", href: "/events", needsMichael: true,
        blurb: "NEEDS_MICHAEL — his sketch shows roughly seven subjects. Two are named." },
    ],
  },
];

/** Utility rail — right of the primary nav */
export const UTILITY_NAV: NavItem[] = [
  { label: "Membership", href: "/membership" },
  { label: "Search", href: "/search" },
  { label: "Sign in", href: "/account" },
];

/** Shown only to a signed-in student, replacing "Sign in" */
export const ACCOUNT_NAV: NavItem[] = [
  { label: "My studies", href: "/account" },
  { label: "Progress", href: "/account/progress" },
  { label: "Orders", href: "/account/orders" },
  { label: "Settings", href: "/account/settings" },
  { label: "Sign out", href: "/account/sign-out" },
];

export const FOOTER_NAV: { heading: string; items: NavItem[] }[] = [
  {
    heading: "Study",
    items: [
      { label: "The Five Laws", href: "/courses/five-laws" },
      { label: "Foundation Course", href: "/courses/foundation" },
      { label: "Extended Foundation", href: "/courses/extended-foundation" },
      { label: "Concept Studies", href: "/concepts" },
      { label: "Concept Families", href: "/concepts/families" },
      { label: "Concept Weaves", href: "/concepts/weaves" },
    ],
  },
  {
    heading: "The Schools",
    items: [
      { label: "Human Consciousness", href: "/schools/human-consciousness" },
      { label: "Concepts and Beliefs", href: "/schools/concepts-and-beliefs" },
      { label: "Human Patterns", href: "/schools/human-patterns" },
      { label: "Identity", href: "/schools/identity" },
      { label: "Relationships", href: "/schools/relationships" },
      { label: "The Symbolic Body", href: "/schools/symbolic-body" },
    ],
  },
  {
    heading: "Library",
    items: [
      { label: "Awakening", href: "/books/awakening" },
      { label: "The Human Operating System", href: "/books/human-operating-system" },
      { label: "Body Symbology", href: "/books/body-symbology" },
      { label: "Workbooks & Portfolios", href: "/books/workbooks" },
    ],
  },
  {
    heading: "The Institute",
    items: [
      { label: "About", href: "/about" },
      { label: "Michael Schwartz", href: "/michael" },
      { label: "Membership", href: "/membership" },
      { label: "Live Events", href: "/events" },
      { label: "Contact", href: "/contact" },
    ],
  },
];

export const LEGAL_NAV: NavItem[] = [
  { label: "Terms", href: "/legal/terms" },
  { label: "Privacy", href: "/legal/privacy" },
  { label: "Refunds", href: "/legal/refunds" },
];
