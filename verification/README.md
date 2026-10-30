# Verification status

The scripts rebuild the current v2 manuscript from `papers/src/direct_image_descent.tex` and check the recorded source/PDF hashes for both versions. `build_manifest.json` records the current build, and `build_manifest_v1.json` preserves the original v1 record. They do not verify any mathematical claim. No numerical verification scripts or proof-assistant formalization have been supplied for either version.

Run `powershell -File verification/scripts/build.ps1` from the repository root, then `python verification/scripts/verify.py`. The default engine is XeLaTeX; the build script accepts an engine override. Install the selected engine and the packages listed in the source. Inspect the resulting PDF. The build disables shell escape and stops on LaTeX errors or unresolved references after three passes. The `.build/` directory retains local logs and is ignored by Git.

Commit `papers/src/direct_image_descent.tex`, `papers/paper_v2.pdf`, and `verification/build_manifest.json` together with each current-source revision. The manifest records a build pairing, not bit-for-bit reproducibility across TeX distributions. Preserve `papers/paper_v1.pdf` and `papers/src/main.tex` unchanged as the archived first version; the current build does not rebuild those historical artifacts.
