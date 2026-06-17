import json
qa = json.load(open("s2_qa_bundles.json"))
JS = r'''export const meta = {
  name: 'qa-iaf-s2',
  description: 'Adversarially QA each IAF Session-2 slide vs its source: fidelity, overflow, legibility, image quality, constraints',
  phases: [{ title: 'QA', detail: 'compare each new slide render against its source' }],
}
const QA = __QA__;
const SCHEMA = { type: 'object', additionalProperties: false, required: ['verdicts'],
  properties: { verdicts: { type: 'array', items: {
    type: 'object', additionalProperties: false, required: ['n','severity','fidelity_ok'],
    properties: {
      n: { type: 'integer' }, severity: { type: 'string', enum: ['ok','minor','major'] },
      fidelity_ok: { type: 'boolean' }, dropped_text: { type: 'array', items: { type: 'string' } },
      overflow: { type: 'boolean' }, legibility: { type: 'string', enum: ['good','cramped','tiny'] },
      image_issue: { type: 'string' }, constraint_violation: { type: 'string' },
      issues: { type: 'array', items: { type: 'string' } }, fix: { type: 'string' },
    } } } } };
const RULES = `
You are an adversarial QA reviewer for the ImpactAI Foundry (IAF) "Session 2: AI Workflows" deck — an IAF-restyled version of a source Decoded Futures deck. Each slide: n, source_text (original ground-truth lines), records (what was built), new_png (path — READ it).

Judge each new_png HARD against the source:
1. FIDELITY: every SUBSTANTIVE source line present & readable? List missing/truncated text in dropped_text. NOT problems (intentional): dropped slide-number chrome ("‹#›"/"#"), lone quote glyphs, blank lines, dropped Decoded Futures logos, and DELIBERATE re-branding (Decoded Futures → ImpactAI Foundry; DF emails/survey URLs replaced with IAF-generic text + a TODO note). Also some near-identical animation-build slides were intentionally MERGED — not a loss.
2. OVERFLOW: any text running off-slide, overlapping a corner motif/footer, or colliding? For "flow" diagrams, check the stage boxes/labels aren't clipped or overrunning.
3. LEGIBILITY: comfortable on a projector, or cramped/tiny? Flow-box sub-text especially.
4. IMAGE QUALITY: right image, well-placed, good quality? If low-res/dated/broken/empty, describe in image_issue.
5. CONSTRAINTS: report any "Mohit"/"Microsoft"/"MSR" (must never appear), or any leftover "Decoded Futures"/"@technyc"/"typeform" identifier that should have been re-branded, in constraint_violation.

severity: "ok" / "minor" / "major" (major = dropped real content, overflow, unreadable, broken image, or a constraint/branding leak). Give a specific "fix" (as a record change) only if not ok.
OUTPUT: { "verdicts": [ {one per slide} ] }
`;
function prompt(chunk){ return RULES + '\n\nQA THESE (Read each new_png):\n' + JSON.stringify(chunk, null, 1); }
phase('QA');
const CHUNK = 7;
const chunks = [];
for (let i=0;i<QA.length;i+=CHUNK) chunks.push(QA.slice(i,i+CHUNK));
const results = await parallel(chunks.map((chunk)=>()=>
  agent(prompt(chunk), { label:`s2qa:${chunk[0].n}-${chunk[chunk.length-1].n}`, phase:'QA', schema: SCHEMA })));
const all=[]; for (const r of results) if (r&&r.verdicts) all.push(...r.verdicts);
all.sort((a,b)=>a.n-b.n);
const major=all.filter(v=>v.severity==='major');
log(`verdicts ${all.length} | major ${major.length}`);
return { verdicts: all, major };
'''
JS = JS.replace("__QA__", json.dumps(qa, ensure_ascii=False))
open("workflows_s2_qa.js","w").write(JS)
print("wrote workflows_s2_qa.js", round(len(JS)/1024,1), "KB")
