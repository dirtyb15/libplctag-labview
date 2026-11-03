# Readability discussion

Review status: **PASS**

Generated (Coordinated Universal Time): 2026-11-03T11:07:02+00:00
Document: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\Help\PLC_Attributes.ctl Help\.support\expanded-help\PLC_Attributes.ctl.html`
Document SHA-256: `7a98bfc8c0c03f3812d3e460ae619fa366611110541f80af152858d51f5b3cf7`

Audience: LabVIEW developer who is new to PLCs and industrial networks
Prerequisites: Basic LabVIEW controls, wires and error clusters; PLC terms introduced in the text
Scope: Current document.
Reviewer: Codex

Tool: approachable-fk/2.0 (English heuristic; one syllable per numeric token)
Target: near ninth grade; 8.0–10.0 is an advisory band. Each measured prose unit at or above 12 fails the numerical check (unrounded comparison).
Numeric tokens count as one word and one syllable. Technical names remain in the score.
This is a writing preference, not a government or Navy requirement.

Estimated English syllables; punctuation cannot prove grammatical completeness. Numeric tokens count as one word and one syllable by local convention, not pronunciation. Review selected text, abbreviations, identifiers, and technical pronunciations. Short samples are unstable. Scores do not measure comprehension or accuracy.

## Numerical check and blockers

Measured prose units: 44; failing units: 0.

No numerical failures. Full semantic and technical review is still required.

## Calculated estimates

Combined scores use pooled counts, not an average of section grades.

| Text scope | Words | Sentences | Estimated syllables | Estimated grade | Band |
| --- | ---: | ---: | ---: | ---: | --- |
| Combined prose | 2270 | 172 | 3573 | 8.13 | within |
| Purpose and scope | 205 | 16 | 328 | 8.29 | within |
| How the fields work together | 155 | 15 | 249 | 7.4 | below |
| Fields and saved values | 36 | 3 | 60 | 8.76 | within |
| Protocol choices | 88 | 8 | 154 | 9.35 | within |
| Controller family: saved dropdown choices | 83 | 7 | 131 | 7.66 | below |
| Other family values accepted by the C lookup | 38 | 3 | 58 | 7.36 | below |
| Understanding path | 489 | 33 | 748 | 8.24 | within |
| Tag names and data-file addresses | 242 | 18 | 369 | 7.65 | below |
| Element size, count and local byte offsets | 227 | 16 | 348 | 8.03 | within |
| Debug dropdown: every level | 89 | 7 | 135 | 7.27 | below |
| Complete hardware examples | 228 | 15 | 378 | 9.9 | within |
| What Create_Tag.vi sends to C | 166 | 12 | 266 | 8.71 | within |
| First connection and troubleshooting | 224 | 19 | 349 | 7.39 | below |

## Purpose and scope

### Review discussion

Section assessment: The opening defines PLC and a library tag, names the consuming VI, and separates string menus from numeric enums.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The string/menu distinction is the main new concept; it follows the plain-language purpose and avoids implying that a saved label guarantees native support.

Most demanding passage (unit-3):

> All eight fields store strings, including the numbers. Four have dropdown suggestions: protocol, path, cpu, and debug level. These are string combo boxes, not LabVIEW numeric enums. Their menu entries are listed below. The C library decides whether a string is valid; an entry in the menu does not prove support.

Density assessment: The string/menu distinction is the main new concept; it follows the plain-language purpose and avoids implying that a saved label guarantees native support.

### Assessed text

Unit `unit-1`: grade 10.25; 62 words, 4 sentences, 104 syllables; below the failure threshold.

> PLC_Attributes.ctl describes which controller to reach and which value to access inside it. A programmable logic controller (PLC) runs the logic for a machine or process. Create_Tag.vi is the LabVIEW virtual instrument (VI) that uses these settings. It creates a library tag, a software object that holds the connection settings and a local copy of the requested data.

Unit `unit-2`: grade 7.43; 51 words, 4 sentences, 78 syllables; below the failure threshold.

> Supply the network address, the route to the controller, its family, and an existing tag name or data-file address. Then state how many values you need and their byte size where required. The saved values are examples; they do not describe every installation. This control alone sends no network requests.

Unit `unit-3`: grade 6.9; 51 words, 5 sentences, 80 syllables; below the failure threshold.

> All eight fields store strings, including the numbers. Four have dropdown suggestions: protocol, path, cpu, and debug level. These are string combo boxes, not LabVIEW numeric enums. Their menu entries are listed below. The C library decides whether a string is valid; an entry in the menu does not prove support.

Unit `unit-4`: grade 8.74; 41 words, 3 sentences, 66 syllables; below the failure threshold.

> This topic covers the current wrapper and the 2.7.2 source behavior discussed below. The bundled libraries identify themselves as 2.7.2; their exact build provenance is not established. Older 2.0.22 behavior is called out where it changes the advice.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## How the fields work together

### Review discussion

Section assessment: The delivery-address explanation connects the Ethernet endpoint, route, controller family and data name before discussing sizes.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. Each field gets one role before the next field is introduced. The concrete Logix and SLC names then distinguish data naming from network routing.

Most demanding passage (unit-5):

> Think of the settings as a delivery address. gatewayIP is the first Ethernet device LabVIEW reaches. Its Internet Protocol (IP) address identifies that endpoint. path gives further directions through that device, if needed. cpu tells the library which controller family is at the destination. tag name identifies the data within that controller.

Density assessment: Each field gets one role before the next field is introduced. The concrete Logix and SLC names then distinguish data naming from network routing.

### Assessed text

Unit `unit-5`: grade 9.57; 52 words, 6 sentences, 96 syllables; below the failure threshold.

> Think of the settings as a delivery address. gatewayIP is the first Ethernet device LabVIEW reaches. Its Internet Protocol (IP) address identifies that endpoint. path gives further directions through that device, if needed. cpu tells the library which controller family is at the destination. tag name identifies the data within that controller.

Unit `unit-6`: grade 7.25; 49 words, 4 sentences, 75 syllables; below the failure threshold.

> ControlLogix usually uses names such as TankLevel or Recipe[0]. SLC 500 uses typed data files, such as N7:0. Those are two ways to name controller data, not two ways to set a network address. A library tag does not create a new variable in the PLC.

Unit `unit-7`: grade 5.67; 54 words, 5 sentences, 78 syllables; below the failure threshold.

> element size and element count describe the requested data block. One element might be one integer or one floating-point value. A byte holds eight bits. A bit holds a single on/off state. Byte size affects how the returned buffer must be read; it does not convert one PLC data type into another.

### Exclusions from the score

None.

### Screening resolutions

- acronym_first_use: SLC may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'SLC 500 is the exact controller-family product name, identified as a PLC family that uses typed data-file addresses.'}
- acronym_first_use: N7 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'N7 is an exact SLC file address, explained by type, file number and element number in the naming section.'}

## Fields and saved values

### Review discussion

Section assessment: The table documents all eight controls, their exact C keys and saved defaults, with expected text formats, byte units and hardware examples.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The size row carries the most detail. It starts with byte size and simple N/F examples, then explains newer size discovery and the older allocation rule.

Most demanding passage (unit-14):

> element sizeelem_size | Empty | Byte size of one value, expressed as decimal text. Typical values are 2 for a 16-bit integer and 4 for a 32-bit integer or single-precision float. Thus, SLC N7:0 uses 2 bytes and F8:0 uses 4; Logix DINT and REAL both use 4 but need different getters.Use the true PLC type. The newer Logix code learns the size during its initial read, and the newer SLC code derives it from the file address. The older Logix code may need this field to allocate the buffer. Supplying the correct explicit size is useful for these simple scalar examples. It is not a way to force a type change.

Density assessment: The size row carries the most detail. It starts with byte size and simple N/F examples, then explains newer size discovery and the older allocation rule.

### Assessed text

Unit `unit-8`: grade 8.76; 36 words, 3 sentences, 60 syllables; below the failure threshold.

> Start here for each field's purpose and expected input. Follow the sections below for dropdown choices, route details and complete hardware examples. Enter the value only, without quotation marks or an attribute prefix such as gateway=.

### Exclusions from the score

- Unit `unit-9`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-10`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-11`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-12`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-13`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-14`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-15`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-16`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-17`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: DH may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'Data Highway Plus (DH+) is expanded; the screen drops the plus sign.'}
- acronym_first_use: EN2T may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': '1756-EN2T is an exact hardware catalog name, identified as an Ethernet module.'}
- acronym_first_use: LGX may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'LGX is an exact saved family alias, explained in both the field and choice tables.'}
- acronym_first_use: F8 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'F8 is an exact SLC float-file identifier, explained with the element example.'}
- acronym_first_use: DINT may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'DINT is retained as the exact Logix type label; its signed 32-bit width appears in the size table.'}
- acronym_first_use: REAL may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'REAL is the exact Logix type label; it is explained as a 32-bit single-precision float.'}
- acronym_first_use: B3 may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'B3 is an exact SLC binary-file address; the row explains word and bit selection.'}
- acronym_first_use: NONE may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'NONE is an exact case-sensitive wrapper sentinel, not an acronym requiring expansion.'}

## Protocol choices

### Review discussion

Section assessment: The protocol section explains both accepted AB spellings and the sole saved menu entry; the Modbus paragraph limits the scope of AB recipes.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The paragraph explains that Modbus changes the meanings of route and name before directing the reader to its separate rules.

Most demanding passage (unit-19):

> The C project also has a Modbus driver over Transmission Control Protocol (TCP). Its path means a unit identifier, and its names identify coils or registers. That is a different configuration: changing only protocol does not adapt these Allen-Bradley settings. See the protocol-specific rules in the libplctag attribute guide.

Density assessment: The paragraph explains that Modbus changes the meanings of route and name before directing the reader to its separate rules.

### Assessed text

Unit `unit-18`: grade 6.83; 37 words, 4 sentences, 59 syllables; below the failure threshold.

> The saved menu offers only ab-eip. The saved default ab_eip is an accepted alternate spelling. Both select the Allen-Bradley EtherNet/IP driver. Keep that driver for the SLC and Logix examples in this help.

Unit `unit-19`: grade 11.36; 51 words, 4 sentences, 95 syllables; below the failure threshold.

> The C project also has a Modbus driver over Transmission Control Protocol (TCP). Its path means a unit identifier, and its names identify coils or registers. That is a different configuration: changing only protocol does not adapt these Allen-Bradley settings. See the protocol-specific rules in the libplctag attribute guide.

### Exclusions from the score

None.

### Screening resolutions

No screening findings; semantic review still required.

## Controller family: saved dropdown choices

### Review discussion

Section assessment: Every saved CPU menu entry is explained, including the unsupported CGLX, FLEXLOGIX and FLGX strings, and how to supply the missing slc500 value.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The CGLX row makes the letter-order error visible and gives the full accepted spelling, so the user does not need to infer a correction.

Most demanding passage (unit-24):

> CGLX | Not recognized by the checked 2.7.2 lookup or current local C lookup. The accepted alias is clgx, with the letters in a different order. Prefer the clearer compactlogix.

Density assessment: The CGLX row makes the letter-order error visible and gives the full accepted spelling, so the user does not need to infer a correction.

### Assessed text

Unit `unit-20`: grade 9.38; 31 words, 3 sentences, 55 syllables; below the failure threshold.

> The field label cpu means central processing unit. Here, it selects the PLC family, not an exact catalog number. The C lookup accepts uppercase or lowercase letters for known family names.

Unit `unit-28`: grade 6.73; 52 words, 4 sentences, 76 syllables; below the failure threshold.

> A SLC 500 user must supply slc500, even though it is missing from the saved suggestions. Wire that string into the cluster field if the front-panel instance restricts typing. The wrapper passes it through; it does not translate menu labels. The menu can therefore be incomplete or out of date.

### Exclusions from the score

- Unit `unit-20`: Unterminated fragment; check selection manually.
- Unit `unit-21`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-22`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-23`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-24`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-25`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-26`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-27`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: CGLX may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'CGLX is the exact unsupported saved menu string and is compared with the accepted clgx alias.'}
- acronym_first_use: FLGX may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'FLGX is an exact unsupported menu string, with its lack of C lookup support explained.'}

## Other family values accepted by the C lookup

### Review discussion

Section assessment: The family table groups every accepted lookup spelling by its actual dispatch and states the limits for Micro800, generic devices and older mapped Logix access.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The PCCC row expands the term and explains that it needs data-table mapping before advising native Logix access for symbolic tags.

Most demanding passage (unit-36):

> logixpccc, lgxpccc, lgxplc5, logixplc5, lgx-pccc, logix-pccc, lgx-plc5, logix-plc5 | Logix through its older PLC-5-style data access. PCCC means Programmable Controller Communication Commands. This mode needs PLC/SLC data-table mapping in the Logix project. Use native controllogix for ordinary symbolic tags.

Density assessment: The PCCC row expands the term and explains that it needs data-table mapping before advising native Logix access for symbolic tags.

### Assessed text

Unit `unit-29`: grade 7.36; 38 words, 3 sentences, 58 syllables; below the failure threshold.

> The following are C string choices, not added menu entries. Use a value that matches the hardware at the end of the route. They identify different message formats; they are not interchangeable ways to reach the same data.

### Exclusions from the score

- Unit `unit-30`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-31`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-32`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-33`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-34`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-35`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-36`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-37`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-38`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: PCCC may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'Programmable Controller Communication Commands (PCCC) is expanded in the family row.'}
- acronym_first_use: NJ may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'NJ is an Omron product-family designation, not a term whose expansion should be invented.'}
- acronym_first_use: NX may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'NX is an Omron product-family designation, with the family identified.'}

## Understanding path

### Review discussion

Section assessment: The route section teaches endpoint, chassis backplane and processor slot; lists all 18 saved choices; then explains longer and DH+ routes.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The multi-hop route is traced in travel order from a stated gateway. The following sentence requires confirmation of the assumed port map.

Most demanding passage (unit-61):

> A longer route can cross more than one chassis or network. For example, 1,4,2,10.20.30.40,1,0 describes this assumed layout: cross the first backplane to an Ethernet bridge in slot 4; leave its port 2 for address 10.20.30.40; then cross that device's backplane to slot 0. This is a route example, not a universal port map. Confirm each module's port numbers and routing support.

Density assessment: The multi-hop route is traced in travel order from a stated gateway. The following sentence requires confirmation of the assumed port map.

### Assessed text

Unit `unit-39`: grade 8.44; 55 words, 4 sentences, 87 syllables; below the failure threshold.

> A ControlLogix system can have several plug-in modules in a chassis. Its backplane is the internal link between those modules. The Ethernet module may receive a message first, then pass it across the backplane to the processor that owns the tag. The gatewayIP reaches the Ethernet module; the path describes what to do next.

Unit `unit-40`: grade 7.23; 71 words, 5 sentences, 104 syllables; below the failure threshold.

> For the usual chassis route, enter comma-separated port and destination pairs. In 1,3, port 1 means the backplane and destination 3 means chassis slot 3. Slots are numbered from zero. If the Ethernet module is in slot 1 and the processor is in slot 3, use the Ethernet module's IP address and path=1,3. Do not use 1,1 merely because the Ethernet module is in slot 1.

Unit `unit-41`: grade 6.72; 41 words, 3 sentences, 59 syllables; below the failure threshold.

> The saved route menu contains every value below. These choices all use the same backplane-port rule. Pick the processor slot from the real hardware configuration; a number in the menu does not mean that the chassis has that many slots.

Unit `unit-61`: grade 7.12; 71 words, 4 sentences, 95 syllables; below the failure threshold.

> A longer route can cross more than one chassis or network. For example, 1,4,2,10.20.30.40,1,0 describes this assumed layout: cross the first backplane to an Ethernet bridge in slot 4; leave its port 2 for address 10.20.30.40; then cross that device's backplane to slot 0. This is a route example, not a universal port map. Confirm each module's port numbers and routing support.

Unit `unit-62`: grade 9.05; 56 words, 4 sentences, 91 syllables; below the failure threshold.

> For a direct SLC 5/05 Ethernet connection, leave path empty. The PLC is already the endpoint. The native SLC path is not the processor's physical rack slot; adding 1,0 is not needed. A plain non-DH+ route can be ignored by the SLC library, which does not mean it successfully routed through another chassis.

Unit `unit-63`: grade 8.68; 85 words, 6 sentences, 135 syllables; below the failure threshold.

> For an SLC 5/04 on Data Highway Plus (DH+), the first Ethernet device may be a ControlLogix bridge. The library has a special final route segment, A:source:destination or B:source:destination, for the bridge's DH+ channel. The preceding pairs reach the 1756-DHRIO module, which bridges the chassis to the DH+ network. The segment must be last. The C parser reads node numbers as decimal; convert a node address shown in octal before entering it. For instance, octal 10 is decimal 8.

Unit `unit-64`: grade 8.93; 43 words, 3 sentences, 69 syllables; below the failure threshold.

> A DH+ route needs the actual bridge slot, channel, source setting and target node. Confirm them with the controls engineer and the 1756-DHRIO manual, connection paths and routing sections. Do not substitute a normal ControlLogix slot route for the bridge-specific form.

Unit `unit-65`: grade 9.96; 67 words, 4 sentences, 108 syllables; below the failure threshold.

> To find a route, start with the electrical drawings and the live hardware tree in Studio 5000 or RSLinx/FactoryTalk Linx. Identify the Ethernet endpoint first, then each module or network hop to the processor. A software browse path may include a computer driver name; that name is not part of libplctag's numeric route. Rockwell's ControlFLASH manual illustrates the distinction between an Ethernet address, backplane and slot.

### Exclusions from the score

- Unit `unit-42`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-43`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-44`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-45`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-46`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-47`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-48`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-49`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-50`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-51`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-52`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-53`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-54`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-55`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-56`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-57`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-58`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-59`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-60`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- long_sentence: 44 words in a sentence; advisory inspection, not a word-count limit Resolution: {'status': 'RESOLVED', 'reason': 'The multi-hop example is one ordered journey; semicolons separate each hop, and the next sentence explicitly requires checking the assumed port map.'}
- acronym_first_use: DHRIO may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': '1756-DHRIO is the exact bridge-module catalog name; its chassis-to-DH+ role is explained.'}

## Tag names and data-file addresses

### Review discussion

Section assessment: The naming section distinguishes controller scope, program scope, arrays and members from SLC file/element/bit addressing, with typed examples.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. File number, element number and type are explained in a concrete N7:0 example before bit-address and byte-access examples.

Most demanding passage (unit-69):

> SLC example | Meaning | Typical local access

Density assessment: File number, element number and type are explained in a concrete N7:0 example before bit-address and byte-access examples.

### Assessed text

Unit `unit-66`: grade 9.31; 64 words, 5 sentences, 108 syllables; below the failure threshold.

> For ControlLogix, open the project in Studio 5000 Logix Designer. Controller Tags contains names visible at controller scope. Program Tags contains names local to a program. Use TankLevel for a controller-scoped tag, or Program:MainProgram.TankLevel for that tag in program MainProgram. An array index selects a starting element, such as Recipe[10]; a dot selects a structure member, such as Pump.Speed.

Unit `unit-67`: grade 7.15; 55 words, 5 sentences, 86 syllables; below the failure threshold.

> Check the tag's type and External Access setting. None prevents external access; read-only access cannot support a write. Reading a whole structure can also fail when a member is restricted. Rockwell explains these restrictions in Logix 5000 Controllers Data Access. The names shown here must be replaced with real tags from the target project.

Unit `unit-68`: grade 6.64; 76 words, 5 sentences, 105 syllables; below the failure threshold.

> For an SLC 500, open Data Files in RSLogix 500 and find the address and file type. In N7:0, N means integer data, 7 is the file number and 0 is the element number. In F8:0, F means floating-point data. A project can use other file numbers, so a float need not be in file 8. A friendly symbol assigned in the ladder editor is not the PCCC address to send.

Unit `unit-75`: grade 8.09; 47 words, 3 sentences, 70 syllables; below the failure threshold.

> See the data-file chapters of the SLC 500 Instruction Set Reference Manual for the address layout and other file types. Timers, counters, strings and whole structures have layouts beyond a single integer or float. Do not guess their byte sizes from the number of visible fields.

### Exclusions from the score

- Unit `unit-69`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-70`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-71`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-72`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-73`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-74`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## Element size, count and local byte offsets

### Review discussion

Section assessment: The size section maps signed integer and real types to byte widths and getters, then traces ten 2-byte SLC elements to offsets 0 through 18.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The version paragraph separates initial Logix discovery from parsed SLC sizes and the older empty-size failure. Earlier rows establish the simple types first.

Most demanding passage (unit-84):

> In the checked 2.7.2 C source, native Logix tags start without a data buffer. An initial read learns the type and size from the controller. SLC sizing comes from its parsed file address. In older 2.0.22 code, an empty size for an ordinary Logix tag can lead to an invalid zero-size buffer. Use explicit correct sizes for simple values when supporting that older library, and check creation status.

Density assessment: The version paragraph separates initial Logix discovery from parsed SLC sizes and the older empty-size failure. Earlier rows establish the simple types first.

### Assessed text

Unit `unit-76`: grade 8.06; 53 words, 4 sentences, 83 syllables; below the failure threshold.

> The field values describe the data you request from the PLC. The typed LabVIEW getter then interprets bytes already held in the library's local buffer. Choose the getter to match the PLC type. Setting size 4 does not make an integer a float: both occupy four bytes but encode values in different ways.

Unit `unit-83`: grade 8.16; 63 words, 4 sentences, 94 syllables; below the failure threshold.

> For ten SLC integers starting at N7:0, enter size 2 and count 10. After a successful tag read, the buffer contains 20 bytes. The first integer starts at byte offset 0, the second at 2 and the tenth at 18. The getter offset is relative to that buffer; it is not the SLC file number or the array's original PLC index.

Unit `unit-84`: grade 7.9; 71 words, 5 sentences, 108 syllables; below the failure threshold.

> In the checked 2.7.2 C source, native Logix tags start without a data buffer. An initial read learns the type and size from the controller. SLC sizing comes from its parsed file address. In older 2.0.22 code, an empty size for an ordinary Logix tag can lead to an invalid zero-size buffer. Use explicit correct sizes for simple values when supporting that older library, and check creation status.

Unit `unit-85`: grade 8.2; 40 words, 3 sentences, 63 syllables; below the failure threshold.

> For current data, complete Read_Tag.vi before using a typed getter. Check Tag_Size.vi before indexing the buffer. A successful getter or setter concerns local data; a setter alone does not prove that a controller write has completed.

### Exclusions from the score

- Unit `unit-77`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-78`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-79`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-80`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-81`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-82`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: SINT may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'SINT is the Logix type label, explicitly defined as signed 8-bit integer in its row.'}
- acronym_first_use: INT may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'INT is defined as signed 16-bit integer in its row.'}
- acronym_first_use: LINT may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'LINT is defined as signed 64-bit integer in its row.'}

## Debug dropdown: every level

### Review discussion

Section assessment: All six saved debug choices and the separate numeric zero case are explained with logging scope, exact NONE matching and version-specific reset behavior.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The zero row separates a named no-debug constant from the create function condition and gives the explicit reset function.

Most demanding passage (unit-94):

> 0 — not a saved menu entry | The C constant for no debug output. However, the checked 2.7.2 create path changes the shared level only for a value greater than zero. Passing 0 here does not reset a level already enabled. Use the library function plc_tag_set_debug_level(0) when an explicit reset is needed; this control does not call that function.

Density assessment: The zero row separates a named no-debug constant from the create function condition and gives the explicit reset function.

### Assessed text

Unit `unit-86`: grade 7.98; 38 words, 3 sentences, 60 syllables; below the failure threshold.

> The saved menu offers NONE and numeric strings 1 through 5. Enter numeric text for a level; the wrapper does not translate words such as INFO into a number. The names in the table describe the C constants.

Unit `unit-95`: grade 6.74; 51 words, 4 sentences, 75 syllables; below the failure threshold.

> The older 2.0.22 create path resets the shared level to zero when debug is omitted. That differs from 2.7.2. Keep this version difference in mind when a second tag changes logging. Use clean numeric text; do not rely on the parser accepting a numeric prefix in a malformed value.

### Exclusions from the score

- Unit `unit-87`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-88`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-89`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-90`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-91`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-92`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-93`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-94`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: INFO may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'INFO is a debug constant label whose informational role is stated.'}
- acronym_first_use: ERROR may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'ERROR is a debug constant label, explained in that table row.'}
- acronym_first_use: WARN may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'WARN is a debug constant label, explained as warnings plus errors.'}
- acronym_first_use: DETAIL may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'DETAIL is the retained debug level name and its diagnostic use is explained.'}
- acronym_first_use: SPEW may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'SPEW is the retained most-verbose debug level name and its output implications are stated.'}

## Complete hardware examples

### Review discussion

Section assessment: Four full cluster recipes cover SLC integer/float and ControlLogix DINT/REAL data, with real hardware assumptions, correct getters and a CompactLogix qualification.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The SimpleReadWrite paragraph connects fixed float calls to the recipes and explicitly explains why an integer configuration cannot change those calls.

Most demanding passage (unit-110):

> SimpleReadWrite.vi passes this cluster to Create_Tag.vi, then uses float getters and a float setter. Its data must therefore be a suitable 32-bit floating-point item, such as the SLC F8:0 or Logix REAL examples. Supplying the integer example does not cause that VI to switch to an integer getter. It also requests a write, so use the example only when that write is intended.

Density assessment: The SimpleReadWrite paragraph connects fixed float calls to the recipes and explicitly explains why an integer configuration cannot change those calls.

### Assessed text

Unit `unit-96`: grade 7.42; 45 words, 4 sentences, 71 syllables; below the failure threshold.

> These are configuration examples, not discovered devices or completed hardware tests. All example names and addresses must be replaced or confirmed. An empty path below means an empty string, not the word empty. Use the existing file or tag and a count that fits it.

Unit `unit-108`: grade 11.16; 63 words, 4 sentences, 110 syllables; below the failure threshold.

> The SLC 5/04 has DH+ rather than the SLC 5/05's Ethernet interface. It needs a supported bridge for this network access. Other SLC models can need other gateways; a serial cable or an Ethernet-to-serial converter alone does not prove compatibility. Check the controller's channels in the SLC 500 Modular Hardware Style User Manual and the gateway's own manual.

Unit `unit-109`: grade 11.68; 50 words, 3 sentences, 88 syllables; below the failure threshold.

> For CompactLogix, a common native configuration uses cpu=compactlogix, an existing symbolic tag and, on models with the usual virtual backplane route, path=1,0. Verify the model and Ethernet port before copying it. An embedded Ethernet port and a separate chassis Ethernet module need not use the same route.

Unit `unit-110`: grade 9.61; 70 words, 4 sentences, 109 syllables; below the failure threshold.

> SimpleReadWrite.vi passes this cluster to Create_Tag.vi, then uses float getters and a float setter. Its data must therefore be a suitable 32-bit floating-point item, such as the SLC F8:0 or Logix REAL examples. Supplying the integer example does not cause that VI to switch to an integer getter. It also requests a write, so use the example only when that write is intended.

### Exclusions from the score

- Unit `unit-97`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-98`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-99`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-100`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-101`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-102`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-103`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-104`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-105`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-106`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-107`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## What Create_Tag.vi sends to C

### Review discussion

Section assessment: The construction section preserves the exact seven attributes, optional debug suffix, empty SLC path and unescaped ampersand behavior, with source navigation.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The concrete SLC string precedes the empty-path and delimiter explanation, giving the reader a visible value to compare.

Most demanding passage (unit-115):

> The empty path= is intentional for that direct SLC example. The VI passes this string and a separate timeout to plc_tag_create. It does not escape special characters: & starts another attribute, so do not put it inside a field value. Do not append extra attributes as an improvised workaround; use a wrapper that explicitly supports them.

Density assessment: The concrete SLC string precedes the empty-path and delimiter explanation, giving the reader a visible value to compare.

### Assessed text

Unit `unit-111`: grade 7.32; 47 words, 4 sentences, 73 syllables; below the failure threshold.

> The VI trims leading and trailing whitespace from all eight fields. It builds the following string, keeping the field values as text. It always includes the seven main attributes, even if a value is empty. It adds &debug=value unless the trimmed debug text is exactly NONE.

Unit `unit-115`: grade 9.43; 57 words, 4 sentences, 94 syllables; below the failure threshold.

> The empty path= is intentional for that direct SLC example. The VI passes this string and a separate timeout to plc_tag_create. It does not escape special characters: & starts another attribute, so do not put it inside a field value. Do not append extra attributes as an improvised workaround; use a wrapper that explicitly supports them.

Unit `unit-116`: grade 9.3; 62 words, 4 sentences, 99 syllables; below the failure threshold.

> The C implementation is maintained in the libplctag Git project. The controller-family lookup and sizing rules are in src/libplctag/protocols/ab/ab_common.c; route encoding is in src/libplctag/protocols/ab/cip.c. These paths are relative to that C repository, not this help folder. The complete attribute guide covers options that this eight-field wrapper does not expose.

### Exclusions from the score

- Unit `unit-112`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-113`: Unterminated fragment; check selection manually.
- Unit `unit-114`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

No screening findings; semantic review still required.

## First connection and troubleshooting

### Review discussion

Section assessment: The procedure moves from verified hardware settings through create/read/getter/cleanup, and the symptom table ties failures to specific fields.

Reading-level review: **PASS** — All measured prose and steps are below grade 12. Short samples make individual scores unstable. All table rows and code were read for meaning although they are excluded from the numerical measure. The pending-create step explains both error channels and handle readiness before the subsequent read and getter step.

Most demanding passage (unit-120):

> Check both the LabVIEW error cluster and the raw error code. With timeout zero, creation can continue after the call returns; check Tag_Status.vi until it is ready or reports an error. Keep only a valid, successfully created handle.

Density assessment: The pending-create step explains both error channels and handle readiness before the subsequent read and getter step.

### Assessed text

Unit `unit-117`: grade 8.04; 37 words, 3 sentences, 59 syllables; below the failure threshold.

> Confirm the controller model, Ethernet endpoint, route, data name and type with the PLC project. Check that the computer can reach that endpoint. A ping reply alone does not prove that the PLC supports the required messages.

Unit `unit-118`: grade 5.32; 31 words, 4 sentences, 47 syllables; below the failure threshold.

> Fill this cluster using the matching hardware example. Start with one known scalar and count 1. For SLC, choose the actual data-file address. For Logix, check scope and External Access.

Unit `unit-119`: grade 8.6; 38 words, 3 sentences, 62 syllables; below the failure threshold.

> Call Create_Tag.vi with a clear incoming error and a suitable timeout, such as 1000 milliseconds. The timeout is a separate input. A positive wait can delay LabVIEW's user interface because this library node uses that thread.

Unit `unit-120`: grade 7.9; 40 words, 3 sentences, 62 syllables; below the failure threshold.

> Check both the LabVIEW error cluster and the raw error code. With timeout zero, creation can continue after the call returns; check Tag_Status.vi until it is ready or reports an error. Keep only a valid, successfully created handle.

Unit `unit-121`: grade 6.44; 37 words, 3 sentences, 54 syllables; below the failure threshold.

> Complete Read_Tag.vi, check its result, then use the getter that matches the PLC data type. Validate the returned buffer size and each byte offset. A plausible value alone does not prove that the read succeeded.

Unit `unit-122`: grade 8.45; 41 words, 3 sentences, 65 syllables; below the failure threshold.

> Release a created handle with Destroy_Tag.vi when finished. Preserve earlier errors while still arranging for cleanup to execute. Changing the cluster after creation does not retarget a handle that already exists; create a new tag with the new settings.

### Exclusions from the score

- Unit `unit-123`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-124`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-125`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-126`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-127`: Non-narrative element; reviewed separately for clarity.
- Unit `unit-128`: Non-narrative element; reviewed separately for clarity.

### Screening resolutions

- acronym_first_use: CPU may need its full term before this use Resolution: {'status': 'RESOLVED', 'reason': 'Central processing unit is expanded in the family section; cpu elsewhere is an exact field identifier.'}

## Revision evidence

Substantive rewrite batches used: 2; limit: 3.

### Rewrite `bf153a39466d6c7cb7a3` (batch 1)

Original snapshot: `6e66e9ef19b44aecee62bfe6c4d7955843241619bac55d3f318f4891e55a8091`; method: approachable-fk/2.0.

Original artifact: `8eab95f3f2fec336815e8a08eda2e4bfd836c9b80dfaa3a980f8f67e600dc397`. Grade 12.04; 37 words, 2 sentences, 64 syllables.

> The field label cpu refers to the PLC's central processing unit, but the value selects a family rather than an exact catalog number. The C lookup compares the following recognized family names without regard to letter case. The saved dropdown contains six entries:

Clarity problem: The passage combined the named component with several dependent roles in a long sentence.

Change: Give the component identity its own sentence, then explain its role and consequence.

Current unit `unit-20`: grade 9.38; 31 words, 3 sentences, 55 syllables.

> The field label cpu means central processing unit. Here, it selects the PLC family, not an exact catalog number. The C lookup accepts uppercase or lowercase letters for known family names. The saved dropdown has six entries:

Preserved facts and relationships:

- cpu selects a controller family rather than a catalog number; matching is case-insensitive and the menu has six entries.

Source references:

- inspection-0.json
- inspection-1.json
- evidence.json

Technical integrity: **PASS** — Compared the rewritten sentences with the archived passage and the control/VI reads; all identities, roles and conditions are preserved.

### Rewrite `ca4b10de973b8f7f4f40` (batch 2)

Original snapshot: `319dd6f624b1e649c1efb1a55dffffe79a28efcd503dad3af06bbc9e9b11b353`; method: approachable-fk/2.0.

Original artifact: `a9253012d53fa4aa575dd73b2f95bf9162070c80bde4976088a53c12a061f1b8`. Grade 12.07; 60 words, 3 sentences, 101 syllables.

> PLC_Attributes.ctl describes which controller to reach and which value to access inside it. A programmable logic controller (PLC) runs the logic for a machine or process. The LabVIEW virtual instrument (VI) Create_Tag.vi uses this cluster to create a library tag: a software object that holds the connection settings and a local copy of the requested data.

Clarity problem: The passage combined the named component with several dependent roles in a long sentence.

Change: Give the component identity its own sentence, then explain its role and consequence.

Current unit `unit-1`: grade 10.25; 62 words, 4 sentences, 104 syllables.

> PLC_Attributes.ctl describes which controller to reach and which value to access inside it. A programmable logic controller (PLC) runs the logic for a machine or process. Create_Tag.vi is the LabVIEW virtual instrument (VI) that uses these settings. It creates a library tag, a software object that holds the connection settings and a local copy of the requested data.

Preserved facts and relationships:

- PLC_Attributes selects the controller and data; a PLC runs machine logic; Create_Tag.vi consumes the cluster and creates a library tag with settings and a local data copy.

Source references:

- inspection-0.json
- inspection-1.json
- evidence.json

Technical integrity: **PASS** — Compared the rewritten sentences with the archived passage and the control/VI reads; all identities, roles and conditions are preserved.


## Whole-document review

Whole document review: **PASS** — Read the full page as a new PLC user. The progression from purpose to field roles, route/data addressing, hardware recipes and checked operations supports the stated audience. All eight fields and saved suggestions are covered; unsupported menu strings and version exceptions remain explicit.

Reader simulation: **PASS** — A newcomer can use an existing SLC N7 or F8 address or a Logix symbolic tag, select the endpoint and route, set count/type, then follow create/read/getter/cleanup without treating the recipes as discovered hardware.

This companion report is separate from the product and is not recursively reviewed.
