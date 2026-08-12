NORTHBEAM DOCS : PRODUCT-LED IA PROPOSAL (v2)
Dated 2026-08-12. Replaces the audit's task-led 8-domain plan with the
product-led structure Ariella sketched. 144 pages mapped into 9 sections.

WHY THIS SHAPE
The audit organized by what a user is DOING (Set Up, Connect, Understand,
Troubleshoot). This version organizes by what Northbeam IS and SELLS
(Onboarding, then the named Products, the Platform screens, the Features).
For a company with branded offerings (Apex, MTA, C+DV, Incrementality,
Unified Marketing Measurement), product-led matches how sales and
marketing already talk, and gives each product a home to grow into.

THE HARD PART, SOLVED
Four sections overlap unless we draw hard lines: Data & Terminology,
Platform, Features, and Products. Use these one-line filing rules. Every
page files in exactly one place.

- Data and Terminology = the MEANING behind a number or word. "What does
  this term/metric mean?" (models in general, windows, modes, glossary)
- Platform = a SCREEN in the app, mirroring the left menu. "What is this
  page I'm looking at?" (Overview, Sales, Attribution, Creative, etc.)
- Features = a CAPABILITY you invoke that isn't a whole screen. "How do I
  use this tool?" (Breakdowns, Benchmarks, Model Comparison, Exports)
- Products = a NAMED offering with its own methodology. "What is this
  Northbeam product and how does it work?" (Apex, MTA, C+DV, Inc, UMM, AI)

Rule of thumb for the MTA/C+DV overlap: the general concept lives in Data
and Terminology (e.g. "Attribution Models"); the branded product page
lives in Products (e.g. "Clicks + Deterministic Views").

=====================================================================
1. ONBOARDING
   (Start here | Set up & Implement | Connect channels)
=====================================================================
Everything to get from zero to a working dashboard. The 26 channel
guides live here under Connect channels.

Start here
- What is Northbeam?  (or fold into homepage per the Start Here note)
- Quickstart / guided ramp-up  (from navigating-northbeam)
- What to expect during implementation
- Confirm setup requirements
- Onboarding FAQs

Set up & Implement
- Invite team | Business information | Currency
- Link DNS  (Add Domain merged in)
- Add pixel | Page view events | Optional additional methods
- Shopify installation | Non-Shopify installation | Third-party checkouts
- Add orders | Shopify order sync | Shopify migration | SFTP orders upload
- Order tags | Add order tags in Shopify (8c) | Configure order exclusions (8d)
- Add spend
- Setting up custom goals
- All other platforms overview
- Setting up multiple stores or regions | Multi-dashboard with configurators

Connect channels
- Integrations and UTMs | UTMs for legacy platforms
- Non-integrated channel setup | Integration matrix (rebuild as table)
- Channel guides (26): Facebook, Google, TikTok, Klaviyo, Amazon,
  Microsoft, Pinterest, Snapchat, X, Attentive, Impact, Keynes,
  LiveIntent, Universal, AppLovin, ROKT, Vibe.co, Bliss Point, MNTN,
  Rakuten, Tatari, TradeDesk, Off-Domain Sites, Shops, Other/Non-Integrated

=====================================================================
2. DATA AND TERMINOLOGY
=====================================================================
The concepts and definitions behind every number. The "understand your
numbers" content.
- Attribution models | Attribution windows | Lookback windows
- Accounting modes | How credit is assigned (credit allocation examples)
- Northbeam Metrics 101 | Subscription metrics | Northbeam's data sources
- How does Northbeam track Orders and Ads?
- What is a good/bad number in Northbeam?
- How to interpret non-click channels
- Organic vs Unattributed
- Case scenario: Cash vs Accrual | Case scenario: Clicks + Views vs Clicks-Only

=====================================================================
3. FEATURES
=====================================================================
Cross-cutting tools you invoke, that aren't a full dashboard screen.
- Manage Breakdowns and Saved Views
- Profit Benchmarks
- Model Comparison Tool
- Exporting Data | Touchpoints Export
- Subscription Analytics
(Custom Goals could sit here or in Onboarding-setup; recommend Onboarding
since it is a setup action.)

=====================================================================
4. PLATFORM (menu and products)
=====================================================================
One page per screen in the app's left menu. "What is this page?"
- Overview Home Page
- Sales
- Attribution Home Page
- Creative Analytics
- Product Analytics
- Orders (orders-tracking)
- Metrics Explorer  (+ Quickstart, + Best Practices 7 Tips as children)

=====================================================================
5. PRODUCTS
   (Incrementality | Apex | Unified Marketing Measurement | MTA | C+DV | AI)
=====================================================================
The named offerings, each with its own methodology and setup.

Apex
- Northbeam Apex (overview) | Apex FAQs | Setting up Apex
- Setting up a Meta Custom Attribution Campaign

MTA (Multi-Touch Attribution)
- What is Northbeam's MTA Methodology?

C+DV (Clicks + Deterministic Views)
- Clicks + Deterministic Views

AI
- Connect Northbeam to Claude (MCP)

Incrementality (Inc)
- GAP: no dedicated page yet. Needs a product overview written.

Unified Marketing Measurement (UMM / MMM)
- GAP: no dedicated page yet. Some of this lives inside the MTA
  methodology page today. Needs its own product overview.

Note: "Why is the Northbeam methodology better than internal platforms"
merged into the MTA methodology page already.

=====================================================================
6. DEVELOPERS & API
=====================================================================
- Using the API | Orders API guide | Order Definition | Hashing Customer Data
- Errors | Spend API | Spend API Best Practices and Limits
- Data Export API (+ GCS export, S3 export, rate limits)
- API Reference (all endpoint pages): Orders v2 + v1 (deprecated),
  Spend (daily + hourly), Data Export

=====================================================================
7. TROUBLESHOOT
=====================================================================
"Something is wrong / the numbers don't match."
- Differences in Ad Performance | Ad Spend/Data | Unattributed | Visits
- Why doesn't Northbeam match my Shopify reporting?
- Why is my FB ROAS so much lower in Northbeam?
- Checking Ad Platform Connections | Checking UTM Tracking
- Troubleshooting Tracking Issues | Troubleshooting Pixel Tracking
- Gclid, Fbclid, and Redirects
- Frequently Asked Questions
- Blotout vs Northbeam

=====================================================================
8. RELEASE NOTES
=====================================================================
- Northbeam 3.0
- GAP: needs an ongoing changelog. Mintlify has a native changelog/update
  format; recommend adopting it so every ship lands here.

=====================================================================
9. NORTHBEAM INTERNAL  (behind a specific firewall)
   Playbooks + official Notion links
=====================================================================
Team-facing content, gated. Mintlify supports authenticated/private
pages for exactly this.
- Best Practices by Teams and Departments
- Paid Social Team | Paid Search Team | Executive Team
- Email/SMS/Retention Team | Offline Channel
- The Media Buyer Newsletter
- Links out to the official Notion playbooks

=====================================================================
DECISIONS YOU NEED TO MAKE
=====================================================================
1. MTA and C+DV live in Products, but their glossary-level definitions
   stay in Data and Terminology. Confirm that split, or pick one home.
2. Incrementality and Unified Marketing Measurement have no pages yet.
   Create product overviews, or leave the Products section with 4 of 6
   for now and add them later.
3. Custom Goals + Subscription Analytics: Onboarding (setup) or Features
   (capability)? Proposal puts Custom Goals in Onboarding, Subscription
   Analytics in Features. Flag if you want them together.
4. Account admin pages (Users, Ad Accounts, Currency-as-admin): currently
   scattered. Recommend a small "Account & Admin" group inside Onboarding,
   OR a section 10. Where do these go?
5. Northbeam Internal firewall: needs Mintlify authentication configured
   for that section. Separate setup task.
6. Release Notes: adopt Mintlify's changelog format now, or just park
   Northbeam 3.0 there for launch?

=====================================================================
WHAT THIS CHANGES vs THE CURRENT LIVE NAV
=====================================================================
The live site currently has 4 tabs (Get Started, Product Guides,
Integrations & Help, API Reference). This proposal is 9 sections. Biggest
moves:
- The channel guides move OUT of a separate "Integrations" area and INTO
  Onboarding > Connect channels.
- The dashboard screens split from the concepts: Platform (screens) vs
  Data and Terminology (concepts) vs Features (tools) vs Products (named
  offerings) become four distinct homes instead of one "Product Guides".
- Playbooks move to a gated Internal section.
- New: Release Notes, and named Product homes.

Building this is a docs.json rewrite (tabs/groups + page order) plus, for
Internal, Mintlify auth. No content rewriting needed beyond the two
Product gaps (Incrementality, UMM) and the changelog.
