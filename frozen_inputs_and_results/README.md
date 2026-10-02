# Frozen inputs and results

The seven files in this folder are the frozen inputs and the recorded outputs of the
pre-registered test described in `../paper/`. They were written by the notebooks in
`../notebooks/` as those notebooks ran, and they are the files the paper's quoted
hashes refer to. Nothing here was edited after the phase that produced it.

| file | written by | what it is |
|---|---|---|
| `sscmek_signatures_frozen_B1.json` | phase B1 | the frozen queries and compound identifiers. Read by B2, B3 and C, each of which refuses to run unless this file hashes to the value below |
| `sscmek_drugs_frozen.csv` | phase B1 | the 18 declared compound identifiers with their assigned roles |
| `sscmek_B2_result.json` | phase B2 | the pre-registered primary result |
| `sscmek_B2_null.npy` | phase B2 | the 10,000-draw permutation null behind the reported p = 0.354 |
| `sscmek_B3_result.json` | phase B3 | the ASC secondary result. B3 also reads `sscmek_B2_result.json` |
| `sscmek_B3_asc_cells.npy` | phase B3 | the recovered cell line label for all 90,834 library rows |
| `sscmek_C_pooling_result.json` | phase C | the pooling control, which withdrew the tie-rate interpretation |

## Hashes quoted in the paper

    sscmek_signatures_frozen_B1.json  c083e3cfb23cca67b26e772d8435b138d982db02bf74347ad13053c6c42e8301
    sscmek_B2_result.json             ed250b767fe831f4c78b9c06b4a09e114669ea6db71fd40b8a397f318cb4c6a8
    sscmek_B3_result.json             3a14ff0d7189482fcc2453535fd0435450ae78729c502d9803f05321e346049a
    sscmek_C_pooling_result.json      b7dda80ae4d25c80e7f853e7b25a32429f2a82ac07d848c605a5c7d7190dd80b

`../make_manifest.py` re-checks these four against the files on disk and refuses to write a
manifest if any of them disagrees. `../MANIFEST_SHA256.txt` covers every file in the
repository, these seven included.

## What is deliberately not here

The working folder these files were produced in also held inputs that are not part of the
deposit: the two GEO platform annotation tables (`GPL13497_table.txt`, `GPL23080_table.txt`),
the phase A survey outputs (`sscmek_series_survey_phaseA.txt`, `sscmek_compounds_phaseA.csv`),
and one downloaded GEO sample file (`GSM3757032_S002_P.txt.gz`). All five are retrieved from
public sources by the notebooks themselves, none is referenced by a quoted hash, and phase A
is a scoping survey that fixes nothing the test depends on. `../results/PHASEA_REPORT_2026-10-01.txt`
records what that survey returned.
