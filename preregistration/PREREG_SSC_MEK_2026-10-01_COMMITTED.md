# Pre-registration: systemic sclerosis skin and MEK inhibition, under the published L1000 benchmark pipeline

**STATE: COMMITTED 2026-10-01 22:24 EDT by Glen Charles Ritschel ("commit now").** Written 2026-10-01 from the Phase A survey report (SHA-256 `7c2187c3...f65b`, filed as `PHASEA_REPORT_2026-10-01.txt`). No disease signature and no connectivity score has been computed for any series named here.

## 1. The question, and what it is not

**Question.** Does the L1000 connectivity pipeline, exactly as published in version 2 of the benchmark paper (concept DOI 10.5281/zenodo.23071560), place PD-0325901 among the compounds that reverse a systemic sclerosis skin signature, when the signature comes from patient cohorts that played no part in the original MEK finding?

**It is not a replication of the P01 analysis.** P01 queried a myofibroblast cluster signature from single-cell data (GSE138669). This test queries a whole-skin, patient-versus-control signature from bulk data. A result here says nothing about whether the P01 cluster analysis reproduces.

**It is not a benchmark.** It is one prospective test of one compound. The instrument's own benchmark was a null at n = 7 (p = 0.098), and every reading of this result has to carry that.

## 2. Excluded by design

GSE138669 and GSE195452, the P01 source data. Never fetched.

## 3. Queries

Group membership is read by field name, never by line position. Each query uses one biopsy per person. Expected counts are stated here; the run stops if either arm differs from them, and an empty arm is fatal.

| | series | cases | controls | one per person | expected |
|---|---|---|---|---|---|
| **Q1** | GSE181549 (GENISOS registry, Houston; one-channel Agilent, GPL13497) | `condition` = `systemic sclerosis patient` | `condition` = `Control` | `sample number within subject` = `1` | 113 and 44 |
| **Q2** | GSE130955 (PRESS registry; RNA-seq) | `diagnosis` = `SSc patient` | `diagnosis` = `healthy control` | `biopsy number for this subject` = `1` | 48 and 33 |

**Q2 is conditional on the deposit.** The series has no expression table; each sample lists a supplementary file. If those files hold a gene-level count or expression table, Q2 is built. If they hold only raw reads, Q2 is excluded on a deposit ground, the same ground as the benchmark's graft-versus-host case, and the test runs on Q1 alone. The write-up says which.

**Not used, with the reason fixed now.**
- GSE58095: its own design text places it in the same GENISOS registry as Q1. Where two series draw on one registry the larger is taken (benchmark Section 9). It is not a second query.
- GSE9285, GSE32413, GSE45485, GSE59785, GSE76886, GSE125362: two-channel reference designs. The orientation of the deposited ratio differs between deposits (GSE76886 states reference over test), and several carry their group labels only in free text. A sign error there inverts the contrast without raising anything.

**Sensitivity only, reported and never gating.** GSE95065 (`dx`: 18 `diffuse cutaneous systemic sclerosis`, 15 `healthy`). It was deposited by the laboratory that deposited GSE138669, so overlap of individuals with the P01 source cannot be ruled out from the deposits.

## 4. Disease signature

Unchanged from the benchmark.
- Statistic per gene: mean difference over the pooled standard deviation, floored at 0.1 times the median pooled standard deviation.
- Gene space: the 978 landmark genes. Landmarks not measured on a platform are dropped, not imputed, and the count is reported.
- Query: the 150 highest and 150 lowest landmark genes.
- Arrays: median across probes mapping to one gene. If the 99th percentile of a series exceeds 100 it is linear scale and gets log2(max(x, 1)).
- RNA-seq: log2 counts per million, library size computed on the full matrix before any gene subsetting.

## 5. Library and scores

Unchanged from the benchmark.
- Library: QC-passing exemplar compound signatures, CMap LINCS 2020: 90,834 signatures, 26,425 compounds, 58 cell lines.
- Score: two-tailed Kolmogorov-Smirnov connectivity, exactly zero when the up and down tails enrich in the same direction.
- Compound score: median over the compound's signatures.
- Percentile: (midrank - 0.5) / N, ascending, so the strongest reversal is lowest. Midrank for ties.

## 6. Compounds

**PD-0325901 (primary).** BRD-K49865102 (25 signatures) and BRD-A50454580 (8 signatures). Same skeleton, SUDAHWBOROXANE. Each identifier's largest-fragment formula must equal C16H14F3IN2O4 or the run stops. The drug's percentile in a query is the median of its identifiers' percentiles.

**MEK1/2 inhibitor class (secondary).** Eleven drugs, fourteen identifiers, named here before any score: selumetinib, PD-0325901, trametinib, PD-184352, U-0126 (three identifiers), PD-98059, AS-703026, refametinib, Ro-4987655, TAK-733, PD-198306.

Annotated as MEK inhibitors in the library and left out, with the reason: BIX-02189 (its targets are MAP2K5 and MAPK7, not MEK1/2); nobiletin and arctigenin (plant natural products, not selective MEK1/2 inhibitors).

**Reference compounds, reported only.** Dasatinib, bosutinib, nintedanib, mycophenolate mofetil.

## 7. Primary statistic and criterion

**Statistic.** The mean, over the primary queries that are built, of PD-0325901's percentile.

**Null.** 10,000 draws of two distinct library identifiers. Each draw is scored exactly as PD-0325901 is: median of the two identifiers' percentiles within each query, then the mean across queries, using the same two identifiers in every query. That keeps whatever correlation exists between the queries, so the two cohorts are not assumed independent.

**Criterion, one condition: permutation p < 0.05.** p = (1 + number of draws at or below the observed value) / (1 + 10,000).

**Stated in advance.**
- If an identifier scores exactly zero in a query, its percentile is the tied block's midrank. If PD-0325901 sits on the tied block throughout, its percentile is near 0.5, the criterion cannot be met, and the result is reported as uninformative, not as a negative.
- Not meeting the criterion does not show that MEK inhibition fails in systemic sclerosis. Meeting it does not show that it works. It is one instrument, and its benchmark was null.

## 8. Declared secondaries, reported and never gating

1. **Mesenchymal-only.** The same analysis restricted to ASC signatures (1,776 compounds, one signature each). ASC is named explicitly, not selected by a lineage field: the library's cell-line metadata is unreliable (HME1 is recorded as leukemia, OCILY10 as placenta), and the library holds no fibroblast line. PD-0325901 has one ASC signature per identifier.
2. **The MEK1/2 class**, scored as the median of its drugs' percentiles, against draws of the same structure.
3. **GSE95065** as a sensitivity query.
4. **Per query:** each identifier's score and percentile, the exact-zero fraction of the library, and which identifiers sit on the tied block.
5. **Reference compounds.**

**Why the mesenchymal analysis is secondary.** It rests on a single signature per identifier, and a single signature scores exactly zero far more often than a median over many. Keeping the published primary also means the instrument is used unchanged.

## 9. A control that can void a query

Before any rank is printed for a query, its healthy controls are split at random into two halves 20 times (seed 12345 plus the split number). Each split is scored as a query and its library ranking is correlated with the ranking from the real signature. If the median correlation exceeds 0.5, that query is void and its ranks are not reported. If more than half the splits return an undefined correlation, the control is inconclusive and the query is not reported.

## 10. Order of operations

1. This file is committed with a SHA-256 hash.
2. Phase B1 builds rosters, signatures and compound identifiers, and freezes them with a hash. No score.
3. The freeze report is read before scoring.
4. Phase B2 scores, locked to the frozen hash.
5. Phase B3 runs the secondaries.

Any departure is written as a dated addendum before scoring.
