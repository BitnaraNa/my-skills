---
name: store-screenshots
description: Use when building App Store or Play Store screenshot pages, generating exportable marketing screenshots for iOS or Android apps, or creating programmatic screenshot generators with Next.js. Triggers on app store, play store, screenshots, marketing assets, html-to-image, phone mockup, tablet mockup.
---

# Store Screenshots Generator

## Overview

Build a Next.js page that renders App Store / Play Store screenshots as **advertisements** (not UI showcases) and exports them via `html-to-image` at required resolutions. Screenshots are the single most important conversion asset on the stores.

## Core Principle

**Screenshots are advertisements, not documentation.** Every screenshot sells one idea. If you're showing UI, you're doing it wrong — you're selling a *feeling*, an *outcome*, or killing a *pain point*.

## Step 1: Project Discovery & Screenshot Planning

Before writing ANY code, understand the app and plan screenshot content collaboratively with the user.

### Phase 1: Auto-Scan the Project

Use the Agent tool to dispatch **parallel exploration agents** that analyze the project:

**Agent 1 — Feature Analyst:**
- Scan source code (screens, routes, components, navigation) to identify all user-facing features
- Read README, CHANGELOG, app manifests (`AndroidManifest.xml`, `Info.plist`, `app.json`, etc.)
- Identify the app's core value proposition — what problem does it solve?
- List features in priority order based on code prominence and navigation hierarchy

**Agent 2 — Brand & Asset Analyst:**
- Find app icon, splash screen, color themes (`colors.xml`, `tailwind.config`, `theme.ts`, etc.)
- Identify brand colors, fonts, existing design tokens
- Locate any existing marketing assets, screenshots, or store metadata (`fastlane/`, `metadata/`, store descriptions)
- Check for UI component libraries or design system in use

**Agent 3 — Competitor & Positioning Analyst:**
- Read store description, keywords, app name, subtitle if available
- Identify the app category and likely competitors from the metadata
- Determine what differentiators to emphasize based on feature set
- Suggest positioning angle: what makes this app unique?

Collect all findings and synthesize into a **Project Brief**.

### Phase 2: Agent Team Proposes Screenshot Concepts

Using the Project Brief, dispatch a second round of **perspective agents** to propose screenshot concepts:

**Marketing Strategist Agent:**
- Proposes slide sequence optimized for conversion (hero → differentiator → features → trust)
- Focuses on the narrative arc — what story do the screenshots tell as a set?
- Considers the "first 3 screenshots" rule — most users never scroll past #3

**Copywriter Agent:**
- Writes 2-3 headline options per proposed slide **per target language** using the three approaches (paint a moment / state an outcome / kill a pain)
- Applies the Iron Rules: one idea per headline, readable at thumbnail size
- Line length per language: EN 3-5 words, KO 2-4 어절, JA 5-10 chars, ZH 4-8 chars
- Ensures no two slides use "and" or compound clauses
- Copy is **adapted, not translated** — each language should feel native

**UX/Visual Director Agent:**
- Proposes layout variety per slide (centered phone, two-phone, phone + floating elements, no-phone)
- Suggests which slides should be dark vs light for visual rhythm
- Recommends style direction based on brand colors and app aesthetic
- Plans which actual app screens to capture for each slide

Each agent returns its proposals independently. Combine into a unified **Screenshot Plan**.

### Phase 3: Present to User for Review

Present the Screenshot Plan as a clear table:

```
| # | Concept         | Headline Options (pick one)       | Layout     | Screen to Capture   |
|---|-----------------|-----------------------------------|------------|---------------------|
| 1 | Hero            | A) "..." B) "..." C) "..."        | Centered   | Home screen         |
| 2 | Differentiator  | A) "..." B) "..." C) "..."        | Two-phone  | Feature X vs Y      |
| 3 | Core Feature    | A) "..." B) "..." C) "..."        | Right-lean | Detail screen       |
| ...                                                                                        |
```

Present the Screenshot Plan with headlines shown **per language**:

```
| # | Concept         | EN Headlines (pick one)           | KO Headlines (pick one)           | Layout     | Screen to Capture   |
|---|-----------------|-----------------------------------|-----------------------------------|------------|---------------------|
| 1 | Hero            | A) "..." B) "..." C) "..."        | A) "..." B) "..." C) "..."        | Centered   | Home screen         |
| 2 | Differentiator  | A) "..." B) "..." C) "..."        | A) "..." B) "..." C) "..."        | Two-phone  | Feature X vs Y      |
| ...                                                                                                                                |
```

Then ask the user:

1. **Languages** — "Which languages do you need? (e.g., English + Korean, or English + Korean + Japanese, etc.) Each language generates a separate set of screenshots."
2. **Review the plan** — "Here's what I found and propose. Adjust the order, swap headlines, add/remove slides, or change anything."
3. **App screenshots** — "I'll need actual device captures for each slide. Can you provide PNGs per language (if localized UI), or should I note which screens to capture?"
4. **Style direction** — "Based on your brand, I suggest [style]. Want to adjust? (warm/organic, dark/moody, clean/minimal, bold/colorful, gradient-heavy, flat)"
5. **Any overrides** — "Anything else you want to change or add?"

**Platform & Device: Always generate ALL.** Do NOT ask the user which platform or device type. Always generate for both iOS and Android, and all device types (phone, 7-inch tablet, 10-inch tablet). The user can delete what they don't need after export.

**Language-specific app screenshots:** If the app has localized UI, the user should provide separate screenshots per language (e.g., `screenshots/en/home.png`, `screenshots/ko/home.png`). If the UI is language-neutral or only in one language, the same screenshots can be shared across all locales.

**Do NOT proceed until the user approves or adjusts the plan.**

### Design Decisions (auto-derive, do NOT ask)

Based on the approved plan, brand analysis, and style direction, decide:
- **Background style**: gradient direction, colors, whether light or dark base
- **Decorative elements**: blobs, glows, geometric shapes, or none — match the style
- **Typography treatment**: weight, tracking, line height — match the brand personality
- **Color palette**: derive text colors, secondary colors, shadow tints from the brand colors

**IMPORTANT:** If the user gives additional instructions at any point during the process, follow them. User instructions always override skill defaults.

## Step 2: Set Up the Project

### Detect Package Manager

Check what's available, use this priority: **bun > pnpm > yarn > npm**

```bash
which bun && echo "use bun" || which pnpm && echo "use pnpm" || which yarn && echo "use yarn" || echo "use npm"
```

### Scaffold (if no existing Next.js project)

```bash
# With bun:
bunx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
bun add html-to-image

# With pnpm:
pnpx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
pnpm add html-to-image

# With yarn:
yarn create next-app . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
yarn add html-to-image

# With npm:
npx create-next-app@latest . --typescript --tailwind --app --src-dir --no-eslint --import-alias "@/*"
npm install html-to-image
```

### Copy the Phone Mockup

The skill includes a pre-measured iPhone mockup at `mockup.png` (co-located with this SKILL.md). Copy it to the project's `public/` directory. The mockup file is in the same directory as this skill file.

**For Android:** Use a suitable Android phone/tablet mockup PNG. The user should provide one, or use a flat bezel frame. Adjust the mockup measurements accordingly (see Phone Mockup Component section).

### File Structure

```
project/
├── public/
│   ├── mockup.png              # Phone frame (included with skill — iPhone)
│   ├── mockup-android.png      # Android phone frame (user-provided or generated)
│   ├── mockup-7inch.png        # 7-inch tablet frame (user-provided or generated)
│   ├── mockup-10inch.png       # 10-inch tablet frame (user-provided or generated)
│   ├── app-icon.png            # User's app icon
│   └── screenshots/            # User's app screenshots (per locale if localized UI)
│       ├── en/
│       │   ├── home.png
│       │   ├── feature-1.png
│       │   └── ...
│       ├── ko/
│       │   ├── home.png
│       │   ├── feature-1.png
│       │   └── ...
│       └── shared/             # Language-neutral screenshots (optional)
│           └── ...
├── src/app/
│   ├── layout.tsx              # Font setup (multi-language fonts)
│   └── page.tsx                # The screenshot generator (single file)
└── package.json
```

**The entire generator is a single `page.tsx` file.** No routing, no extra layouts, no API routes. i18n is handled inline via a `TRANSLATIONS` record and a `locale` state variable.

### Font Setup (Multi-Language)

When supporting multiple languages, load fonts for each script:

```tsx
// src/app/layout.tsx
import { Inter, Noto_Sans_KR } from "next/font/google";

// Latin script (English, etc.)
const inter = Inter({ subsets: ["latin"], variable: "--font-latin" });

// Korean script
const notoKR = Noto_Sans_KR({
  subsets: ["latin"],  // next/font requires at least "latin"
  weight: ["400", "600", "700"],
  variable: "--font-ko",
});

// Add more as needed:
// const notoJP = Noto_Sans_JP({ subsets: ["latin"], weight: [...], variable: "--font-ja" });

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html>
      <body className={`${inter.variable} ${notoKR.variable}`}>
        {children}
      </body>
    </html>
  );
}
```

In `page.tsx`, use the appropriate CSS variable per locale:

```typescript
const LOCALE_FONTS: Record<Locale, string> = {
  en: "var(--font-latin), sans-serif",
  ko: "var(--font-ko), var(--font-latin), sans-serif",
  // ja: "var(--font-ja), var(--font-latin), sans-serif",
};

// Apply on the offscreen export container and slide wrapper:
// style={{ fontFamily: LOCALE_FONTS[locale] }}
```

## Step 3: Plan the Slides

### Screenshot Framework (Narrative Arc)

Adapt this framework to the user's requested slide count. Not all slots are required — pick what fits:

| Slot | Purpose | Notes |
|------|---------|-------|
| #1 | **Hero / Main Benefit** | App icon + tagline + home screen. This is the ONLY one most people see. |
| #2 | **Differentiator** | What makes this app unique vs competitors |
| #3 | **Ecosystem** | Widgets, extensions, watch — beyond the main app. Skip if N/A. |
| #4+ | **Core Features** | One feature per slide, most important first |
| 2nd to last | **Trust Signal** | Identity/craft — "made for people who [X]" |
| Last | **More Features** | Pills listing extras + coming soon. Skip if few features. |

**Rules:**
- Each slide sells ONE idea. Never two features on one slide.
- Vary layouts across slides — never repeat the same template structure.
- Include 1-2 contrast slides (inverted bg) for visual rhythm.

## Step 4: Write Copy FIRST (All Languages)

Get all headlines approved **in every target language** before building layouts. Bad copy ruins good design.

### The Iron Rules

1. **One idea per headline.** Never join two things with "and."
2. **Short, common words.** 1-2 syllables. No jargon unless it's domain-specific.
3. **3-5 words per line.** Must be readable at thumbnail size in the store.
4. **Line breaks are intentional.** Control where lines break with `<br />`.

### Multi-Language Copy Rules

- **Do NOT just translate.** Each language should have copy that feels native — adapted, not translated. Korean copy should feel natural in Korean, not like translated English.
- **Character count varies by language.** CJK (Korean, Japanese, Chinese) characters are wider — fewer characters per line. Adjust line breaks accordingly.
  - English: 3-5 words per line
  - Korean: 2-4 어절 per line (shorter due to wider characters)
  - Japanese: 5-10 characters per line
  - Chinese: 4-8 characters per line
- **Same concept, different expression.** The *idea* stays the same, but the phrasing should match each language's marketing conventions.
- **Present ALL languages together** in the review table so the user can compare.

### Three Approaches (pick one per slide)

| Type | What it does | EN Example | KO Example |
|------|-------------|------------|------------|
| **Paint a moment** | You picture yourself doing it | "Check your coffee without opening the app." | "앱 안 열어도 커피를 확인하세요." |
| **State an outcome** | What your life looks like after | "A home for every coffee you buy." | "모든 커피의 기록이 한곳에." |
| **Kill a pain** | Name a problem and destroy it | "Never waste a great bag of coffee." | "좋은 원두, 더는 낭비 없이." |

### What NEVER Works

- **Feature lists as headlines**: "Log every item with tags, categories, and notes"
- **Two ideas joined by "and"**: "Track X and never miss Y"
- **Compound clauses**: "Save and customize X for every Y you own"
- **Vague aspirational**: "Every item, tracked"
- **Marketing buzzwords**: "AI-powered tips" (unless it's actually AI)
- **Literal translations**: Translating word-for-word without cultural adaptation

### Copy Process

1. Write 3 options per slide per language using the three approaches
2. Read each at arm's length — if you can't parse it in 1 second, it's too complex
3. Check line lengths per language (see character count rules above)
4. Present options to the user in a comparison table with reasoning for each

### Reference Apps for Copy Style

- **Raycast** — specific, descriptive, one concrete value per slide
- **Turf** — ultra-simple action verbs, conversational
- **Mela / Notion** — warm, minimal, elegant

## Step 5: Build the Page

### Architecture

```
page.tsx
├── Constants (W, H, SIZES, design tokens from user's brand)
├── Locale types & translations (LOCALES, LocaleTexts, TRANSLATIONS)
├── Phone component (mockup with screen overlay)
├── Caption component (label + headline — reads from current locale)
├── Decorative components (blobs, glows, shapes — based on style direction)
├── Screenshot1..N components (one per slide, receives locale prop)
├── SCREENSHOTS array (registry)
├── ScreenshotPreview (ResizeObserver scaling + hover export)
└── ScreenshotsPage (grid + toolbar + locale selector + export logic)
```

### i18n Architecture

#### Locale Types

```typescript
// Extensible locale system — add new languages by adding to this array and TRANSLATIONS
const LOCALES = ["en", "ko"] as const;  // extend: ["en", "ko", "ja", "zh", ...]
type Locale = (typeof LOCALES)[number];

const LOCALE_LABELS: Record<Locale, string> = {
  en: "English",
  ko: "한국어",
  // ja: "日本語",
  // zh: "中文",
};
```

#### Translations Structure

```typescript
// Each slide has localized label + headline per language
type SlideTexts = {
  label: string;    // category label (e.g., "PRODUCTIVITY" / "생산성")
  headline: string; // main headline with <br /> for line breaks
};

// All slides' text for one locale
type LocaleTexts = Record<string, SlideTexts>; // key = slide name

const TRANSLATIONS: Record<Locale, LocaleTexts> = {
  en: {
    hero:         { label: "YOUR APP", headline: "Your main<br />tagline here" },
    feature1:     { label: "FEATURE", headline: "One clear<br />benefit" },
    // ... one entry per slide
  },
  ko: {
    hero:         { label: "앱 이름", headline: "핵심 가치를<br />한 줄로" },
    feature1:     { label: "기능", headline: "하나의 명확한<br />혜택" },
    // ... matching entries
  },
};
```

#### Screenshot Components Receive Locale

```tsx
// Every screenshot component takes locale as a prop
function ScreenshotHero({ locale }: { locale: Locale }) {
  const t = TRANSLATIONS[locale].hero;
  return (
    <div style={{ width: W, height: H, position: "relative", overflow: "hidden" }}>
      {/* background, decorations */}
      <Caption label={t.label} headline={t.headline} />
      <Phone src={`/screenshots/${locale}/home.png`} alt="Home" />
      {/* If screenshots are language-neutral, use: src="/screenshots/home.png" */}
    </div>
  );
}
```

#### Screenshot Registry with Locale

```typescript
const SCREENSHOTS = [
  { name: "hero",     component: ScreenshotHero },
  { name: "feature1", component: ScreenshotFeature1 },
  // ...
] as const;

// Render: SCREENSHOTS.map(s => <s.component locale={currentLocale} />)
```

#### Localized App Screenshots Path Convention

```
public/screenshots/
├── en/                    # English UI captures
│   ├── home.png
│   ├── feature-1.png
│   └── ...
├── ko/                    # Korean UI captures
│   ├── home.png
│   ├── feature-1.png
│   └── ...
└── shared/                # Language-neutral screenshots (optional)
    ├── settings.png
    └── ...
```

If the app UI is not localized, all screenshots go in `public/screenshots/` without locale subfolders, and components use the same `src` for all locales.

### Export Sizes

#### iOS App Store (iPhone only, portrait)

```typescript
const IOS_SIZES = [
  { label: '6.9"', w: 1320, h: 2868 },
  { label: '6.5"', w: 1284, h: 2778 },
  { label: '6.3"', w: 1206, h: 2622 },
  { label: '6.1"', w: 1125, h: 2436 },
] as const;
```

#### Google Play Store (portrait)

```typescript
const ANDROID_PHONE_SIZES = [
  { label: 'Phone', w: 1080, h: 1920 },
] as const;

const ANDROID_7INCH_SIZES = [
  { label: '7"', w: 1200, h: 1920 },
] as const;

const ANDROID_10INCH_SIZES = [
  { label: '10"', w: 1600, h: 2560 },
] as const;
```

#### Combined Size Registry

```typescript
type Platform = 'ios' | 'android';
type DeviceType = 'phone' | '7inch' | '10inch';

const SIZES: Record<Platform, Partial<Record<DeviceType, { label: string; w: number; h: number }[]>>> = {
  ios: {
    phone: IOS_SIZES,
  },
  android: {
    phone: ANDROID_PHONE_SIZES,
    '7inch': ANDROID_7INCH_SIZES,
    '10inch': ANDROID_10INCH_SIZES,
  },
};
```

Design at the LARGEST size per device type and scale down for export.

- iOS phone: design at 1320x2868
- Android phone: design at 1080x1920
- 7-inch tablet: design at 1200x1920
- 10-inch tablet: design at 1600x2560

### Language Selector & Export (Toolbar)

The toolbar should include:
- **Language toggle**: Buttons for each locale (EN / KO / ...). Switching re-renders all slides with that locale's text and font.
- **Export current language**: Exports all platforms & device types for the selected locale.
- **Export all**: Exports all platforms, device types, and all languages at once.

```tsx
// Toolbar state — language only. Platform & device are always ALL.
const [locale, setLocale] = useState<Locale>(LOCALES[0]);
```

When the user selects a locale, the preview re-renders with that language's headlines, fonts, and (if applicable) localized app screenshots. Export always generates all platform/device combinations — no selection needed.

### Rendering Strategy

Each screenshot is designed at full resolution. Two copies exist:

1. **Preview**: CSS `transform: scale()` via ResizeObserver to fit a grid card
2. **Export**: Offscreen at `position: absolute; left: -9999px` at true resolution

### Phone Mockup Component

The included iPhone `mockup.png` has these pre-measured values:

```typescript
// iPhone mockup measurements
const IPHONE_MK = {
  W: 1022, H: 2082,
  SC_L: (52 / 1022) * 100,
  SC_T: (46 / 2082) * 100,
  SC_W: (918 / 1022) * 100,
  SC_H: (1990 / 2082) * 100,
  SC_RX: (126 / 918) * 100,
  SC_RY: (126 / 1990) * 100,
};
```

**Android / tablet mockups** (included with skill, generated by `generate-mockups.py`):

```typescript
// Android phone mockup measurements (mockup-android.png: 1004x2084)
const ANDROID_PHONE_MK = {
  W: 1004, H: 2084,
  SC_L: (42 / 1004) * 100,
  SC_T: (42 / 2084) * 100,
  SC_W: (920 / 1004) * 100,
  SC_H: (2000 / 2084) * 100,
  SC_RX: (80 / 920) * 100,
  SC_RY: (80 / 2000) * 100,
};

// 7-inch tablet mockup measurements (mockup-7inch.png: 1156x1876)
const TABLET_7_MK = {
  W: 1156, H: 1876,
  SC_L: (48 / 1156) * 100,
  SC_T: (48 / 1876) * 100,
  SC_W: (1060 / 1156) * 100,
  SC_H: (1780 / 1876) * 100,
  SC_RX: (40 / 1060) * 100,
  SC_RY: (40 / 1780) * 100,
};

// 10-inch tablet mockup measurements (mockup-10inch.png: 1512x2312)
const TABLET_10_MK = {
  W: 1512, H: 2312,
  SC_L: (56 / 1512) * 100,
  SC_T: (56 / 2312) * 100,
  SC_W: (1400 / 1512) * 100,
  SC_H: (2200 / 2312) * 100,
  SC_RX: (44 / 1400) * 100,
  SC_RY: (44 / 2200) * 100,
};
```

```tsx
function Phone({ src, alt, style, className = "", mockup = "iphone" }: {
  src: string; alt: string; style?: React.CSSProperties; className?: string;
  mockup?: "iphone" | "android" | "7inch" | "10inch";
}) {
  const mk = mockup === "iphone" ? IPHONE_MK
    : mockup === "android" ? ANDROID_PHONE_MK
    : mockup === "7inch" ? TABLET_7_MK
    : TABLET_10_MK;

  const mockupSrc = mockup === "iphone" ? "/mockup.png"
    : mockup === "android" ? "/mockup-android.png"
    : mockup === "7inch" ? "/mockup-7inch.png"
    : "/mockup-10inch.png";

  return (
    <div className={`relative ${className}`}
      style={{ aspectRatio: `${mk.W}/${mk.H}`, ...style }}>
      <img src={mockupSrc} alt=""
        className="block w-full h-full" draggable={false} />
      <div className="absolute z-10 overflow-hidden"
        style={{
          left: `${mk.SC_L}%`, top: `${mk.SC_T}%`,
          width: `${mk.SC_W}%`, height: `${mk.SC_H}%`,
          borderRadius: `${mk.SC_RX}% / ${mk.SC_RY}%`,
        }}>
        <img src={src} alt={alt}
          className="block w-full h-full object-cover object-top"
          draggable={false} />
      </div>
    </div>
  );
}
```

### Typography (Resolution-Independent)

All sizing relative to canvas width W:

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| Category label | `W * 0.028` | 600 (semibold) | default |
| Headline | `W * 0.09` to `W * 0.1` | 700 (bold) | 1.0 |
| Hero headline | `W * 0.1` | 700 (bold) | 0.92 |

### Phone Placement Patterns

Vary across slides — NEVER use the same layout twice in a row:

**Centered phone** (hero, single-feature):
```
bottom: 0, width: "82-86%", translateX(-50%) translateY(12-14%)
```

**Two phones layered** (comparison):
```
Back: left: "-8%", width: "65%", rotate(-4deg), opacity: 0.55
Front: right: "-4%", width: "82%", translateY(10%)
```

**Phone + floating elements** (only if user provided component PNGs):
```
Cards should NOT block the phone's main content.
Position at edges, slight rotation (2-5deg), drop shadows.
If distracting, push partially off-screen or make smaller.
```

### "More Features" Slide (Optional)

Dark/contrast background with app icon, headline ("And so much more."), and feature pills. Can include a "Coming Soon" section with dimmer pills.

## Step 6: Export

### Why html-to-image, NOT html2canvas

`html2canvas` breaks on CSS filters, gradients, drop-shadow, backdrop-filter, and complex clipping. `html-to-image` uses native browser SVG serialization — handles all CSS faithfully.

### Export Implementation

```typescript
import { toPng } from "html-to-image";

// Before capture: move element on-screen
el.style.left = "0px";
el.style.opacity = "1";
el.style.zIndex = "-1";

const opts = { width: W, height: H, pixelRatio: 1, cacheBust: true };

// CRITICAL: Double-call trick — first warms up fonts/images, second produces clean output
await toPng(el, opts);
const dataUrl = await toPng(el, opts);

// After capture: move back off-screen
el.style.left = "-9999px";
el.style.opacity = "";
el.style.zIndex = "";
```

### Bulk Export by Platform/Device/Language

```typescript
// Export one language
async function exportLocale(locale: Locale, platform: Platform, deviceType: DeviceType) {
  const sizes = SIZES[platform]?.[deviceType] ?? [];
  for (const size of sizes) {
    for (let i = 0; i < SCREENSHOTS.length; i++) {
      // Folder: {locale}/{platform}-{device}/  e.g., "en/ios-phone/", "ko/android-7inch/"
      const filename = `${locale}/${platform}-${deviceType}/${String(i + 1).padStart(2, "0")}-${SCREENSHOTS[i].name}-${size.w}x${size.h}.png`;
      // ... resize and download
    }
  }
}

// Export one language — all platforms & device types
async function exportLocaleAll(locale: Locale) {
  const allCombos: [Platform, DeviceType][] = [
    ['ios', 'phone'],
    ['android', 'phone'],
    ['android', '7inch'],
    ['android', '10inch'],
  ];
  for (const [platform, deviceType] of allCombos) {
    await exportLocale(locale, platform, deviceType);
  }
}

// Export ALL languages × ALL platforms × ALL device types
async function exportEverything() {
  for (const locale of LOCALES) {
    setLocale(locale);
    await new Promise(r => setTimeout(r, 500)); // wait for re-render
    await exportLocaleAll(locale);
  }
}
```

#### Export Folder Structure

```
export/
├── en/
│   ├── ios-phone/
│   │   ├── 01-hero-1320x2868.png
│   │   ├── 01-hero-1284x2778.png
│   │   └── ...
│   ├── android-phone/
│   │   ├── 01-hero-1080x1920.png
│   │   └── ...
│   ├── android-7inch/
│   │   └── ...
│   └── android-10inch/
│       └── ...
├── ko/
│   ├── ios-phone/
│   │   └── ...
│   ├── android-phone/
│   │   └── ...
│   ├── android-7inch/
│   │   └── ...
│   └── android-10inch/
│       └── ...
└── ja/  (if added)
    └── ...
```

### Key Rules

- **Double-call trick**: First `toPng()` loads fonts/images lazily. Second produces clean output. Without this, exports are blank.
- **On-screen for capture**: Temporarily move to `left: 0` before calling `toPng`.
- **Offscreen container**: Use `position: absolute; left: -9999px` (not `fixed`).
- **Resizing**: Load data URL into Image, draw onto canvas at target size.
- 300ms delay between sequential exports.
- Set `fontFamily` on the offscreen container.
- **Numbered filenames**: Prefix exports with zero-padded index so they sort correctly: `01-hero-1320x2868.png`, `02-freshness-1320x2868.png`, etc. Use `String(index + 1).padStart(2, "0")`.
- **Folder per locale, platform, and device type**: Organize exports as `{locale}/{platform}-{device}/`. e.g., `en/ios-phone/`, `ko/android-7inch/`.
- **Font on export container**: Set `fontFamily` to `LOCALE_FONTS[locale]` on the offscreen container before each locale's export.
- **Re-render before export**: When bulk-exporting all locales, wait for React to re-render after locale change before capturing.

## Common Mistakes

| Mistake | Fix |
|---------|-----|
| All slides look the same | Vary phone position (center, left, right, two-phone, no-phone) |
| Decorative elements invisible | Increase size and opacity — better too visible than invisible |
| Copy is too complex | "One second at arm's length" test |
| Floating elements block the phone | Move off-screen edges or above the phone |
| Plain white/black background | Use gradients — even subtle ones add depth |
| Too cluttered | Remove floating elements, simplify to phone + caption |
| Too simple/empty | Add larger decorative elements, floating items at edges |
| Headlines use "and" | Split into two slides or pick one idea |
| No visual contrast across slides | Mix light and dark backgrounds |
| Export is blank | Use double-call trick; move element on-screen before capture |
| Same mockup for all platforms | Use platform-appropriate mockups (iPhone vs Android vs tablet) |
| Tablet screenshots look like stretched phone | Design separate layouts for tablet aspect ratios |
| Wrong export sizes per store | Use the SIZES registry — don't hardcode dimensions |
| Same headline translated literally | Adapt copy natively per language — don't word-for-word translate |
| Wrong font for CJK text | Use LOCALE_FONTS map — each locale needs its own font family |
| Forgot to re-render before export | Wait 500ms after setLocale() before capturing — React needs time to re-render |
| All languages in one folder | Organize by `{locale}/{device}/` — stores require separate uploads per language |
| English line breaks applied to Korean | CJK characters are wider — fewer words per line, adjust `<br />` positions |
