// before-slot transform script (JavaScript) — switch the execution model by plan mode.
//
// Mounted on the entry model in the console; runs before routing.
// The engine is sandboxed (no network, no filesystem) and applies live — no redeploy.
//
// Contract:
//   transform(body, context) -> body
//     body     the request JSON in the *client's* format, before protocol translation
//     context  read-only request metadata: sourceProtocol, useModel(name), ...
//
// Return the (possibly rewritten) body. Returning it unchanged is a no-op.

function transform(body, context) {
    // Only our Anthropic-facing clients get the plan/execute split; leave everything
    // else on the model the caller asked for.
    if (context.sourceProtocol !== "Anthropic") {
        return body;
    }

    const EXEC_MODEL = "qwen3.8-max"; // a model name configured in the gateway

    const PLAN = /plan mode is active/i;
    const EXIT = /exited plan mode/i;

    // Take the last marker-bearing message: a later marker wins over an earlier one.
    const messages = body.messages || [];
    for (let i = messages.length - 1; i >= 0; i--) {
        const s = JSON.stringify(messages[i].content || "");
        const inPlan = PLAN.test(s);
        const exited = EXIT.test(s);
        if (inPlan || exited) {
            // Out of plan mode -> switch execution to the cost-efficient model.
            if (exited || !inPlan) context.useModel(EXEC_MODEL);
            return body;
        }
    }

    // No marker anywhere: treat the turn as execution.
    context.useModel(EXEC_MODEL);
    return body;
}
