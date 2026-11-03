<!-- customer-text-review:e6ba651a06456acf9e1c:start -->
## Customer text review: Datatype.ctl.html

Product SHA-256: `46f82826d8eef3596364cbac71efbf9d3a58e70711515cf4dba0ba6cf4fc9327`

Review dispositions are recorded below. Current delivery acceptance is checked separately.

### Editorial finding: clarify-instance-default

Location: Control type and choices, final paragraph
Originating snapshot: `a684e20fb4d372e9e2e313e39a65c1ce997ee03b8b518180f704a3bf8f3f9c90`

Original passage:

> The recorded control default was not established. The selector VI's I8 default case is a case-structure rule; it does not establish the saved default of every instance of this control.

Reason: The first sentence reports an analysis gap; the reader needs the resulting distinction and action.
Disposition: rewrite
Effect on claims: The page still makes no claim about a specific saved default; it tells the caller not to infer it from the case default.
Status: resolved

Resulting customer text:

> The selector VI's I8 default case is a case-structure rule; it does not establish the saved default of an individual control instance. Wire or verify the intended selection.

Analysis context: The control reader returned no established default for the typedef.

Evidence: Help/.support/help-generation/snapshot-evidence/Datatype.ctl.json

Evidence: Help/.support/help-generation/stable-live/Read_By_Datatype.vi.307467c08b5e.json

<!-- customer-text-review:e6ba651a06456acf9e1c:end -->
