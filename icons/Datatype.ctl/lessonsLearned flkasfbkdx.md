# LabVIEW Icon Creator — Lessons Learned

Run: 628be6bce06a415c99eeb76a5c3c50b4
Skill version: 1.3.0

## Incident Evidence

- `SMALL-ACTION-006`; candidate candidate-03; option 3; attempt 1; stage small_size; size/value 30x18: At 30x18 the pointer merges into the ring, leaving a barred I in a circle that resembles an information symbol.
  Correction: Use a much larger separated dial pointer and visible tick positions to convey an adjustable selector.. Outcome: PASS after review of candidate-06.
- `VIS-CONCEPT-002`; candidate candidate-04; option 4; attempt 1; stage source_visual; size/value source: The intended datatype tile is invisible; a barred I sits alone between two outward arrows and suggests distribution rather than a selector.
  Correction: Enclose the I in a solid high-contrast tile and make large side arrows read as navigation controls.. Outcome: PASS after review of candidate-08.
- `SMALL-ACTION-006`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x18: The unframed I and outward arrows do not clearly represent selection or cycling.
  Correction: Add a clear colored tile behind the I and separated navigation arrow buttons.. Outcome: PASS after review of candidate-08.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The list, dropdown, dial, flanking arrows and cursor have distinct layouts, but the dial can be mistaken for an information symbol and the arrows lost their tile. Replace the failed images and compare the final selected five again.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `SMALL-ACTION-006` (2 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-CONCEPT-002` (1 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-DISTINCT-012` (1 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
