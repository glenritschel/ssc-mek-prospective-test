# The instrument declined to score it: a pre-registered prospective test of MEK inhibition in systemic sclerosis skin, and an explanation that did not survive its own control

**Glen Charles Ritschel**  
Ritschel Research, Tega Cay, South Carolina, USA  
ORCID 0009-0006-5341-8840  

**Version 1, 2026-10-02.**

---

## Abstract

A published connectivity pipeline, benchmarked retrospectively and reported as a null at n = 7 (p = 0.098), was used once, prospectively, on a question it had not been built for. The hypothesis was that MEK/ERK inhibition reverses a systemic sclerosis skin signature, and the test was whether PD-0325901 ranks among the reversers of whole-skin patient-versus-control signatures from two cohorts that played no part in generating that hypothesis.

The pre-registration was committed with a SHA-256 hash before any disease signature or any score existed. It fixed one condition: a permutation p below 0.05 on the drug's mean percentile across the primary queries, against 10,000 draws of two library identifiers. It named the cohorts in advance, excluded the hypothesis-generating data by design, and specified a control capable of voiding a query before anything was scored.

**The criterion was not met, p = 0.354.** More consequentially, **the pipeline returned a connectivity score of exactly zero for 45.6% and 51.2% of the library in the two primary queries**, and both identifiers of the test compound returned exact zero in the second, so its percentile there was a constant that no compound-specific signal could have moved. The pre-registration had fixed that case in advance as uninformative rather than negative. In the first query the tied block holds 15 of the 18 declared compounds, including all four reference compounds, which return the same number as one another.

A declared mesenchymal-only secondary is likewise uninformative: both identifiers sit on the tied block in all three queries.

**One claim is reported and then withdrawn inside this document.** The mesenchymal subset showed a lower exact-zero rate than the full library, which was written up as evidence that the pipeline's median-over-signatures rule inflates the tie rate by about fifteen points. That comparison confounds two differences. A control holding cell-line composition fixed, run on ten queries, measures the pooling effect at a median of **+0.46 percentage points**, positive in 7 of 10 and never above +2.52. The claim is wrong. The effect belongs to the cell line.

The result does not show that MEK inhibition fails in systemic sclerosis. It shows that this instrument, on these cohorts, could not address the question, and it supplies a sharper reason for caution about transcriptomic connectivity screening than the retrospective null did.

---

## 1. What was tested, and what was not

The MEK/ERK hypothesis in this program originated in a myofibroblast cluster signature derived from one single-cell dataset. A hypothesis generated from a dataset cannot be tested on that dataset, so the two series behind it, GSE138669 and GSE195452, were **excluded by design and never fetched**. Nothing in this report touches them, and a negative here is not a negative on that cluster analysis, which remains untested.

What is tested is narrower and prospective: whether an independent, whole-skin, patient-versus-control signature places PD-0325901 among the compounds the pipeline scores as reversing it. The pipeline is the one deposited with the retrospective benchmark (concept DOI 10.5281/zenodo.23071560), used unchanged. No parameter was tuned for this question, and the scoring function used here was verified against the deposited implementation to the bit on 3,000 library signatures before any query was scored.

**This is one prospective test of one compound on an instrument whose own benchmark was null.** It is not a benchmark, and the sample size of the claim is one.

## 2. Order of operations, and what each step was allowed to see

| phase | what it did | artifact |
|---|---|---|
| pre-registration | committed before any signature or score existed | `45de35e2…c3a4c9` |
| B1 | built rosters, signatures and compound identifiers, froze them, scored nothing | `c083e3cf…c8301` |
| B2 | ran the voiding control, then the primary | `ed250b76…c4b6a8` |
| B3 | ran the declared secondaries | `3a14ff0d…6049a` |
| C | ran the pooling control described in Section 8 | `b7dda80a…dd80b` |

Each phase asserts the hash of the previous phase's output before it runs, and B3 reproduced all 54 of B2's recorded identifier percentiles to a worst difference of exactly 0.00e+00 before restricting anything. The pre-registration is reproduced in the deposit; it is not paraphrased here, because a paraphrase of a pre-registration is not one.

## 3. Queries

Group membership was read by field name across all sample characteristics lines, never by line position, and one biopsy per person was taken. Expected arm sizes were stated in the pre-registration and the run was required to stop if either arm differed.

| | series | cohort | cases | controls | usable landmarks |
|---|---|---|---|---|---|
| **Q1** | GSE181549 | GENISOS registry, one-channel Agilent | 113 | 44 | 969 |
| **Q2** | GSE130955 | PRESS registry, RNA-seq | 48 | 33 | 978 |
| **S1** | GSE95065 | sensitivity only, never gating | 18 | 15 | 963 |

**Not used, with the reason fixed before any score.** GSE58095 draws on the same registry as Q1, and where two series share a registry the larger is taken. Six two-channel reference-design series were dropped because the orientation of the deposited ratio differs between deposits and several carry group labels only in free text, so a sign error there would invert the contrast silently.

**S1 is reported and never gating, and the reason matters later.** It was deposited by the laboratory that deposited the hypothesis-generating data, so overlap of individuals cannot be ruled out from the deposits.

**⛔ Q2's deposit is not counts, and the write-up must not call it counts.** Of the first sample file's 60,468 values, 41.0% are whole numbers, and per-sample sums run 774,224 / 979,354 / 1,299,823. A raw-count library is 1e7 or more and a transcripts-per-million column sums to exactly 1e6. This is a per-kilobase normalized deposit. The pre-registered transformation was applied unchanged, and gene length cancels in a per-gene case-versus-control contrast, so the analysis is unaffected. The description would have been wrong.

## 4. The control that can void a query

Before any rank was reported, each query's healthy controls were split at random into two halves twenty times, each split scored as a query, and its library ranking correlated with the ranking from the real signature. A median correlation above 0.5 voids the query.

| | split | median rho | range | undefined |
|---|---|---|---|---|
| Q1 | 22/22 | −0.0879 | −0.299 to 0.173 | 0 |
| Q2 | 16/17 | −0.0786 | −0.246 to 0.212 | 0 |
| S1 | 7/8 | +0.0993 | −0.517 to 0.537 | 0 |

**Neither primary query was voided and both were scored**, so nothing was dropped on the way to the result.

## 5. Result

**The criterion was not met.**

| | value |
|---|---|
| PD-0325901 in Q1 | 0.3561 |
| PD-0325901 in Q2 | 0.5051 |
| observed mean percentile | 0.4306 |
| null | mean 0.5013, sd 0.1636, 10,000 draws |
| **permutation p** | **0.354** |

Percentiles are ascending, so the strongest reversal is lowest, and ties take the midrank.

## 6. ⛔ Half the statistic was a constant, and the pre-registration said so in advance

The connectivity statistic returns **exactly zero** when a query's up and down gene sets enrich in the same direction. That is not a measurement of no effect. It is a refusal to measure.

| | exact-zero fraction | tied block at |
|---|---|---|
| Q1 | 0.456 | 0.4835 |
| Q2 | 0.512 | 0.5051 |
| S1 | 0.421 | 0.4942 |

**In Q2 both PD-0325901 identifiers returned exact zero.** Its Q2 percentile of 0.5051 *is* the tied block, a constant that no compound-specific signal could have moved, and it contributes half of the primary statistic. Section 7 of the pre-registration anticipated this case and fixed its reading in advance: a drug sitting on the tied block has a percentile near 0.5, the criterion cannot be met, and the result is reported as uninformative rather than negative. That clause applies to Q2 in full. It does not apply to Q1, where one identifier escaped the block at 0.2286 while the other sat on it.

**The defensible statement is therefore narrow.** Under this pipeline and these two cohorts, PD-0325901 is not distinguishable from a random pair of library compounds, and roughly half the reason is that the pipeline declined to score it.

**This is not a property of the test compound.** In Q1 the tied block holds 15 of the 18 declared identifiers and in Q2 it holds 15 of 18. Among them are all four reference compounds, dasatinib, bosutinib, nintedanib and mycophenolate mofetil, which return the same number as one another in both primary queries. A ranking that cannot separate those four is not resolving compounds, and any percentile read off it carries less information than its three decimal places suggest.

## 7. The declared secondaries

| secondary | result |
|---|---|
| MEK1/2 class over Q1 and Q2, 11 drugs in 14 identifiers | statistic 0.4943, null 0.4962, **p = 0.913** |
| mesenchymal-only (ASC), PD-0325901 | statistic 0.4904, null 0.4989, **p = 0.490** |
| mesenchymal-only (ASC), MEK1/2 class | statistic 0.4357, null 0.4988, **p = 0.334** |

**The mesenchymal secondary is uninformative rather than negative, for the same reason as Q2.** Both PD-0325901 identifiers sit on the ASC tied block in all three queries: 0.4505 in Q1, 0.5304 in Q2, 0.4586 in S1, each exactly the block. The compound was never resolved in that subset, and p = 0.490 is what non-resolution produces. The ASC class figure rests on 4 of the 10 class drugs, since the other six have no ASC signature at all.

**One pre-registered quantity was checked rather than repeated and is correct.** The library holds exactly 1,776 ASC compounds with exactly one signature each. The row-to-cell-line mapping was rebuilt from the reference matrix's own column identifiers and asserted equal to the frozen library's compound array element for element before any subsetting.

## 8. ⛔ A claim made in this work, and withdrawn in it

The mesenchymal subset showed a **lower** exact-zero fraction than the full library in both primaries, 0.304 against 0.456 and 0.372 against 0.512. This was written up, in the program's own result record on 2026-10-02 at 11:22, as a measured property of the pipeline: that taking a median across a compound's many signatures raises the tie rate by about fifteen points, because the median of a set that is roughly half zeros is itself zero.

**The comparison cannot support that claim, and the claim is wrong.** The mesenchymal subset differs from the full library in two ways at once: one signature per compound, and one cell line of fifty-eight. Nothing separated them. The sensitivity query, where the difference ran the other way, was the signal that something else was happening.

The control that separates them draws **one signature per compound at random from the full library**, which holds cell-line composition at the library's own. It was run on ten queries, the seven deposited benchmark rows and the three here, with its criterion fixed before any number existed: the pooling effect is accepted only if positive in at least 8 of 10 queries with a median of at least +5.0 percentage points.

| | pooling effect | cell-line effect |
|---|---|---|
| 7 benchmark rows | −0.42 to +0.94 | −9.83 to +6.04 |
| Q1 | +2.23 | −15.39 |
| Q2 | +2.52 | −13.52 |
| S1 | +0.32 | +2.03 |
| **all 10** | **positive in 7, median +0.46** | **median −1.84** |

**Not met. The pooling effect is nil**, and the entire difference was the cell line. The claim is withdrawn rather than softened, and no addendum to the deposited benchmark follows from it: the benchmark's decision to take a median over signatures costs nothing measurable in resolution.

**Why the wrong claim was convincing, since the mechanism will recur.** The arithmetic argument sounds airtight, and it reproduced: on a synthetic noise fixture built to test the control's own code, the pooling effect appeared at about +13 points. It vanishes on the real library because a compound's signatures are not independent draws and the condition that produces an exact zero is correlated across them. **A mechanism that reproduces on simulated data and disappears on real data is not an explanation. It is a coincidence that survived one check.**

**The cell-line effect is recorded here and deliberately not promoted.** It is large, it is query-dependent, and in both skin queries the mesenchymal line resolves substantially more compounds than a random library signature does. It is also unregistered, and it came out of a run whose purpose was to retire a different claim. Replacing a withdrawn finding with a fresh post-hoc one from the same output is the error this report would be committing. If it is worth anything, it needs its own pre-registration.

## 9. Post-hoc description, carrying no inference

Two quantities below were computed after the result was seen. They have no p-values, they cannot rescue or damage any pre-registered conclusion, and they are reported because the alternative is to leave an obvious question unexamined while implying it was never asked.

The run left one ambiguity. S1, the cohort sharing a depositing laboratory with the hypothesis-generating data, was the only query in which the MEK class reversed strongly (class median 0.1860 against the tied block in both independent cohorts). Either the signal attaches to that laboratory's cohorts, or S1 is simply the query that resolves compounds at all.

Ranking **only the compounds that scored nonzero** separates the readings.

| | compounds resolved | PD-0325901 | MEK class | class drugs resolved |
|---|---|---|---|---|
| Q1 | 54.4% | 0.4206 (1 of 2 ids) | 0.2731 | 2 of 10 |
| Q2 | 48.8% | not resolved | 0.4591 | 3 of 10 |
| S1 | 57.9% | 0.3472 (1 of 2 ids) | 0.2475 | 7 of 10 |

**Once ties are removed, S1 and Q1 place the MEK class in nearly the same position**, 0.2475 against 0.2731. What differed was how many class members the instrument resolved at all, seven against two. The apparent S1-only signal is therefore mostly resolution rather than evidence of laboratory specificity. Q2 does not follow the pattern, which is a real limit on the reading, and the whole quantity is descriptive.

## 10. Errors made in producing this work

Reported rather than removed, on the same principle as the preceding work.

**A claim asserted, then withdrawn by its own control.** Section 8. It was written up as a measured property of the pipeline before the comparison behind it had been checked for confounding, and it reached a program result record in that form. The interval between assertion and correction was three minutes, and the interval between correction and disproof was twenty. Neither interval is the point. The point is that it was written as a finding at all.

**A cached file accepted on its filename.** The first signature-freeze run read a platform annotation file by checking only that the name existed. The file present was a leftover with no annotation table in it, and the run failed on a downstream assertion rather than on the wrong check. Fixed by validating file contents, trying three sources, reporting each rejection with its first 120 characters, and recording in the freeze which source was used.

**A test harness that supplied what the notebook was required to supply.** The scoring notebook never built the landmark gene maps, and its integration test could not detect this because the harness injected those maps into the namespace. The omission surfaced only when the notebook was run by hand. The harness was rewritten to inject only what the environment cannot provide, and the notebook now builds and asserts its own maps.

**A guard that could not fire, recorded because it looked like it had passed.** A control meant to confirm that a row-order assertion would catch a scrambled axis permuted that axis with a cyclic shift. A cyclic shift preserves the relative order of the identifiers, so the assertion correctly stayed silent, and the silence was nearly recorded as a successful guard. **A check that returns a negative result has not verified anything until the check itself has been shown capable of returning a positive one**, and that standard applies to the checks on the checks.

**A write-back that reported success and did not occur.** A corrected result record was written to disk, the write returned success, and the file on disk was unchanged. It was caught by hashing the file after writing rather than trusting the return value.

## 11. What this does not show

It does not show that MEK inhibition fails in systemic sclerosis. It does not test the myofibroblast cluster analysis that generated the hypothesis, whose source data was excluded by design and never fetched. It is one compound, two cohorts, one instrument.

What it adds to that instrument's record is sharper than the retrospective null. On two independent patient cohorts the pipeline declined to score roughly half the library, every reference compound landed on the same number as every other, and the compound under test was unresolvable in one of the two primary queries and in the mesenchymal subset entirely. **A screening instrument that cannot distinguish dasatinib from mycophenolate mofetil against a disease signature is not producing a ranking that a reader should act on, whatever p-value accompanies it.**

## Data and code availability

The pre-registration, the frozen signature and compound inputs, the four phase notebooks, the three phase result records and a SHA-256 manifest covering every file are deposited with this version. Every hash quoted in this document refers to a file in that deposit. The reference library derives from the CMap LINCS 2020 release and the scoring implementation is the one deposited under concept DOI 10.5281/zenodo.23071560, reused without modification and verified against it. Disease transcriptomic series are identified by public accession above.

## Author contributions and disclosure

Sole author. Prepared with AI assistance. All reported figures are produced by the accompanying code and every measured quantity in this report was computed rather than recalled.

The author holds filed provisional patent applications in therapeutic areas adjacent to the application domain discussed here. No claim in those applications depends on any result reported in this document, and no result in this document is favorable to them.
