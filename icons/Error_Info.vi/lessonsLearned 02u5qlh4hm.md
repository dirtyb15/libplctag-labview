# LabVIEW Icon Creator — Lessons Learned

Run: ed5066ff928943cd96a1f4671d7d8f86
Skill version: 1.3.0

## Incident Evidence

- `VIS-DISTINCT-012`; candidate candidate-03; option 3; attempt 1; stage source_visual; size/value source: The round outlined bubble with a diagonal tail resembles the magnifying-glass silhouette used by Read_U8.vi candidate-06.
  Correction: Replace the round ring-and-tail layout with a structurally different error-description concept.. Outcome: PASS after review of candidate-09.
- `VIS-DISTINCT-012`; candidate candidate-04; option 4; attempt 1; stage source_visual; size/value source: The left block, rightward arrow, and right text-bars layout repeats the buffer-to-U8 structure of Read_U8.vi candidate-01.
  Correction: Use a materially different arrangement or conversion metaphor.. Outcome: PASS after review of candidate-07.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The round bubble resembles the U8 magnifier, and the error-to-bars layout repeats the U8 buffer-to-value structure. Replace both and compare actual images again.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-06; option 3; attempt 1; stage source_visual; size/value source: A triangle above a blue circle containing a white i strongly resembles Datatype.ctl candidate-06, which has a triangle above a blue dial containing an I.
  Correction: Replace with a silhouette that does not use a triangle over a blue circular I/i.. Outcome: PASS after review of candidate-09.
- `VIS-DISTINCT-012`; candidate candidate-06; option 3; attempt 1; stage small_size; size/value 30x18: The triangle-over-blue-circle structure remains too similar to the datatype selector.
  Correction: Use a different dominant silhouette for the error description.. Outcome: PASS after review of candidate-09.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The separated triangle and information circle is too similar to the datatype selector's triangle over blue I dial. Keep the curved decode candidate and replace the circle option.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-MARGIN-005`; candidate candidate-08; option 3; attempt 1; stage source_visual; size/value source: The quotation marks approach the left and right canvas edges, leaving about three percent clearance and risking clipping.
  Correction: Keep the same quoted exclamation but scale the entire group down and leave at least ten percent white space on every side.. Outcome: PASS after review of candidate-09.

## Generalized Lessons

- `VIS-DISTINCT-012` (6 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.
- `VIS-MARGIN-005` (1 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
