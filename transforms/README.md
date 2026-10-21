# Transform scripts

A sandboxed JavaScript engine rewrites request and response JSON inside the gateway.
Edit the script in the console; it applies live, with no redeploy.

| File | Slot | What it does |
|---|---|---|
| `before-slot-transform.js` | before request | Routes planning turns to a top-tier model and execution turns to a cheaper one, by scanning the conversation for a plan-mode marker. |

## Slots

- **before request** — sees the request in the client's format, before protocol translation.
  `context.useModel(name)` switches the whole route: base URL, protocol and credentials together.
- **after request** — sees the request in the upstream provider's format.
- **response** — sees the response before it is translated back.

## Rules

- The sandbox has no network and no filesystem access.
- A script that throws is handled by the route's fail-open / fail-closed setting — decide
  which one you want before mounting it on production traffic.
- `transform(body, context)` must return the body. Return it unchanged for a no-op.
