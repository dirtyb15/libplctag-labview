# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:42+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Lock.vi Help\Lock.vi.html`
Document SHA-256: `7571f7eeb027bd14df8e971dd6ee99e52a7f9a92467eb37f00728f28affcfbfd`

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

Measured prose units: 13; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 610 | 47 | 943 | 7.71 | below |
| Purpose and scope | 56 | 6 | 90 | 7.01 | below |
| Called function and library selection | 68 | 6 | 104 | 6.88 | below |
| Inputs | 12 | 2 | 21 | 7.4 | below |
| Outputs and error handling | 41 | 3 | 64 | 8.16 | within |
| Execution and C implementation | 266 | 19 | 407 | 7.92 | below |
| Example and recommended call sequence | 88 | 6 | 136 | 8.37 | within |
| Library version differences | 79 | 5 | 121 | 8.65 | within |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> Locks the tag for a series of library calls. The lock uses the tag's external mutex.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-1`: grade 4.49; 16 words, 2 sentences, 23 syllables; below the failure threshold. Short sample.

> Locks the tag for a series of library calls. The lock uses the tag's external mutex.

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

> Its error output is wired into the library node before the native call.

Density assessment: The reader first sees the native symbol, then the selector path and error dependency.

### Assessed text

Unit `unit-5`: grade 7.36; 23 words, 2 sentences, 36 syllables; below the failure threshold. Short sample.

> The node uses the C calling convention and runs in the LabVIEW user interface (UI) thread. Its numeric arguments are passed by value.

Unit `unit-6`: grade 6.63; 45 words, 4 sentences, 68 syllables; below the failure threshold.

> Choose_Lib.vi supplies the path. Its error output is wired into the library node before the native call. Its target cases select plctag32.dll, plctag64.dll or libplctag64.so under the application directory. The default target case returns an empty path.

### Exclusions from the score

- Unit `unit-3`: Unterminated fragment; check selection manually.
- Unit `unit-4`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Inputs

### Review discussion

Section assessment: The input table lists the signed 32-bit tag identifier and incoming error, with wiring and default guidance.

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

Density assessment: This condition follows the result-channel distinction and prevents interpreting a bypassed call as success.

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

Section assessment: The execution section covers both mutexes, same-thread recursive acquisition, cross-thread deadlock and abandoned or failed Windows waits.

Reading-level review: **PASS** — Every measured prose unit in this section is below grade 12. Code and table rows are numerical exclusions but were reviewed for exact semantics; short samples limit the score.

Most demanding passage (unit-19):

> The same thread then acquires the mutex a second time, so one unlock leaves it held.

Density assessment: The preceding sentences explain abandoned ownership and the legacy retry, which establish the cause of the extra acquisition.

### Assessed text

Unit `unit-16`: grade 8.31; 52 words, 4 sentences, 83 syllables; below the failure threshold.

> The legacy function looks up the tag, takes its internal mutex and calls the external mutex lock. It releases the internal mutex and temporary tag reference after that call. -19 means that the tag was not found; other negative codes can report a mutex failure. Pair a successful lock with Unlock.vi.

Unit `unit-17`: grade 9.1; 70 words, 4 sentences, 106 syllables; below the failure threshold.

> In the v2.0.22 Windows implementation, the external mutex is owned by the operating-system thread and can be acquired again by its owner. Both Lock.vi and Unlock.vi call the library on the LabVIEW UI thread. Separate LabVIEW tasks can therefore enter Lock.vi on the same thread and both receive success while their sequences overlap. Do not rely on this lock alone to serialize those tasks.

Unit `unit-18`: grade 7.31; 80 words, 6 sentences, 120 syllables; below the failure threshold.

> The library waits for the external mutex while holding its internal mutex. If another thread owns the external mutex and then tries to unlock through the library, the waiting lock and unlock calls can block one another. The Windows wait has no timeout. Because this node runs on the UI thread, a blocked call can also stop UI work. The Linux build uses a default pthread mutex. Do not assume its repeated-lock or non-owner unlock behavior matches Windows.

Unit `unit-19`: grade 7.47; 64 words, 5 sentences, 98 syllables; below the failure threshold.

> On Windows, an abandoned mutex is granted to the next waiting thread. The legacy wait loop retries after this result instead of reporting it. The same thread then acquires the mutex a second time, so one unlock leaves it held. The protected state may also be inconsistent. If the Windows wait fails, the loop retries instead of reporting the failure and can run forever.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example provides handle 42, native success code 0, the passed-through output and whole-sequence coordination.

Reading-level review: **PASS** — Every measured prose unit in this section is below grade 12. Code and table rows are numerical exclusions but were reviewed for exact semantics; short samples limit the score.

Most demanding passage (unit-20):

> If this VI returns no LabVIEW error and native code 0, the lock was acquired; tag handle out remains 42.

Density assessment: The example starts with an explicitly hypothetical valid handle before stating the observable result.

### Assessed text

Unit `unit-20`: grade 7.15; 29 words, 2 sentences, 42 syllables; below the failure threshold. Short sample.

> For example, suppose a valid tag handle is 42. If this VI returns no LabVIEW error and native code 0, the lock was acquired; tag handle out remains 42.

Unit `unit-21`: grade 8.96; 59 words, 4 sentences, 94 syllables; below the failure threshold.

> Serialize the entire shared-tag sequence with a LabVIEW synchronization mechanism, such as a semaphore or a single-owner loop. If this VI is used as well, pair each successful acquisition with Unlock.vi and check its result. Plan cleanup so an acquired lock is not left held. Do not assume the external mutex alone separates UI-thread callers.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW developer audience.'}

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, the lock tries the external mutex while holding the internal mutex, then releases the internal mutex before waiting and retrying. This avoids the legacy nested-wait pattern. A Windows mutex is still owned by its operating-system thread and can be reacquired by that thread. Because this node uses the UI thread, do not rely on it alone to serialize separate LabVIEW tasks. A blocked retry loop can also delay UI work.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-22):

> In the checked upstream 2.7.2 source, the lock tries the external mutex while holding the internal mutex, then releases the internal mutex before waiting and retrying. This avoids the legacy nested-wait pattern. A Windows mutex is still owned by its operating-system thread and can be reacquired by that thread. Because this node uses the UI thread, do not rely on it alone to serialize separate LabVIEW tasks. A blocked retry loop can also delay UI work.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-22`: grade 8.65; 79 words, 5 sentences, 121 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, the lock tries the external mutex while holding the internal mutex, then releases the internal mutex before waiting and retrying. This avoids the legacy nested-wait pattern. A Windows mutex is still owned by its operating-system thread and can be reacquired by that thread. Because this node uses the UI thread, do not rely on it alone to serialize separate LabVIEW tasks. A blocked retry loop can also delay UI work.

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
