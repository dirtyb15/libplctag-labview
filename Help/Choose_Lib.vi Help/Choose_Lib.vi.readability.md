# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:41+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Choose_Lib.vi Help\Choose_Lib.vi.html`
Document SHA-256: `958fd6da7c4db42157263943f722fd49282eaf5d24028a4182f98f80f61458f8`

Audience: LabVIEW developer using this control or VI
Prerequisites: Basic LabVIEW dataflow and error clusters
Scope: Current document.
Reviewer: Codex

Tool: approachable-fk/2.0 (English heuristic; one syllable per numeric token)
Target: near ninth grade; 8.0–10.0 is an advisory band. Each measured prose unit at or above 12 fails the numerical check (unrounded comparison).
Numeric tokens count as one word and one syllable. Technical names remain in the score.
This is a writing preference, not a government or Navy requirement.

Estimated English syllables; punctuation cannot prove grammatical completeness. Numeric tokens count as one word and one syllable by local convention, not pronunciation. Review selected text, abbreviations, identifiers, and technical pronunciations. Short samples are unstable. Scores do not measure comprehension or accuracy.

## Numerical check and blockers

Measured prose units: 10; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 529 | 42 | 850 | 8.28 | within |
| Purpose and scope | 95 | 8 | 153 | 8.05 | within |
| Called VIs and dependencies | 87 | 8 | 155 | 9.67 | within |
| Inputs | 9 | 1 | 14 | 6.28 | below |
| Outputs and error handling | 140 | 9 | 210 | 8.18 | within |
| Execution | 151 | 13 | 245 | 8.09 | within |
| Example and recommended call sequence | 47 | 3 | 73 | 8.85 | within |

## Purpose and scope

### Review discussion

Section assessment: The current selector wiring was rechecked: first call computes the path, while later calls return the retained path and pass their incoming error.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> The VI retains the selected path for later calls in the same execution instance.

Density assessment: Retained state is the most advanced relationship in this opening; the output and wrapper context come first.

### Assessed text

Unit `unit-1`: grade 8.22; 55 words, 4 sentences, 86 syllables; below the failure threshold.

> Choose_Lib.vi builds a path to the libplctag shared library for the current LabVIEW target operating system (OS). Other wrapper VIs wire this path to their Call Library Function Nodes. The VI retains the selected path for later calls in the same execution instance. It does not load the library or contact a controller.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW developer audience.'}

## Called VIs and dependencies

### Review discussion

Section assessment: The current selector wiring was rechecked: first call computes the path, while later calls return the retained path and pass their incoming error.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-3):

> The selected path is kept in an uninitialized shift register for later calls.

Density assessment: The paragraph introduces First Call? and target selection before explaining how the result is retained.

### Assessed text

Unit `unit-3`: grade 9.31; 50 words, 5 sentences, 89 syllables; below the failure threshold.

> On the first call of an execution instance, First Call? selects the initialization case. That case reads the application target operating system. Each supported target case gets Application Directory.vi and appends a filename with Build Path. The selected path is kept in an uninitialized shift register for later calls.

Unit `unit-9`: grade 10.27; 37 words, 3 sentences, 66 syllables; below the failure threshold.

> The Windows 95/NT case is the legacy 32-bit Windows target case. The exact path depends on the directory returned by Application Directory.vi in the running environment. Place the matching binary in that resolved directory.

### Exclusions from the score

- Unit `unit-4`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-5`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-6`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-7`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: NT may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'Windows 95/NT is the exact saved target-case label and is followed by the legacy 32-bit explanation.'}

## Inputs

### Review discussion

Section assessment: The current selector wiring was rechecked: first call computes the path, while later calls return the retained path and pass their incoming error.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-12):

> LabVIEW supplies the target OS and the base folder.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-12`: grade 6.28; 9 words, 1 sentences, 14 syllables; below the failure threshold. Short sample.

> LabVIEW supplies the target OS and the base folder.

### Exclusions from the score

- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Outputs and error handling

### Review discussion

Section assessment: The current selector wiring was rechecked: first call computes the path, while later calls return the retained path and pass their incoming error.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-16):

> The VI does not check that the resulting file exists, matches the process architecture or exports the desired function. Check both error out and the path; the default target case can return an empty path without creating an error. A caller's library node can also report an error when loading or calling the path.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-16`: grade 9.35; 54 words, 3 sentences, 82 syllables; below the failure threshold.

> The VI does not check that the resulting file exists, matches the process architecture or exports the desired function. Check both error out and the path; the default target case can return an empty path without creating an error. A caller's library node can also report an error when loading or calling the path.

Unit `unit-17`: grade 7.56; 86 words, 6 sentences, 128 syllables; below the failure threshold.

> The error shift register is initialized from the incoming cluster on each call. On the first call, the property node receives that cluster and returns its error output. Later calls pass their incoming error through while returning the retained path. The property error is not stored with the path. A clear error on a later call alone does not prove the retained path is valid. An error on the first call can prevent a valid selection, so initialize with a clear error and check both outputs.

### Exclusions from the score

- Unit `unit-13`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-15`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Execution

### Review discussion

Section assessment: The current selector wiring was rechecked: first call computes the path, while later calls return the retained path and pass their incoming error.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-19):

> The saved execution settings mark the VI as preallocated-clone reentrant and inline; retained state belongs to an execution instance.

Density assessment: This is the densest passage because it combines reentrancy and state scope; the prior sentences establish the loop and retained path.

### Assessed text

Unit `unit-18`: grade 9.94; 55 words, 4 sentences, 94 syllables; below the failure threshold.

> The VI uses First Call? to choose whether to calculate a path. When that function returns true, it passes the incoming error to the property node, reads the application target and selects the corresponding case. A supported case appends its fixed library filename to the application directory; the default target case produces an empty path.

Unit `unit-19`: grade 7.13; 96 words, 9 sentences, 151 syllables; below the failure threshold.

> A while loop has its stop-if-true terminal wired to true, so it runs once per call. The selected path is retained in an uninitialized shift register. When First Call? returns false, the VI uses that retained path instead of reading the target again. The saved execution settings mark the VI as preallocated-clone reentrant and inline; retained state belongs to an execution instance. Do not assume that all callers share one path cache. First Call? becomes true again according to the top-level caller's execution lifecycle. There is no search or alternate-library fallback.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The Windows x64 example identifies the selected file and tells the caller to check both sources of errors.

Reading-level review: **PASS** — All measured prose units in this section are below grade 12; table rows and exact identifiers are excluded from the numerical score but were read for meaning. Short samples limit the score as a measure of comprehension.

Most demanding passage (unit-20):

> For a Windows x64 target, the first-call selection appends plctag64.dll to the application directory.

Density assessment: The target and selected exact filename are a concrete instance of the preceding table.

### Assessed text

Unit `unit-20`: grade 8.85; 47 words, 3 sentences, 73 syllables; below the failure threshold.

> For a Windows x64 target, the first-call selection appends plctag64.dll to the application directory. Pass the output to the path input of the relevant Call Library Function Node. Check this VI's error out and the library node's error output when using the library.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The saved HTML text preserves target mappings, the error bypass, instance-retained path, one-iteration loop and the limits of path validation. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A LabVIEW developer can provide the error cluster, wire the resulting path, identify the relevant library and check both selector and call-node errors. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
