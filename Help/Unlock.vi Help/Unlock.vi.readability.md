# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:51+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Unlock.vi Help\Unlock.vi.html`
Document SHA-256: `f68d1e9ba10cb04da785b92ac197c8dbbfff3a9ea9388ce8bb4db190fd73d74b`

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

Measured prose units: 12; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 483 | 35 | 773 | 8.68 | within |
| Purpose and scope | 49 | 5 | 85 | 8.7 | within |
| Called function and library selection | 68 | 5 | 106 | 8.11 | within |
| Inputs | 12 | 2 | 21 | 7.4 | below |
| Outputs and error handling | 41 | 3 | 64 | 8.16 | within |
| Execution and C implementation | 160 | 11 | 253 | 8.74 | within |
| Example and recommended call sequence | 106 | 6 | 169 | 10.11 | above |
| Library version differences | 47 | 3 | 75 | 9.35 | within |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> Releases a tag's external mutex after a protected sequence.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-1`: grade 11.52; 9 words, 1 sentences, 18 syllables; below the failure threshold. Short sample.

> Releases a tag's external mutex after a protected sequence.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Called function and library selection

### Review discussion

Section assessment: The exact C declaration, node thread and calling convention, and dynamic library selector are given together.

Reading-level review: **PASS** — Every measured prose unit in this section is below grade 12. Code and table rows are numerical exclusions but were reviewed for exact semantics; short samples limit the score.

Most demanding passage (unit-6):

> Its target cases select plctag32.dll, plctag64.dll or libplctag64.so under the application directory.

Density assessment: The selector supplies the path and error before the filename cases are listed.

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

Section assessment: The input table lists the signed 32-bit handle and incoming error, with wiring and default guidance.

Reading-level review: **PASS** — Every measured prose unit in this section is below grade 12. Code and table rows are numerical exclusions but were reviewed for exact semantics; short samples limit the score.

Most demanding passage (unit-9):

> Signed 32-bit tag identifier from a successful tag creation.

Density assessment: The row couples the exact I32 LabVIEW type to its signed width and handle meaning.

### Assessed text

Unit `unit-7`: grade 7.4; 12 words, 2 sentences, 21 syllables; below the failure threshold. Short sample.

> Connected terminals are marked recommended. Wire the values needed for the call.

### Exclusions from the score

- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table explicitly describes I32 as a signed 32-bit value.'}

## Outputs and error handling

### Review discussion

Section assessment: The output table distinguishes the pass-through handle, native result and LabVIEW error.

Reading-level review: **PASS** — Every measured prose unit in this section is below grade 12. Code and table rows are numerical exclusions but were reviewed for exact semantics; short samples limit the score.

Most demanding passage (unit-15):

> A numeric result is not proof of a completed call when an incoming LabVIEW error skipped the node.

Density assessment: The skip condition follows the result-channel distinction and prevents an unsupported success inference.

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

Section assessment: The execution section explains native release, Windows thread ownership and recursion, Linux limits and the possible lock-order deadlock.

Reading-level review: **PASS** — Every measured prose unit in this section is below grade 12. Code and table rows are numerical exclusions but were reviewed for exact semantics; short samples limit the score.

Most demanding passage (unit-18):

> An unlock that needs that internal mutex can then be blocked, creating a deadlock.

Density assessment: The previous sentence identifies the competing lock and the internal mutex, making the dependency clear.

### Assessed text

Unit `unit-16`: grade 10.03; 43 words, 3 sentences, 73 syllables; below the failure threshold.

> The legacy function looks up the tag, takes its internal mutex and calls the external mutex unlock. It releases the internal mutex and its temporary tag reference afterward. -19 means the tag was not found; other negative codes can report an unlock failure.

Unit `unit-17`: grade 7.06; 70 words, 5 sentences, 102 syllables; below the failure threshold.

> On Windows, mutex ownership belongs to the operating-system thread. A thread that has acquired the same mutex more than once must release it the same number of times. This node runs on the LabVIEW UI thread, so do not assume it can release a lock acquired by a different native thread. On Linux, the library uses a default pthread mutex. Do not assume a non-owner unlock is valid.

Unit `unit-18`: grade 10.1; 47 words, 3 sentences, 78 syllables; below the failure threshold.

> In v2.0.22, a competing lock can wait for the external mutex while holding the internal mutex. An unlock that needs that internal mutex can then be blocked, creating a deadlock. Use application-level synchronization to prevent overlapping lock attempts and coordinate the whole tag sequence.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example gives a hypothetical locked handle, one release and its expected outputs, followed by the clean-error cleanup sequence.

Reading-level review: **PASS** — Every measured prose unit in this section is below grade 12. Code and table rows are numerical exclusions but were reviewed for exact semantics; short samples limit the score.

Most demanding passage (unit-20):

> Preserve the earlier error separately, provide a no-error cluster for cleanup, and handle the raw unlock code as well as the cleanup error cluster.

Density assessment: The prior sentences explain why a true incoming error bypasses cleanup and why the UI thread must own the lock.

### Assessed text

Unit `unit-19`: grade 9.09; 34 words, 2 sentences, 52 syllables; below the failure threshold. Short sample.

> For example, suppose a successful lock used tag handle 42 on the UI thread. If this VI returns no LabVIEW error and native code 0, one acquisition was released; tag handle out remains 42.

Unit `unit-20`: grade 10.61; 72 words, 4 sentences, 117 syllables; below the failure threshold.

> After a successful Lock.vi call and the protected operations, call this VI and check both outputs. The external mutex must be owned by the operating-system thread that executes the unlock; this node uses the UI thread. An incoming true LabVIEW error skips the library call. Preserve the earlier error separately, provide a no-error cluster for cleanup, and handle the raw unlock code as well as the cleanup error cluster.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW developer audience.'}

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, unlock still takes the internal mutex before releasing the external mutex. On Windows, the external mutex remains owned by the acquiring operating-system thread. A thread that acquires it more than once must release it the same number of times.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-21):

> In the checked upstream 2.7.2 source, unlock still takes the internal mutex before releasing the external mutex. On Windows, the external mutex remains owned by the acquiring operating-system thread. A thread that acquires it more than once must release it the same number of times.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-21`: grade 9.35; 47 words, 3 sentences, 75 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, unlock still takes the internal mutex before releasing the external mutex. On Windows, the external mutex remains owned by the acquiring operating-system thread. A thread that acquires it more than once must release it the same number of times.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The actual HTML distinguishes LabVIEW errors from native results and retains the platform-specific ownership, concurrency and cleanup conditions. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A LabVIEW user can wire an existing tag, check both result channels and coordinate and release the protected sequence. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
