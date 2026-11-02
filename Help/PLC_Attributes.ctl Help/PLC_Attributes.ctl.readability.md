# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:43+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\PLC_Attributes.ctl Help\PLC_Attributes.ctl.html`
Document SHA-256: `dfc0b9280b51d84fd69e6eaf820737b696baff529bd1fa6f28bb1439d5413243`

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
| Combined prose | 626 | 45 | 968 | 8.08 | within |
| Purpose and scope | 109 | 8 | 168 | 7.91 | below |
| Fields and saved values | 158 | 12 | 255 | 8.59 | within |
| Attribute construction | 214 | 16 | 336 | 8.15 | within |
| Example and recommended call sequence | 108 | 7 | 153 | 7.14 | below |
| Library version differences | 37 | 2 | 56 | 9.48 | within |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> The control groups the values; it does not create a tag or contact a controller by itself.

Density assessment: This distinguishes configuration from controller operations after identifying the cluster.

### Assessed text

Unit `unit-1`: grade 9.13; 36 words, 2 sentences, 54 syllables; below the failure threshold. Short sample.

> PLC_Attributes.ctl is a cluster of strings used to supply connection and tag attributes to Create_Tag.vi. The control groups the values; it does not create a tag or contact a controller by itself.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

Unit `unit-3`: grade 7.65; 33 words, 2 sentences, 47 syllables; below the failure threshold. Short sample.

> Create_Tag.vi trims whitespace from each field and builds the attribute string passed to libplctag. Its timeout is a separate virtual instrument (VI) input and is not a field in this control.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Fields and saved values

### Review discussion

Section assessment: The table identifies each of the eight string fields and control defaults; adjacent prose distinguishes instance values and explains the legacy zero-size and asynchronous cases. The actual HTML text and table cells were checked against the draft.

Reading-level review: **PASS** — The actual HTML paragraphs were measured below grade 12. The table rows and headings are valid score exclusions and were inspected for exact names, values and meaning.

Most demanding passage (unit-15):

> In the upstream v2.0.22 implementation, the saved empty size can produce a zero-byte buffer and a PLCTAG_ERR_BAD_PARAM status.

Density assessment: The field table establishes bytes, then this passage connects the empty value, version and status.

### Assessed text

Unit `unit-4`: grade 7.12; 36 words, 3 sentences, 55 syllables; below the failure threshold.

> Every field is a LabVIEW string. The values below are saved control defaults, not a guarantee that they match the target system. Set the address, route, controller type and tag to values appropriate for the application.

Unit `unit-14`: grade 6.01; 30 words, 3 sentences, 45 syllables; below the failure threshold.

> A control instance can carry values different from these defaults. For example, an application may save its own route and tag name. Check the actual instance used by the caller.

Unit `unit-15`: grade 10.27; 92 words, 6 sentences, 155 syllables; below the failure threshold.

> For an ordinary Logix tag, provide the element size in bytes, such as 4 for a 32-bit value, and the number of elements as decimal text. The wrapper does not send an elem_type attribute. In the upstream v2.0.22 implementation, the saved empty size can produce a zero-byte buffer and a PLCTAG_ERR_BAD_PARAM status. With zero timeout, creation can return a handle before that error is checked. Check tag status and release any returned handle. A replacement library or other tag type may handle sizing differently.

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

### Screening resolutions

- acronym_first_use: LGX may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'LGX is an exact saved controller-type value; the row identifies its role.'}
- acronym_first_use: NONE may need its full term before this use Resolution: {'status': 'PASS', 'reason': 'NONE is an exact debug-field value and its omission effect is explained in the row.'}

## Attribute construction

### Review discussion

Section assessment: The prose maps fields to attribute names, explains trimming and delimiters, and gives the version-scoped shared debug behavior. The actual HTML text and table cells were checked against the draft.

Reading-level review: **PASS** — The actual HTML paragraphs were measured below grade 12. The table rows and headings are valid score exclusions and were inspected for exact names, values and meaning.

Most demanding passage (unit-18):

> If the wrapper omits debug for NONE, the library uses zero; it does not preserve a prior debug level.

Density assessment: The preceding sentence identifies a library-shared level; this gives the exact condition and consequence.

### Assessed text

Unit `unit-16`: grade 7.79; 55 words, 4 sentences, 84 syllables; below the failure threshold.

> Create_Tag.vi reads and trims the eight fields. It concatenates the protocol, gateway, path, controller type, element size, element count and tag name into a single string. For a debug level other than the exact trimmed text NONE, it appends a debug attribute. It then passes the string and timeout to plc_tag_create.

Unit `unit-17`: grade 7.4; 74 words, 6 sentences, 114 syllables; below the failure threshold.

> The field names in the cluster and the C attribute names are not all identical. In particular, gatewayIP becomes gateway, while the element fields become elem_size and elem_count. The values are sent as text. The wrapper does not escape field values. In the legacy parser, & in a value starts another attribute, so avoid it in these fields. This control does not itself validate a network route or prove that a tag exists.

Unit `unit-18`: grade 9.09; 85 words, 6 sentences, 138 syllables; below the failure threshold.

> In upstream v2.0.22, tag creation sets the debug level shared by the loaded library. Use numeric text from 0 through 5: zero disables debug messages, and higher levels include more detail. If the wrapper omits debug for NONE, the library uses zero; it does not preserve a prior debug level. Text with no parseable integer also falls back to zero. Use a clean integer because the parser can accept a numeric prefix. This setting can affect other tags using the same loaded library.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example uses a concrete data width, valid-sized text values and a placeholder target, then identifies success checks and cleanup. The actual HTML text and table cells were checked against the draft.

Reading-level review: **PASS** — The actual HTML paragraphs were measured below grade 12. The table rows and headings are valid score exclusions and were inspected for exact names, values and meaning.

Most demanding passage (unit-20):

> If the LabVIEW error cluster is clear and the raw error code is 0, retain the returned handle.

Density assessment: The example distinguishes the two result channels before requiring the handle to be retained and later released.

### Assessed text

Unit `unit-19`: grade 7.22; 63 words, 4 sentences, 89 syllables; below the failure threshold.

> For an example with one 32-bit Logix tag, set protocol to ab_eip, path to 1,0, cpu to LGX, element size to 4, and element count to 1. Set gatewayIP to the actual controller address and tag name to the name of an existing 32-bit tag. Leave debug level as NONE. The route and tag must match the target system.

Unit `unit-20`: grade 7.04; 45 words, 3 sentences, 64 syllables; below the failure threshold.

> Pass the cluster and a 1000-millisecond timeout to Create_Tag.vi. If the LabVIEW error cluster is clear and the raw error code is 0, retain the returned handle. Use it for later operations, check each result, and call Destroy_Tag.vi when finished.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, creation changes the shared debug level only when the parsed debug value is greater than zero. The NONE choice omits that attribute, so it does not reset an existing level.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-21):

> In the checked upstream 2.7.2 source, creation changes the shared debug level only when the parsed debug value is greater than zero. The NONE choice omits that attribute, so it does not reset an existing level.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-21`: grade 9.48; 37 words, 2 sentences, 56 syllables; below the failure threshold. Short sample.

> In the checked upstream 2.7.2 source, creation changes the shared debug level only when the parsed debug value is greater than zero. The NONE choice omits that attribute, so it does not reset an existing level.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 0; limit: 3.


## Whole-document review

Whole document review: **PASS** — The actual HTML contains the same four reviewed sections, paragraphs and field values as the source draft. It progresses from purpose through fields and debug behavior to an example. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — The HTML text gives the LabVIEW reader the setup values, version-scoped cautions and check/cleanup sequence in usable order. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
