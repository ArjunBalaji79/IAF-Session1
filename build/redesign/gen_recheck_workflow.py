import json
qa = json.load(open("qa_recheck.json"))
JS = r'''export const meta = {
  name: 'recheck-iaf-fixes',
  description: 'Verify the fixed/changed slides resolved their QA issues with no regressions',
  phases: [{ title: 'Recheck', detail: 'confirm each changed slide is fixed and clean' }],
}
const QA = __QA__;
const SCHEMA = {
  type: 'object', additionalProperties: false, required: ['verdicts'],
  properties: { verdicts: { type: 'array', items: {
    type: 'object', additionalProperties: false, required: ['src', 'resolved', 'severity'],
    properties: {
      src: { type: 'string' }, resolved: { type: 'boolean' },
      severity: { type: 'string', enum: ['ok', 'minor', 'major'] },
      issues: { type: 'array', items: { type: 'string' } },
      fix: { type: 'string' },
    } } } }
};
const RULES = `
You are doing a FINAL verification of slides that were just FIXED in a redesigned NGO AI-training deck.
For each slide you get: src id, source_text (original ground-truth lines), records (what was built), new_png (path — READ it).
Read each new_png and confirm:
1. FIDELITY: all substantive source_text present & readable (template chrome like "IMPACT AI FOUNDRY" headers and lone quote glyphs are intentionally dropped — not a problem). For split slides (src like 59a/59b, 67a/67b) the two halves TOGETHER should cover the source; judge each half only for what it should contain.
2. NO OVERFLOW: nothing runs off the slide, overlaps a corner motif, or collides with the footer.
3. LEGIBLE: comfortable to read on a projector (not cramped/tiny).
4. CLEAN: gold rule not striking through the title; ghost watermark numerals subtle and not split/cut.
Set resolved=true if the slide is clean and faithful. severity: "ok" if good, "minor" for tiny polish, "major" if a real problem remains (dropped content, overflow, unreadable). Give a specific "fix" only if not resolved.
OUTPUT: { "verdicts": [ {one per slide} ] }
`;
phase('Recheck');
const CHUNK = 7;
const chunks = [];
for (let i = 0; i < QA.length; i += CHUNK) chunks.push(QA.slice(i, i + CHUNK));
const results = await parallel(chunks.map((chunk) => () =>
  agent(RULES + '\n\nVERIFY (Read each new_png):\n' + JSON.stringify(chunk, null, 1),
    { label: `recheck:${chunk[0].src}-${chunk[chunk.length-1].src}`, phase: 'Recheck', schema: SCHEMA })
));
const all = [];
for (const r of results) { if (r && r.verdicts) all.push(...r.verdicts); }
const unresolved = all.filter(v => v.severity === 'major' || !v.resolved);
log(`rechecked ${all.length} | unresolved: ${unresolved.length}`);
return { verdicts: all, unresolved };
'''
JS = JS.replace("__QA__", json.dumps(qa, ensure_ascii=False))
open("workflows_recheck.js", "w").write(JS)
print("wrote workflows_recheck.js", round(len(JS)/1024,1), "KB")
