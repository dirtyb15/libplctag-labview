# LabVIEW help generation specification

## 1. Purpose and authority

This specification defines how to create two help files for each LabVIEW virtual instrument (VI) and control (`.ctl`) in the repository root. The detailed help uses Hypertext Markup Language (HTML). It explains each VI and its connector inputs and outputs, or each control and its fields or choices. A separate plain-text file provides the short description used for Context Help.

The approved examples are [the Set_U8 detailed help](<Set_U8.vi Help/Set_U8.vi.html>) and [its Context Help](<Set_U8.vi Help/Set_U8.vi Context Help.txt>). Follow their presentation and naming. Inspect each VI before writing its content. The example's defaults, error codes and library behavior must not be copied into other topics without evidence.

In this document, **must** marks an acceptance requirement. **Should** marks the preferred practice; record a reason when departing from it. **May** marks an optional feature. A batch is complete only when every VI and control found in scope has an accepted pair of files.

## 2. Scope and discovery

Treat the directory containing the wrapper VIs as the repository root, written as `.`. Discover files directly in that directory whose extension equals `.vi` or `.ctl`, ignoring extension case. Sort their names for a stable processing order. Do not search subdirectories for additional targets.

Include wrapper, helper, selector and example VIs, as well as control files. Thus, files such as `Choose_Lib.vi`, `Read_By_Datatype.vi` and `SimpleReadWrite.vi` remain in scope even if they have no direct C call. Existing help does not remove a VI from the inventory.

Inspect dependencies outside this target set when their behavior affects a target VI. That inspection does not add those dependencies to the set of help topics. Libraries, projects, archives and shared-library binaries are supporting inputs rather than extra topics.

This Python example lists the files in scope. It shows how to find targets; it does not generate help.

```python
from pathlib import Path

repo_root = Path(".")
targets = sorted(
    (p for p in repo_root.iterdir()
     if p.is_file() and p.suffix.casefold() in {".vi", ".ctl"}),
    key=lambda p: (p.name.casefold(), p.name),
)
```

Take the inventory at the start of a run. Check it again before declaring the batch complete. Process added or changed targets, and record removed targets. Do not silently delete their old help folders.

## 3. Output names and relative paths

Let `vi_name` be the complete source filename, including `.vi` or `.ctl`. Preserve its spelling, spaces and extension. Create the output folder and two primary files by these rules:

| Item | Repository-relative path |
|---|---|
| Source VI or control | `<vi_name>` |
| Topic folder | `Help/<vi_name> Help/` |
| Detailed help | `Help/<vi_name> Help/<vi_name>.html` |
| Context Help | `Help/<vi_name> Help/<vi_name> Context Help.txt` |
| Topic working files | `Help/<vi_name> Help/.support/` |
| Batch inventory and manifest | `Help/.support/help-generation/` |

The same pattern applies to controls. For example, `Datatype.ctl` uses the folder `Help/Datatype.ctl Help/` and files `Datatype.ctl.html` and `Datatype.ctl Context Help.txt`.

For the approved VI example, the two primary outputs are:

```text
Help/Set_U8.vi Help/Set_U8.vi.html
Help/Set_U8.vi Help/Set_U8.vi Context Help.txt
```

All filesystem paths in this specification, portable source records and generated help must be relative. Paths in commands and manifest entries are relative to the repository root. Links inside a document are relative to that document's folder. Use forward slashes in saved paths and links.

For example, a link from the Set_U8 topic to the Read_U8 topic uses `../Read_U8.vi%20Help/Read_U8.vi.html`. A link from this specification to the approved example uses `Set_U8.vi%20Help/Set_U8.vi.html`. Encode spaces in HTML link targets and escape reserved characters correctly.

Do not embed drive letters, user-profile directories, network shares or local file URLs in either help product. A tool may need an absolute path while it runs. Resolve that path from the chosen root at run time; keep it out of the portable products and manifest.

The upstream web address identifies the C source project. It is not a path on disk. Use this project link, with no tracking fields: [libplctag/libplctag](https://github.com/libplctag/libplctag).

Keep drafts, evidence, extracted diagrams, source text and review records inside `Help`. Do not create another copy in an installed skill folder or an external artifact folder. If a review tool needs reports beside a product, retain those reports in its topic folder. They are separate from the two primary help files.

## 4. Read the source before writing

Use LVKit to read each binary VI and its actual dataflow. Read each control with a LabVIEW-aware control reader and capture its type, fields or enum choices, and saved values. A filename, icon, old description or family resemblance is not proof of behavior. Do not use text searches over a binary VI as a substitute for a LabVIEW-aware reader.

Capture the interface and follow the wires through each relevant structure. Read helper VIs when they determine paths, errors, units, selected operations or output values. Resolve unsupported nodes before making claims that depend on them. A missing fact must remain unknown until evidence resolves it.

The evidence record must cover these items when present:

| Area | Facts to capture |
|---|---|
| Identity | Relative VI path, content hash, saved LabVIEW version and inspection tool version. |
| Connector pane | Pattern, connected terminals, directions, exact labels, types and required or recommended wiring rules. |
| Defaults | Saved control values, type-defined defaults and any defaults that cannot be established. |
| Dataflow | Producers of every output; cases, loops, sequences, constants, conversions, subVI calls and unwired outputs that affect interpretation. |
| Execution | Reentrancy and thread settings when relevant and supported by decoded evidence. |
| Library calls | Exported symbols, argument order, return types, calling convention, scalar or pointer passing, callbacks, library path inputs and their producers. |
| Dependencies | Helpers, typedefs and native functions whose behavior is needed to explain the VI. |

Keep a saved value distinct from an allowed range or suggested value. A missing decoded default does not prove that the default is zero. Preserve meaningful label quirks in the evidence record; explain them in the help only when they help the caller identify or use a terminal.

Preserve source VIs, controls and dependencies. Write help and support files only. Do not resave source files, run VIs, call a bundled library, communicate with a controller or install help into VI properties as part of this workflow.

## 5. Upstream C source and version selection

Use the [upstream libplctag Git project](https://github.com/libplctag/libplctag) as the authority for native C behavior. A sibling local checkout may be a read cache, but it must not be a required path. Verify any cached source against the selected upstream commit.

First identify the shared libraries the VI can actually load. On Windows these are dynamic link libraries (DLLs). Follow dynamic path wiring and target selection; the library name saved on a node may differ from the runtime filename. Check each relevant bundled binary's identity and available version evidence.

Select the upstream tag or revision that matches the deployed library version as closely as the evidence allows. Resolve the selection to a full commit identifier. If a tag points to another tag object, follow it to the commit. Read the function declaration, implementation, called helpers, constants and relevant protocol code at that same commit.

Do not infer an exact build match from an embedded version string alone. Record the distinction between a matching version and proven build provenance. If the deployed version is unknown, explain only the scope supported by the evidence. Do not present a newer branch as the bundled binary's behavior.

For a separate comparison with newer source, choose and record its commit too. Label the versions in the help and explain only differences that affect callers. Do not make the latest branch a moving source for an already accepted topic.

The earlier Set_U8 analysis provides a verified upstream example. Tag `v2.0.22` resolves to commit `b5a038a9bfbf31649927ee1959d7fbceffd3876a`. At that commit, its setter is in [src/lib/lib.c](https://github.com/libplctag/libplctag/blob/b5a038a9bfbf31649927ee1959d7fbceffd3876a/src/lib/lib.c#L1465-L1498). This is an example of a pinned source record, not a fixed version for every future run.

Discover source paths at the selected revision. Older and newer revisions may use different directory layouts. Search by the actual exported symbol rather than assuming a path from the approved example.

## 6. Technical meaning to establish

Explain the combined behavior of the LabVIEW wrapper and the native implementation. Keep the wrapper's checks and conversions distinct from behavior inside the C library. Follow the application programming interface (API) contract far enough to explain what success and failure mean for the caller.

| Topic | Required interpretation when applicable |
|---|---|
| Handles and resources | What a handle identifies, how it is obtained, when it is valid and who releases it. |
| Local and remote data | Whether the operation changes local memory, starts a controller transfer, waits for completion or only checks a result. |
| Offsets and sizes | Byte, bit or element units; indexing origin; bounds; element widths; buffer ownership and length rules. |
| Values | Numeric range, signedness, representation, byte order, conversions, text encoding, special values and pointer-result lifetime. |
| Timing | Timeout units, zero-timeout meaning, pending states, polling, retries and completion conditions. |
| Errors | Native return codes, LabVIEW error clusters, incoming-error behavior, warnings and whether the wrapper converts between results. |
| Getter results | Returned data versus status; ambiguous sentinel values; how the selected version reports a failed get. |
| Concurrency | Mutex scope, shared data, reentrancy and whether a series of calls needs caller coordination. |
| Library choice | Target cases, filenames, path construction and behavior for unsupported targets. |
| Cleanup | Resource release, failed-operation cleanup and ownership after an error. |

Never assume that every error-like number is a library status. A getter may return data, a tag creator may return a handle or an error, and a wrapper may pass a scalar through unchanged. Trace the source and the output wire for each case.

Check what each function actually does. Some calls touch only local data; others start a network request. Read each timeout rule in the selected source version. A raw library failure reaches the LabVIEW error cluster only if the wrapper puts it there. Follow the wires to check that step. Do not borrow behavior from another VI.

## 7. Detailed-help content

The HTML body must start with the visible heading **Purpose and scope**. Do not put the VI name, a page title, a banner or a table of contents above it. A descriptive browser-tab title inside the document head is allowed.

Use the following order. Adapt conditional sections to the VI's actual role without adding empty boilerplate:

| Order | Heading | Content |
|---|---|---|
| 1 | Purpose and scope | What the VI does, why a caller uses it, local or remote effects, prerequisites and the supported library-version scope. |
| 2 | Called function and library selection | For a native wrapper: exact C prototype, symbol, argument mapping, runtime binary selection and deployment behavior. |
| 2, alternative | Called VIs and dependencies | For a helper or composite VI: called operations and their roles. Include this instead of inventing a native call. |
| 3 | Inputs | Functional signature, type explanations and a table with exact terminal name, type, meaning and established default. Explain units and constraints in prose. |
| 4 | Outputs and error handling | Every connector output and its producer, success criteria, error channels, normal failure codes and useful caller responses. |
| 5 | Execution and C implementation | Ordered wrapper and native behavior. Use the shorter heading Execution when no C implementation is relevant. Explain control flow, cleanup and concurrency. |
| 6 | Example and recommended call sequence | At least one concrete usage example with expected results, followed by the relevant setup, call, checks and cleanup steps. |
| 7, conditional | Library version differences | Only material differences verified between the relevant source revisions. Omit when no such comparison is needed. |

List every connector input and output exactly once in its interface table. For a VI with no inputs or outputs, state that fact in the relevant section and omit the empty table. Do not invent connector inputs for controls that are not wired to the pane. Explain such controls elsewhere if they affect a runnable example.

For a cluster, describe every field that the caller must supply or interpret. For an enum, list the named choices and what each choice does. For arrays, show the element type and dimensions. For strings or paths, state the required form, units and encoding when the code defines them. Resolve typedefs to explain their contents; a type name alone is not a field description.

For a control, adapt these sections to its type. Describe its fields, enum choices and established saved defaults. Explain how the control is used, but do not invent a connector pane or a native call for it.

Include the wiring rule beside each VI input or in nearby prose. For a native call, map the LabVIEW terminals to the C arguments and return value. Explain any conversion between them.

Examples must use internally consistent values and show what the caller can observe. Distinguish a proposed example from an executed test. A controller example may use a clearly marked placeholder endpoint; it must not include a real machine address taken from the author's environment.

The detailed help must contain no References, Bibliography, Sources or Context Help section. Do not add an authoring appendix, source-code citation list, absolute local link, parser report or drafting history. Store source traceability in support records. Retain operating qualifications that the caller needs, such as a version limit or a separate required write.

## 8. HTML format and visual design

Write the page as a complete HTML file. Use UTF-8 without a byte-order mark. The following shell defines its required structure. Replace `{vi_name}` with the source filename. Fill the main element with the topic's sections, starting with Purpose and scope.

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{vi_name} - Detailed Help</title>
  <style>/* Embed the approved stylesheet here. */</style>
</head>
<body>
<main>
  <h2>Purpose and scope</h2>
  <!-- Add the verified topic content and remaining sections. -->
</main>
</body>
</html>
```

Escape code and text. Pointer marks, comparison signs and terminal labels must show as literal content.

Use the [approved stylesheet](templates/vi-help.css) as the design template. Embed its Cascading Style Sheets (CSS) rules inside each HTML file. The delivered page must open from disk without a server, external font, script, network stylesheet or build step.

| Design element | Required baseline |
|---|---|
| Body | Segoe UI with Arial and sans-serif fallbacks; 16-pixel base size; line height 1.65. |
| Content panel | White panel, maximum width 980 pixels, centered on a light gray page; 36-pixel outer margin and 36-by-44-pixel padding at desktop width. |
| Section headings | Blue, 1.3-rem size, bottom rule and clear spacing. Use the approved section-heading treatment, with no visible top-level document title. |
| Tables | Full width, collapsed borders, shaded header, alternating light rows, top-aligned text and adequate cell padding. |
| Code | Consolas with monospace fallbacks; inline code shading; preformatted blocks with a left rule and horizontal overflow. |
| Narrow windows | At 650 pixels or below, reduce panel padding and remove the outer frame. Wide tables scroll within their wrapper. |
| Printing | White background, no panel frame, readable text and sensible breaks around headings, rows and code. |

Use real heading, paragraph, list, table-header and code elements. Give column headers `scope="col"`. Do not use screenshots of text or tables. Preserve the example's spacing and contrast, while allowing longer names and wider interface tables.

Related-help links may appear in relevant prose if useful. They must be relative and point to accepted topics. Do not add placeholder links or reintroduce a references list. If a linked topic is not ready, use its plain VI name until the destination exists.

## 9. Context Help text

Write Context Help as a separate UTF-8 plain-text file without a byte-order mark. Use Windows line endings for easy copying into a VI description. Start with the operation itself, without a title or filename prefix.

Aim for one or two short paragraphs, usually 60 to 120 words. A simple helper may need fewer words. Do not remove a critical condition merely to meet the target. The text should make sense when shown without the detailed help.

The first paragraph should state the purpose, key input meanings, units and major side effect. The second should state the essential success or failure rule and any important follow-up call. For a simple helper, combine these into one paragraph when clear.

Use plain names such as `Write_Tag.vi`, but do not include Markdown backticks, headings, tables, bullets, HTML tags, citations or source links. Explain an acronym if the text introduces it. Do not copy the detailed help's terminal tables, implementation steps or version-comparison table into this file.

The short text must agree with the detailed help about what success proves. For a local setter, it must retain the separate controller-write requirement when applicable. For a getter, creator, selector or example, write the rule supported by that VI instead.

## 10. Evidence and batch manifest

Keep source traceability separate from user help. Use JavaScript Object Notation (JSON) for a machine-readable batch manifest. Each target needs a record that identifies its source, output paths, evidence, review state and any unresolved problem.

A content hash records which bytes were read. Use the Secure Hash Algorithm 256 (SHA-256) method for these hashes. Hash the source VI or control, its relevant dependencies, the library candidates, the style template and the accepted outputs. A source line number alone does not identify the source. Each C-source record must name the repository, full commit, relative file path and symbol.

The following record illustrates relative paths and a pinned C source. It is deliberately pending; null hashes are not accepted results:

```json
{
  "schema_version": 1,
  "source": "Set_U8.vi",
  "state": "pending",
  "vi_sha256": null,
  "dependencies": [],
  "libraries": [],
  "c_sources": [{
    "repository": "https://github.com/libplctag/libplctag",
    "ref": "v2.0.22",
    "commit": "b5a038a9bfbf31649927ee1959d7fbceffd3876a",
    "path": "src/lib/lib.c",
    "symbol": "plc_tag_set_uint8"
  }],
  "detailed_help": "Help/Set_U8.vi Help/Set_U8.vi.html",
  "context_help": "Help/Set_U8.vi Help/Set_U8.vi Context Help.txt",
  "detailed_sha256": null,
  "context_sha256": null,
  "style_sha256": null,
  "review_state": "pending",
  "issues": []
}
```

An accepted record must also contain completed dependency and library identities where relevant, tool versions, a review date and the review-record paths. Use `not_applicable` with a reason for a topic that has no native call. Do not substitute empty evidence lists for missing analysis.

Use the states `pending`, `in_progress`, `accepted` and `blocked`. Blocked means a necessary fact or check prevents acceptance; record the exact issue. A blocked VI stays in the inventory. Other independent VIs may still be completed.

## 11. Generation sequence and safe updates

Use the following sequence for each batch. Save progress so an interrupted run can resume from its manifest.

1. Discover and sort the root-level VI and control inventory. Record source hashes before analysis.
2. Read the relevant VIs, dependencies, library-choice logic and binary-version evidence. Build a fact record before drafting.
3. Resolve and inspect the upstream C revisions needed for each actual native call. Reuse verified evidence for identical content where appropriate.
4. Draft both products from the fact record. Use the shared style and the exact naming rules. Keep candidate files under the topic's `.support/` folder.
5. Read both draft files to check their facts and layout. Check that the short text agrees with the detailed help and that the prose is clear. Correct the files and repeat the checks that the change affects.
6. Render and inspect the HTML in a browser. Check the top, tables, code, lower sections, narrow-window behavior and print layout. Read the plain-text file as a standalone description.
7. Recheck source and dependency hashes before publishing. If they changed, re-read the affected code and repeat its content review.
8. Replace the final pair only after both candidates pass. Publish the pair and its manifest state together, with recovery from an interrupted replacement. Keep the prior accepted pair until the replacement is verified.
9. Recheck the root inventory, resolve remaining entries and write a batch summary with accepted and blocked counts.

Do not overwrite a hand-edited accepted file without detecting its changed hash. Preserve the edited content in support, compare it with the proposed version and retain useful corrections. Do not alter or clean up unrelated repository files.

Reuse a prior accepted pair only if its source file, relevant dependencies, library identity, C revision, style and governing rules still match. Changes to a shared helper or source revision must invalidate affected topics. Existing Set_U8 help must pass the same checks as the rest of the batch.

## 12. Acceptance and completion

Review every substantive section, table, example, code block and plain-text paragraph. Write for a LabVIEW user who understands wires, subVIs and error clusters but is new to libplctag. Define new terms before relying on them, and preserve exact types, units, ranges and conditions.

Aim for ninth-grade explanatory prose. Measure paragraphs and procedural items with a consistent method. A measured unit at grade 12 or above must be revised; a low document average cannot clear it. Keep technical identifiers in the measure. Review tables, code and other valid exclusions for meaning even when they receive no numerical score.

The acceptance record must show these checks for each pair:

| Check | Pass condition |
|---|---|
| Coverage | Every root-level VI and control has an inventory entry; every accepted entry has both correctly named files. |
| Interface | All VI connector inputs and outputs, and all control fields or choices, match the current source. Types, defaults and constraints have evidence. |
| Native behavior | Every native-call claim is tied to the selected upstream commit and supported version scope. |
| Error meaning | Data, handles, raw status, pending results and LabVIEW error clusters are distinguished correctly. |
| Detailed structure | First visible heading is Purpose and scope. There is no visible document title, references list or Context Help block. |
| Context format | Separate plain text with no markup or references; readable alone and consistent with the detailed topic. |
| Portability | Published filesystem paths are relative; local links resolve from the document folder; no environment-specific path is embedded. |
| Rendering | Offline opening succeeds. Tables, code and paragraphs remain readable at desktop, narrow and print sizes. |
| Writing | Technical and section-level readability reviews pass on the current saved text. |
| Integrity | Source hashes still match; accepted output hashes and review records identify the final files. |
| Clean delivery | Drafts and evidence stay in support; no unresolved necessary fact is presented as accepted help. |

Screening tools can flag omissions and format faults, but they cannot approve technical meaning. Record actual review decisions and the reason for any conditional omission. Keep analysis problems and authoring notes in separate review records, not in the help body.

The batch must not report complete while any discovered VI or control lacks an accepted pair. Its summary must identify blocked topics and what evidence or correction remains. A file that merely exists is not a completed topic.
