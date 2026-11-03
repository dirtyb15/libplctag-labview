# LabVIEW Icon Creator — Lessons Learned

Run: 83995451bb8f4f3b8c04e733ff46bf0e
Skill version: 1.3.0

## Incident Evidence

- `VIS-DISTINCT-012`; candidate candidate-01; option 1; attempt 1; stage small_size; size/value 30x18: X remains visible, but the overall tag-and-badge composition closely resembles the create-tag plus option.
  Correction: Use a different dominant silhouette and composition from create-tag and the other deletion options.. Outcome: PASS after review of candidate-01.
- `VIS-DISTINCT-012`; candidate candidate-03; option 3; attempt 1; stage small_size; size/value 30x18: Tag-and-badge composition closely resembles both create-tag plus and destroy-tag X.
  Correction: Use a different dominant silhouette and composition from create-tag and the other deletion options.. Outcome: PASS after review of candidate-10.
- `SMALL-RECOG-001`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x18: The shreds merge into a pale blue blur, so the shredder cue is ambiguous.
  Correction: Use fewer, thicker and widely separated strips and a recognizable shredder.. Outcome: PASS after review of candidate-08.
- `VIS-SEM-001`; candidate candidate-05; option 5; attempt 1; stage source_visual; size/value source: A red lightning bolt splits a blue tag; the result suggests a fault or broken connection rather than deleting a software tag.
  Correction: Use an unmistakable deletion or disposal metaphor without a lightning bolt.. Outcome: PASS after review of candidate-11.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidates 01 and 03 both use a navy tag with a red lower-right badge; candidates 02 and 04 both show a tag entering a red receptacle at small size.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The original create badge collision has been removed from that set, but the destroy minus badge repeats the destroy X layout, shredder strips merge, and the lightning tag suggests a fault. Replace those three and reassess all five.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-SEM-001`; candidate candidate-06; option 3; attempt 1; stage source_visual; size/value source: A crossed-out tag inside a prohibition sign commonly means tags are forbidden or unavailable rather than an action to destroy an existing tag.
  Correction: Use an explicit disposal action rather than a prohibition sign.. Outcome: PASS after review of candidate-10.
- `VIS-CONCEPT-002`; candidate candidate-07; option 4; attempt 2; stage source_visual; size/value source: The three blue shapes below the slot are horizontal bars, not vertical shreds, so the illustration does not clearly show shredding.
  Correction: Show three broad vertical strips hanging down from the slot, separated by clear gaps.. Outcome: PASS after review of candidate-08.
- `SMALL-RECOG-001`; candidate candidate-07; option 4; attempt 2; stage small_size; size/value 30x18: The horizontal lines merge and fail to convey shredding.
  Correction: Show fewer broad vertical strips with clear white space.. Outcome: PASS after review of candidate-08.
- `SMALL-RECOG-001`; candidate candidate-07; option 4; attempt 2; stage small_size; size/value 30x23: The horizontal bars look like a list under the slot rather than shredded fragments.
  Correction: Make three short vertical strips with large gaps.. Outcome: PASS after review of candidate-08.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The X and bin remain provisionally distinct, but the prohibition sign suggests restriction and the horizontal shredder output does not show shreds. The old lightning draft is also failed.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-RECOG-001`; candidate candidate-09; option 3; attempt 1; stage small_size; size/value 30x23: The white eraser tip and missing tag merge into the background, leaving a red shape that no longer clearly reads as an eraser.
  Correction: Give the eraser tip a thick dark outline and remove tiny fragments.. Outcome: PASS after review of candidate-10.
- `SMALL-RECOG-001`; candidate candidate-09; option 3; attempt 1; stage small_size; size/value 30x18: The red shape and blue tag do not clearly convey erasing because the white eraser tip disappears.
  Correction: Add a dark outline around a larger eraser and simplify its surroundings.. Outcome: PASS after review of candidate-10.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Tag with X, tag in bin, and vertical shredder are different silhouettes. The eraser loses its tip at required sizes and the lightning draft remains semantically failed.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `VIS-DISTINCT-012` (6 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.
- `SMALL-RECOG-001` (5 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-SEM-001` (2 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-CONCEPT-002` (1 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
