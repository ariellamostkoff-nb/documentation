NORTHBEAM DOCS : ALL RECOMMENDED EDITS FROM THE AUDIT
Generated from the 159-page audit (v2.2). Instructions only, ready to work from.
Now living in the Mintlify repo at edits/ for version tracking.

Revision log:
- 2026-08-12 : retired the "Start Here" section (see STRUCTURE CHANGE
  below). Orientation moves to the homepage + one Quickstart.

How to use:
- Read STRUCTURE CHANGE first: it changes what section 1 becomes.
- Do PART 1 first (the 12 high-priority fixes).
- PART 2 is batched sweeps: fastest way through the mechanical fixes.
- PART 3 is every page edit, grouped by target section.
- PART 4 is the 19 merges. Rule for every merge: move any unique content
  into the target page, then add a redirect (docs.json).
- Done bar for every page: no false facts, no dead links, no video-only
  info without a text summary.

=====================================================================
STRUCTURE CHANGE : RETIRE "START HERE" (2026-08-12)
=====================================================================
"Start Here" as a named nav section is dated. Modern docs put
orientation on the homepage, not in a folder. So the section dissolves
and its job moves to two places:

1. The homepage (index.mdx) does the orienting:
   - The pitch that was "What is Northbeam?" becomes the hero + a short
     intro block on the homepage.
   - Add persona paths on the homepage ("I'm setting up Northbeam" vs
     "I'm integrating with code") so a new reader self-routes.
2. One Quickstart page, framed by action, is the only survivor as a
   standalone page. Title it for the outcome, e.g. "Get started:
   connect Northbeam in about 15 minutes." Not "Start Here", not
   "Getting Started".

Per page:
- What is Northbeam? : fold the substance into the homepage hero + a
  1-paragraph Introduction at the top of the homepage. Do not keep it as
  a separate section page.
- Navigating Northbeam / Ramp-Up Guide : DELETE the "how to navigate the
  docs" framing (a page that explains the nav is a smell). Keep any
  genuinely useful first-week content and move it into the Quickstart.
- New to the Team : merged away already (PART 4).

Net: section 1 is no longer a shelf. Nav becomes the homepage + one
Quickstart + the 7 content sections. Everything below that referred to
"Start Here" is superseded by this block.

=====================================================================
PART 1 : HIGH PRIORITY (do these first)
=====================================================================

1. Metrics Explorer Home Page
   Fix "correlation is equal to causation" : change to "is NOT equal to".

2. Using the API
   State the real base URLs: api.northbeam.io/v2 (Orders), /v1 (Spend),
   /v1/exports (Data Export). Remove the docs URL presented as "the
   production API". Document UAT per API or remove the UAT promise.

3. Setting Up Multiple Stores or Regions
   Decision Summary table: two multi-domain rows say Option 2B.
   Change both to Option 2A.

4. Attribution Home Page
   Verify or fix the swapped funnel labels (Demand Capture vs Demand
   Generation). Expand the 170-word stub: metric table + link per tile.

5. Why is my FB ROAS so much lower in Northbeam
   Fill the literal "#" placeholders with real example numbers.
   Then merge with the other FB ROAS page (see PART 4).

6. Product Analytics
   Delete the published internal note "NOTE: Should we put in a visual
   for the above?" Add the visual it asks about.

7. Upsert orders V1 endpoint (post_orders)
   Add a deprecation banner + V1 to V2 migration note. Repoint the 7
   guide deep-links to the V2 endpoint. Fix the pagination link on
   addorderaliases that leads into the deprecated section.

8. 9. Integrations and UTMs
   Fix 2 dead links (Pinterest and Bliss Point renamed slugs) and the
   attentive-copy 404. Fix "TitkTok".

9. Tracking for Non-Integrated Channels
   Remove Impact and LiveIntent from the non-integrated list (both have
   native guides now). Fix the checklist reference to a Step 2 this page
   does not have.

10. Tracking Ads using Off-Domain Sites
    Write the missing "Option 2 : Pixel Placement" section. It is
    promised and referenced but does not exist.

11. Tracking for TradeDesk
    Write the missing scheduled-report step (referenced twice, absent).
    Write text steps for the UTM video (2:09 Loom is the only carrier).

12. Northbeam's Integrations (integration matrix)
    Rebuild the image as a real table (searchable, accessible,
    copyable). Add an integration-type column.

=====================================================================
PART 2 : BATCHED SWEEPS (mechanical, do each in one sitting)
=====================================================================

SWEEP A : DEAD LINKS (verified 404s)
- accounting-modes : /docs/northbeam-pixel : point to /docs/purchase-pixel
- northbeam-data-sources : /docs/northbeam-pixel : same fix
- northbeam-data-sources : What's Next link (FB/Northbeam reporting page) : remove or point to differences-ad-performance
- metrics-explorer-best-practices-7-tips : /docs/best-practices-1 : point to best-practices-by-teams-and-departments
- integrations-and-utms + 8-append-our-utms : setting-up-pinterest-ads-for-northbeam : point to tracking-for-pinterest-ads
- integrations-and-utms + 8-append-our-utms : tracking-for-bliss-point-media : point to tracking-for-bliss-point-by-tinuiti
- integrations-and-utms : working-tracking-for-attentive-copy : point to working-tracking-for-attentive

SWEEP B : LEGACY HARDCODED LINKS
Replace northbeam-customer-sucess.readme.io links with relative /docs/
paths on: northbeam-metrics-101, order-tags, tracking-for-influencers,
working-tracking-for-attentive, troubleshooting-tracking-issues,
differences-in-ad-data, differences-in-unattributed-data.
Replace /update/docs/ editor links (302 to a login page) on: orders-api,
tracking-for-universal.
Repoint working 301s to live slugs: clicks-views-enhanced links (on
navigating-northbeam, case-scenario-clicks-views) to
clicks-deterministic-views; orders-api-1 (on add-orders) to orders-api.

SWEEP C : TYPO AND ARTIFACT PASS (exact strings)
- "Tartari" : Tatari (navigating-northbeam)
- "TitkTok" : TikTok (integrations-and-utms)
- "utm_mediun" : utm_medium (tracking-for-snapchat-ads)
- "add our the end" : add ours to the end (tracking-for-snapchat-ads)
- "Norhtbeam" : Northbeam (email-sms-retention, what-is-northbeam-mta-methodology)
- "Northeam" : Northbeam (add-spend, northbeam-data-sources)
- "CFOS" : CFOs (executive-team)
- "Media Efficiency Radio" : Media Efficiency Ratio (executive-team)
- "about are best practices" : about our best practices (executive-team)
- "$30,0000" : $30,000 (offline-channel)
- "optionalL" : optional (order-definition)
- "Key Takeways" : Key Takeaways (differences-ad-performance)
- "diving" : divide or intended word (frequently-asked-questions)
- "oder" : order, "each dashboards" : each dashboard (how-does-northbeam-track-orders-and-ads)
- "CVS" : CSV, "platforns" : platforms (what-is-northbeam-model-comparison-tool)
- "please to contact" : please contact (tracking-for-rakuten)
- "blind posts" : blind spots, fix mid-word bold split "upper-funne l" (whats-the-difference-between-organic-vs-unattributed)
- "not currently not supported" : remove one "not" (setting-up-custom-goals)
- "we'd know to hear" : we'd love to hear (new-to-northbeam, before merge)
- literal ** artifacts : remove (link-dns heading, add-pixel code span, tracking-for-snapchat-ads, tracking-for-x-ads)
- stray "\" artifact : remove (guide-to-troubleshooting-pixel-tracking)
- "3-Step Process" : 4 steps listed, fix the count (non-integrated-channel-setup)
- "+ADD TITLES" : +ADD TILES (overview-page)

SWEEP D : STALE BANNERS AND DATES
- tracking-for-mntn : remove the "currently being updated" banner (8 months old) and finish or cut the promised rewrite
- northbeam-apex : update the three "planned for June 2026" claims (date passed) and "coming soon" A/B test line
- lookback-windows : rewrite "now allows" launch phrasing as evergreen
- applovin : date or remove "excited to announce"

SWEEP E : CONTACTS AND CTAS
- the-media-buyer-newsletter : fix schemeless signup links (they resolve to a broken docs path); replace personal email with a team address
- guide escalations : replace any personal email with the named support channel

SWEEP F : HEADING HYGIENE (site-wide)
- Demote body H1s to H2/H3 (worst: order-tags with 9, non-shopify-installation, new-to-northbeam, guide-to-troubleshooting-pixel-tracking, tracking-for-shops)
- Remove markup nested inside headings; it renders "[object Object]" skip links (navigating-northbeam, best-practices hub, FAQ hub, manage-breakdowns, facebook-utms-for-legacy-platforms, several channel guides, order-definition, pixel troubleshooting)

SWEEP G : VIDEO MINIMUMS (text summary required where video is the only carrier)
- checking-utm-tracking : write text steps for both Looms
- checking-api-connections : write the short flow as text
- ad-accounts : write the add/remove account steps (10 guides depend on this one Loom)
- sales : metric table + text walkthrough
- orders-tracking : write out what the video shows
- what-is-northbeam-model-comparison-tool : numbered steps + screenshots
- manage-breakdowns : write the custom-breakdown steps
- tracking-for-tradedesk : Step 2 text steps
- add-spend : text summaries for all three Looms
- new-to-northbeam (or merged target) : one-paragraph UI tour summary

SWEEP H : OWNERSHIP (DROPPED 2026-08-12)
Not doing page-level owner/review-date frontmatter. Git history covers
who-changed-what. Skip this sweep.

=====================================================================
PART 3 : PER-PAGE EDITS BY TARGET SECTION
(merges are in PART 4; keep-pages with no edits are not listed)
=====================================================================

1 . START HERE  (RETIRED : see STRUCTURE CHANGE at top)
- Section dissolves. Orientation moves to homepage (index.mdx) + one
  action-framed Quickstart.
- Quickstart page : build from the Navigating Northbeam / ramp-up
  source, but drop the "how to read the docs" framing; keep first-week
  actions only. Fix the Tartari typo, repoint the 301 link, remove the
  broken skip links while you are in it.
- What is Northbeam : fold into the homepage hero + intro paragraph.
- New to the Team : merged away (PART 4).

2 . SET UP AND IMPLEMENT
- Confirm Setup Requirements : replace legacy support link; demote body H1s; move multi-dashboard decision content to Setting Up Multiple Stores
- 2. Invite Team : fix broken dashboard.northbeam.io link; keep ONE users procedure, cross-link Adding/Removing Users
- 3. Business Information : copyedit pass
- 4. Currency : match tab title to H1; cross-link Changing Currency
- 6. Link DNS : add per-provider steps (GoDaddy, Cloudflare); remove Google Domains; fix ** in heading
- 7. Pixel and Event Tracking : add 1-line text summary + platform links under the Loom; fix ** in code span
- Additional Events : fix fireCustomGoal second-argument description (copy-pasted from purchase event); document the object properties; defer React Router example to Page View Events
- All Other Platforms Installation : demote body H1s; fix blank headings and grammar; repoint 3 order-API links to V2
- Custom Goals : fix double negative
- 10. Add Spend : text summaries for 3 Looms; fix Northeam typo
- 8. Add Orders : add SFTP and Amazon sync to the router list; repoint orders-api-1 link
- 8b. Order Tags (onboarding) : de-duplicate against Order Tags; fix garbled heading; fix order-tags-1 slug
- All Other Platforms Overview : complete the truncated sentence; update stale section name; add real Data Export links
- Order Tags : make canonical over 8b-8d; demote 9 body H1s; replace readme.io links; fix duplicated phrase
- Shopify (order sync) : retitle from bare "Shopify"; fix brand/business link label; add required permissions + historical sync window
- Subscription Analytics : defer tag mechanics to Order Tags; write the tag-filter check sub-steps
- Multi-Dashboard Setup with Configurators : de-duplicate the two Setup Process H2s
- Setting Up Multiple Stores or Regions : fix Option 2B to 2A (2 rows); absorb the 3 config pages with redirects

3 . CONNECT YOUR CHANNELS
- 9. Integrations and UTMs : fix dead links + TitkTok; absorb Append UTMs child page
- Tracking for Amazon : fix duplicate Step 1 heading; repoint broken TikTok-guide link
- Tracking for AppLovin : add Input/Output table + metric scope; date the announcement; rename slug to tracking-for-applovin
- Tracking for Attentive : fix reversed Input/Output columns; drop "working-" slug + 301; replace readme.io link; fix missing-space typos
- Tracking for Microsoft Ads : fix Error 106 pointing at the wrong requirement number; fix App ID bold-split
- Tracking for Pinterest Ads : resolve the 30-day vs 7-day window contradiction with the integration owner, then state one
- Tracking for Snapchat Ads : fix ** artifacts and typos; use shared text for add/remove account steps
- Tracking for Universal : fix C+DV expansion to "Clicks + Deterministic Views" (2 places); replace /update/ preview link
- Tracking for X Ads : retitle Twitter leftovers (sheet + Loom label); write Builder-sheet text steps; fix ** placeholders
- Tracking for Bliss Point by Tinuiti : add where to find AWS keys; expand the 2-step stub onto the standard template
- Tracking for MNTN : remove stale banner; finish the promised rewrite
- Tracking for Rakuten : fix nb_creative_id row (copy-paste of the publisher_sid row); fix "please to contact"
- Tracking for Tatari : add missing Step 4 to the page ToC; fix dead step-4 anchor
- Tracking for TradeDesk : write the missing scheduled-report step; write UTM text steps
- Non-Integrated Channel Setup : fix the 3-step/4-step count; trim overlap with the parent page
- Integration matrix : rebuild as a real table; add integration-type column
- Shops Tracking : replace Meta screenshots inside the TikTok FAQ; demote H1s; consider re-homing beside Third-Party Checkouts
- Tracking Ads using Off-Domain Sites : write the missing Option 2 Pixel Placement section
- Tracking for Non-Integrated Channels : remove Impact + LiveIntent from the list; fix the checklist Step 2 reference; absorb Influencers page

4 . UNDERSTAND YOUR DATA
- Accounting Modes : fix northbeam-pixel 404; refresh 2022-era screenshots
- Attribution Models : fix minor typos; use the glossary definitions instead of restating them
- Attribution Windows : resolve the 60-day contradiction (in the table, missing from the availability list); fix the "$" cell
- Lookback Windows : evergreen the launch phrasing
- Northbeam Metrics 101 : fix mislabeled column, empty bullets, stray ")"; replace readme.io URL; long-term, convert to glossary entries
- Northbeam's Data Sources : add Orders API + SFTP to the Backend table; fix Northeam typo; fix 2 dead links
- The Media Buyer Newsletter : fix signup links; replace personal email
- Organic vs Unattributed : fix bold split and blind posts typo; make this the canonical unattributed answer
- What is a good/bad number : answer the title question; add a benchmarks/heuristics section
- How does Northbeam track Orders and Ads : fix oder/each dashboards; replace the duplicated unattributed-causes list with a link to the canonical page
- Interpreting non-click channels : grammar pass
- Case scenario Clicks+Views vs Clicks-Only : repoint the 301 link

5 . USE THE PLATFORM
- Attribution Home Page : verify/fix funnel labels; expand the stub (metric table + per-tile links)
- Creative Analytics : add current-UI screenshots; fix the guide-order contradiction with Orders
- Northbeam 3.0 : add screenshots; turn the renames into glossary version notes and link them
- Orders : write the page (rewrite; video-only today); fix the contradictory ending
- Overview Home Page : link Academy definitions instead of restating; fix +ADD TITLES; update to 3.0 names
- Product Analytics : delete the internal note; add the visual
- Sales : write the metric table + walkthrough; update 1.0 names
- Metrics Explorer : fix the correlation sentence; label for 3.0
- Metrics Explorer Best Practices : fix the What's Next 404
- Model Comparison Tool : write numbered steps + screenshots; fix CVS/platforns
- Manage Breakdowns and Saved Views : cover Saved Views (in the title, absent); write custom-breakdown steps; fix skip links
- Northbeam Apex : update the June 2026 claims; split the 4,290-word page into concept + tasks
- Email/SMS/Retention Team : rewrite the garbled attribution-model recommendation; fix Norhtbeam's
- Executive Team : fix CFOS, Radio, about-are typos
- Paid Search Team : give the Model Comparison Loom context or remove it (duplicates the tool page)
- Offline Channel : fix $30,0000

6 . DEVELOPERS AND API
- Errors : add a status-code + error-payload table
- Order Definition : fix optionalL + the garbled sentence; replace readme.io links; fix skip link
- Orders API guide : absorb Authentication, Getting Started, Limits; fix the /update/ editor link; replace legacy subdomains
- Using the API : real base URLs (see PART 1)
- Fetch orders V1 : deprecation banner + migration note
- Upsert orders V1 : deprecation banner + repoint 7 deep links + fix pagination trap
- Spend API guide : de-duplicate the intro restated in Add Spend
- Spend Best Practices and Limits : page says "orders" throughout; rewrite in spend terms
- List spend records (daily + hourly) : fill empty descriptions; fix garbled parameter prose and the required-flag contradiction; differentiate the two titles
- Upsert spend records (daily + hourly) : fill empty descriptions; expand collapsed schemas
- Delete spend record (daily + hourly) : fill empty descriptions; differentiate titles
- Exporting To GCS : say where to input/validate the bucket; fix the boilerplate subtitle
- Exporting To S3 : fix the boilerplate subtitle

7 . TROUBLESHOOT AND FAQ
- Checking Ad Platform Connections : write the flow as text steps
- Checking UTM Tracking : write text steps for both Looms; single-source with Troubleshooting Tracking Issues
- Troubleshooting Pixel Tracking : de-duplicate the inline ToC; demote H1s; remove the stray backslash
- Troubleshooting Tracking Issues : text alternative to the 9.6-minute Loom; replace readme.io link
- Differences in Ad Performance : fix Takeways; defer the FB ROAS answer to the merged canonical page
- Differences in Ad Spend : complete the truncated sentence; refresh the integrated-platform list
- Differences in Unattributed Data : verify the Shopify App ID table; fix the duplicated Draft Orders phrase; replace 3 readme.io links; absorb the FAQ twin
- Frequently Asked Questions : convert to a curated map (question + one-line answer + link); fix typos and anchors
- Onboarding FAQs : add the Shopify-match page to the list; publish or unlink the nav-hidden differences-in-total-revenue page
- Blotout vs Northbeam : resolve the TL;DR contradiction on first-party pixel tracking; re-verify the competitive claims

8 . MANAGE AND AI ACCESS
- Adding / Removing Ad Accounts : write the text steps once here; every guide links or transcludes this page
- Adding / Removing Users : rename the -copy slug + 301; reconcile with 2. Invite Team (keep one procedure)
- Changing Currency : rename the -copy-1 slug + 301; retitle properly (it is a currency FAQ on a cloned users slug)

=====================================================================
PART 4 : THE 19 MERGES
(move unique content to the target, then 301 the old URL)
=====================================================================

- New to the Team : into the Quickstart (formerly "into Navigating Northbeam")
- 1. Welcome to Northbeam : into What To Expect During Implementation
- Dashboard Access : into the implementation journey pages
- 5. Add Domain : into 6. Link DNS
- Shopify Overview : into What To Expect During Implementation
- Multi-region configuration : into Setting Up Multiple Stores or Regions
- Multi-business configuration : into Setting Up Multiple Stores or Regions
- Multi-domain configuration : into Setting Up Multiple Stores or Regions
- Append Northbeam UTMs (8/9) : into 9. Integrations and UTMs
- Tracking Influencer Performance : into Tracking for Non-Integrated Channels
- Influencer (best practices page) : into the merged influencer section
- What is Northbeam's MTA Methodology + Why is it better than internal platforms : merge the pair into ONE methodology page (keep the $100 journey example once)
- My FB ROAS is 0.7 + Why is my FB ROAS so much lower : merge the pair into ONE FB ROAS page (fill the # placeholders first)
- Why is so much of my revenue unattributed : into Differences in Unattributed Data
- Authentication : into the Orders API guide
- Getting Started (API) : into the Orders API guide
- Limits (API) : into the Orders API guide

=====================================================================
COUNTS
=====================================================================
- 159 pages audited : 93 updates, 19 merges, 2 rewrites, 45 keeps
- After merges : 140 pages
- Keeps needing zero work : 45 (verify owner + review date only)
