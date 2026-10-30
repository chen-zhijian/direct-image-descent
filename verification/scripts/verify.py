"""Check the recorded source/PDF pairing. This does not verify mathematics."""
from pathlib import Path
import hashlib, json

repo = Path(__file__).resolve().parents[2]
for manifest_name in ("build_manifest.json", "build_manifest_v1.json"):
    manifest = json.loads((repo / "verification" / manifest_name).read_text(encoding="utf-8-sig"))
    for kind in ("source", "pdf"):
        path = repo / manifest[kind]
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != manifest[f"{kind}_sha256"]:
            action = "Restore the archived v1 file." if manifest_name == "build_manifest_v1.json" else "Rebuild with verification/scripts/build.ps1."
            raise SystemExit(f"{path.relative_to(repo)} changed since the recorded build. {action}")
        if kind == "pdf" and not data.startswith(b"%PDF-"):
            raise SystemExit(f"{path.relative_to(repo)} is not a PDF.")
json.loads((repo / "prompts_and_logs/conversation.json").read_text(encoding="utf-8-sig"))
for name in ("README.md", "LICENSE", "prompts_and_logs/system_prompt.txt", "prompts_and_logs/cost_summary.md"):
    if not (repo / name).is_file():
        raise SystemExit(f"Missing required file: {name}")
print("Current and archived source/PDF hashes, PDF headers, provenance JSON, and required files pass. Mathematics is not checked.")
