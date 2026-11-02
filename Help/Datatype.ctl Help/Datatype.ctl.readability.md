# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:41+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Datatype.ctl Help\Datatype.ctl.html`
Document SHA-256: `46f82826d8eef3596364cbac71efbf9d3a58e70711515cf4dba0ba6cf4fc9327`

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

Measured prose units: 11; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 468 | 34 | 753 | 8.76 | within |
| Purpose and scope | 118 | 10 | 188 | 7.81 | below |
| Control type and choices | 38 | 3 | 59 | 7.67 | below |
| Use with Read_By_Datatype.vi | 213 | 15 | 346 | 9.12 | within |
| Example | 55 | 3 | 90 | 10.87 | above |
| Library version differences | 44 | 3 | 70 | 8.9 | within |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-3):

> The caller must interpret the variant with the type produced by the selected case.

Density assessment: The relationship between the enum, a typed read and the variant is introduced in the preceding sentence, so the reader can see why the extraction type matters.

### Assessed text

Unit `unit-1`: grade 7.63; 39 words, 3 sentences, 60 syllables; below the failure threshold.

> Datatype.ctl is an enumerated control that names the data type to read from a libplctag tag buffer. It contains eleven named choices. The control itself selects a value; it does not read a tag or contact a controller.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

Unit `unit-3`: grade 7.94; 39 words, 3 sentences, 61 syllables; below the failure threshold.

> Read_By_Datatype.vi uses this selection to choose a typed read virtual instrument (VI). That VI returns the selected value in a LabVIEW variant. The caller must interpret the variant with the type produced by the selected case.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Control type and choices

### Review discussion

Section assessment: The table lists the unsigned 16-bit enum values and explains every one of the eleven choices. The final paragraph separates the case default from an instance default.

Reading-level review: **PASS** — The current actual text units are below grade 12. Table rows, headings and identifiers were inspected separately for exact meaning.

Most demanding passage (unit-17):

> The selector VI's I8 default case is a case-structure rule; it does not establish the saved default of an individual control instance.

Density assessment: The sentence distinguishes two meanings of default. The table identifies I8 as the structure default, then this sentence prevents the reader from assuming an instance value.

### Assessed text

Unit `unit-4`: grade 3.76; 8 words, 1 sentences, 11 syllables; below the failure threshold. Short sample.

> The control is an unsigned 16-bit enum.

Unit `unit-17`: grade 9.14; 30 words, 2 sentences, 48 syllables; below the failure threshold. Short sample.

> The selector VI's I8 default case is a case-structure rule; it does not establish the saved default of an individual control instance. Wire or verify the intended selection.

### Exclusions from the score

- Unit `unit-4`: Unterminated fragment; check selection manually.
- Unit `unit-5`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-6`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-7`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-12`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-13`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-15`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-16`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I8 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: I16 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: I64 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: U8 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: U16 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: U32 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: U64 may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: FLOAT may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: DOUBLE may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}
- acronym_first_use: BOOL may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'This is an exact enum/type label; its table row explains signedness, width, floating-point type or U8 result.'}

## Use with Read_By_Datatype.vi

### Review discussion

Section assessment: The revised text preserves the interface and qualifies the changed version or selector behavior.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-21):

> In the upstream v2.0.22 implementation, getter failures can return values that also look like valid data; a later tag-status check does not reliably identify those failures.

Density assessment: This combines the library version, failure sentinel ambiguity and a limit on tag-status checking. The preceding sentences give the practical response: validate handle and buffer size.

### Assessed text

Unit `unit-18`: grade 7.16; 54 words, 4 sentences, 80 syllables; below the failure threshold.

> Wire a valid tag handle, a byte offset, this enum and an error cluster to Read_By_Datatype.vi. The selected case calls the matching read VI and converts its result to a variant. The enum and tag handle are also passed to outputs. The caller remains responsible for destroying the tag when finished.

Unit `unit-19`: grade 9.49; 31 words, 2 sentences, 50 syllables; below the failure threshold. Short sample.

> The called read VI uses the tag's local buffer; a separate completed tag read is needed when fresh controller data is required. A configured read cache can still return existing data.

Unit `unit-20`: grade 7.82; 47 words, 4 sentences, 75 syllables; below the failure threshold.

> The BOOL case deserves special care. It uses the same unsigned-byte getter as U8. It does not convert the result to a LabVIEW Boolean before making the variant. Extract a U8 value from the variant and apply the Boolean interpretation needed by the application.

Unit `unit-21`: grade 11.27; 81 words, 5 sentences, 141 syllables; below the failure threshold.

> For an ordinary non-bit tag, the full value must fit at the chosen byte offset. Integer choices use one, two, four or eight bytes according to their bit width. FLOAT uses four bytes, DOUBLE uses eight, and BOOL uses one. Validate the handle and available buffer size before the selected getter. In the upstream v2.0.22 implementation, getter failures can return values that also look like valid data; a later tag-status check does not reliably identify those failures.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example

### Review discussion

Section assessment: The example supplies a known buffer type, byte offset, enum selection, expected variant type and the checks needed before trusting the result.

Reading-level review: **PASS** — The current actual text units are below grade 12. Table rows, headings and identifiers were inspected separately for exact meaning.

Most demanding passage (unit-22):

> On a successful call, extract a single-precision value from the resulting variant.

Density assessment: The output extraction depends on the FLOAT selection and on successful completion; the preceding sentence supplies both the tag condition and the selection.

### Assessed text

Unit `unit-22`: grade 10.87; 55 words, 3 sentences, 90 syllables; below the failure threshold.

> For a ready tag whose buffer contains a single-precision value at byte offset 0, select FLOAT and call Read_By_Datatype.vi with that offset. On a successful call, extract a single-precision value from the resulting variant. Check the LabVIEW error output and the getter's error behavior before treating the result as valid.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, integer getters on a bit tag read the configured bit as 0 or 1 and ignore the byte offset. FLOAT and DOUBLE getters reject bit tags. The selector still stores the BOOL case result as U8.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-23):

> In the checked upstream 2.7.2 source, integer getters on a bit tag read the configured bit as 0 or 1 and ignore the byte offset. FLOAT and DOUBLE getters reject bit tags. The selector still stores the BOOL case result as U8.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-23`: grade 8.9; 44 words, 3 sentences, 70 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, integer getters on a bit tag read the configured bit as 0 or 1 and ignore the byte offset. FLOAT and DOUBLE getters reject bit tags. The selector still stores the BOOL case result as U8.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The current text retains the selection, BOOL/U8 distinction, buffer validation and version-scoped failure caveat. The saved-state warning was removed after a fresh source read. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A LabVIEW user can identify the required variant type and validate the buffer before relying on the getter. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
