# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:51+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Write_Tag.vi Help\Write_Tag.vi.html`
Document SHA-256: `11456068c59f23f09f986b836e750999b85a4ddb68285bb13e9ee91b10be8a5c`

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

Measured prose units: 15; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 683 | 50 | 1080 | 8.4 | within |
| Purpose and scope | 53 | 5 | 89 | 8.36 | within |
| Called function and library selection | 68 | 5 | 106 | 8.11 | within |
| Inputs | 12 | 2 | 21 | 7.4 | below |
| Outputs and error handling | 63 | 5 | 106 | 9.18 | within |
| Execution and C implementation | 331 | 22 | 524 | 8.96 | within |
| Example and recommended call sequence | 106 | 7 | 155 | 7.57 | below |
| Library version differences | 50 | 4 | 79 | 7.93 | below |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> Starts a write of the tag's local data to the configured controller destination.

Density assessment: The data direction and destination are given before the version caveat.

### Assessed text

Unit `unit-1`: grade 9.45; 13 words, 1 sentences, 22 syllables; below the failure threshold. Short sample.

> Starts a write of the tag's local data to the configured controller destination.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Called function and library selection

### Review discussion

Section assessment: The section gives the native prototype, C calling convention, UI thread and target-specific library selection.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded from scoring but were read for meaning; short samples limit interpretation.

Most demanding passage (unit-5):

> The node uses the C calling convention and runs in the LabVIEW user interface (UI) thread.

Density assessment: The prototype precedes the saved node settings, followed by the path source.

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

Section assessment: The input table states the signed 32-bit handle, millisecond timeout and incoming-error behavior.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded from scoring but were read for meaning; short samples limit interpretation.

Most demanding passage (unit-10):

> Wait time in milliseconds. Use 0 for an operation that can return pending, or a positive value to wait.

Density assessment: The timeout units and supported choices are together in the input row.

### Assessed text

Unit `unit-7`: grade 7.4; 12 words, 2 sentences, 21 syllables; below the failure threshold. Short sample.

> Connected terminals are marked recommended. Wire the values needed for the call.

### Exclusions from the score

- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'I32 is explained as signed 32-bit in the same input row.'}

## Outputs and error handling

### Review discussion

Section assessment: The revised text preserves the interface and qualifies the changed version or selector behavior.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-24):

> A timeout alone does not establish whether the controller received or applied any data.

Density assessment: The status table introduces timeout before the text explains why the controller outcome remains uncertain.

### Assessed text

Unit `unit-16`: grade 8.16; 41 words, 3 sentences, 64 syllables; below the failure threshold.

> Check error out first, then the native result. The wrapper does not convert a negative native return into a LabVIEW error-cluster error. A numeric result is not proof of a completed call when an incoming LabVIEW error skipped the node.

Unit `unit-24`: grade 11.23; 22 words, 2 sentences, 42 syllables; below the failure threshold. Short sample.

> Other negative values report library or protocol errors. A timeout alone does not establish whether the controller received or applied any data.

### Exclusions from the score

- Unit `unit-12`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-13`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-15`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-17`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-18`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-19`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-20`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-21`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-22`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-23`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: OK may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'OK is the exact success-status label, not an unexplained acronym.'}

## Execution and C implementation

### Review discussion

Section assessment: The execution text explains native wait, abort, mutex and UI behavior, the protocol type-discovery pre-read, and shared-tag coordination.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded from scoring but were read for meaning; short samples limit interpretation.

Most demanding passage (unit-28):

> That pre-read does not copy the returned data into the local buffer.

Density assessment: The prior sentence identifies the type-discovery pre-read; the next explains why a separate read is needed to preserve other bytes.

### Assessed text

Unit `unit-25`: grade 8.53; 64 words, 4 sentences, 97 syllables; below the failure threshold.

> The legacy function looks up the tag, locks its internal mutex and asks the protocol to write the local data. If the protocol returns an error, the function passes it back. With timeout 0, a started operation can return 1 while it is pending. If the write is pending and the timeout is positive, the function polls until it finishes or the wait expires.

Unit `unit-26`: grade 10.77; 72 words, 4 sentences, 118 syllables; below the failure threshold.

> If it is still pending at the deadline, the library calls the protocol abort function when available and returns -32. A different error found while waiting also triggers that abort when available; the error code is retained. The protocol start and other overhead are outside the wait interval, so the timeout is not a strict limit on the whole call. The function releases the mutex and its temporary tag reference before returning.

Unit `unit-27`: grade 6.66; 70 words, 6 sentences, 105 syllables; below the failure threshold.

> The internal mutex stays held while the function waits, and this node runs on the UI thread. A long wait can delay other operations that need that mutex and can block UI work. Use a nonnegative timeout. For a negative timeout, the legacy wait deadline is already past. If the write start reports pending, the library attempts to abort it and returns -32. An immediate OK can still return 0.

Unit `unit-28`: grade 10.14; 92 words, 6 sentences, 154 syllables; below the failure threshold.

> For the legacy Allen-Bradley EtherNet/IP Common Industrial Protocol (CIP) implementation, a first write can start a preliminary read to obtain type information. That pre-read does not copy the returned data into the local buffer. After a successful pre-read, the library starts the write. Do not rely on that pre-read to preserve unchanged fields. If other bytes must retain their controller values, complete a separate read before changing the buffer, then write the prepared data. A local setter result alone is not proof that the controller write succeeded.

Unit `unit-29`: grade 8.72; 33 words, 2 sentences, 50 syllables; below the failure threshold. Short sample.

> For a shared tag, coordinate the read, local changes and write as a sequence. The mutex protects individual library calls, but it does not make a series of calls from different tasks atomic.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: IP may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'EtherNet/IP is the exact protocol name; CIP is expanded in the same sentence.'}

## Example and recommended call sequence

### Review discussion

Section assessment: The example gives a zero timeout, pending status and polling, then explains preparation and checks.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded from scoring but were read for meaning; short samples limit interpretation.

Most demanding passage (unit-30):

> If the native code is 1 and error out is clear, the write is pending.

Density assessment: The first sentence supplies a valid tag, prepared local data and zero timeout before stating the conditional result.

### Assessed text

Unit `unit-30`: grade 6.78; 45 words, 3 sentences, 63 syllables; below the failure threshold.

> For example, wire 0 for timeout on a valid tag with prepared local data. If the native code is 1 and error out is clear, the write is pending. Poll Tag_Status.vi until it reports a final result before treating the write as complete.

Unit `unit-31`: grade 8.15; 61 words, 4 sentences, 92 syllables; below the failure threshold.

> If other bytes must be retained, complete a tag read and check its result. Prepare the local buffer using the appropriate setter and check the setter result. Call this VI with a nonnegative timeout, then check error out and error code. When the result is pending, use Tag_Status.vi and wait for a final status before considering the write complete.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW developer audience.'}

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, a negative timeout returns -7. A tag with an operation in flight can return -39. The wait occurs outside the internal mutex. Its Allen-Bradley CIP first-write pre-read still obtains type information without copying the response data into the local buffer.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-32):

> In the checked upstream 2.7.2 source, a negative timeout returns -7. A tag with an operation in flight can return -39. The wait occurs outside the internal mutex. Its Allen-Bradley CIP first-write pre-read still obtains type information without copying the response data into the local buffer.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-32`: grade 7.93; 50 words, 4 sentences, 79 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, a negative timeout returns -7. A tag with an operation in flight can return -39. The wait occurs outside the internal mutex. Its Allen-Bradley CIP first-write pre-read still obtains type information without copying the response data into the local buffer.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 1; limit: 3.

### Rewrite `808c1a7e156d167261f6` (batch 1)

Original snapshot: `91e52fab07067826d46ceccd34ebfd15dece9940e0f4c4fd55a50be66dc37aca`; method: approachable-fk/2.0.

Original artifact: `b8f926f613f606c562c2b2c751da36882639c3e8776986dfb827367b60f9dcea`. Grade 14.87; 56 words, 3 sentences, 110 syllables.

> In the checked upstream 2.7.2 source, a negative timeout returns PLCTAG_ERR_BAD_PARAM (-7), and an operation already in flight can return PLCTAG_ERR_BUSY (-39). The wait occurs outside the internal mutex. Its Allen-Bradley CIP first-write pre-read still obtains type information without copying the response data into the local buffer.

Clarity problem: Two symbolic error identifiers made the timeout and pre-read discussion dense.

Change: Use numeric values in prose and put their exact names in the output code table.

Current unit `unit-32`: grade 7.93; 50 words, 4 sentences, 79 syllables.

> In the checked upstream 2.7.2 source, a negative timeout returns -7. A tag with an operation in flight can return -39. The wait occurs outside the internal mutex. Its Allen-Bradley CIP first-write pre-read still obtains type information without copying the response data into the local buffer.

Preserved facts and relationships:

- A negative timeout returns PLCTAG_ERR_BAD_PARAM (-7).
- An in-flight operation can return PLCTAG_ERR_BUSY (-39).
- The wait is outside the internal mutex and the CIP pre-read does not copy data into the buffer.

Source references:

- Help/.support/help-generation/upstream-7712ed7/src/libplctag/lib/lib.c
- Help/.support/help-generation/upstream-7712ed7/src/libplctag/protocols/ab/eip_cip.c

Technical integrity: **PASS** — Compared the current prose and any adjacent table with the archived failing passage and the pinned source; the exact conditions, codes and operational effects remain intact.


## Whole-document review

Whole document review: **PASS** — The saved HTML distinguishes local data preparation, a pending controller write, its timeout limits and the protocol type-discovery pre-read. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A caller can prepare the buffer, start a write, check both channels and wait for its final status. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
