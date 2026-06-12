import sys
from pptx import Presentation
from pptx.oxml.ns import qn
src="/Users/arjun/Desktop/IAF-Session1/ImpactAI_Foundry_Session1_Deck.pptx"
target=int(sys.argv[1]); out=sys.argv[2]
p=Presentation(src)
sldIdLst=p.slides._sldIdLst; ids=list(sldIdLst)
for i,el in enumerate(ids,1):
    if i!=target:
        rId=el.get(qn('r:id')); p.part.drop_rel(rId); sldIdLst.remove(el)
p.save(out)
