<!-- customer-text-review:d123b6155e36c8bea7f3:start -->
## Customer text review: Set_U8.vi Context Help.txt

Product SHA-256: `226988b761ec2b78e3ab6c412536978ef15d3f06ed4cfea9f5420d6d9183e109`

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

<!-- customer-text-review:d123b6155e36c8bea7f3:end -->
