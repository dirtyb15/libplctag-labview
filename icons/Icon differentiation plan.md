# Icon differentiation plan

Scope: 32 VIs and 2 controls in the repository root. Each file receives its own folder and five independently reviewed options. All options must be compared across files at 30 × 18 pixels, not merely checked for different hashes or colors.

## Visual grammar

- Reserve distinct, large operation silhouettes: incoming arrow for Read, outgoing arrow for Set, tag with incoming arrow for Read_Tag, tag with outgoing arrow for Write_Tag, plus for Create_Tag, cross for Destroy_Tag, closed and open padlocks for Lock and Unlock, ruler for Tag_Size, status gauge for Tag_Status, warning and information symbol for Error_Info, selector for Choose_Lib, and opposing arrows for SimpleReadWrite.
- Make datatype an essential readable identifier. Use the actual short type name (I8, I16, I32, I64, U8, U16, U32, U64, FLT, DBL) in bold high-contrast lettering. Signedness and width must survive at the required PNG sizes; color alone is insufficient. If a label cannot be read, redesign the composition rather than accepting a near duplicate.
- Give Read_By_Datatype a type selector plus incoming arrow, Datatype.ctl a datatype selector silhouette, and PLC_Attributes.ctl a PLC configuration silhouette. Controls must also differ visibly from VIs.
- Plan five different arrangements or metaphors for each file; reserve their combinations globally so that another file cannot reuse the same structural signature. Review the complete set at native size and magnified size. Reject any pair whose function or type cannot be reliably distinguished.
- Check semantics against each VI before generation, including whether Set changes a local tag buffer rather than writing directly to the PLC. Preserve this distinction in the action cue.

## Production and acceptance

For each file, generate five independent square masters, prepare 29 × 29, 30 × 23 and 30 × 18 PNGs and multi-frame ICOs, inspect the masters and size previews, and record evidence and hashes in a manifest. Publish only after both within-set and cross-file comparison. Keep source artwork and the working run until acceptance; never modify the original VIs or controls as part of asset generation.

## Current state

Five preliminary Choose_Lib masters exist in the working run. They are not accepted: the key suggests unlocking, the plug suggests electrical connection and is clipped, and the cursor in the books concept points away from the books. The other designs also need small-size and cross-file review. No complete icon sets have been published.
