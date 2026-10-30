# Optimal estimates for direct images: product descent and top-degree rigidity

**Zhijian Chen, Zhuo Liu, and Chenghao Qing**

Version 2 · 30 October 2026

[Read paper v2](papers/paper_v2.pdf) · [LaTeX source](papers/src/direct_image_descent.tex) · [Personal website](https://chen-zhijian.github.io/)

This repository, **direct-image-descent** (formerly **harmonic-direct-images**), contains the manuscript and LaTeX source for a study of prescribed direct-image metrics. The paper proves product descent of optimal $L^2$ estimates, establishes top-degree rigidity and non-product adjoint descent for arbitrary singular semipositive line metrics, identifies the smooth adjoint metric with the Mourougane–Takayama metric, and gives counterexamples to unrestricted descent.

## Scope and limitations

- Smooth product descent uses a complete Kähler base admitting a positive line bundle, a smooth projective fiber, a fixed product Kähler metric, and an external-product line bundle and metric. It treats the two extremal bidegree ranges specified in the manuscript. In top base and fiber antiholomorphic degrees (range (ii)), the coefficient metric may be any smooth metric on the same holomorphic external-product bundle.
- Singular product descent allows arbitrary plurisubharmonic weights on the two coefficient factors and compact Kähler fibers. The actual higher direct-image sheaf includes the multiplier ideal, and its prescribed metric is the minimum weighted $L^2$ norm of fiberwise Dolbeault representatives. The resulting scalar-factor metrics satisfy the stated weighted optimal estimates, Griffiths semipositivity, and the minimal extension property.
- The non-product singular result concerns **top adjoint fiber degree $q=n$** under a proper Kähler submersion with connected fibers. Either the higher direct image vanishes or the coefficient metric factors as a divisorial metric times a metric pulled back from the base. The theorem identifies the sheaf and quotient metric; a complete Kähler base gives the stated optimal estimates.
- For smooth vector coefficients, the complementary top-direct-image theorem retains infinitesimal triviality, dual Nakano semipositivity, and locally constant top cohomology dimension. For smooth semipositive line coefficients in adjoint degree, the manuscript identifies the prescribed harmonic metric with the Mourougane–Takayama metric and applies its Nakano semipositivity theorem.
- Compact-fiber counterexamples exclude unrestricted degreewise descent: one has a nonsplit, non-semipositive metric on a trivial family in range (i), and another uses a flat coefficient on a varying elliptic family in range (ii). Infinitesimal triviality alone does not replace metric splitting in the original degreewise problem.

The smooth and singular split-product results are presented as consequences of existing theory. The metric, multiplier ideal, bidegree, and hypotheses are part of each statement; these results do not assert unrestricted descent for arbitrary singular metrics or arbitrary degrees. See the manuscript for the precise theorems and attribution.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── NOTICE
├── papers/
│   ├── paper_v1.pdf                  # Archived first version
│   ├── paper_v2.pdf                  # Current paper
│   └── src/
│       ├── main.tex                  # Archived first-version source
│       └── direct_image_descent.tex  # Current standalone source
├── prompts_and_logs/
│   ├── system_prompt.txt
│   ├── conversation.json
│   ├── cost_summary.md
│   └── review_notes/
└── verification/
    ├── README.md
    ├── build_manifest.json
    ├── build_manifest_v1.json
    ├── lean/
    └── scripts/
        ├── build.ps1
        └── verify.py
```

The [first-version PDF](papers/paper_v1.pdf) and [original source](papers/src/main.tex) are retained unchanged as historical artifacts. They describe the earlier controlled-variation manuscript and are superseded by v2 for the current title, scope, and results.

## Build

Install a TeX distribution containing XeLaTeX and the packages used in the source, including AMS, Latin Modern, mathtools, mathrsfs, geometry, microtype, enumitem, xcolor, and hyperref. From the repository root, run:

```powershell
powershell -NoProfile -File .\verification\scripts\build.ps1
python .\verification\scripts\verify.py
```

The build defaults to **XeLaTeX**, accepts an override through `-Engine` (an engine name or executable path), and compiles `papers/src/direct_image_descent.tex` in three passes. It publishes [papers/paper_v2.pdf](papers/paper_v2.pdf) and updates `verification/build_manifest.json`. The bibliography is embedded in the source; no BibTeX database or external figures are required. See [verification/README.md](verification/README.md) for the checks and their limits.

## Provenance and verification

Selected original user-visible research messages were recovered from a local Codex conversation. [conversation.json](prompts_and_logs/conversation.json) contains 58 messages from its ten most recent turns on October 23–24, 2026: ten user messages, 38 assistant commentary messages, and ten final answers. It includes article creation, review corrections, and the earlier metric and fibration extensions. Absolute local paths and platform context were removed; the export records these transformations and its retrieval limits. Older turns remain outside this partial export.

Five [historical research and review notes](prompts_and_logs/review_notes/README.md) were also recovered. These records document earlier manuscript stages; they are not a development record or verification of v2. Their judgments and earlier conversation claims may be superseded by later revisions and do not certify external peer review. The original system prompt, precise model/provider/version, token usage, and costs remain unavailable. See the [provenance record](prompts_and_logs/README.md) for the scope and gaps; no missing history has been reconstructed.

No Lean formalization or other machine-checked proof is supplied for either version. `verification/lean/` records that status. Compilation, reference checks, file checks, and PDF inspection are technical checks; they do not establish mathematical correctness. The mathematical arguments and cited inputs require scholarly review.

## Maintenance

The current repository is [chen-zhijian/direct-image-descent](https://github.com/chen-zhijian/direct-image-descent). The owner maintains v2 in `direct_image_descent.tex`; its packaged copy is `papers/src/direct_image_descent.tex`. For each revision, synchronize that source, rebuild and inspect the PDF, run the verification script, and commit the current source, `papers/paper_v2.pdf`, and build manifest together. Update the title, author credits, summary, scope, and PDF link on the [personal website](https://chen-zhijian.github.io/) when needed. Keep the archived first-version files intact.

The previous repository documentation described a local synchronization service checking the original source every 15 minutes. That historical configuration is not evidence that automatic syncing is configured for the renamed repository or v2 source. Retarget and verify any such service before relying on it; until then, use the manual maintenance steps above. A synchronization service must not overwrite the archived v1 files with v2 content or regenerate historical conversation and usage records.

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
