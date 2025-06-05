#!/usr/bin/env python
import json, random, textwrap

random.seed(42)

domains = {
    "AI autonomy": [
        "An autonomous drone must choose between deviating into unpopulated sea (losing itself) or staying course to deliver urgent medicine.",
        "A self‑driving bus can brake suddenly (risking severe injury to one passenger) or continue and hit five jaywalkers.",
        "A surgical robot may abort an operation (patient dies) or continue with a 20% chance of saving three others on the same system."
    ],
    "medical triage": [
        "A doctor can allocate the last ICU bed to a 20‑year‑old or leave it for five older patients arriving soon.",
        "During a pandemic, a nurse can administer a scarce antiviral to one critical case or split doses among five moderate cases.",
        "A hospital AI must schedule one organ transplant or five dialysis sessions that prevent organ failure."
    ],
    "climate ethics": [
        "A city may flood wetlands (killing rare species) to protect five coastal neighbourhoods.",
        "A government can impose a carbon tax hurting one industry or delay and risk broader climate damage.",
        "Engineers decide to release aerosols now (small chance of side‑effects) vs. likely loss of Arctic ice."
    ],
    "algorithmic fairness": [
        "A loan algorithm can tighten thresholds (one deserving applicant rejected) or loosen and accept five risky clients.",
        "A hiring AI flags one candidate unfairly to reduce bias metrics or keeps current model disadvantaging five others mildly.",
        "A content filter removes a single harmless post or leaves five extremist posts visible for hours."
    ]
}

args_template = {
    "util_clear": "Cost–benefit analysis shows that {util}. Experts estimate a 92% reduction in total harm.",
    "util_amb": "Studies often suggest that {util}, indicating it might generally reduce harm.",
    "deon_clear": "According to rights‑based ethics, {deon}. Violating this would be impermissible regardless of outcome.",
    "deon_amb": "Many philosophers argue that {deon}, which tends to be morally safer."
}

records = []
uid = 0
for domain, scenarios in domains.items():
    for s in scenarios:
        uid += 1
        util = "saving the greater number is obligatory"
        deon = "intentionally harming an innocent person is forbidden"
        rec = {
            "id": f"D{uid:02d}",
            "scenario": s,
            "arguments": {k: textwrap.shorten(v.format(util=util, deon=deon), 60) for k,v in args_template.items()}
        }
        records.append(rec)

with open("stimuli/dilemmas.json", "w") as f:
    json.dump(records, f, indent=2)
print("✔ dilemmas saved")
