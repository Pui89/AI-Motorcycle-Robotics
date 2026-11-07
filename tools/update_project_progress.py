#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
root=Path(__file__).resolve().parents[1]
data=json.loads((root/"docs/project-progress.json").read_text(encoding="utf-8"))
weights=data["gate_weights"]; credits=data["evidence_credit"]; gates=data["gate_names"]
if len(credits)!=8 or any(not isinstance(c,int) or c<0 or c>w for c,w in zip(credits,weights)): raise SystemExit("Invalid evidence credits")
score=sum(credits); pct=round(score/sum(weights)*100)
colour,label=("🟢","Advanced evidence stage") if pct>=75 else ("🟡","Developing evidence stage") if pct>=50 else ("🟠","Foundation and prototype stage") if pct>=25 else ("🔴","Early foundation stage")
bar="🟦"*round(pct/5)+"⬜"*(20-round(pct/5))
rows="\n".join(f"| {g} | {c}/{w} | {'🟩'*c}{'⬜'*(w-c)} |" for g,c,w in zip(gates,credits,weights))
start="<!-- PUI89_DAILY_PROGRESS:START -->"; end="<!-- PUI89_DAILY_PROGRESS:END -->"
section=f"""{start}
## Daily project progress

**{colour} {pct}% — {label}**  
**Evidence score:** {score}/100 · **Review date:** {datetime.now(ZoneInfo("Asia/Bangkok")).strftime("%d %B %Y")} (Asia/Bangkok)  
**Progress graph:** {bar} {pct}%

Evidence-weighted commercial-readiness estimate, not code completion, sales forecast, certification or measured real-world performance. The daily run refreshes the review date only. Scores change only when evidence credits are reviewed and updated; time passing never increases a score.

| Readiness gate | Evidence credit | Visual score |
|---|---:|---|
{rows}
| **Total** | **{score}/100** | **{bar}** |

**Next milestone:** Improve the lowest-scoring applicable gate with reproducible project-specific evidence. Planned work, concept artwork and unrun tests earn no credit.

**Status boundary:** Software tests and simulations do not establish a built, certified, field-tested or commercially validated vehicle.

{end}"""
readme=(root/"README.md").read_text(encoding="utf-8")
if start in readme and end in readme: readme=readme.split(start)[0]+section+readme.split(end)[1]
else: readme=readme.rstrip()+"\n\n"+section+"\n"
(root/"README.md").write_text(readme,encoding="utf-8")
