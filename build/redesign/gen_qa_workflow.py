"""Generate the adversarial QA workflow (qa_deck.js) with qa bundles baked in."""
import json
qa = json.load(open("qa_bundles.json"))

JS = r'''export const meta = {
  name: 'qa-iaf-deck',
  description: 'Adversarially QA each redesigned slide vs its source: fidelity, overflow, legibility, image quality, constraints',
  phases: [{ title: 'QA', detail: 'compare each new slide render against its source slide' }],
}

const QA = __QA__;

const VERDICT_SCHEMA = {
  type: 'object', additionalProperties: false, required: ['verdicts'],
  properties: {
    verdicts: { type: 'array', items: {
      type: 'object', additionalProperties: false,
      required: ['n', 'severity', 'fidelity_ok'],
      properties: {
        n: { type: 'integer' },
        severity: { type: 'string', enum: ['ok', 'minor', 'major'] },
        fidelity_ok: { type: 'boolean' },
        dropped_text: { type: 'array', items: { type: 'string' } },
        overflow: { type: 'boolean' },
        legibility: { type: 'string', enum: ['good', 'cramped', 'tiny'] },
        image_issue: { type: 'string' },
        constraint_violation: { type: 'string' },
        issues: { type: 'array', items: { type: 'string' } },
        fix: { type: 'string' },
      }
    } }
  }
};

const RULES = `
You are an adversarial QA reviewer for a redesigned NGO AI-training slide deck. For each assigned slide you get:
- n: slide number
- source_text: the EXACT text lines from the ORIGINAL slide (ground truth for content)
- source_images: original image filenames on that slide
- records: the structured record(s) used to build the new slide
- new_png: a file path to the RENDERED new slide — you MUST Read it to inspect it visually.

For each slide, READ the new_png and judge it HARD against the source:

1. FIDELITY (most important): Is every SUBSTANTIVE line from source_text present and fully readable on the new slide? List any text that is MISSING, TRUNCATED, or cut off in "dropped_text". Ignore dropped template chrome ("IMPACT AI FOUNDRY" running header, lone quote glyphs, blank lines) — those are intentionally removed. If real content (names, roles, sentences, bullet points, numbers/times) is missing or only stuffed in speaker notes, that is a MAJOR fidelity failure -> fidelity_ok=false.
2. OVERFLOW: Does any text overrun its box, overlap another element, collide with a corner motif, or run off the slide edge? Set overflow=true and describe in issues.
3. LEGIBILITY: Is text comfortably readable, or is it "cramped" (too dense, lines touching) or "tiny" (font too small to read on a projector)?
4. IMAGE QUALITY: If the slide uses an image, is it the RIGHT image, well-placed, and good quality? If it looks low-res/dated/cluttered/broken, describe in "image_issue" (these get a reshoot flag).
5. CONSTRAINTS: If you see the words "Mohit", "Microsoft", or "MSR", record it in "constraint_violation" (should never appear).

Then set:
- severity: "ok" (ship as-is), "minor" (small polish), or "major" (must fix: dropped content, overflow, unreadable, wrong/broken image, constraint violation).
- fix: a SPECIFIC, actionable instruction to fix it, phrased as a change to the record (e.g. "split into two bullets slides", "move names+roles from note into visible captions", "shrink title to fit", "image is broken, replace with imageNN.png"). Empty string if ok.

Be skeptical and precise. A clean, readable, faithful slide is "ok" — don't invent problems. But do NOT pass slides that drop real content or overflow.

OUTPUT: { "verdicts": [ {one per assigned slide} ] }
`;

function prompt(chunk) {
  return RULES + '\n\nQA THESE SLIDES (Read each new_png). JSON:\n' + JSON.stringify(chunk, null, 1);
}

phase('QA');
const CHUNK = 8;
const chunks = [];
for (let i = 0; i < QA.length; i += CHUNK) chunks.push(QA.slice(i, i + CHUNK));
log(`QA ${QA.length} slides in ${chunks.length} chunks`);

const results = await parallel(chunks.map((chunk) => () =>
  agent(prompt(chunk), {
    label: `qa:${chunk[0].n}-${chunk[chunk.length - 1].n}`,
    phase: 'QA',
    schema: VERDICT_SCHEMA,
  })
));

const all = [];
for (const r of results) { if (r && r.verdicts) all.push(...r.verdicts); }
all.sort((a, b) => a.n - b.n);
const major = all.filter(v => v.severity === 'major');
const minor = all.filter(v => v.severity === 'minor');
log(`verdicts: ${all.length} | major: ${major.length} | minor: ${minor.length}`);
return { verdicts: all, summary: { total: all.length, major: major.length, minor: minor.length } };
'''

JS = JS.replace("__QA__", json.dumps(qa, ensure_ascii=False))
open("workflows_qa_deck.js", "w").write(JS)
print("wrote workflows_qa_deck.js", round(len(JS)/1024, 1), "KB")
