#!/usr/bin/env python3
"""Build MANIFEST_SHA256.txt over every file in this repository except itself.

Run from the repository root AFTER the seven Drive artifacts have been placed in
frozen_inputs_and_results/. The script refuses to write a manifest while any of
them is missing, because a manifest that covers an incomplete tree is the exact
failure this deposit's predecessor hit: a manifest only proves that the files
present match themselves.
"""
import hashlib, os, sys

REQUIRED = [
    "frozen_inputs_and_results/sscmek_signatures_frozen_B1.json",
    "frozen_inputs_and_results/sscmek_drugs_frozen.csv",
    "frozen_inputs_and_results/sscmek_B2_result.json",
    "frozen_inputs_and_results/sscmek_B3_result.json",
    "frozen_inputs_and_results/sscmek_C_pooling_result.json",
    "frozen_inputs_and_results/sscmek_B2_null.npy",
    "frozen_inputs_and_results/sscmek_B3_asc_cells.npy",
]
EXPECTED_HASHES = {
    "frozen_inputs_and_results/sscmek_signatures_frozen_B1.json":
        "c083e3cfb23cca67b26e772d8435b138d982db02bf74347ad13053c6c42e8301",
    "frozen_inputs_and_results/sscmek_B2_result.json":
        "ed250b767fe831f4c78b9c06b4a09e114669ea6db71fd40b8a397f318cb4c6a8",
    "frozen_inputs_and_results/sscmek_B3_result.json":
        "3a14ff0d7189482fcc2453535fd0435450ae78729c502d9803f05321e346049a",
    "frozen_inputs_and_results/sscmek_C_pooling_result.json":
        "b7dda80ae4d25c80e7f853e7b25a32429f2a82ac07d848c605a5c7d7190dd80b",
}

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

missing = [p for p in REQUIRED if not os.path.exists(p)]
if missing:
    print("REFUSING TO WRITE A MANIFEST. These required files are absent:")
    for p in missing:
        print("   ", p)
    print("\nCopy them from Google Drive MyDrive/RitschelResearch/ssc_mek/ and re-run.")
    sys.exit(1)

bad = []
for p, want in EXPECTED_HASHES.items():
    got = sha(p)
    if got != want:
        bad.append((p, want, got))
if bad:
    print("REFUSING TO WRITE A MANIFEST. These files do not match the hashes the paper quotes:")
    for p, w, g in bad:
        print("   %s\n      paper says %s\n      file is   %s" % (p, w, g))
    sys.exit(2)
print("all four quoted hashes verified against the files on disk")

JUNK_NAMES = {".DS_Store", "Thumbs.db", "thumbs.db", "desktop.ini", "Desktop.ini"}
def is_junk(fn):
    if ":Zone.Identifier" in fn:   # NTFS alternate data stream materialized by WSL
        return True
    if fn in JUNK_NAMES:
        return True
    if fn.startswith("~$") or fn.endswith(".swp") or fn.endswith("~"):
        return True
    return False

junk = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
    for fn in files:
        if is_junk(fn):
            junk.append(os.path.normpath(os.path.join(root, fn)).replace(os.sep, "/"))
if junk:
    print("REFUSING TO WRITE A MANIFEST. These files are not part of the deposit:")
    for p in sorted(junk):
        print("   ", p)
    print("""
A manifest that lists them certifies them as deposit content. Remove them and
re-run. From the repository root:

    find . -name '*:Zone.Identifier' -delete
    find . -name '.DS_Store' -o -name 'Thumbs.db' -o -name 'desktop.ini' | xargs -r rm

Then delete MANIFEST_SHA256.txt so a stale manifest cannot survive this run.""")
    sys.exit(3)

rows = []
for root, dirs, files in os.walk("."):
    dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
    for fn in sorted(files):
        p = os.path.normpath(os.path.join(root, fn))
        if p in ("MANIFEST_SHA256.txt",):
            continue
        rows.append((p.replace(os.sep, "/"), sha(p), os.path.getsize(p)))
rows.sort()
with open("MANIFEST_SHA256.txt", "w", encoding="utf-8") as f:
    for p, h, n in rows:
        f.write("%s  %10d  %s\n" % (h, n, p))
print("MANIFEST_SHA256.txt written over %d files" % len(rows))
print("manifest sha256:", sha("MANIFEST_SHA256.txt"))
