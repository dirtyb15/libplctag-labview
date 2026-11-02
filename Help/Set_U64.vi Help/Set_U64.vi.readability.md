# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:49+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Set_U64.vi Help\Set_U64.vi.html`
Document SHA-256: `fa519b1a236d47d6ea61c8127a16f702736fea2f7d202f7b6c003ebb218c61f8`

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

Measured prose units: 14; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 642 | 46 | 971 | 7.7 | below |
| Purpose and scope | 98 | 7 | 149 | 7.81 | below |
| Called function and library selection | 92 | 7 | 142 | 7.75 | below |
| Inputs | 87 | 6 | 137 | 8.65 | within |
| Outputs and error handling | 55 | 5 | 88 | 7.58 | below |
| Execution and C implementation | 103 | 7 | 154 | 7.79 | below |
| Example and recommended call sequence | 137 | 9 | 193 | 6.97 | below |
| Library version differences | 70 | 5 | 108 | 8.08 | within |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> The call changes local data; it does not itself send a write request to the controller.

Density assessment: The first sentence identifies the tag buffer; the next explains the separate write.

### Assessed text

Unit `unit-1`: grade 8.63; 58 words, 3 sentences, 82 syllables; below the failure threshold.

> For an ordinary non-bit tag, Set_U64.vi stores one unsigned 64-bit integer at a zero-based byte offset in an existing tag's local data buffer. The call changes local data; it does not itself send a write request to the controller. With the bundled library, use Write_Tag.vi to send the tag data.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Called function and library selection

### Review discussion

Section assessment: The section gives the exact native prototype, C convention, UI thread, selector and raw status result.

Reading-level review: **PASS** — Every measured prose unit is below grade 12. Code and table rows were excluded numerically but read for exact meaning; short samples limit the score.

Most demanding passage (unit-6):

> The node's return is the raw library status.

Density assessment: The selected path and native arguments precede this result classification.

### Assessed text

Unit `unit-5`: grade 7.36; 23 words, 2 sentences, 36 syllables; below the failure threshold. Short sample.

> The node uses the C calling convention and runs in the LabVIEW user interface (UI) thread. Its numeric arguments are passed by value.

Unit `unit-6`: grade 7.92; 69 words, 5 sentences, 106 syllables; below the failure threshold.

> Choose_Lib.vi receives the incoming error and supplies the path and its error output to the library node. The configured cases select plctag32.dll, plctag64.dll or libplctag64.so under the application directory. The default target case returns an empty path. The library arguments are the tag handle and byte offset, followed by the value to store. The node's return is the raw library status.

### Exclusions from the score

- Unit `unit-3`: Unterminated fragment; check selection manually.
- Unit `unit-4`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Inputs

### Review discussion

Section assessment: The offset and fit rules explicitly apply to ordinary non-bit tags; the comparison explains 2.7.2 bit-tag behavior.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-13):

> If the data buffer has size N, valid offsets satisfy 0 <= offset <= N - 8, provided N is at least 8.

Density assessment: The prior sentence explains that offsets count bytes; the following guidance validates size and guards legacy overflow.

### Assessed text

Unit `unit-7`: grade 9.24; 17 words, 2 sentences, 31 syllables; below the failure threshold. Short sample.

> All connected terminals are marked recommended, rather than required. Wire the values needed for a predictable call.

Unit `unit-13`: grade 9.1; 70 words, 4 sentences, 106 syllables; below the failure threshold.

> For an ordinary non-bit tag, the offset counts bytes, not array elements. If the data buffer has size N, valid offsets satisfy 0 <= offset <= N - 8, provided N is at least 8. Use Tag_Size.vi to obtain the buffer size and check the size result. Validate the offset before the call; the older library uses an addition-based bounds expression that can overflow for extreme I32 values.

### Exclusions from the score

- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-12`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The input row explains I32 as signed 32-bit.'}
- acronym_first_use: U64 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The value row describes U64 as a unsigned 64-bit integer.'}

## Outputs and error handling

### Review discussion

Section assessment: The output and status tables distinguish the pass-through handle, raw native code and LabVIEW error; they qualify skipped calls and the separate write.

Reading-level review: **PASS** — Every measured prose unit is below grade 12. Code and table rows were excluded numerically but read for exact meaning; short samples limit the score.

Most demanding passage (unit-18):

> A zero raw code is meaningful only when the node actually called the library.

Density assessment: The preceding sentence says to check the LabVIEW error first and the following sentence explains the separate result channel.

### Assessed text

Unit `unit-18`: grade 7.72; 37 words, 3 sentences, 58 syllables; below the failure threshold.

> Check error out first and then error code. A zero raw code is meaningful only when the node actually called the library. This wrapper does not translate a negative native return into a LabVIEW error-cluster error.

Unit `unit-24`: grade 7.59; 18 words, 2 sentences, 30 syllables; below the failure threshold. Short sample.

> A successful setter result does not confirm a controller write. Check the result of Write_Tag.vi separately.

### Exclusions from the score

- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-15`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-16`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-17`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-19`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-20`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-21`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-22`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-23`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Execution and C implementation

### Review discussion

Section assessment: The execution section describes lookup, internal mutex, local 8-byte update and temporary-reference release.

Reading-level review: **PASS** — Every measured prose unit is below grade 12. Code and table rows were excluded numerically but read for exact meaning; short samples limit the score.

Most demanding passage (unit-25):

> The legacy source uses the byte at the lowest offset as the least significant byte.

Density assessment: The paragraph introduces the typed local update before its byte-order meaning.

### Assessed text

Unit `unit-25`: grade 7.56; 71 words, 5 sentences, 106 syllables; below the failure threshold.

> The node calls plc_tag_set_uint64 with the handle, byte offset and value. The legacy C function looks up the tag and takes its internal mutex. It checks for a data buffer and space for 8 bytes. On success it updates those local bytes, leaves the protected block and releases its temporary tag reference. The legacy source uses the byte at the lowest offset as the least significant byte.

Unit `unit-26`: grade 8.35; 32 words, 2 sentences, 48 syllables; below the failure threshold. Short sample.

> The reference release does not destroy the caller's tag. Coordinate a sequence of changes and writes when multiple tasks share the tag; one setter call does not make the whole sequence atomic.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example supplies a valid tag, offset zero, a value, expected 8-byte data and the separate write.

Reading-level review: **PASS** — Every measured prose unit is below grade 12. Code and table rows were excluded numerically but read for exact meaning; short samples limit the score.

Most demanding passage (unit-28):

> A separate Write_Tag.vi operation is needed to send the prepared data to the controller.

Density assessment: The prior sentences give the value and expected bytes before distinguishing the controller transfer.

### Assessed text

Unit `unit-27`: grade 5.8; 60 words, 4 sentences, 79 syllables; below the failure threshold.

> For a valid tag with at least 8 bytes, use offset 0 and wire the intended U64 value. If error out has no error and the raw error code is 0, the local buffer has been updated. Call Write_Tag.vi and check its result to send the tag data. Preserve any other bytes that the write must retain.

Unit `unit-28`: grade 9.15; 55 words, 3 sentences, 82 syllables; below the failure threshold.

> For example, wire value 1 and offset 0 for a valid tag with at least 8 bytes. If the call completes successfully, the first 8 bytes are 0x01 0x00 0x00 0x00 0x00 0x00 0x00 0x00 in the legacy implementation. A separate Write_Tag.vi operation is needed to send the prepared data to the controller.

Unit `unit-29`: grade 5.86; 22 words, 2 sentences, 32 syllables; below the failure threshold. Short sample.

> When finished with the tag, release it with Destroy_Tag.vi. Ensure cleanup can run even when an earlier operation has failed.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, an integer setter on a bit tag ignores the byte offset. Zero clears the configured bit; a nonzero value sets it. For an ordinary tag, byte order follows the tag settings. If automatic writing is configured, a successful set marks the tag dirty so the library can schedule a later write. A successful local set does not confirm that the later write completed.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-30):

> In the checked upstream 2.7.2 source, an integer setter on a bit tag ignores the byte offset. Zero clears the configured bit; a nonzero value sets it. For an ordinary tag, byte order follows the tag settings. If automatic writing is configured, a successful set marks the tag dirty so the library can schedule a later write. A successful local set does not confirm that the later write completed.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-30`: grade 8.08; 70 words, 5 sentences, 108 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, an integer setter on a bit tag ignores the byte offset. Zero clears the configured bit; a nonzero value sets it. For an ordinary tag, byte order follows the tag settings. If automatic writing is configured, a successful set marks the tag dirty so the library can schedule a later write. A successful local set does not confirm that the later write completed.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The saved page distinguishes the local unsigned 64-bit integer update, native and LabVIEW errors, saved default and separate controller write. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A caller can validate the 8-byte range, wire the intended value, check both results and perform a separate write. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
