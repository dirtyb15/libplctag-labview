# LabVIEW Icon Creator — Lessons Learned

Run: a229685eea644bfb83e3a602115e1991
Skill version: 1.3.0

## Incident Evidence

- `VIS-SEM-001`; candidate candidate-01; option 1; attempt 1; stage source_visual; size/value source: The orange tag appears attached to a controller side, with no cue distinguishing insertion from removal.
  Correction: Add an unambiguous inward action cue.. Outcome: PASS after review of candidate-06.
- `SMALL-ACTION-006`; candidate candidate-01; option 1; attempt 1; stage small_size; size/value 30x18: The side tag looks like a connected tab or plug and does not indicate a write direction.
  Correction: Add a large inward arrow.. Outcome: PASS after review of candidate-06.
- `SMALL-ACTION-006`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x23: The curved blue arrow blends into the controller and its arrowhead is not clearly separated.
  Correction: Use a high-contrast orange arrowhead with clear space at the controller.. Outcome: PASS after review of candidate-07.
- `SMALL-ACTION-006`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x18: The blue curve meets the blue controller without a discernible arrowhead.
  Correction: Make the arrow a contrasting color and enlarge its tip.. Outcome: PASS after review of candidate-07.
- `SMALL-RECOG-001`; candidate candidate-05; option 5; attempt 1; stage small_size; size/value 30x18: The orange tag hole disappears and the fingertip appears to press a button on the controller, not transfer tag data.
  Correction: Use a larger recognizable tag and preserve its hole or choose a clearer transfer action.. Outcome: PASS after review of candidate-13.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The vertical transfer and diagonal input differ, but the attached tag lacks direction, the curved arrow blends into the PLC, and the hand presses what looks like a button at 30x18. Revise these candidates before acceptance.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Left input, vertical upward transfer, diagonal incoming arrow and curved transfer differ in layout, but the fifth hand design still reads like a button press and needs correction. Compare the side-input design with PLC read after its rejected draft is replaced.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-SEM-001`; candidate candidate-08; option 5; attempt 2; stage source_visual; size/value source: The lower object has become a plain two-part slot, not a recognizable industrial controller; the hand is also very close to the top edge.
  Correction: Restore a large PLC face with display and two modules, reduce hand size, and center with wide margins.. Outcome: PASS after review of candidate-13.
- `SMALL-RECOG-001`; candidate candidate-08; option 5; attempt 2; stage small_size; size/value 30x18: The base reads as a tray rather than a PLC, so this resembles a generic tag insertion.
  Correction: Give the PLC a large white display and broad module divisions while keeping the tag readable.. Outcome: PASS after review of candidate-13.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The revised hand design no longer identifies the target as a controller. Correct it before completing the set.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-ACTION-006`; candidate candidate-10; option 5; attempt 1; stage small_size; size/value 30x23: The arrow blends with the blue PLC; the embedded tag is too small to identify.
  Correction: Use a contrasting orange arrow with larger tip and simplify the envelope.. Outcome: PASS after review of candidate-13.
- `SMALL-ACTION-006`; candidate candidate-10; option 5; attempt 1; stage small_size; size/value 30x18: The tag mark becomes a white blur and the blue arrowhead merges with the controller, obscuring dispatch.
  Correction: Simplify the envelope and use a larger high-contrast arrow tip.. Outcome: PASS after review of candidate-13.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The packet adds a different envelope silhouette, but the tag mark and diagonal arrowhead do not survive 30x18; revise before acceptance.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-ACTION-006`; candidate candidate-11; option 5; attempt 2; stage small_size; size/value 30x18: At native size the arrowhead is absorbed into the controller edge and the tag mark is not distinct.
  Correction: Provide more white space around an enlarged arrow and a simpler envelope marking.. Outcome: PASS after review of candidate-13.
- `SMALL-ACTION-006`; candidate candidate-11; option 5; attempt 2; stage small_size; size/value 30x23: The black arrowhead merges into the dark controller despite its white border.
  Correction: Separate the arrow tip physically from the controller and make its outline wider.. Outcome: PASS after review of candidate-13.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Packet and diagonal arrow cannot yet be evaluated as an accepted concept because its arrowhead merges into the PLC at required sizes.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-ACTION-006`; candidate candidate-12; option 5; attempt 3; stage small_size; size/value 30x18: The tiny arrow becomes dark pixels and the embedded tag mark is not identifiable.
  Correction: Use a larger action cue and avoid a small nested marking.. Outcome: PASS after review of candidate-13.
- `SMALL-ACTION-006`; candidate candidate-12; option 5; attempt 3; stage small_size; size/value 30x23: The small floating diagonal arrow compresses and its head is indistinct.
  Correction: Retire the packet layout and simplify the transfer metaphor.. Outcome: PASS after review of candidate-13.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Packet transfer exhausted three attempts without a reliable arrow and tag mark at 30x18. Retire the concept.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `VIS-SEM-001` (2 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `SMALL-ACTION-006` (9 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `SMALL-RECOG-001` (2 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-DISTINCT-012` (6 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
