# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:51+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Tag_Status.vi Help\Tag_Status.vi.html`
Document SHA-256: `62de816e86cbab75c2d7e8a488481e096ad6cbfc59584f771f4aa85e68a08fb2`

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
| Combined prose | 364 | 31 | 581 | 7.82 | below |
| Purpose and scope | 49 | 5 | 83 | 8.22 | within |
| Called function and library selection | 68 | 5 | 106 | 8.11 | within |
| Inputs | 12 | 2 | 21 | 7.4 | below |
| Outputs and error handling | 41 | 3 | 64 | 8.16 | within |
| Execution and C implementation | 68 | 6 | 112 | 8.27 | within |
| Example and recommended call sequence | 81 | 7 | 117 | 5.97 | below |
| Library version differences | 45 | 3 | 78 | 10.71 | above |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> Returns the current library status of an existing tag.

Density assessment: The operation and existing-tag prerequisite are stated before the version caveat.

### Assessed text

Unit `unit-1`: grade 8.9; 9 words, 1 sentences, 16 syllables; below the failure threshold. Short sample.

> Returns the current library status of an existing tag.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Called function and library selection

### Review discussion

Section assessment: The section gives the native prototype, C convention, UI thread and runtime library selector.

Reading-level review: **PASS** — All measured units are below grade 12. Code and table rows were excluded from numerical scoring but read for meaning; short samples limit the score.

Most demanding passage (unit-5):

> The node uses the C calling convention and runs in the LabVIEW user interface (UI) thread.

Density assessment: The native prototype precedes its saved node settings and path source.

### Assessed text

Unit `unit-5`: grade 7.36; 23 words, 2 sentences, 36 syllables; below the failure threshold. Short sample.

> The node uses the C calling convention and runs in the LabVIEW user interface (UI) thread. Its numeric arguments are passed by value.

Unit `unit-6`: grade 8.62; 45 words, 3 sentences, 70 syllables; below the failure threshold.

> Choose_Lib.vi receives the incoming error and supplies the path and its error output to the library node. Its target cases select plctag32.dll, plctag64.dll or libplctag64.so under the application directory. The default target case returns an empty path.

### Exclusions from the score

- Unit `unit-3`: Unterminated fragment; check selection manually.
- Unit `unit-4`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Inputs

### Review discussion

Section assessment: The input table gives the signed 32-bit tag handle, incoming error and wiring guidance.

Reading-level review: **PASS** — All measured units are below grade 12. Code and table rows were excluded from numerical scoring but read for meaning; short samples limit the score.

Most demanding passage (unit-9):

> Signed 32-bit tag identifier from a successful tag creation.

Density assessment: The row explains the handle origin and signed width next to the exact LabVIEW type.

### Assessed text

Unit `unit-7`: grade 7.4; 12 words, 2 sentences, 21 syllables; below the failure threshold. Short sample.

> Connected terminals are marked recommended. Wire the values needed for the call.

### Exclusions from the score

- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'I32 is explained as signed 32-bit in the input row.'}

## Outputs and error handling

### Review discussion

Section assessment: The outputs distinguish the pass-through handle, native status and LabVIEW error, including the skipped-call caveat.

Reading-level review: **PASS** — All measured units are below grade 12. Code and table rows were excluded from numerical scoring but read for meaning; short samples limit the score.

Most demanding passage (unit-15):

> A numeric result is not proof of a completed call when an incoming LabVIEW error skipped the node.

Density assessment: The result channels are introduced before this condition.

### Assessed text

Unit `unit-15`: grade 8.16; 41 words, 3 sentences, 64 syllables; below the failure threshold.

> Check error out first, then the native result. The wrapper does not convert a negative native return into a LabVIEW error-cluster error. A numeric result is not proof of a completed call when an incoming LabVIEW error skipped the node.

### Exclusions from the score

- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-12`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-13`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Execution and C implementation

### Review discussion

Section assessment: The native sequence describes lookup, mutex, protocol progress and status, return codes and the setter caveat.

Reading-level review: **PASS** — All measured units are below grade 12. Code and table rows were excluded from numerical scoring but read for meaning; short samples limit the score.

Most demanding passage (unit-16):

> This status is not a substitute for the raw result of a prior setter.

Density assessment: The paragraph first explains the returned current protocol status and then limits its use for earlier local setter failures.

### Assessed text

Unit `unit-16`: grade 8.27; 68 words, 6 sentences, 112 syllables; below the failure threshold.

> The legacy function looks up the tag and takes its internal mutex. It runs the protocol progress routine when available and requests its protocol-specific status. It then releases the mutex and its temporary tag reference. It returns 0 for OK, 1 for pending, or a negative library error. A missing handle returns -19. This status is not a substitute for the raw result of a prior setter.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: OK may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'OK is the exact success-status label.'}

## Example and recommended call sequence

### Review discussion

Section assessment: The example shows pending code 1 followed by an OK result and recommends bounded polling with a delay.

Reading-level review: **PASS** — All measured units are below grade 12. Code and table rows were excluded from numerical scoring but read for meaning; short samples limit the score.

Most demanding passage (unit-17):

> If error out is clear and this VI returns 1, the tag remains pending.

Density assessment: The preceding sentence supplies a pending read and the same valid handle before interpreting this status.

### Assessed text

Unit `unit-17`: grade 5.82; 39 words, 3 sentences, 54 syllables; below the failure threshold.

> For example, if a read returns code 1, call this VI with the same valid handle. If error out is clear and this VI returns 1, the tag remains pending. A later clear error and code 0 reports OK.

Unit `unit-18`: grade 6.21; 42 words, 4 sentences, 63 syllables; below the failure threshold.

> A create, read or write can return pending. Check error out before using each raw result. Call this VI with a delay between checks until it returns a final code, or until the application stops waiting. A negative code reports an error.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW audience.'}

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, an invalid negative handle is returned as that negative value. An unknown nonnegative handle returns PLCTAG_ERR_NOT_FOUND (-19). For a valid tag, the status routine reports pending while a read or write is marked in flight.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-19):

> In the checked upstream 2.7.2 source, an invalid negative handle is returned as that negative value. An unknown nonnegative handle returns PLCTAG_ERR_NOT_FOUND (-19). For a valid tag, the status routine reports pending while a read or write is marked in flight.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-19`: grade 10.71; 45 words, 3 sentences, 78 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, an invalid negative handle is returned as that negative value. An unknown nonnegative handle returns PLCTAG_ERR_NOT_FOUND (-19). For a valid tag, the status routine reports pending while a read or write is marked in flight.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The saved HTML distinguishes current native status, a prior setter result and the separate LabVIEW error. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A caller can check an ongoing operation without mistaking a skipped node for success. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
