# Dual Nakano positivity of top direct images and optimal estimates under controlled variation

**Zhijian Chen, Zhuo Liu, and Chenghao Qing**

[Read the paper](papers/paper_v1.pdf) · [LaTeX source](papers/src/main.tex) · [Personal website](https://chen-zhijian.github.io/)

This repository contains the manuscript and LaTeX source for a study of prescribed harmonic metrics on direct images. The paper proves dual Nakano semipositivity of top direct images under infinitesimal triviality, and descent of optimal $L^2$ estimates in two extremal bidegree ranges. It also treats nonsplit coefficient metrics on products and conditional extensions to smooth proper Kähler fibrations.

## Scope and limitations

- The top-direct-image theorem assumes a proper surjective holomorphic submersion between Kähler manifolds, vanishing Kodaira–Spencer maps, a smooth dual Nakano semipositive coefficient bundle, and locally constant top cohomology dimension.
- The product descent theorem uses a complete Kähler base admitting a positive line bundle, a smooth projective fiber, a fixed product Kähler metric, and an external-product line bundle and metric. Its bidegree ranges are specified in the manuscript; it is not a statement in arbitrary bidegrees.
- On the same product geometry and holomorphic external-product bundle, metric splitting can be removed in top base and fiber antiholomorphic degrees. The other range requires a sufficient quantitative bound on harmonic variation.
- The fibration extension requires an explicit bound involving curvature margin, fiber Bochner energy, harmonic variation, Kodaira–Spencer insertion, horizontal brackets, and metric comparison. A separate top-degree result assumes an adapted horizontal metric and pointwise Kodaira–Spencer annihilation on Serre-dual sections.
- An elliptic-family example excludes unconditional descent for arbitrary fibrations. The sufficient bounds are not claimed to be necessary or sharp. Degree-specific curvature conclusions should not be read as unrestricted Griffiths or Nakano positivity.

The manuscript attributes the curvature and estimate mechanisms to earlier work and makes no priority claim for these consequences. It uses the ordinary fiberwise harmonic metric; no identification with the Mourougane–Takayama metric in higher degree is asserted. See the manuscript's final section for the comparison with earlier results.

## Repository layout

```text
.
├── README.md
├── LICENSE
├── papers/
│   ├── paper_v1.pdf
│   └── src/
│       └── main.tex
├── prompts_and_logs/
│   ├── system_prompt.txt
│   ├── conversation.json
│   ├── cost_summary.md
│   └── review_notes/
├── verification/
│   ├── lean/
│   └── scripts/
│       └── build.ps1
└── .github/                  # Optional repository automation
```

## Build

Install a TeX distribution containing pdfLaTeX and the standard AMS, Latin Modern, geometry, and hyperref packages. From the repository root, run:

```powershell
powershell -NoProfile -File .\verification\scripts\build.ps1
```

The repository build script is configured for **pdfLaTeX** and `papers/src/main.tex`. The bibliography is embedded in the source; no BibTeX database or external figures are required. The published PDF is [papers/paper_v1.pdf](papers/paper_v1.pdf).

## Provenance and verification

Selected original user-visible research messages were recovered from a local Codex conversation. [conversation.json](prompts_and_logs/conversation.json) contains 58 messages from its ten most recent turns on October 23–24, 2026: ten user messages, 38 assistant commentary messages, and ten final answers. It includes article creation, review corrections, and the metric and fibration extensions. Absolute local paths and platform context were removed; the export records these transformations and its retrieval limits. Older turns remain outside this partial export.

Five [historical research and review notes](prompts_and_logs/review_notes/README.md) were also recovered. Their judgments and earlier conversation claims describe the state at that time and may be superseded by later revisions; they do not certify external peer review. The original system prompt, precise model/provider/version, token usage, and costs remain unavailable. See the [provenance record](prompts_and_logs/README.md) for the scope and gaps; no missing history has been reconstructed.

No Lean formalization or other machine-checked proof is supplied. `verification/lean/` records that status. Compilation, reference checks, file checks, and PDF inspection are technical checks; they do not establish mathematical correctness. The mathematical arguments and cited inputs require scholarly review.

## Maintenance

The owner maintains the manuscript in its original local LaTeX file. Automatic syncing is configured to check for changes every 15 minutes while the owner's computer and synchronization service are available. A successful run publishes the packaged source, rebuilt `papers/paper_v1.pdf`, and `verification/build_manifest.json` together. Failed builds leave the last published manuscript in place. The PDF path stays stable, so the existing repository and [personal website](https://chen-zhijian.github.io/) links reach the updated manuscript.

When the manuscript changes, the maintenance agent reviews the title, author credits, summary, and scope statements in this README and on the website, and updates them where needed. Build and consistency checks do not establish mathematical correctness. Automatic syncing does not reconstruct or regenerate the historical AI conversation and usage records.

Other contributors can use the documented build procedure above: edit `papers/src/`, rebuild and inspect the PDF, run `python verification/scripts/verify.py`, and commit the source, PDF, and build manifest together. Coordinate manuscript revisions with the owner so the original source and repository remain consistent.

See [LICENSE](LICENSE) for the repository's licensing status.

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE).
