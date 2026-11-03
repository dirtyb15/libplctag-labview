# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:43+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Read_Double.vi Help\Read_Double.vi.html`
Document SHA-256: `fa3e362d791785c6e813c5685cb45dd242ed0e3be9993e5f0c14d5ddebfbdf1d`

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
| Combined prose | 712 | 50 | 1086 | 7.96 | below |
| Purpose and scope | 101 | 7 | 155 | 8.15 | within |
| Called function and library selection | 85 | 7 | 131 | 7.33 | below |
| Inputs | 87 | 6 | 137 | 8.65 | within |
| Outputs and error handling | 149 | 10 | 231 | 8.51 | within |
| Execution and C implementation | 98 | 7 | 147 | 7.57 | below |
| Example and recommended call sequence | 120 | 8 | 175 | 7.47 | below |
| Library version differences | 72 | 5 | 110 | 8.05 | within |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> The call reads local data; it does not itself request new data from the controller.

Density assessment: The local buffer is introduced before the statement about controller refresh.

### Assessed text

Unit `unit-1`: grade 9.36; 61 words, 3 sentences, 88 syllables; below the failure threshold.

> For an ordinary non-bit tag, Read_Double.vi reads one double-precision floating-point value at a zero-based byte offset in an existing tag's local data buffer. The call reads local data; it does not itself request new data from the controller. Use Read_Tag.vi first when fresh tag data is needed, subject to the configured read cache.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Called function and library selection

### Review discussion

Section assessment: The section gives the native prototype, C convention, UI thread, selector and typed return.

Reading-level review: **PASS** — All measured prose is below grade 12. Code and table rows are excluded numerically but reviewed for meaning; short samples limit the score.

Most demanding passage (unit-6):

> The node's return is the typed value.

Density assessment: The path and two native arguments precede this result classification.

### Assessed text

Unit `unit-5`: grade 7.36; 23 words, 2 sentences, 36 syllables; below the failure threshold. Short sample.

> The node uses the C calling convention and runs in the LabVIEW user interface (UI) thread. Its numeric arguments are passed by value.

Unit `unit-6`: grade 7.33; 62 words, 5 sentences, 95 syllables; below the failure threshold.

> Choose_Lib.vi receives the incoming error and supplies the path and its error output to the library node. The configured cases select plctag32.dll, plctag64.dll or libplctag64.so under the application directory. The default target case returns an empty path. The library arguments are the tag handle and byte offset. The node's return is the typed value.

### Exclusions from the score

- Unit `unit-3`: Unterminated fragment; check selection manually.
- Unit `unit-4`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Inputs

### Review discussion

Section assessment: The offset and fit rules explicitly apply to ordinary non-bit tags; the comparison explains 2.7.2 bit-tag behavior.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-12):

> If the data buffer has size N, valid offsets satisfy 0 <= offset <= N - 8, provided N is at least 8.

Density assessment: The first sentence establishes byte offsets; later sentences require size validation and warn about legacy overflow.

### Assessed text

Unit `unit-7`: grade 9.24; 17 words, 2 sentences, 31 syllables; below the failure threshold. Short sample.

> All connected terminals are marked recommended, rather than required. Wire the values needed for a predictable call.

Unit `unit-12`: grade 9.1; 70 words, 4 sentences, 106 syllables; below the failure threshold.

> For an ordinary non-bit tag, the offset counts bytes, not array elements. If the data buffer has size N, valid offsets satisfy 0 <= offset <= N - 8, provided N is at least 8. Use Tag_Size.vi to obtain the buffer size and check the size result. Validate the offset before the call; the older library uses an addition-based bounds expression that can overflow for extreme I32 values.

### Exclusions from the score

- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'I32 is explained as a signed 32-bit handle in the same row.'}

## Outputs and error handling

### Review discussion

Section assessment: The output section distinguishes double data from call errors and explains the ambiguous DBL_MAX and zero-bit failure cases.

Reading-level review: **PASS** — All measured prose is below grade 12. Code and table rows are excluded numerically but reviewed for meaning; short samples limit the score.

Most demanding passage (unit-17):

> If the tag exists but has no buffer or the offset is out of bounds, the source copies an all-zero bit pattern into the double result.

Density assessment: The missing-handle result is stated first and the next sentence qualifies the usual IEEE 754 meaning of the zero pattern.

### Assessed text

Unit `unit-17`: grade 9.09; 111 words, 7 sentences, 174 syllables; below the failure threshold.

> For an invalid handle, the legacy getter returns DBL_MAX, the largest finite C double. This can also be valid data. If the tag exists but has no buffer or the offset is out of bounds, the source copies an all-zero bit pattern into the double result. That pattern is normally 0.0 on IEEE 754 systems and can also be valid data. The legacy getter does not set the tag status in these paths. This wrapper exposes no separate native status output for the getter. Validate the handle, size and read operation before using the value; do not treat a later tag-status result as proof that this getter succeeded.

Unit `unit-18`: grade 7.05; 38 words, 3 sentences, 57 syllables; below the failure threshold.

> error out is the LabVIEW error cluster from the Call Library Function Node. An incoming true error status skips the call. A clear LabVIEW error cluster alone does not prove that the native getter found valid tag data.

### Exclusions from the score

- Unit `unit-13`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-15`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-16`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: DBL may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'DBL is the LabVIEW double-precision type described in the opening.'}
- acronym_first_use: IEEE may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'IEEE 754 is the exact standard designation qualifying the example.'}

## Execution and C implementation

### Review discussion

Section assessment: The execution section describes tag lookup, internal mutex, byte order and temporary-reference release.

Reading-level review: **PASS** — All measured prose is below grade 12. Code and table rows are excluded numerically but reviewed for meaning; short samples limit the score.

Most demanding passage (unit-19):

> The legacy source uses the byte at the lowest offset as the least significant byte.

Density assessment: The four prior sentences establish the local read and type before the byte-order rule.

### Assessed text

Unit `unit-19`: grade 7.98; 72 words, 4 sentences, 101 syllables; below the failure threshold.

> The node calls plc_tag_get_float64 with the handle and byte offset. The legacy C function looks up the tag, takes its internal mutex and checks for a data buffer and space for 8 bytes. On the normal path it decodes the local bytes into a DBL value and returns that value to tag value. The legacy source uses the byte at the lowest offset as the least significant byte.

Unit `unit-20`: grade 8.67; 26 words, 3 sentences, 46 syllables; below the failure threshold.

> The getter releases its temporary tag reference before returning. It does not destroy the caller's tag. The call itself makes no request to refresh controller data.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example gives a ready tag, offset zero, eight bytes and the IEEE 754 condition.

Reading-level review: **PASS** — All measured prose is below grade 12. Code and table rows are excluded numerically but reviewed for meaning; short samples limit the score.

Most demanding passage (unit-22):

> The legacy getter returns 1.0 on an IEEE 754 target, provided the handle and range are valid.

Density assessment: The preceding sentence gives the exact bytes and this sentence supplies the representation and validity conditions.

### Assessed text

Unit `unit-21`: grade 6.98; 60 words, 4 sentences, 85 syllables; below the failure threshold.

> For a ready tag with at least 8 bytes, call Read_Tag.vi when fresh data is needed and check the read result. Use offset 0 to interpret the first 8 bytes as a DBL value. Ensure the tag layout actually contains that type at that location. Check error out and the native getter limitations before relying on tag value.

Unit `unit-22`: grade 9.83; 38 words, 2 sentences, 58 syllables; below the failure threshold. Short sample.

> For example, assume a ready tag has local bytes 0x00 0x00 0x00 0x00 0x00 0x00 0xF0 0x3F starting at offset 0. The legacy getter returns 1.0 on an IEEE 754 target, provided the handle and range are valid.

Unit `unit-23`: grade 5.86; 22 words, 2 sentences, 32 syllables; below the failure threshold. Short sample.

> When finished with the tag, release it with Destroy_Tag.vi. Ensure cleanup can run even when an earlier operation has failed.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, this getter returns DBL_MIN on failure. That is the smallest positive normal C value for the type, and it can also be valid data. A bit tag is unsupported. For an ordinary tag, the byte order follows the tag settings. The library updates tag status on the checked data and range paths, but the VI still returns data rather than a separate native status.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-24):

> In the checked upstream 2.7.2 source, this getter returns DBL_MIN on failure. That is the smallest positive normal C value for the type, and it can also be valid data. A bit tag is unsupported. For an ordinary tag, the byte order follows the tag settings. The library updates tag status on the checked data and range paths, but the VI still returns data rather than a separate native status.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-24`: grade 8.05; 72 words, 5 sentences, 110 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, this getter returns DBL_MIN on failure. That is the smallest positive normal C value for the type, and it can also be valid data. A bit tag is unsupported. For an ordinary tag, the byte order follows the tag settings. The library updates tag status on the checked data and range paths, but the VI still returns data rather than a separate native status.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW developer audience.'}

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The saved page distinguishes local double data, ambiguous native failure returns, a separate LabVIEW error and the representation-dependent byte example. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A caller can validate the eight-byte range and avoid treating a plausible double as a native status. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
