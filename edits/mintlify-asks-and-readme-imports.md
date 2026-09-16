Part 1 : What we need from Mintlify to get up and running
For Djibril and Marco. Grouped by when we need it. Repo is github.com/ariellamostkoff-nb/documentation, site is northbeam.mintlify.io.

This week (by Fri 19 Sep)
1. Contract signed 16 Sep. Confirm any remaining security or legal paperwork is closed.
2. Confirm the plan tier and exactly what it unlocks for us: custom domain, partial authentication, private authentication for employees, Slack agent, web editor seats, API playground, Intercom integration. Tell us which of these need Enterprise.
3. Editor seats and dashboard access for Christine Anderson, Tyler, Scott and Dan, in addition to Ariella.
4. Custom domain: add docs.northbeam.io in the Mintlify dashboard and send us the two TXT record values (_acme-challenge and _cf-custom-hostname). Our zone is Google Cloud DNS, not Cloudflare proxied. We will add the TXT records on 22 Sep and the CNAME on 29 Sep.
5. A shared Slack channel between the two teams for the launch window, and a named contact for cutover day.

Next week (by Fri 26 Sep)
6. Authentication: help us move the site from fully gated to partial authentication with only the Northbeam Internal tab gated. Confirm how Northbeam employees get access under private authentication (are they org members, do they need seats, how are they invited and removed).
7. Slack agent: connect the Northbeam Slack workspace, confirm the agent is connected to the documentation repo, and set the review mode (pull request versus direct commit) once we decide.
8. Confirm the Mintlify GitHub App is what deploys the repo today, and whether connecting the Northbeam dashboard repo for agent read context is possible on our plan.
9. Intercom setup. What exactly do we configure on each side? On the Mintlify side we understand it is the Intercom app id in docs.json; confirm that and whether it needs the Enterprise plan. On the Intercom side, what does Northbeam set so that Fin and the help center answer from the new docs, and so that answers link to docs.northbeam.io rather than the mintlify.io address? Does the Mintlify messenger know who the logged in user is, and does it conflict with the built in assistant or feedback widget? Dan is building the NB AI plus Intercom flow (answer with a docs link, or say it does not know and open a ticket), so we need this working by Fri 19 Sep for testing.
9b. Product repo and links. The Northbeam app generates 163 links to docs.northbeam.io across 93 files, and our emails and marketing do the same. If we connect the product repo to Mintlify through the GitHub App, can the Mintlify agent find and update those links for us, or does it only read code for context and write to the docs repo? If it cannot, what do you recommend: rely on redirects at launch and have our engineers rewrite the links after, or something else?
10. llms.txt and the MCP server: confirm both are served on docs.northbeam.io after cutover, not only on the mintlify.io host, and what the MCP URL will be so Dan can point Northbeam AI at it.
11. Redirects: confirm whether URL fragments (anchors) are preserved through docs.json redirects, and whether wildcard redirects are supported. We have 79 redirects to test.
12. Analytics: which analytics integrations are available on our plan (Google Analytics, PostHog, Segment), and whether 404 reporting is available so we can watch redirects after cutover.
13. Images: 206 image references in 70 articles still load from files.readme.io. Confirm the recommended way to bulk host them (repo images folder versus Mintlify asset upload) and any size limits.
14. API reference: confirm the API playground works with our four OpenAPI files and the authentication scheme (Authorization plus Data-Client-ID headers), and whether we can hide the playground per endpoint.

Before cutover (by Mon 28 Sep)
15. A cutover checklist from your side: what you watch during DNS propagation, expected time to HTTPS, rollback steps.
16. Confirmation that the mintlify.io hostname keeps working after the custom domain is live, or redirects to it.
17. Support hours on 29 and 30 Sep.

Post MVP, for the roadmap conversation
18. Required approvers before publish inside the web editor.
19. OAuth or JWT for customer segment gating, and what Northbeam has to build on its side.
20. Agent integrations with Notion, Jira and Google Drive.
21. Versioning and changelog RSS.

Part 2 : What Ariella imports from ReadMe
Everything below is checked against the live ReadMe sitemap on 16 Sep 2026.

A. New articles not in the Mintlify repo (16)
Raw markdown is already downloaded for each. Convert to MDX, place in the nav, add to the parity manifest.
tracking-for-openai-ads : Tracking for OpenAI
tracking-for-paramount : Tracking for Paramount
tracking-for-shopmy : Tracking for ShopMy
purchase-pixel : Purchase Events (has a video)
northbeam-api-data-exports-overview : Data Exports
northbeam-api-orders-export : Orders Export
sales-page-export : Sales Page Export
orders-api-limits : Limits (replaces the old limits page)
northbeam-mcp : Connect Northbeam to Your AI Assistant
northbeam-mcp-server-faqs : Northbeam MCP Server FAQs
connect-northbeam-to-chatgpt : Connect Northbeam to ChatGPT
new-vs-returning-data-1 : First-Time and Returning Data
order-segmentation : Order Segmentation
purchases-or-orders-are-missing : Purchases or Orders Are Missing
dashboard-and-export-data-dont-match : Dashboard and Export Data Don't Match
why-northbeam-differs-from-another-platform : Why Northbeam Differs From Another Platform

B. Articles in the repo that changed on ReadMe after import (3)
Diff and port the ReadMe changes.
setting-up-apex : Enable Apex for Meta
apex-faqs : Apex FAQs
setting-up-a-meta-custom-attribution-campaign : Set up a Meta Custom Attribution Campaign

C. Articles modified on ReadMe since the 21 Jul audit (63)
Most dated 26 and 27 Aug. Run a content diff of each against its Mintlify copy and port anything added. Full list is produced by the sitemap script; the biggest risk items are the channel guides (Meta, Google, TikTok, Klaviyo, Pinterest, Snapchat, Microsoft, Impact, Attentive, Amazon, and the rest), the data export pages, and troubleshooting-tracking-issues.

D. API reference
One new endpoint on ReadMe is missing from our OpenAPI files: POST data-export orders (slug post_data-export-orders). Add it to the data export spec so the reference page and playground generate. The other 17 endpoints match.

E. Images (206 references in 70 articles)
Download every files.readme.io asset referenced in the repo, store under images, rewrite the references. These break the day the ReadMe account is closed, so this is a launch item, not cleanup.

F. Redirects
Add redirects for the 13 dead dashboard slugs: 5-install-the-northbeam-pixel, creative-analytics-walkthrough, getting-started-with-northbeam, google-tag-manager-installation, purchase-pixel (resolved by import A), saved-views-and-breakdowns, setting-up-pinterest-ads-for-northbeam, tracking-for-bliss-point-media, tracking-for-openai-ads (resolved by import A), tracking-for-twitter-ads, update-your-dns. Then rerun the sweep over the 178 live sitemap URLs and the 101 dashboard URLs.

G. Not needed
ReadMe versions: only v2.2 is public, nothing else to carry.
ReadMe changelog, recipes, custom pages, glossary: none exist on the live site.
Search, feedback widget, and the API playground are Mintlify native and need configuration, not import.

H. Archive
Export the full ReadMe project before cutover and keep it with the audit package as the rollback copy.
