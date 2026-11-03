# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:43+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Read_By_Datatype.vi Help\Read_By_Datatype.vi.html`
Document SHA-256: `71395293e0c4d061a5dc9ba5c768c9ec1301171c3d98d7976df1f091c4c1cebb`

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

Measured prose units: 17; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 573 | 43 | 915 | 8.45 | within |
| Purpose and scope | 125 | 9 | 197 | 8.42 | within |
| Called VIs and dependencies | 101 | 8 | 155 | 7.44 | below |
| Inputs | 63 | 6 | 111 | 9.3 | within |
| Outputs and error handling | 98 | 6 | 158 | 9.8 | within |
| Execution | 54 | 4 | 88 | 8.9 | within |
| Example and recommended call sequence | 86 | 7 | 136 | 7.86 | below |
| Library version differences | 46 | 3 | 70 | 8.35 | within |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> Read_By_Datatype.vi selects a typed read VI from the Datatype enum and reads one value from an existing tag's local data buffer. It returns that value as a LabVIEW variant. For an ordinary non-bit tag, the selected type determines the number of bytes read and the type stored in the variant.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-1`: grade 8.91; 54 words, 3 sentences, 80 syllables; below the failure threshold.

> Read_By_Datatype.vi selects a typed read VI from the Datatype enum and reads one value from an existing tag's local data buffer. It returns that value as a LabVIEW variant. For an ordinary non-bit tag, the selected type determines the number of bytes read and the type stored in the variant.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

Unit `unit-3`: grade 9.49; 31 words, 2 sentences, 50 syllables; below the failure threshold. Short sample.

> The VI does not itself request fresh data from the controller. Complete a Read_Tag.vi operation first when current controller data is needed, and account for any configured read cache.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW audience.'}

## Called VIs and dependencies

### Review discussion

Section assessment: The case table lists each enum choice, called VI and contained variant type, including BOOL to U8.

Reading-level review: **PASS** — All measured prose and list items are below grade 12. Table rows are excluded numerically but were read for exact mapping; short samples limit the score.

Most demanding passage (unit-18):

> The BOOL case does not create a Boolean variant.

Density assessment: The table first shows BOOL selecting Read_U8 and returning U8, then the prose calls out the non-obvious type.

### Assessed text

Unit `unit-4`: grade 8.38; 29 words, 2 sentences, 45 syllables; below the failure threshold. Short sample.

> Datatype.ctl supplies the enum choices. A case structure selects one read VI, passes it the handle, byte offset and error cluster, and converts its result to a variant.

Unit `unit-17`: grade 9.54; 28 words, 3 sentences, 51 syllables; below the failure threshold.

> I choices are signed integers; U choices are unsigned integers. The number in each name is the bit width. FLOAT is single precision and DOUBLE is double precision.

Unit `unit-18`: grade 5.95; 44 words, 3 sentences, 59 syllables; below the failure threshold.

> The BOOL case does not create a Boolean variant. It puts the byte returned by Read_U8.vi into the variant. The I8 case is the default case of the structure; this does not establish the saved default of an enum control.

### Exclusions from the score

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

- acronym_first_use: I8 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: I16 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: I64 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: U8 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: U16 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: U32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: U64 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: FLOAT may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: SGL may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: DOUBLE may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: DBL may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}
- acronym_first_use: BOOL may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'The table uses exact enum and LabVIEW type names; the following prose explains I/U widths, FLOAT/DOUBLE precision and the BOOL/U8 distinction.'}

## Inputs

### Review discussion

Section assessment: The offset and fit rules explicitly apply to ordinary non-bit tags; the comparison explains 2.7.2 bit-tag behavior.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-19):

> LabVIEW marks the terminals as recommended. Wire the handle, offset, datatype and error cluster.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-19`: grade 9.05; 14 words, 2 sentences, 26 syllables; below the failure threshold. Short sample.

> LabVIEW marks the terminals as recommended. Wire the handle, offset, datatype and error cluster.

Unit `unit-25`: grade 9.66; 49 words, 4 sentences, 85 syllables; below the failure threshold.

> For an ordinary non-bit tag, the chosen type must fit in the available buffer bytes. Integer choices use the number of bits in their name divided by eight. FLOAT uses four bytes, DOUBLE uses eight, and BOOL uses one. Validate the offset and size for the selected type.

### Exclusions from the score

- Unit `unit-20`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-21`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-22`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-23`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-24`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Outputs and error handling

### Review discussion

Section assessment: The revised text preserves the interface and qualifies the changed version or selector behavior.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-31):

> The selected getter returns a value rather than a separate native status output.

Density assessment: This sentence establishes the result channel before the paragraph explains ambiguous and indeterminate legacy failures.

### Assessed text

Unit `unit-31`: grade 9.11; 62 words, 4 sentences, 98 syllables; below the failure threshold.

> The selected getter returns a value rather than a separate native status output. In upstream v2.0.22, integer getters can return a limit value on invalid input; that same value can be valid data. The old floating-point getters have different failure paths. Check the selected read VI's detailed help and validate the handle and buffer range before using the variant.

Unit `unit-32`: grade 11.1; 36 words, 2 sentences, 60 syllables; below the failure threshold. Short sample.

> The LabVIEW error output is not a complete native-getter success indication. If the incoming error status causes the underlying library node to skip, do not use the returned value as evidence of a successful read.

### Exclusions from the score

- Unit `unit-26`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-27`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-28`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-29`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-30`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Execution

### Review discussion

Section assessment: The execution steps follow case selection, local read, To Variant and the connector outputs.

Reading-level review: **PASS** — All measured prose and list items are below grade 12. Table rows are excluded numerically but were read for exact mapping; short samples limit the score.

Most demanding passage (unit-35):

> A To Variant function wraps the returned value without converting its numeric type.

Density assessment: The first two steps establish the selected value before explaining the variant conversion.

### Assessed text

Unit `unit-33`: grade 7.59; 9 words, 1 sentences, 15 syllables; below the failure threshold. Short sample.

> The case structure selects a read VI using Datatype.

Unit `unit-34`: grade 7.57; 14 words, 1 sentences, 21 syllables; below the failure threshold. Short sample.

> The selected VI reads the chosen type from the tag's local buffer at offset.

Unit `unit-35`: grade 8.54; 13 words, 1 sentences, 21 syllables; below the failure threshold. Short sample.

> A To Variant function wraps the returned value without converting its numeric type.

Unit `unit-36`: grade 11.75; 18 words, 1 sentences, 31 syllables; below the failure threshold. Short sample.

> The selected VI's handle and error outputs, the variant, and the datatype selection pass to the connector outputs.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example supplies a four-byte FLOAT at offset zero, status checks, SGL extraction, BOOL/U8 handling and cleanup.

Reading-level review: **PASS** — All measured prose and list items are below grade 12. Table rows are excluded numerically but were read for exact mapping; short samples limit the score.

Most demanding passage (unit-37):

> If a four-byte single-precision value starts at byte 0, select FLOAT and set offset to 0.

Density assessment: The first sentences establish a ready tag and optional controller refresh before the specific choice and offset.

### Assessed text

Unit `unit-37`: grade 7.56; 59 words, 4 sentences, 87 syllables; below the failure threshold.

> Create a tag and confirm that it is ready. When fresh data is required, perform a tag read and check its result. If a four-byte single-precision value starts at byte 0, select FLOAT and set offset to 0. After the selected read, check the error cluster and the getter limitations, then extract an SGL from the variant.

Unit `unit-38`: grade 9.33; 27 words, 3 sentences, 49 syllables; below the failure threshold.

> For BOOL, extract U8 rather than Boolean. Apply the application's intended Boolean interpretation to that byte. Destroy the tag when the application no longer needs it.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, integer getters on a bit tag read the configured bit as 0 or 1 and ignore the byte offset. The FLOAT and DOUBLE getters reject bit tags. The BOOL case still wraps the U8 result in a variant.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-39):

> In the checked upstream 2.7.2 source, integer getters on a bit tag read the configured bit as 0 or 1 and ignore the byte offset. The FLOAT and DOUBLE getters reject bit tags. The BOOL case still wraps the U8 result in a variant.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-39`: grade 8.35; 46 words, 3 sentences, 70 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, integer getters on a bit tag read the configured bit as 0 or 1 and ignore the byte offset. The FLOAT and DOUBLE getters reject bit tags. The BOOL case still wraps the U8 result in a variant.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The saved page consistently maps every enum case to its getter and variant type and retains the BOOL and getter-failure cautions. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A LabVIEW caller can choose a type, validate the buffer and extract the actual variant type before cleanup. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
