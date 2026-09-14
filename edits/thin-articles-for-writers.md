Thin articles to bolster
Articles created or split during the August 2026 restructure that need a content writer's pass. Paths are under docs/. Grouped by what is missing, thinnest first within each group.

1. Placeholder pages (currently say "being built out")
journey/northbeam-ai : one link to the Claude connection guide. Needs: what Northbeam AI is, what questions it answers well, what it cannot do, how to verify an answer.
journey/set-up-and-track-alerts : one link to the ROAS-drop use case. Needs: what alerts exist, how to subscribe, what a triggered alert looks like, what to do when one fires.
changelog : a single "docs refresh" entry. Needs product to own it and add an entry per release.

2. Channel overviews that lost their intro in the split
These open on a fragment ("Spend and Impressions, which enables...") or a bare bullet list because the lead-in sentence stayed with the old page. Each needs: one paragraph on what the integration does, what data Northbeam ingests (spend, impressions, clicks), which attribution models it supports, and any prerequisites.
channels/rakuten/overview
channels/tradedesk/overview
channels/rokt/overview
channels/vibe/overview
channels/mntn/overview
channels/tatari/overview : jump list of steps only, plus the Streaming vs Linear notice
channels/keynes/overview

3. Confirm tracking pages : the same generic block on 19 channels
amazon, applovin, attentive, google, impact, keynes, klaviyo, liveintent, meta, microsoft, pinterest, rakuten, rokt, snapchat, tiktok, tradedesk, universal, vibe, x
Each currently says "check UTMs, check the connection" with two links. Needs per channel: where in Northbeam the channel appears once data flows, how long the first data takes, what a healthy row looks like (spend present, clicks present, attributed orders), and the one or two failure modes specific to that channel. MNTN, Shops, and Tatari already have real content and can serve as the model.

4. Insert the UTMs pages with no procedure
channels/rokt/insert-the-utms : "contact your ROKT account lead." Needs: what parameters the lead injects, how to confirm they landed, what to do if the lead is unresponsive.
channels/tradedesk/insert-the-utms : video only. Needs the written steps.

5. Use cases : link hubs, not procedures
All twelve follow the Best for / Steps / What to expect / Related anatomy, but each step is one sentence plus a link, and "What to expect" is a single line. Needs per article: the actual clicks inside each step, the setting values to use (model, window, accounting mode), a concrete example of the output, and what a bad result looks like. Thinnest six:
use-cases/ask-your-data-from-claude
use-cases/evaluate-creative
use-cases/send-attribution-to-meta
use-cases/report-across-stores
use-cases/build-a-weekly-report
use-cases/pull-data-into-your-warehouse
The other six (validate-with-incrementality, choose-an-attribution-model, audit-tracking-before-a-big-sale, compare-channels-fairly, reconcile-northbeam-vs-shopify, diagnose-a-roas-drop) have more substance but still lack examples.

6. Journey pages : one sentence per stage
journey/get-started : also contains a stray test phrase "this is a change" from the web editor.
journey/understand-your-platform
journey/integrations
journey/watch-the-competition
journey/design-your-dashboard
journey/utilize-advanced-features
These are meant to be short, but each stage should say why it matters and what "done" looks like before linking out.

7. Section overviews : link lists only
overviews/features
overviews/products
Each needs a framing paragraph and one line per item explaining when you would reach for it.

8. New API pages written from the OpenAPI spec, not yet reviewed by the API team
authentication : where keys live, header names. Needs: key rotation, scopes if any, what an auth failure returns.
environments : UAT vs production base URLs. Needs: confirmation of the production URL (open audit marker on using-the-api), how UAT data differs, rate limits.

Not on this list on purpose
Channel FAQ, connect-the-account, and most insert-the-utms pages carried their full text over from the original guides. Landings and chapter indexes are designed pages, not prose. The four templates are hidden.
