# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-02T22:39:41+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\Create_Tag.vi Help\Create_Tag.vi.html`
Document SHA-256: `77ed589e5203ac65957e7252747a9c222ff77ba88f986083de2a74963b660ac3`

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
| Combined prose | 818 | 62 | 1333 | 8.78 | within |
| Purpose and scope | 85 | 7 | 141 | 8.72 | within |
| Called function and library selection | 89 | 7 | 136 | 7.4 | below |
| Inputs | 140 | 12 | 237 | 8.94 | within |
| Outputs and error handling | 44 | 3 | 74 | 9.98 | within |
| Execution and C implementation | 289 | 20 | 470 | 9.24 | within |
| Example and recommended call sequence | 105 | 9 | 161 | 7.05 | below |
| Library version differences | 66 | 4 | 114 | 11.23 | above |

## Purpose and scope

### Review discussion

Section assessment: The purpose retains the operation and separates bundled version-string evidence from the legacy source description.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-1):

> The VI returns a tag handle for later operations or a native error code when creation fails.

Density assessment: The preceding sentences introduce the tag and attribute conversion before the two outcomes.

### Assessed text

Unit `unit-1`: grade 9.66; 45 words, 3 sentences, 74 syllables; below the failure threshold.

> Create_Tag.vi creates a libplctag tag for a programmable logic controller (PLC). It turns the PLC Attributes cluster into an attribute string and calls plc_tag_create. The VI returns a tag handle for later operations or a native error code when creation fails.

Unit `unit-2`: grade 8.07; 40 words, 4 sentences, 67 syllables; below the failure threshold.

> The bundled binaries contain the version string 2.7.2. Native behavior below is based on upstream 2.0.22 unless a newer version is identified. The bundled binaries may behave differently. Version strings alone do not prove exact binary build provenance.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: VI may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'VI is standard terminology for the stated LabVIEW audience.'}

## Called function and library selection

### Review discussion

Section assessment: The section gives the C prototype, calling convention, UI thread, null-terminated string and library selector.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded numerically but were reviewed for exact meaning; short samples limit the score.

Most demanding passage (unit-5):

> An embedded null byte ends the string seen by the library.

Density assessment: The preceding sentence introduces the C string pointer before the embedded-null limitation.

### Assessed text

Unit `unit-5`: grade 7.56; 44 words, 3 sentences, 65 syllables; below the failure threshold.

> The node uses the C calling convention and runs in the LabVIEW user interface (UI) thread. It passes the timeout by value and the attribute text as a null-terminated C string pointer. An embedded null byte ends the string seen by the library.

Unit `unit-6`: grade 7.42; 45 words, 4 sentences, 71 syllables; below the failure threshold.

> Choose_Lib.vi selects the library path. Its error output is wired into the library node before the native call. The attribute string and timeout are passed to the C function. A tag handle is a library identifier, not a PLC address or memory pointer.

### Exclusions from the score

- Unit `unit-3`: Unterminated fragment; check selection manually.
- Unit `unit-4`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Inputs

### Review discussion

Section assessment: The input and field tables identify the cluster members, saved values, timeout and native attribute mapping; the prose explains element sizing and zero-timeout errors.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded numerically but were reviewed for exact meaning; short samples limit the score.

Most demanding passage (unit-22):

> With zero timeout, the call can return a handle whose status reports the error; check its status and release the handle.

Density assessment: The earlier sentences state the missing-size condition and distinguish it from a nonzero-timeout error.

### Assessed text

Unit `unit-7`: grade 9.9; 14 words, 2 sentences, 27 syllables; below the failure threshold. Short sample.

> The connector inputs are marked recommended. Wire the cluster, timeout and error cluster explicitly.

Unit `unit-21`: grade 6.85; 26 words, 3 sentences, 42 syllables; below the failure threshold.

> These are saved values, not settings guaranteed to work for another controller. Choose appropriate protocol, address, route, CPU and tag values. All cluster fields are strings.

Unit `unit-22`: grade 9.81; 100 words, 7 sentences, 168 syllables; below the failure threshold.

> For an ordinary Logix tag, supply the element size in bytes and the element count as text. This wrapper does not send elem_type. With the upstream v2.0.22 implementation, an empty element size can leave the buffer size at zero and set PLCTAG_ERR_BAD_PARAM. A nonzero timeout returns that error during creation. With zero timeout, the call can return a handle whose status reports the error; check its status and release the handle. For example, use 4 for the size of a 32-bit element. Different tag types or replacement libraries can have different sizing rules.

### Exclusions from the score

- Unit `unit-8`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-12`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-13`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-15`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-16`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-17`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-18`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-19`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-20`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: I32 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'I32 is explained as signed 32-bit in the timeout row.'}
- acronym_first_use: LGX may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'LGX is an exact saved CPU value in the table.'}
- acronym_first_use: NONE may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'NONE is the exact saved debug value, not an acronym.'}

## Outputs and error handling

### Review discussion

Section assessment: The output table and prose distinguish the handle, mapped native error and independent LabVIEW call error.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded numerically but were reviewed for exact meaning; short samples limit the score.

Most demanding passage (unit-27):

> If an incoming LabVIEW error skips the C call, the numeric outputs do not establish successful creation.

Density assessment: The prior sentences identify the separate error channels before the skipped-call consequence.

### Assessed text

Unit `unit-27`: grade 9.98; 44 words, 3 sentences, 74 syllables; below the failure threshold.

> The wrapper does not convert a negative native return into the LabVIEW error cluster. Check error out and error code, then verify the returned handle is usable. If an incoming LabVIEW error skips the C call, the numeric outputs do not establish successful creation.

### Exclusions from the score

- Unit `unit-23`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-24`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-25`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-26`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Execution and C implementation

### Review discussion

Section assessment: The execution section covers field trimming and separators, global debug parsing, native setup, timeout, UI-thread delay and cleanup.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded numerically but were reviewed for exact meaning; short samples limit the score.

Most demanding passage (unit-29):

> If the wrapper omits debug for NONE, the library uses zero; it does not preserve a prior debug level.

Density assessment: The paragraph first identifies the shared debug setting and accepted numeric levels before explaining the omitted attribute.

### Assessed text

Unit `unit-28`: grade 9.15; 68 words, 5 sentences, 112 syllables; below the failure threshold.

> The VI unbundles the cluster and trims whitespace from each field. It concatenates protocol, gateway, path, cpu, elem_size, elem_count and name in that order. Unless the trimmed debug text is exactly NONE, it appends a debug attribute. The VI does not add an escaping step for separators inside field values. Avoid unescaped & and = in field values because they can change how the library parses the string.

Unit `unit-29`: grade 9.09; 85 words, 6 sentences, 138 syllables; below the failure threshold.

> In upstream v2.0.22, tag creation sets the debug level shared by the loaded library. Use numeric text from 0 through 5: zero disables debug messages, and higher levels include more detail. If the wrapper omits debug for NONE, the library uses zero; it does not preserve a prior debug level. Text with no parseable integer also falls back to zero. Use a clean integer because the parser can accept a numeric prefix. This setting can affect other tags using the same loaded library.

Unit `unit-30`: grade 10.63; 69 words, 4 sentences, 114 syllables; below the failure threshold.

> The legacy library initializes its state, parses the attributes and chooses a protocol-specific tag constructor. With a nonzero timeout it waits for setup to finish or fail, and it returns a negative timeout code if setup remains pending at the deadline. With zero timeout, use Tag_Status.vi to determine when the new tag is ready. A successfully created tag must later be released with Destroy_Tag.vi.

Unit `unit-31`: grade 8.3; 67 words, 5 sentences, 106 syllables; below the failure threshold.

> The node waits on the LabVIEW UI thread, so a long setup wait can delay the interface. Library initialization and tag construction occur before the timed wait. Use a nonnegative timeout. With a negative timeout, the deadline is already past; a tag that is still pending at the first status check is aborted and returns a timeout error. A tag already ready can still return a handle.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Example and recommended call sequence

### Review discussion

Section assessment: The example gives concrete protocol, CPU, size, count and timeout values while asking the reader for the actual destination and tag.

Reading-level review: **PASS** — All measured prose units are below grade 12. Code and table rows are excluded numerically but were reviewed for exact meaning; short samples limit the score.

Most demanding passage (unit-32):

> If error out is clear and error code is 0, the handle identifies the created tag.

Density assessment: The earlier sentences supply the example attributes and timeout before stating the observable result.

### Assessed text

Unit `unit-32`: grade 7.04; 48 words, 4 sentences, 73 syllables; below the failure threshold.

> For example, configure protocol as ab_eip, cpu as LGX, element size as 4 and element count as 1. Supply the actual controller address, route and tag name. Wire 1000 for timeout. If error out is clear and error code is 0, the handle identifies the created tag.

Unit `unit-33`: grade 7.07; 57 words, 5 sentences, 88 syllables; below the failure threshold.

> Populate the cluster for the intended controller and tag. Wire a timeout, such as 1000 milliseconds, and call this VI. If the LabVIEW error cluster is clear and the native code is 0, retain the handle. When asynchronous setup is used, check status until it is ready before read or write operations. Destroy the tag when finished.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Library version differences

### Review discussion

Section assessment: The version-specific comparison states the behavior and its scope: In the checked upstream 2.7.2 source, a negative timeout returns PLCTAG_ERR_BAD_PARAM (-7). A constructor error can be returned before a handle is created, even with timeout zero. The library changes its shared debug level only when the parsed debug value is greater than zero. If NONE is omitted by this wrapper, or the value is zero, the existing level is not reset.

Reading-level review: **PASS** — The saved prose is below the numeric grade threshold. Table rows and short passages were also read for meaning; short samples limit the score.

Most demanding passage (unit-34):

> In the checked upstream 2.7.2 source, a negative timeout returns PLCTAG_ERR_BAD_PARAM (-7). A constructor error can be returned before a handle is created, even with timeout zero. The library changes its shared debug level only when the parsed debug value is greater than zero. If NONE is omitted by this wrapper, or the value is zero, the existing level is not reset.

Density assessment: This passage states the condition and the resulting behavior together; the surrounding section supplies the caller context.

### Assessed text

Unit `unit-34`: grade 11.23; 66 words, 4 sentences, 114 syllables; below the failure threshold.

> In the checked upstream 2.7.2 source, a negative timeout returns PLCTAG_ERR_BAD_PARAM (-7). A constructor error can be returned before a handle is created, even with timeout zero. The library changes its shared debug level only when the parsed debug value is greater than zero. If NONE is omitted by this wrapper, or the value is zero, the existing level is not reset.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Revision evidence

Substantive rewrite batches used: 1; limit: 3.

### Rewrite `c1d920af22681d40058d` (batch 1)

Original snapshot: `5b251dd6bac5a4fdbdb63382cba7fb8e90928eae7f46cd9567aa597923751477`; method: approachable-fk/2.0.

Original artifact: `2164ffde82ba8cdca80d283e07087a4a7ccec5ddeba6fb8a74e4200362e147c8`. Grade 12.27; 40 words, 2 sentences, 68 syllables.

> Create_Tag.vi converts the PLC Attributes cluster for a programmable logic controller (PLC) into a libplctag attribute string and calls plc_tag_create. It returns a tag handle for later operations or a native error code when creation fails.

Clarity problem: The initial sentence combined the PLC expansion, attribute conversion and native call.

Change: Separate the operation, conversion and result into three sentences.

Current unit `unit-1`: grade 9.66; 45 words, 3 sentences, 74 syllables.

> Create_Tag.vi creates a libplctag tag for a programmable logic controller (PLC). It turns the PLC Attributes cluster into an attribute string and calls plc_tag_create. The VI returns a tag handle for later operations or a native error code when creation fails.

Preserved facts and relationships:

- The PLC Attributes cluster becomes an attribute string.
- The VI calls plc_tag_create and returns a handle or native error code.

Source references:

- Help/.support/help-generation/stable-live/Create_Tag.vi.a03fb59c98e0.json
- Help/Set_U8.vi Help/.support/Set_U8/evidence/v2.0.22/lib.c

Technical integrity: **PASS** — Compared the current prose and any adjacent table with the archived failing passage and the pinned source; the exact conditions, codes and operational effects remain intact.


## Whole-document review

Whole document review: **PASS** — The page preserves field and default meanings, string construction, timeout and shared-debug side effects, separate result channels and tag ownership. The current version notice and comparison were reviewed against the saved binaries and pinned source.

Reader simulation: **PASS** — A caller can choose attributes, wire a timeout, check the returned handle and status, and release the tag. Version-scoped exceptions are available before the caller relies on native behavior.

This companion report is separate from the product and is not recursively reviewed.
