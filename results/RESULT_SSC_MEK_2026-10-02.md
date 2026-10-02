# Result: the pre-registered SSc skin / MEK test, complete through Phase B3

**Pre-registration** `45de35e26156bf1c70d22bc9100adaeec30f3fc4e70b803e075c124960c3a4c9`, committed 2026-10-01 22:24 EDT, before any signature or score existed.
**Frozen inputs** `c083e3cfb23cca67b26e772d8435b138d982db02bf74347ad13053c6c42e8301` (B1).
**Primary result** `ed250b767fe831f4c78b9c06b4a09e114669ea6db71fd40b8a397f318cb4c6a8` (B2, 2026-10-01).
**Secondary result** `3a14ff0d7189482fcc2453535fd0435450ae78729c502d9803f05321e346049a` (B3, 2026-10-02).
**Pooling control** `b7dda80ae4d25c80e7f853e7b25a32429f2a82ac07d848c605a5c7d7190dd80b` (C, 2026-10-02).

Every phase in Section 10 of the pre-registration has now run. Nothing remains unexecuted.

---

## 1. The criterion

**NOT MET.** One condition was pre-registered: permutation p < 0.05 on PD-0325901's mean percentile across the surviving primary queries, against 10,000 draws of two distinct library identifiers.

| | value |
|---|---|
| PD-0325901 in Q1 (GSE181549, GENISOS, 113 vs 44) | 0.3561 |
| PD-0325901 in Q2 (GSE130955, PRESS, 48 vs 33) | 0.5051 |
| observed mean percentile | 0.4306 |
| null | mean 0.5013, sd 0.1636 |
| **permutation p** | **0.354** |

Both primary queries survived the Section 9 control (median rho −0.0879 and −0.0786, zero undefined), so nothing was dropped on the way to this number.

## 2. The result is half uninformative, not wholly negative, and the pre-registration said so in advance

The instrument returned **exactly zero** for 45.6% of the library in Q1 and 51.2% in Q2. An exact zero is what the two-tailed Lamb statistic gives when the up and down tails enrich in the same direction: not a measurement of no effect, but a refusal to measure.

In Q2, **both** PD-0325901 identifiers returned exact zero. Its Q2 percentile, 0.5051, *is* the tied block, a constant no compound-specific signal could have moved. Pre-registration Section 7 fixed that reading in advance: "the result is reported as uninformative, not as a negative." The clause applies to Q2 in full. It does not apply to Q1, where one identifier escaped the block at 0.2286 while the other sat on it.

**The defensible statement is narrow:** under this pipeline and these two independent cohorts, PD-0325901 is not distinguishable from a random pair of library compounds, and roughly half the reason is that the pipeline declined to score it.

The tied block is not a PD-0325901 problem. In Q1 it holds 15 of the 18 declared identifiers, including all four reference compounds; in Q2, 15 of 18. A test in which dasatinib, bosutinib, nintedanib and mycophenolate mofetil all return the same number is not resolving compounds.

## 3. The declared secondaries, all run

| secondary | result |
|---|---|
| MEK1/2 class over Q1 and Q2 (full library) | statistic 0.4943, null 0.4962, **p = 0.913** |
| **Mesenchymal-only (ASC), PD-0325901** | statistic 0.4904, null 0.4989, **p = 0.490** |
| **Mesenchymal-only (ASC), MEK1/2 class** | statistic 0.4357, null 0.4988, **p = 0.334** |
| S1 (GSE95065) sensitivity, never gating | PD-0325901 0.3476; class median 0.1860 |

**The ASC secondary is uninformative for PD-0325901, and that is a statement about the instrument, not a second negative.** Both identifiers sit on the ASC tied block in **all three** queries: 0.4505 in Q1, 0.5304 in Q2, 0.4586 in S1, each exactly the tied-block percentile. The compound was never resolved in the mesenchymal subset at all, so p = 0.490 is what that non-resolution produces and nothing more.

The ASC class figure rests on **4 of the 10 class drugs**; the other six have no ASC signature. It is reported for completeness and carries little.

**One pre-registered fact checked rather than repeated and found correct:** the library holds exactly **1,776 ASC compounds with exactly one signature each**, as Section 8 stated. The row-to-cell-line mapping was rebuilt from the gctx column identifiers and asserted equal to the frozen library's compound array element for element before any subsetting.

## 4. WITHDRAWN. The tie-rate claim was wrong, and Phase C says so

**This section asserted, on 2026-10-02 at 11:22, that the median-over-signatures rule raises the exact-zero rate by about fifteen points. That claim is withdrawn in full.** It was marked confounded at 11:25 and tested at 11:45. It does not survive.

**Phase C**, result `b7dda80ae4d25c80e7f853e7b25a32429f2a82ac07d848c605a5c7d7190dd80b`, measured three quantities on 10 queries: the 7 deposited benchmark rows and the 3 SSc-MEK queries. The control was one signature per compound drawn at random from the full library, which holds cell-line composition at the library's own, so pooling could be separated from cell line instead of being measured together with it. The criterion was fixed in the notebook before any number existed: positive in at least 8 of 10 queries and a median of at least +5.0 points.

| | pooling effect (pooled minus random-single) | cell-line effect (ASC minus random-single) |
|---|---|---|
| 7 benchmark rows | −0.42 to +0.94 | −9.83 to +6.04 |
| SSc Q1 | +2.23 | −15.39 |
| SSc Q2 | +2.52 | −13.52 |
| SSc S1 | +0.32 | +2.03 |
| **across all 10** | **positive in 7, median +0.46** | **median −1.84** |

**CRITERION NOT MET.** The pooling effect is nil. The largest value anywhere is +2.52 points and the median is under half a point, against a claim of fifteen. **The entire B3 gap was the cell line**, and the pre-registration's original reasoning in Section 8 is neither confirmed nor refuted here, because the comparison that appeared to refute it was never measuring pooling at all.

**What this says about the error.** The arithmetic argument was persuasive and wrong: a median over a set that is roughly half zeros *sounds* like it must be zero more often, and on a synthetic noise fixture it was, by about thirteen points. On the real library it is not, because a compound's signatures are not independent draws and the zero-producing condition is correlated across them. **A mechanism that reproduces on simulated data and vanishes on real data is not an explanation; it is a coincidence that survived one check.**

**No benchmark addendum follows from this.** The deposited benchmark's decision to take a median over signatures costs nothing measurable in resolution, which is the opposite of what Section 4 claimed and is worth nothing to anyone as a publication.

**An observation from the control run, recorded and NOT promoted.** The cell-line effect is large and query-dependent, from −15.39 to +6.04 points, and in both SSc skin queries the ASC line resolves substantially more compounds than a random library signature does. That is the quantity that actually moved. **It is not a finding.** It comes from a run whose purpose was to retire a different claim, it was not specified in advance, and nothing is built on it. If it is worth anything it needs its own pre-registered test, and replacing a withdrawn claim with a fresh post-hoc one from the same output is precisely the move this program exists to refuse.

## 5. The S1 ambiguity, answered descriptively and in the direction of resolution

B2 left a question open. S1 is the cohort sharing a depositing laboratory with the P01 source data, and it was the only query where the MEK class reversed strongly (class median 0.1860 against the tied block in both independent cohorts). Two explanations fit: the signal attaches to that laboratory's cohorts, or S1 is simply the query that resolves compounds at all.

The post-hoc ranking among **only the compounds that scored nonzero** separates them. **This is descriptive, was computed after the result was seen, carries no p-value, and cannot rescue or damage any pre-registered conclusion.**

| | compounds resolved | PD-0325901 | MEK class | class drugs resolved |
|---|---|---|---|---|
| Q1 | 54.4% | 0.4206 (1 of 2 ids) | 0.2731 | 2 of 10 |
| Q2 | 48.8% | not resolved | 0.4591 | 3 of 10 |
| S1 | 57.9% | 0.3472 (1 of 2 ids) | 0.2475 | 7 of 10 |

**Once the ties are removed, S1 and Q1 put the MEK class in nearly the same place: 0.2475 and 0.2731.** What differed was how many class members the instrument resolved at all, seven against two. The apparent S1-only signal is therefore largely an artifact of resolution rather than evidence that the MEK result is specific to one laboratory's cohorts.

**Two limits on that reading, both real.** Q2 does not follow the pattern: its resolved class sits at 0.4591, near the middle. And this is a description computed after seeing the outcome, so it settles nothing. It does, however, remove the most alarming interpretation available after B2, which is worth recording precisely because it is the interpretation that would have been convenient to leave unexamined.

**Not a finding, recorded so it is not rediscovered as one:** in the ASC subset of Q1, dasatinib ranks at 0.0397 and PD-184352 at 0.0724. Dasatinib is a declared reference compound, not a hypothesis, and one signature in one cell line in one cohort is not evidence of anything.

## 6. Carried forward to any write-up

- **Q2's deposit is not counts.** 41.0% of the first file's 60,468 values are whole numbers, and per-sample sums run 774,224 / 979,354 / 1,299,823. A raw-count library is 1e7 or more; a TPM column sums to exactly 1e6. This is a per-kilobase normalized deposit. The pre-registered transformation was applied unchanged and gene length cancels in a per-gene contrast, but the write-up must not call these counts.
- **Section 4 is withdrawn and there is no benchmark addendum.** Phase C settled it. Nothing in the write-up may carry the tie-rate claim forward in any softened form.
- **Two defects were caught during execution and both were the same class**: a cached platform annotation accepted on its filename with no table in it, and a test harness that supplied the gene maps the notebook was required to build itself. Both were checks that could not have failed. The second was caught only because the notebook broke in Glen's hands.

## 7. What this does not show

It does not show that MEK inhibition fails in systemic sclerosis. It does not test the P01 myofibroblast-cluster analysis, whose source data was excluded by design and never fetched. It is one prospective test of one compound on an instrument whose own retrospective benchmark was null at n = 7, p = 0.098.

What it adds to that instrument's record is sharper than the n = 7 null: on two independent SSc cohorts the pipeline declined to score roughly half the library, and every reference compound landed on the same number. The pooling rule the benchmark fixed in advance is **not** responsible for that, and this document said otherwise in its first version. A control holding cell-line composition fixed puts the pooling effect at a median of +0.46 points across ten queries. The exact-zero rate is a property of the two-tailed score on this library, not of the median-over-signatures step.
