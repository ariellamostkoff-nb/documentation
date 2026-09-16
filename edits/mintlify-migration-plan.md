ReadMe to Mintlify launch plan
Revised 16 Sep 2026. Soft launch Mon 21 Sep, launch Wed 23 Sep. Owner tags: NB, MINT, BOTH.

MVP for 23 Sep
1. New design and structure live on docs.northbeam.io.
2. No broken connections: every link the app, emails, Intercom and marketing generate still lands on a page.
3. Content can be updated and added through prompts and templates.
4. Permissioning controls who sees which sections.
Everything else rolls out through October.

Team
Christine Anderson : sponsor, go/no-go (out 17 and 18 Sep)
Ariella Mostkoff : lead, import, redirects, design, permissions config
Tyler Yee : link inventory, testing, CS readiness
Scott : authoring pilot, Intercom help center, testing
Dan : NB AI plus Intercom flow, DNS changes, dashboard links
Mintlify (Djibril, Marco) : plan tier, auth, custom domain, agent

Day by day

Tue 16 Sep | Plan approved, asks sent | BOTH
Contract signed. Send Mintlify the asks list. Request TXT record values for docs.northbeam.io and seats for Tyler, Scott, Dan and Christine.
Test: none.

Wed 17 Sep | Import and DNS pre-stage | NB, MINT
NB: add the two TXT records in Google Cloud DNS (Dan). Import the 16 new ReadMe articles, port the 3 changed Apex articles, add redirects for the 13 dead dashboard slugs, add the missing Orders export endpoint, start image rehosting (206 references).
MINT: custom domain added in dashboard, TXT values sent, seats for Tyler, Scott, Dan, Christine.
Test: TXT records verified in Mintlify dashboard; broken link check on the repo passes.

Thu 18 Sep | Permissions and authoring | BOTH
MINT: site switched from fully gated to partial authentication with only Northbeam Internal gated; Slack agent connected to the repo.
NB: mark every public group public; confirm employees can sign in; authoring guide and Loom for Tyler and Scott; Intercom app id added to docs.json.
Test (MVP 3 and 4): logged out visitor sees all public tabs, Internal prompts for login, employee sees Internal, a customer account does not. Scott creates an article from a prompt in Slack and it publishes; Tyler edits an article in the visual editor from a template and it publishes in the right nav spot.

Fri 19 Sep | Parity freeze and connection tests | BOTH
NB: scripted sweep of all 178 live ReadMe URLs and all 101 dashboard URLs against northbeam.mintlify.io, every one returns a page; anchor spot check; marketing link inventory (site, HubSpot, decks, macros) checked; Beamscope help index and email templates checked on staging.
NB AI plus Intercom test with Dan (Tyler and Ariella): a question with a docs answer returns a Mintlify link that opens the right article; a question with no docs answer says it does not know and creates a ticket; links inside Intercom conversations resolve.
Go or no-go for soft launch, Ariella and Tyler, Christine by message.
Test (MVP 2): the sweep and the two AI scenarios above pass.

Mon 21 Sep | Soft launch | BOTH
Morning: change the docs.northbeam.io CNAME to cname.mintlify.builders. TTL is 30 minutes. ReadMe stays fully live on its readmessl.com host with its custom domain setting untouched. Nothing is deleted or cancelled.
Once HTTPS is valid: rerun the URL sweep against production, check Internal gate, Intercom messenger, an app help link, an NB AI answer link. Tell CS and support internally.
Test (MVP 1 and 2): docs.northbeam.io serves the new site over valid HTTPS; sweep passes; permissions and Intercom behave as on Thu.

Tue 22 Sep | Hypercare day | NB
Watch 404s and support tickets, add redirects same day. Recheck NB AI links with Dan. Final go or no-go for the announcement by end of day.
Rollback if needed (see below).

Wed 23 Sep | Launch | BOTH
Customer announcement. Marketing links pointed at new pages where slugs changed. Mintlify confirms the mintlify.io host redirects to the custom domain.
Test: announcement links open; sweep rerun once more.

Rollback plan for 21 and 22 Sep
Trigger: the new site is down, HTTPS fails, or the sweep shows widespread 404s that cannot be fixed with redirects within an hour.
Steps: 1. Dan changes the CNAME back to northbeam-customer-sucess-175385b1.readmessl.com. 2. Within 30 minutes docs.northbeam.io serves ReadMe again; nothing on ReadMe was changed so no restore is needed. 3. Ariella posts in the shared Slack channel and to CS. 4. The new site stays reachable at northbeam.mintlify.io for fixing. 5. Retry the CNAME once the cause is fixed.
Preconditions: ReadMe project active with custom domain configured until at least 23 Oct; full ReadMe export archived before 21 Sep; Dan or a backup has Google Cloud DNS access on both days.

Roll out after launch, through Oct 23
Week of 28 Sep: content diff of the 63 articles modified on ReadMe since July; finish image rehosting if not complete; dashboard link rewrite PR to new slugs; remaining anchor redirects.
Week of 5 Oct: writers bolster the thin articles; llms.txt and MCP on the custom domain confirmed for NB AI; analytics and 404 reporting.
Week of 12 Oct: review mode decision (pull request required or direct publish); enterprise customer gating scoped with Mintlify (OAuth or JWT) and Dan.
Week of 19 Oct: ReadMe export final, custom domain removed from ReadMe, ReadMe cancelled after 23 Oct.
Post MVP backlog: approvals before publish, Notion and Jira agent integrations, versioning, changelog RSS.

Risks
Mintlify turnaround on TXT values, partial authentication and the Slack agent by Thu 18 Sep: each day late moves soft launch day for day.
Ariella is the single owner of import, redirects and config on 17 and 18 Sep; Tyler and Scott take testing and authoring so those days stay parallel.
Anchors on split channel guides may land on the overview rather than the step; acceptable for MVP, fixed in the week of 28 Sep.
Partial authentication misconfigured would gate the public site; caught by the Thu 18 and Mon 21 tests.
