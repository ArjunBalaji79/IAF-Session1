import importlib, deckbuild
SLIDES=[]
for i in range(1,6):
    SLIDES += importlib.import_module(f"part_{i}").PART
assert len(SLIDES)==76, len(SLIDES)
OUT="/Users/arjun/Desktop/IAF-Session1/ImpactAI_Foundry_Session1_Deck.pptx"
n=deckbuild.build_deck(SLIDES, OUT)
print("built", n, "slides ->", OUT)
