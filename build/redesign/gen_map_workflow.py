"""Generate the mapping workflow script (map_deck.js) with slide bundles baked in."""
import json

bundles = json.load(open("slide_bundles.json"))
# strip pixel dims to keep prompt lean; keep file + geometry
for b in bundles:
    for im in b["images"]:
        im.pop("px", None)

JS = r'''export const meta = {
  name: 'map-iaf-deck',
  description: 'Map 88 source slides into redesign archetype records (verbatim text, constraint-scrubbed, dense splits)',
  phases: [{ title: 'Map', detail: 'classify + structure each source slide into archetype records' }],
}

const BUNDLES = __BUNDLES__;

const ARCHES = ['cover','divider','statement','quote','two_col','comparison','numbered','bullets','bars','exercise','image_text','image_full','image_grid'];

const REC_PROPS = {
  src: { type: 'string' },
  arch: { type: 'string', enum: ARCHES },
  dark: { type: 'boolean' },
  corners: { type: 'string', enum: ['tl_br','tl_tr','bl_br','all','tl','none'] },
  note: { type: 'string' },
  eyebrow: { type: 'string' }, title: { type: 'string' }, subtitle: { type: 'string' },
  quote: { type: 'string' }, attribution: { type: 'string' },
  intro: { type: 'string' }, body: { type: 'string' },
  bullets: { type: 'array', items: { type: 'string' } },
  rows: { type: 'array', items: { type: 'object', additionalProperties: false,
          required: ['lead'], properties: { num: { type: 'string' }, lead: { type: 'string' }, body: { type: 'string' } } } },
  bars: { type: 'array', items: { type: 'object', additionalProperties: false,
          required: ['name'], properties: { num: { type: 'string' }, name: { type: 'string' }, desc: { type: 'string' },
          color: { type: 'string', enum: ['navy','terra','gold','green','spice'] } } } },
  left: { type: 'object', additionalProperties: false, properties: { label: { type: 'string' }, body: { type: 'string' }, bullets: { type: 'array', items: { type: 'string' } } } },
  right: { type: 'object', additionalProperties: false, properties: { label: { type: 'string' }, body: { type: 'string' }, bullets: { type: 'array', items: { type: 'string' } } } },
  card: { type: 'array', items: { type: 'string' } },
  question: { type: 'string' },
  visual: { type: 'string', enum: ['laptop','none'] },
  ghost: { type: 'string' }, kicker: { type: 'string' },
  meta: { type: 'array', items: { type: 'object', additionalProperties: false, required: ['label','value'], properties: { label: { type: 'string' }, value: { type: 'string' } } } },
  image: { type: 'string' }, image_side: { type: 'string', enum: ['left','right'] },
  images: { type: 'array', items: { type: 'string' } },
  fit: { type: 'string', enum: ['contain','cover'] },
};

const SCHEMA = {
  type: 'object', additionalProperties: false, required: ['records'],
  properties: {
    records: { type: 'array', items: {
      type: 'object', additionalProperties: false, required: ['src','arch'], properties: REC_PROPS
    } }
  }
};

const CATALOG = `
ARCHETYPE CATALOG — choose ONE arch per output record, fill ONLY the fields listed:

cover        — title, subtitle, eyebrow, meta:[{label,value}]   (deck title slide only)
divider      — eyebrow, title, subtitle, dark:true   (full section break; navy bg)
statement    — eyebrow, title, subtitle   (a single centered statement on CREAM; like divider but light)
quote        — quote, attribution   (a pulled quotation; the giant quote mark is automatic)
two_col      — eyebrow, title, ghost(optional 2-digit numeral string), left:{label,body|bullets}, right:{label,body|bullets}
comparison   — same fields as two_col (use when the two columns contrast A vs B, e.g. "Big model / Small model")
numbered     — eyebrow, title, rows:[{num,lead,body}], kicker(optional italic footnote)   (2–5 rows)
bullets      — eyebrow, title, intro(optional lead sentence), bullets:[...]   (a single list)
bars         — eyebrow, title, bars:[{num,name,desc,color}]   (sequential phases/stages; colors cycle navy,terra,spice,gold,green)
exercise     — eyebrow, title, card:[lines of the prompt/scenario], question(the "→" task line), visual:"laptop"(optional)
image_text   — eyebrow, title, body|bullets, image:"imageNN.png", image_side:"right"|"left"   (text + ONE supporting image)
image_full   — image:"imageNN.png", caption(optional), eyebrow(optional), dark:true   (a screenshot/photo that fills the slide; use for slides that are mostly one big image)
image_grid   — eyebrow, title, images:["imageNN.png",...]   (a gallery of photos, e.g. cohort headshots)
`;

const RULES = `
YOU ARE MAPPING SLIDES FROM AN EXISTING NGO AI-TRAINING DECK INTO A NEW DESIGN SYSTEM.
Each input slide bundle has: n (slide number), text (shapes with lines, each line has lvl=indent level), images (file + % geometry), src_png (a rendered PNG of the original slide — READ IT to see the layout/visual type), char_count.

CRITICAL RULES:
1. VERBATIM TEXT. Copy the slide's wording EXACTLY into the record fields — do NOT paraphrase, summarize, shorten, rewrite, or invent any text. Preserve punctuation and capitalization (you may convert ALL-CAPS running titles to normal case ONLY for the eyebrow). Every meaningful word from the source must appear in the output.
2. DROP TEMPLATE CHROME. The recurring running-header line "IMPACT AI FOUNDRY" (or "IMPACTAI FOUNDRY") at the very top is template branding — DROP it (the new design adds its own footer). Use the slide's real section label (e.g. "WHAT AI ACTUALLY IS", "PHASE 01 · DISCOVER", "THREE GUARDRAILS") as the eyebrow. Drop empty/blank lines and decorative lone quote-mark glyphs (the quote archetype adds its own).
3. CHOOSE THE RIGHT ARCHETYPE by reading src_png. Section-break slides with just a centered title → divider (if it reads as a bold break / navy) or statement (lighter). Phase cards with FOCUS/GOALS-style columns → two_col. "A vs B" → comparison. Lists → bullets. Numbered principles → numbered. Sequential stages → bars. Big quote → quote. Exercises/activities/"table talk"/prompts → exercise. A slide dominated by one screenshot/photo → image_full. Text beside a screenshot → image_text. Multiple photos → image_grid.
4. IMAGES. Reference real files from the bundle's images list (e.g. "image41.png"). For image_full pick the dominant image. For image_text pick the most relevant one. For image_grid list the photo files. If an image looks low-quality / dated / cluttered in src_png, ADD note:"ugly-image — flag for reshoot" (it will go into speaker notes; the image is still used). Dark screenshots → set dark:true on image_full.
5. SPLIT DENSE SLIDES. If a slide is too dense for one clean slide (roughly >6 bullets, or >4 numbered rows, or char_count high and cramped in src_png), SPLIT it into TWO records: src "Na" and "Nb" (e.g. "59a","59b"). Keep the SAME title (optionally add eyebrow "…CONTINUED" on the second). Divide the bullets/rows sensibly. Otherwise output exactly one record with src = the slide number as a string.
6. CONSTRAINTS (hard): NEVER output the strings "Mohit", "Microsoft", "MSR", or "Microsoft Research" anywhere. Advisors named may ONLY be Prof. Rajiv Joshi and/or Prof. Sarah Holloway. Partners may ONLY be Tech:NYC's Decoded Futures and Bridging Ventures NYC. Do not invent people/orgs not in the source; just never introduce a forbidden one.
7. CORNERS. Omit the "corners" field normally (the renderer picks tl+br for content, tl+tr for bars/grids). Only set corners:"tl_tr" if YOUR content slide is bottom-heavy (fills the lower third with a table/wide block).
8. Keep eyebrows SHORT (a label, ALL-CAPS-ish phrase). Put the slide's main heading in "title".

OUTPUT: { "records": [ ... ] } — one or two records per input slide, in slide order. Use ONLY the fields each archetype lists. The hidden slide (n=4) STILL gets a record (it will be re-hidden in the build).
`;

function buildPrompt(chunk) {
  return RULES + '\n' + CATALOG +
    '\n\nMAP THESE SLIDES (read each src_png for layout). Source bundles JSON:\n' +
    JSON.stringify(chunk, null, 1);
}

phase('Map');
const CHUNK = 8;
const chunks = [];
for (let i = 0; i < BUNDLES.length; i += CHUNK) chunks.push(BUNDLES.slice(i, i + CHUNK));
log(`mapping ${BUNDLES.length} slides in ${chunks.length} chunks of ${CHUNK}`);

const results = await parallel(chunks.map((chunk) => () =>
  agent(buildPrompt(chunk), {
    label: `map:${chunk[0].n}-${chunk[chunk.length - 1].n}`,
    phase: 'Map',
    schema: SCHEMA,
  })
));

const all = [];
for (const r of results) { if (r && r.records) all.push(...r.records); }
all.sort((a, b) => (parseFloat(a.src) - parseFloat(b.src)) || a.src.localeCompare(b.src));
log(`collected ${all.length} records`);
return { records: all };
'''

JS = JS.replace("__BUNDLES__", json.dumps(bundles, ensure_ascii=False))
open("workflows_map_deck.js", "w").write(JS)
print("wrote workflows_map_deck.js", round(len(JS) / 1024, 1), "KB")
