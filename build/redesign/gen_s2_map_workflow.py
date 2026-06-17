"""Generate the S2 mapping workflow (s2_map.js) with S2 bundles baked in."""
import json
bundles = json.load(open("s2_slide_bundles.json"))

JS = r'''export const meta = {
  name: 'map-iaf-s2',
  description: 'Map Decoded Futures Session 2 slides into IAF archetype records (verbatim content, IAF-branded, dedupe animation builds)',
  phases: [{ title: 'Map', detail: 'classify + structure each source slide into archetype records' }],
}
const BUNDLES = __BUNDLES__;
const ARCHES = ['cover','divider','statement','quote','two_col','comparison','numbered','bullets','bars','exercise','image_text','image_full','image_grid','team','flow'];
const REC_PROPS = {
  src: { type: 'string' }, arch: { type: 'string', enum: ARCHES },
  dark: { type: 'boolean' }, corners: { type: 'string', enum: ['tl_br','tl_tr','bl_br','all','tl','none'] },
  note: { type: 'string' },
  eyebrow: { type: 'string' }, title: { type: 'string' }, subtitle: { type: 'string' },
  quote: { type: 'string' }, attribution: { type: 'string' },
  intro: { type: 'string' }, body: { type: 'string' },
  bullets: { type: 'array', items: { type: 'string' } },
  rows: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['lead'],
          properties: { num: { type: 'string' }, lead: { type: 'string' }, body: { type: 'string' } } } },
  bars: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['name'],
          properties: { num: { type: 'string' }, name: { type: 'string' }, desc: { type: 'string' },
          color: { type: 'string', enum: ['navy','terra','gold','green','spice'] } } } },
  steps: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['label'],
           properties: { label: { type: 'string' }, sub: { type: 'string' } } } },
  caption: { type: 'string' },
  left: { type: 'object', additionalProperties: false, properties: { label: { type: 'string' }, body: { type: 'string' }, bullets: { type: 'array', items: { type: 'string' } } } },
  right: { type: 'object', additionalProperties: false, properties: { label: { type: 'string' }, body: { type: 'string' }, bullets: { type: 'array', items: { type: 'string' } } } },
  card: { type: 'array', items: { type: 'string' } },
  question: { type: 'string' }, visual: { type: 'string', enum: ['laptop','none'] },
  ghost: { type: 'string' }, kicker: { type: 'string' },
  meta: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['label','value'], properties: { label: { type: 'string' }, value: { type: 'string' } } } },
  image: { type: 'string' }, image_side: { type: 'string', enum: ['left','right'] },
  images: { type: 'array', items: { type: 'string' } },
  people: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['name'],
            properties: { name: { type: 'string' }, role: { type: 'string' }, sub: { type: 'string' }, photo: { type: 'string' } } } },
  fit: { type: 'string', enum: ['contain','cover'] },
};
const SCHEMA = { type: 'object', additionalProperties: false, required: ['records'],
  properties: { records: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['src','arch'], properties: REC_PROPS } } } };

const CATALOG = `
ARCHETYPE CATALOG — choose ONE arch per record, fill ONLY the listed fields:
cover      — title, subtitle, eyebrow, meta:[{label,value}]  (the deck title slide)
divider    — eyebrow, title, subtitle, dark:true  (full section break on navy)
statement  — eyebrow, title, subtitle  (single centered statement on cream)
quote      — quote, attribution  (a pulled quotation)
two_col    — eyebrow, title, ghost(2-digit numeral), left:{label,body|bullets}, right:{label,body|bullets}
comparison — like two_col, for A-vs-B contrasts
numbered   — eyebrow, title, rows:[{num,lead,body}], kicker  (2–5 numbered rows)
bullets    — eyebrow, title, intro, bullets:[...]
bars       — eyebrow, title, bars:[{num,name,desc,color}]  (sequential phases; colors cycle navy,terra,spice,gold,green)
flow       — eyebrow, title, steps:[{label,sub}], caption  (a WORKFLOW / NODE diagram: horizontal connected stages like Trigger → Inputs → Instructions → Model → Output. USE THIS for node anatomy, workflow chains, and the human→automated spectrum.)
exercise   — eyebrow, title, card:[lines], question, visual:"laptop"
image_text — eyebrow, title, body|bullets, image:"imageNN.png", image_side
image_full — image, caption, eyebrow, dark:true  (slide dominated by one screenshot/photo)
image_grid — eyebrow, title, images:[...]
`;

const RULES = `
You are mapping slides from "Decoded Futures — Session 2: AI Workflows" into the ImpactAI Foundry (IAF) design system. Each bundle: n, text (shapes→lines with lvl indent), images (file+geometry), src_png (READ it to see layout), char_count.

RULES:
1. VERBATIM TEACHING CONTENT. Copy the slide's instructional wording EXACTLY — do not paraphrase, summarize, or invent. Preserve punctuation. (You may normalize an ALL-CAPS running header into a normal-case eyebrow.)
2. RE-BRAND IDENTITY ONLY. This deck is being rebuilt FOR IAF. On the COVER and any identity/branding element, use "ImpactAI Foundry" — never "Decoded Futures". Drop Decoded Futures logos (don't reference their logo image files). The cover = arch:cover, eyebrow "IMPACTAI FOUNDRY · SESSION 2", title "AI Workflows" (or the slide's real title), subtitle from the slide. Teaching content elsewhere stays verbatim.
3. DROP CHROME. Drop slide-number placeholders that render as "‹#›" or "#", lone decorative quote glyphs, and blank lines. Use the real heading as eyebrow/title.
4. DEDUPE ANIMATION BUILDS. Several consecutive slides are progressive-reveal duplicates of ONE slide (e.g. 21&22 identical "Success"; 24&25 identical; 30&31 near-identical node detail). When you see near-identical adjacent slides, emit ONE record (use the FULLEST version) with src = the LAST slide number of the group (so later slides still map). If a later slide in your chunk is a pure duplicate of an earlier one, SKIP it (emit no record for it). Note the merge in "note".
5. WORKFLOWS & NODES → use arch:flow. The node-anatomy slides (Trigger/Inputs/Instructions/Model/Output), workflow chains, and the "Fully human → Fully automated" spectrum are flow diagrams: put each stage in steps:[{label, sub}]. For a detailed single-node breakdown table, you may instead use two_col or numbered if that's clearer — pick what reads best from src_png.
6. SPLIT only if genuinely too dense for one clean slide (rare here). Use src "Na"/"Nb".
7. CONSTRAINTS (hard): never output "Mohit", "Microsoft", or "MSR". Don't invent advisors/partners.
8. Eyebrows short & label-like; main heading in title.

OUTPUT: { "records": [ ... ] } in slide order. Use ONLY each archetype's fields.
`;

function buildPrompt(chunk) {
  return RULES + '\n' + CATALOG + '\n\nMAP THESE SLIDES (read each src_png). JSON:\n' + JSON.stringify(chunk, null, 1);
}

phase('Map');
const CHUNK = 7;
const chunks = [];
for (let i = 0; i < BUNDLES.length; i += CHUNK) chunks.push(BUNDLES.slice(i, i + CHUNK));
log(`mapping ${BUNDLES.length} S2 slides in ${chunks.length} chunks`);
const results = await parallel(chunks.map((chunk) => () =>
  agent(buildPrompt(chunk), { label: `s2map:${chunk[0].n}-${chunk[chunk.length-1].n}`, phase: 'Map', schema: SCHEMA })
));
const all = [];
for (const r of results) { if (r && r.records) all.push(...r.records); }
all.sort((a, b) => (parseFloat(a.src) - parseFloat(b.src)) || String(a.src).localeCompare(String(b.src)));
log(`collected ${all.length} records`);
return { records: all };
'''
JS = JS.replace("__BUNDLES__", json.dumps(bundles, ensure_ascii=False))
open("workflows_s2_map.js", "w").write(JS)
print("wrote workflows_s2_map.js", round(len(JS)/1024,1), "KB")
