# LabVIEW Icon Creator — Lessons Learned

Run: 82fb5600786a4e1b89f0dfeecaadb934
Skill version: 1.3.0

## Incident Evidence

- `SMALL-TEXT-007`; candidate candidate-01; option 1; attempt 1; stage small_size; size/value 30x18: The I is a plain stroke resembling 1.
  Correction: Make the type label much larger, with a barred capital I and separated characters.. Outcome: PASS after review of candidate-13.
- `VIS-TEXT-010`; candidate candidate-01; option 1; attempt 1; stage source_visual; size/value source: The I is a plain stroke resembling 1.
  Correction: Use a barred capital I.. Outcome: PASS after review of candidate-13.
- `SMALL-TEXT-007`; candidate candidate-02; option 2; attempt 1; stage small_size; size/value 30x18: I16 merges into dark strokes at 30x18.
  Correction: Make the type label much larger, with a barred capital I and separated characters.. Outcome: PASS after review of candidate-07.
- `SMALL-TEXT-007`; candidate candidate-03; option 3; attempt 1; stage small_size; size/value 30x18: The type label becomes too small at 30x18.
  Correction: Make the type label much larger, with a barred capital I and separated characters.. Outcome: PASS after review of candidate-14.
- `SMALL-TEXT-007`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x18: The I is a plain stroke resembling 1.
  Correction: Make the type label much larger, with a barred capital I and separated characters.. Outcome: PASS after review of candidate-15.
- `VIS-TEXT-010`; candidate candidate-04; option 4; attempt 1; stage source_visual; size/value source: The I is a plain stroke resembling 1.
  Correction: Use a barred capital I.. Outcome: PASS after review of candidate-15.
- `SMALL-TEXT-007`; candidate candidate-05; option 5; attempt 1; stage small_size; size/value 30x18: The type label becomes an unreadable blob at 30x18.
  Correction: Make the type label much larger, with a barred capital I and separated characters.. Outcome: PASS after review of candidate-17.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidates 01 and 04 both show a buffer, horizontal arrow and I16 text; they differ mainly by orientation.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-TEXT-007`; candidate candidate-06; option 1; attempt 2; stage small_size; size/value 30x18: The I and 1 merge at the baseline, making the type ambiguous.
  Correction: Increase whitespace between characters and allocate more pixels to the datatype.. Outcome: PASS after review of candidate-13.
- `SMALL-TEXT-007`; candidate candidate-08; option 3; attempt 2; stage small_size; size/value 30x18: I16 letters merge within the tray and no longer read reliably.
  Correction: Increase whitespace between characters and allocate more pixels to the datatype.. Outcome: PASS after review of candidate-14.
- `SMALL-TEXT-007`; candidate candidate-09; option 4; attempt 2; stage small_size; size/value 30x18: I and 1 merge along their bottom bars, and the extraction arrow is small.
  Correction: Increase whitespace between characters and allocate more pixels to the datatype.. Outcome: PASS after review of candidate-15.
- `VIS-SEM-001`; candidate candidate-10; option 5; attempt 2; stage source_visual; size/value source: I16 appears inside an orange magnifier with no visible buffer. The result suggests searching for a type rather than extracting a value from a buffer.
  Correction: Show an explicit read or extraction action from a buffer.. Outcome: PASS after review of candidate-17.
- `SMALL-TEXT-007`; candidate candidate-10; option 5; attempt 2; stage small_size; size/value 30x18: The I and 1 merge into a dark cluster, obscuring the datatype.
  Correction: Increase whitespace between characters and allocate more pixels to the datatype.. Outcome: PASS after review of candidate-17.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidates 08 and 09 both use a blue lower buffer and an orange upward arrow with I16; their structures are too similar.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-MARGIN-005`; candidate candidate-11; option 1; attempt 3; stage source_visual; size/value source: Cylinder and digit 6 sit about five percent from the canvas sides, leaving cramped margins.
  Correction: Use a different compact composition with larger white margins.. Outcome: PASS after review of candidate-13.
- `SMALL-ACTION-006`; candidate candidate-11; option 1; attempt 3; stage small_size; size/value 30x18: The arrow becomes a blue bar touching the I, losing an unambiguous extraction direction.
  Correction: Retire this concept and use a larger separated extraction cue.. Outcome: PASS after review of candidate-13.
- `VIS-MARGIN-005`; candidate candidate-12; option 3; attempt 3; stage source_visual; size/value source: The tray and arrow approach the canvas edges, leaving cramped margins.
  Correction: Use a smaller, simpler composition with clear margins.. Outcome: PASS after review of candidate-14.
- `SMALL-TEXT-007`; candidate candidate-12; option 3; attempt 3; stage small_size; size/value 30x18: The tiny I, 1 and 6 blur into dark fragments within the tray.
  Correction: Retire the tray layout and enlarge the exact type label.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The cylinder arrow loses its head and the tray type is unreadable at 30x18; the two vertical extraction concepts also resemble one another. Both three-attempt concepts need replacement.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The new leftward and diagonal extraction compositions differ from the eye, but the older vertical arrow and magnifying-glass candidates have unresolved failed reviews and require replacement or revision.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-16; option 5; attempt 1; stage source_visual; size/value source: I16 above a horizontal buffer and arrow repeats candidate-13: both place the type over a horizontal orange arrow and blue block, merely reversing direction and outlining the block.
  Correction: Use a substantially different silhouette instead of a horizontal arrow below the label.. Outcome: PASS after review of candidate-17.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidate-13 and candidate-16 both place I16 above a horizontal arrow and blue block, differing mainly in direction and fill. Replace one with a different composition.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `SMALL-TEXT-007` (10 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-TEXT-010` (2 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-DISTINCT-012` (6 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.
- `VIS-SEM-001` (1 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-MARGIN-005` (2 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `SMALL-ACTION-006` (1 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
