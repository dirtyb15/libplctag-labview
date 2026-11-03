<!-- customer-text-review:b38ae0c6c76f3222b55b:start -->
## Customer text review: Set_U8-help.md

Product SHA-256: `eecb47fccbbabc9944df9bd0fb9ff7c7c4ddc357e69ba7e201ed99767627a07a`

Review dispositions are recorded below. Current delivery acceptance is checked separately.

### Analysis issue: binary-provenance

Problem: The bundled binaries embed 2.0.22, but no reproducible-build provenance ties their bytes to the local source tag.
Affected claims: Legacy binary behavior and version applicability
Consequence: Legacy details are explicitly based on the matching source tag; exact build identity is not asserted.
Status: limitation

Evidence: evidence/v2.0.22/lib.c

Evidence: Bundled DLL and SO version strings; SHA-256 values in source-analysis notes

### Analysis issue: no-runtime-test

Problem: The wrapper and PLC write sequence were inspected statically; no VI, DLL, or PLC transaction was executed.
Affected claims: Runtime deployment and hardware operation
Consequence: Help describes source behavior; no runtime or hardware validation is claimed.
Status: limitation

### Analysis issue: compiled-block-fallback

Problem: pylv extraction left VICD compiled-code patches and VITS tags unparsed.
Affected claims: Scope of binary inspection
Consequence: No claims depend on compiled instruction decoding or VITS. Interface, defaults, DLL node and wiring are available in decoded structures.
Status: resolved

Recovery evidence: LVKit decoded Set_U8 and Choose_Lib dataflow; FPHb/BDHb/VCTP/DFDS decoding provided typed terminals, call symbol and default 14. The raw fallback concerns other blocks.

Evidence: evidence/Set_U8/Set_U8_BDHb.xml

Evidence: evidence/Set_U8/Set_U8.xml

### Analysis issue: repository-changed

Problem: Wrapper working-status fingerprint changed during the read-only analysis; source files were resaved from LabVIEW 19 to 26 by an unidentified external activity.
Affected claims: Current VI interface and dataflow; unchanged repository assertion
Consequence: Do not claim the wrapper workspace stayed unchanged. Current files were re-read and the help still matches their interface, default, DLL call and chooser behavior.
Status: resolved

Recovery evidence: Current Set_U8.vi and Choose_Lib.vi were inspected again with LVKit; current Set_U8 was extracted independently. No rollback was attempted. C repository fingerprints match.

Evidence: source-analysis-notes.md

Evidence: evidence/Set_U8-current/Set_U8_BDHb.xml

Evidence: evidence/Set_U8-current/Set_U8.xml


# Source analysis notes

No LabVIEW VI, DLL call, or PLC operation was run. Both source repositories were used for reads only.

Bundled library SHA-256 values:

- plctag32.dll: b791eeb4101376adeaeed0a75de9ba83a9550bd35b0681ae98ce48a27350a9c2
- plctag64.dll: a7513244583f5bfac381d142f09d36cda84705da8abe6b71b0d73c6345b9afbc
- libplctag64.so: 20502238297ddfa00b5a4e611cec4dc54a726551f1c6de757fe0d4b056e5dedd

Each binary contains 2.0.22. Build provenance was not available; the local v2.0.22 Git tag supplies matching-version source evidence. Modern 2.7.2 differences are scoped separately in the help.

## Repository safety check

The wrapper status fingerprint changed during this analysis (d354e74d... to 51153a78...). This is an unexpected-change safety failure, not evidence that the workspace stayed unchanged. HEAD, index, config, and refs stayed identical. The C repository fingerprint stayed identical.

The wrapper files have modification times of 2026-11-02 19:19:05 UTC. Set_U8.vi and Choose_Lib.vi now record LabVIEW 26.0.0 instead of 19.0.0. The analysis tools used read-only VI inspection and extraction; no source-editing or LabVIEW execution tool was called. The cause of the workspace update is not established.

Both current VIs were re-read. Their relevant interfaces, Set_U8 default value 14, DLL function, library filenames, and dataflow still match this help. Current Set_U8 evidence is in evidence/Set_U8-current. No files were reverted.

<!-- customer-text-review:b38ae0c6c76f3222b55b:end -->

<!-- customer-text-review:162b34f13204fc6121fb:start -->
## Customer text review: Set_U8.vi.html

Product SHA-256: `f41a1f23a72f8642ec78f27caf7b438c9ce43c7deba0334879effe94b33a1c9a`

Review dispositions are recorded below. Current delivery acceptance is checked separately.

### Analysis issue: binary-provenance

Problem: The bundled binaries embed 2.0.22, but no reproducible-build provenance ties their bytes to the local source tag.
Affected claims: Legacy binary behavior and version applicability
Consequence: Legacy details are explicitly based on the matching source tag; exact build identity is not asserted.
Status: limitation

Evidence: evidence/v2.0.22/lib.c

Evidence: Bundled DLL and SO version strings; SHA-256 values in source-analysis notes

### Analysis issue: no-runtime-test

Problem: The wrapper and PLC write sequence were inspected statically; no VI, DLL, or PLC transaction was executed.
Affected claims: Runtime deployment and hardware operation
Consequence: Help describes source behavior; no runtime or hardware validation is claimed.
Status: limitation

### Analysis issue: compiled-block-fallback

Problem: pylv extraction left VICD compiled-code patches and VITS tags unparsed.
Affected claims: Scope of binary inspection
Consequence: No claims depend on compiled instruction decoding or VITS. Interface, defaults, DLL node and wiring are available in decoded structures.
Status: resolved

Recovery evidence: LVKit decoded Set_U8 and Choose_Lib dataflow; FPHb/BDHb/VCTP/DFDS decoding provided typed terminals, call symbol and default 14. The raw fallback concerns other blocks.

Evidence: evidence/Set_U8/Set_U8_BDHb.xml

Evidence: evidence/Set_U8/Set_U8.xml

### Analysis issue: repository-changed

Problem: Wrapper working-status fingerprint changed during the read-only analysis; source files were resaved from LabVIEW 19 to 26 by an unidentified external activity.
Affected claims: Current VI interface and dataflow; unchanged repository assertion
Consequence: Do not claim the wrapper workspace stayed unchanged. Current files were re-read and the help still matches their interface, default, DLL call and chooser behavior.
Status: resolved

Recovery evidence: Current Set_U8.vi and Choose_Lib.vi were inspected again with LVKit; current Set_U8 was extracted independently. No rollback was attempted. C repository fingerprints match.

Evidence: source-analysis-notes.md

Evidence: evidence/Set_U8-current/Set_U8_BDHb.xml

Evidence: evidence/Set_U8-current/Set_U8.xml


# Source analysis notes

No LabVIEW VI, DLL call, or PLC operation was run. Both source repositories were used for reads only.

Bundled library SHA-256 values:

- plctag32.dll: b791eeb4101376adeaeed0a75de9ba83a9550bd35b0681ae98ce48a27350a9c2
- plctag64.dll: a7513244583f5bfac381d142f09d36cda84705da8abe6b71b0d73c6345b9afbc
- libplctag64.so: 20502238297ddfa00b5a4e611cec4dc54a726551f1c6de757fe0d4b056e5dedd

Each binary contains 2.0.22. Build provenance was not available; the local v2.0.22 Git tag supplies matching-version source evidence. Modern 2.7.2 differences are scoped separately in the help.

## Repository safety check

The wrapper status fingerprint changed during this analysis (d354e74d... to 51153a78...). This is an unexpected-change safety failure, not evidence that the workspace stayed unchanged. HEAD, index, config, and refs stayed identical. The C repository fingerprint stayed identical.

The wrapper files have modification times of 2026-11-02 19:19:05 UTC. Set_U8.vi and Choose_Lib.vi now record LabVIEW 26.0.0 instead of 19.0.0. The analysis tools used read-only VI inspection and extraction; no source-editing or LabVIEW execution tool was called. The cause of the workspace update is not established.

Both current VIs were re-read. Their relevant interfaces, Set_U8 default value 14, DLL function, library filenames, and dataflow still match this help. Current Set_U8 evidence is in evidence/Set_U8-current. No files were reverted.

## Help delivery revision

At the user's request, the detailed HTML omits its References and Context Help sections. The Context Help is a separate plain-text artifact. An inline documentation-citation sentence was removed from the detailed help while its operating rule was retained. Source citations and prior context wording remain in supporting evidence; no technical behavior was changed. Both products and their supporting files now reside under Help/Set_U8.vi Help.

<!-- customer-text-review:162b34f13204fc6121fb:end -->

<!-- customer-text-review:e29f9e0d17e706219e96:start -->
## Customer text review: Set_U8.vi.html

Product SHA-256: `426dbd37995d2773db767899c1943f3bf754cfa8e4db20545ce57f4ea583d389`

Review dispositions are recorded below. Current delivery acceptance is checked separately.

### Editorial finding: purpose-scope-1

Location: Purpose and scope, version paragraph
Originating snapshot: `518958805812324d29d6b2ab441db48da539961c939f51016548d078b1e5fbbb`

Original passage:

> This help covers the supplied LabVIEW virtual instrument (VI) and distinguishes two library versions.

Reason: Replace document-process narration with the actual version scope.
Disposition: remove
Effect on claims: The following sentences retain the bundled 2.0.22 version evidence and the separately pinned 2.7.2 comparison.
Status: resolved

Analysis context: Version selection remains fully qualified in the retained paragraph.

Evidence: Help/.support/help-generation/upstream-7712ed7/evidence.json

### Editorial finding: purpose-audience-2

Location: Purpose and scope, final paragraph
Originating snapshot: `518958805812324d29d6b2ab441db48da539961c939f51016548d078b1e5fbbb`

Original passage:

> The intended reader knows LabVIEW wires, subVIs, numeric controls, and error clusters. No knowledge of the C library internals is needed to use the VI.

Reason: Remove authoring audience narration that does not explain the VI or a caller action.
Disposition: remove
Effect on claims: No operating fact, limitation, or input rule is removed.
Status: resolved

Analysis context: The target audience remains recorded in the review profile.

<!-- customer-text-review:e29f9e0d17e706219e96:end -->
