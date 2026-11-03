# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:51+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Tag_Size.vi Help\Tag_Size.vi.html`
Document SHA-256: `9c1348c3eeab411937ca7732a14b9ae7419b7b44e289359950cc63757340ad07`

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
| Combined prose | 338 | 25 | 499 | 7.1 | below |
| Purpose and scope | 52 | 5 | 86 | 7.98 | below |
| Called function and library selection | 68 | 5 | 106 | 8.11 | within |
| Inputs | 12 | 2 | 21 | 7.4 | below |
| Outputs and error handling | 41 | 3 | 64 | 8.16 | within |
| Execution and C implementation | 49 | 3 | 67 | 6.91 | below |
| Example and recommended call sequence | 89 | 5 | 116 | 6.73 | below |
| Library version differences | 27 | 2 | 39 | 6.72 | below |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> Returns the size in bytes of an existing tag's local data buffer.

Density assessment: The operation, units and local data boundary are given in one sentence before the version caveat.

### Assessed text

Unit `unit-1`: grade 7.77; 12 words, 1 sentences, 19 syllables; below the failure threshold. Short sample.

> Returns the size in bytes of an existing tag's local data buffer.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Called function and library selection

### Review discussion

Section assessment: The section supplies the exact native prototype, calling settings and target-specific library selection.

Reading-level review: **PASS** — All scored prose units are below grade 12. Code and table rows are excluded numerically but were checked for meaning; the short samples do not prove comprehension.

Most demanding passage (unit-6):

> Choose_Lib.vi receives the incoming error and supplies the path and its error output to the library node.

Density assessment: The reader sees the native function first and then the path and error producers.

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

Section assessment: The input table explains the signed 32-bit tag handle and incoming error, including wiring and default guidance.

Reading-level review: **PASS** — All scored prose units are below grade 12. Code and table rows are excluded numerically but were checked for meaning; the short samples do not prove comprehension.

Most demanding passage (unit-9):

> Signed 32-bit tag identifier from a successful tag creation.

Density assessment: The exact I32 type is paired with signed width and the handle origin.

### Assessed text

Unit `unit-7`: grade 7.4; 12 words, 2 sentences, 21 syllables; below the failure threshold. Short sample.

> Connected terminals are marked recommended. Wire the values needed for the call.

### Exclusions from the score

- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The I32 type is explained as signed 32-bit in the same input row.'}

## Outputs and error handling

### Review discussion

Section assessment: The outputs distinguish a passed-through handle, the byte count or native error, and the LabVIEW error cluster.

Reading-level review: **PASS** — All scored prose units are below grade 12. Code and table rows are excluded numerically but were checked for meaning; the short samples do not prove comprehension.

Most demanding passage (unit-15):

> A numeric result is not proof of a completed call when an incoming LabVIEW error skipped the node.

Density assessment: The skip caveat follows the distinction between the native result and LabVIEW error channel.

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

Section assessment: The execution section describes the lookup, internal mutex, size result and not-found error.

Reading-level review: **PASS** — All scored prose units are below grade 12. Code and table rows are excluded numerically but were checked for meaning; the short samples do not prove comprehension.

Most demanding passage (unit-16):

> The returned number is the C function result, so a negative value is an error and must not be used as a buffer length.

Density assessment: The native lookup and returned field are established before the consequence of a negative result.

### Assessed text

Unit `unit-16`: grade 6.91; 49 words, 3 sentences, 67 syllables; below the failure threshold.

> The legacy function looks up the tag and returns its size while holding the internal mutex. If the handle is not found, it returns -19. The returned number is the C function result, so a negative value is an error and must not be used as a buffer length.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example gives the offset bounds and illustrates a four-byte value in a 16-byte buffer.

Reading-level review: **PASS** — All scored prose units are below grade 12. Code and table rows are excluded numerically but were checked for meaning; the short samples do not prove comprehension.

Most demanding passage (unit-18):

> For example, if the returned size is 16 bytes, a four-byte value fits at offset 12.

Density assessment: The preceding sentence gives the general offset rule; the example substitutes concrete values.

### Assessed text

Unit `unit-17`: grade 7.35; 57 words, 3 sentences, 75 syllables; below the failure threshold.

> Wire a valid tag handle and check error out. Accept tag size as a byte count only when the call ran and the returned value is nonnegative. For a value of width W bytes, the starting offset must be at least zero and no greater than size minus W; the buffer must contain at least W bytes.

Unit `unit-18`: grade 5.77; 32 words, 2 sentences, 41 syllables; below the failure threshold. Short sample.

> For example, if the returned size is 16 bytes, a four-byte value fits at offset 12. It does not fit at offset 13 because the value would extend past the buffer.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, a successful size query also sets the tag status to OK. The return remains the local buffer size in bytes.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-19):

> In the checked upstream 2.7.2 source, a successful size query also sets the tag status to OK. The return remains the local buffer size in bytes.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-19`: grade 6.72; 27 words, 2 sentences, 39 syllables; below the failure threshold. Short sample.

> In the checked upstream 2.7.2 source, a successful size query also sets the tag status to OK. The return remains the local buffer size in bytes.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: OK may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'OK is the library status value meaning success.'}

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The actual page consistently distinguishes local byte size, negative native errors and LabVIEW error bypass. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A LabVIEW user can identify the valid size, check both channels and apply the illustrated byte-offset bound. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
