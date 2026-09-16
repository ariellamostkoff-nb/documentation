ReadMe to Mintlify migration plan
Prepared 16 Sep 2026 for Christine. Owner tags: NB = Northbeam, MINT = Mintlify, BOTH = joint.

Answer to the headline question
Yes, a September launch is possible. Target cutover is Tuesday 29 September, with Wednesday 30 September as the buffer day. Two conditions have to hold:
1. Contract, security and legal are signed by Friday 19 September. Mintlify's own tracker listed these as incomplete on 28 August. Custom domain, the Slack agent and gated content all need a paid plan.
2. MVP keeps the docs.northbeam.io hostname and relies on redirects for every old URL. Rewriting the 163 links inside the dashboard code is post launch cleanup, not a launch blocker.
If the contract slips past Tuesday 22 September, cutover moves to the week of 5 October.

Where we already are
: 147 articles migrated into the Mintlify repo (github.com/ariellamostkoff-nb/documentation), restructured into nine tabs, redesigned, hosted at northbeam.mintlify.io behind Mintlify login.
: All 159 pages in the ReadMe sitemap either exist at the same path (120) or have a redirect (39).
: API reference: 17 endpoint pages generated from the four OpenAPI files (orders v1/v2, spend, data export).
: The dashboard links to 101 distinct docs paths (163 occurrences in 93 files, per Tyler's audit). 88 resolve today; 13 point at slugs that no longer exist anywhere, including on ReadMe.
: Content templates (concept, task, reference, process overview) exist. Four hidden test pages and one duplicate template folder need cleanup.
: Writers' brief listing the thin articles is in edits/thin-articles-for-writers.md.

Launch team
Christine Anderson : sponsor, go/no-go
Ariella Mostkoff : migration lead, IA, design, redirects, governance config
Tyler : content QA, dashboard link inventory, CS readiness
Scott : content QA, authoring pilot, Intercom/help center
Dan : engineering sign-off, Northbeam AI and llms.txt/MCP, dashboard URL sweep owner
Mintlify : Djibril (account), Marco (solutions) : plan tier, auth setup, custom domain, agent enablement

Timeline
Start : Wed 17 Sep 2026
Cutover : Tue 29 Sep 2026
Buffer : Wed 30 Sep 2026
Hypercare : Thu 1 Oct to Fri 9 Oct 2026

Milestones

M0 | Wed 17 Sep | Kickoff and scope lock | BOTH
Confirm MVP definition: 1:1 replacement of ReadMe public docs, same hostname, plus Mintlify governance, WYSIWYG and prompt authoring, Slack agent. Confirm launch team, meeting cadence (15 min daily standup through cutover), and this plan.
Test: none. Exit = plan accepted by Christine and Mintlify.

M1 | Fri 19 Sep | Commercial and access unblocked | BOTH
MINT: contract, security questionnaire, legal. Confirm plan tier and what it unlocks (see Governance note). Enable Slack agent and web editor seats.
NB: sign; add Tyler, Scott, Dan as editors; confirm who controls DNS for docs.northbeam.io and whether it is Cloudflare proxied.
Test: Tyler and Scott each log into the web editor, make a one line edit on a branch, and see the preview build.

M2 | Mon 22 Sep | DNS pre-staging | BOTH
Add the two Mintlify TXT verification records for docs.northbeam.io now. They do not affect ReadMe traffic; only the CNAME does. This removes propagation time from cutover day.
Test: both TXT records show verified in the Mintlify dashboard.

M3 | Tue 22 Sep | Content parity freeze | NB
Redirects for the 13 dead dashboard paths (pinterest, twitter/x, bliss point, saved views, update your dns, install the pixel, getting started, GTM install, purchase pixel, creative analytics walkthrough, openai ads). Anchor check on redirected channel guides: old step anchors land on the new split pages. Remove test pages, duplicate templates folder, stray "this is a change" text, root level interpreting-your-results moved under docs with a redirect. Tyler and Scott final read of the new and restructured articles (writers' brief); fix anything wrong, bolster later.
Test: automated broken link check on the repo; scripted request of all 159 sitemap URLs plus all 101 dashboard URLs against northbeam.mintlify.io, every one returns 200 after redirects; manual check of 20 anchors.

M4 | Wed 23 Sep | Governance MVP | BOTH
Flip the site from fully gated to partial authentication: every public group marked public, the Northbeam Internal tab stays gated. Internal access via Mintlify private authentication (Northbeam employees sign in with their Mintlify org account). Decide review mode for the web editor and agent: publish direct to main, or pull request required.
Test: logged out visitor sees all public tabs and search; hitting an Internal article prompts for login; an NB employee logs in and sees Internal; a customer cannot.

M5 | Thu 24 Sep | Authoring workflow live | BOTH
MINT: Slack workspace connected, @mintlify agent responding, agent connected to the documentation repo.
NB: authoring guide and short Loom from Ariella (Tyler's request): create an article from the WYSIWYG, from a prompt, from Slack; how the templates work; how to place a page in the nav.
Test: Scott creates an article from a prompt in Slack and it lands as a pull request or commit and builds; Tyler edits an existing article in visual mode and publishes; both render in the correct nav position.

M6 | Fri 25 Sep | Product, Intercom and AI integration | BOTH
NB: Intercom app id added to docs.json so the messenger loads on docs; Intercom help center and Fin sources pointed at the new site (Scott); Beamscope help-docs index in nb-api updated for the 13 dead paths; transactional email templates checked; llms.txt and MCP endpoint verified for Northbeam AI (Dan).
MINT: confirm llms.txt and MCP are served for the custom domain after cutover, not only the mintlify.io host.
Test: messenger opens on a docs page; an Intercom conversation link to a doc resolves; a Northbeam AI query returns a doc citation; Beamscope help links resolve on staging.

M7 | Fri 25 Sep | Marketing and external URL inventory | NB
Inventory every docs.northbeam.io link outside the product: northbeam.io site nav and footer, HubSpot and newsletter templates, sales and CS decks, Notion playbooks, support macros. Anything on a dead slug is fixed; anything on a live or redirected slug is left as is for MVP.
Test: click-through of the inventory list against northbeam.mintlify.io.

M8 | Mon 28 Sep | Launch readiness and go/no-go | BOTH
Full regression on northbeam.mintlify.io: nav, search, API playground on the 17 endpoints, mobile, dark mode, analytics tag, sitemap, 404 page, feedback widget. Export and archive the ReadMe project as backup. Go/no-go by Christine end of day.
Test: the checklist above, signed off by Tyler and Scott.

M9 | Tue 29 Sep | Cutover | BOTH
Change the docs.northbeam.io CNAME to Mintlify. Keep ReadMe running untouched until HTTPS is confirmed on the new host, then remove the custom domain from ReadMe. ReadMe stays on its readme.io subdomain, read only, for 30 days.
Test: docs.northbeam.io serves Mintlify over valid HTTPS; rerun the 260 URL sweep against production; Internal gate works; Intercom loads; a dashboard help link opens the right article.

M10 | Wed 30 Sep to Fri 9 Oct | Buffer and hypercare | BOTH
Watch Mintlify analytics for 404s and add redirects same day. Tyler and Scott triage any CS tickets about docs. Dashboard link rewrite PR (all 163 occurrences to new slugs) opened by engineering in this window.

Post MVP
: Content approvals before publishing. Today this is a pull request review on GitHub; a required-approver flow inside the editor is not in MVP.
: Audience gating for enterprise customers versus other customers. Needs OAuth or JWT single sign-on from the Northbeam app, which is an Enterprise plan feature plus engineering work from Dan's team.
: Full rewrite of dashboard and email links to new slugs (redirects carry MVP).
: Agent integrations with Notion, Jira, Linear and Google Drive (Enterprise plan).
: Bolster the thin articles per the writers' brief.
: Versioning, translations, changelog RSS, API playground prefilled per user.
: Cancel ReadMe after the 30 day read-only period.

Governance note for the plan tier decision
Mintlify offers four ways to gate content. Password (Pro or Enterprise) is one shared password with no per-user tracking. Private authentication (all plans) limits gated pages to members of the Mintlify org, which covers Northbeam employees. OAuth and JWT (Enterprise) give per-user sessions and groups, which is what customer segment gating requires. Gating is per page or per group, not per tab. Recommendation for MVP: private authentication on the Internal tab; decide on Enterprise when the customer gating work is scheduled.

Risks
: Contract timing is the only hard dependency on the date.
: DNS propagation can take up to 48 hours; pre-staging TXT records on 22 Sep reduces this to the CNAME change only. If Cloudflare proxies the domain, SSL mode must be Full (strict) and Always Use HTTPS off during issuance.
: Old anchors on channel guides that were split into step pages may land on the overview instead of the step. Fix is a per-anchor redirect or accepting the overview landing.
: The hosted site is currently fully gated. If partial authentication is misconfigured, the public docs go dark at cutover. M4 test covers this; M8 rechecks.
: ReadMe's API "Try it" behavior versus Mintlify's playground needs a side by side check on the orders and spend endpoints.
