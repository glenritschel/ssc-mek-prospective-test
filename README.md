# A pre-registered prospective test of MEK inhibition in systemic sclerosis skin

**Criterion not met, p = 0.354.** More consequentially, the connectivity pipeline returned a score of
exactly zero for 45.6 and 51.2 percent of the library in the two primary cohorts, and both
identifiers of the test compound returned exact zero in the second, so half the test statistic was a
constant no compound-specific signal could have moved.

**Glen Charles Ritschel**, Ritschel Research. ORCID 0009-0006-5341-8840.
Paper version 1, 2026-10-02.

---

## What this is

One prospective test of one compound, on a connectivity pipeline whose own retrospective benchmark
was a null at n = 7, p = 0.098 (concept DOI 10.5281/zenodo.23071560). The pipeline is reused here
without modification. The pre-registration was committed with a SHA-256 hash before any disease
signature or any score existed, and it fixed one criterion.

**It is not a replication of the analysis that generated the hypothesis.** The two series behind that
analysis, GSE138669 and GSE195452, were excluded by design and never fetched.

## The hashes every phase asserts

| artifact | SHA-256 |
|---|---|
| pre-registration | `45de35e26156bf1c70d22bc9100adaeec30f3fc4e70b803e075c124960c3a4c9` |
| frozen inputs (B1) | `c083e3cfb23cca67b26e772d8435b138d982db02bf74347ad13053c6c42e8301` |
| primary result (B2) | `ed250b767fe831f4c78b9c06b4a09e114669ea6db71fd40b8a397f318cb4c6a8` |
| secondary result (B3) | `3a14ff0d7189482fcc2453535fd0435450ae78729c502d9803f05321e346049a` |
| pooling control (C) | `b7dda80ae4d25c80e7f853e7b25a32429f2a82ac07d848c605a5c7d7190dd80b` |

Each phase refuses to run unless the previous phase's output hashes to the value above. Phase B3
additionally reproduces all 54 of B2's recorded identifier percentiles to a worst difference of
exactly 0.00e+00 before it restricts anything.

## Layout

    paper/                       the manuscript, markdown and PDF
    preregistration/             committed 2026-10-01 22:24 EDT, before any score existed
    notebooks/                   the five phases, in order
    frozen_inputs_and_results/   the frozen signatures, the drug table, and the three result records
    results/                     the Phase A survey report and the consolidated result record
    make_manifest.py             builds MANIFEST_SHA256.txt, and refuses to if anything is missing
    MANIFEST_SHA256.txt          generated, covers every file in this tree

## Phases

| notebook | what it does | scores anything? |
|---|---|---|
| `RR_SSC_MEK_phaseA_survey.ipynb` | surveys candidate series | no |
| `RR_SSC_MEK_phaseB1_freeze.ipynb` | builds and freezes rosters, signatures and compound identifiers | no |
| `RR_SSC_MEK_phaseB2_control_and_score.ipynb` | runs the query-voiding control, then the pre-registered primary | yes |
| `RR_SSC_MEK_phaseB3_asc_secondary.ipynb` | the declared mesenchymal-only secondary | yes, secondary only |
| `RR_SSC_MEK_phaseC_pooling_control.ipynb` | the control that retired a claim this work had already made | diagnostic only |

**Phase C exists because of an error.** Phase B3 produced an observation that was written up as a
measured property of the pipeline, and the comparison behind it was confounded. Phase C separates the
two causes, and the claim does not survive. Section 8 of the paper reports the claim, the control and
the withdrawal rather than quietly omitting them.

## Running it

The notebooks were run in Google Colab against a Drive-mounted copy of the CMap LINCS 2020
QC-passing exemplar compound library (90,834 signatures, 26,425 compounds, 58 cell lines), built as
`libA_matrix.npy`, `libA_perts.npy` and `libA_genes.npy`, together with `geneinfo_beta.txt` and
`siginfo_beta.txt` from the same release. **Those library files are not redistributed here**; they
derive from CMap LINCS 2020 and are rebuilt by the deposited benchmark's Phase A notebook.

Phase B3 and Phase C additionally read the column-identifier axis of the LINCS level-5 gctx over the
network, which is the only step requiring internet access.

## Before depositing

1. Copy the seven artifacts listed by `make_manifest.py` from
   `MyDrive/RitschelResearch/ssc_mek/` into `frozen_inputs_and_results/`.
2. Run `python3 make_manifest.py`. It verifies the four quoted hashes against the files on disk and
   refuses to write a manifest if any file is missing or any hash disagrees.
3. Only then zip and deposit.

**A manifest only proves that the files present match themselves.** This deposit's predecessor
passed its own manifest while carrying a placeholder manuscript, which is why the script checks the
quoted hashes rather than only recomputing them.

## Data

Disease transcriptomic series are identified by public accession in the pre-registration and in the
paper: GSE181549, GSE130955 and GSE95065. **GSE130955's deposit is per-kilobase normalized rather
than raw counts**, measured at 41.0 percent whole-number values with per-sample sums near 1e6; the
pre-registered transformation is applied unchanged and gene length cancels in a per-gene contrast,
but it must not be described as counts.

## License and citation

Code and documents CC BY 4.0, consistent with the rest of this program's deposits. Cite the paper in
`paper/`, and the pipeline it tests at concept DOI 10.5281/zenodo.23071560.

## Disclosure

Sole author. Prepared with AI assistance. All reported figures are produced by the accompanying code
and every measured quantity was computed rather than recalled. The author holds filed provisional
patent applications in therapeutic areas adjacent to the application domain discussed here. No claim
in those applications depends on any result reported here, and no result here is favorable to them.
