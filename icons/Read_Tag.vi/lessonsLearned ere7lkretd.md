# LabVIEW Icon Creator — Lessons Learned

Run: da53d276d8b848fb896e53bc782cc243
Skill version: 1.3.0

## Incident Evidence

- `VIS-DISTINCT-012`; candidate candidate-01; option 1; attempt 1; stage small_size; size/value 30x18: The PLC-to-tag composition is a mirror of the write-tag PLC-and-tag concept.
  Correction: Choose a visibly different transfer composition from both read and write options.. Outcome: PASS after review of candidate-12.
- `VIS-DISTINCT-012`; candidate candidate-02; option 2; attempt 1; stage small_size; size/value 30x18: The downward arrow over tag closely matches candidate 05.
  Correction: Choose a visibly different transfer composition from both read and write options.. Outcome: PASS after review of candidate-14.
- `VIS-SEM-001`; candidate candidate-03; option 3; attempt 1; stage source_visual; size/value source: A transmitter and radio-wave arcs appear above an orange tag; this suggests a wireless transport not required by the VI.
  Correction: Use a transport-neutral cue for reading a PLC tag.. Outcome: PASS after review of candidate-15.
- `SMALL-RECOG-001`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x18: The outgoing arrow can be read as extracting a value or sending data, not specifically reading a PLC tag.
  Correction: Show a clearly identifiable source and destination for the read action.. Outcome: PASS after review of candidate-16.
- `SMALL-SHAPE-004`; candidate candidate-05; option 5; attempt 1; stage small_size; size/value 30x18: The tag and tray merge, obscuring the object being read.
  Correction: Separate and contrast the tag from the receiving tray.. Outcome: PASS after review of candidate-07.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidates 02 and 05 both use a downward blue arrow above orange tag/tray; candidate 01 mirrors the PLC-and-tag composition in Write_Tag.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-06; option 1; attempt 1; stage small_size; size/value 30x18: The curved transfer remains readily confusable with the opposed Write_Tag curved transfer at small size.
  Correction: Use a different action and arrangement than the write curved route.. Outcome: PASS after review of candidate-12.
- `VIS-DISTINCT-012`; candidate candidate-06; option 1; attempt 1; stage source_visual; size/value source: The generator made a curved controller-to-tag route. It closely mirrors Write_Tag candidate-07, which shows a curved tag-to-controller route; both have the same three dominant components.
  Correction: Use a different silhouette, not a mirrored curved controller and tag route.. Outcome: PASS after review of candidate-12.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The curved PLC-to-tag image mirrors the opposite write transfer, and three older candidates remain failed. Keep the contrasting tray candidate provisionally and replace the conflicts.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-08; option 2; attempt 1; stage source_visual; size/value source: A tag, vertical upward arrow, and PLC repeat the same three-element vertical transfer composition as Write_Tag candidate-02 with top and bottom objects swapped.
  Correction: Replace with a read concept whose dominant silhouette is not a vertical tag-arrow-PLC stack.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate candidate-08; option 2; attempt 1; stage small_size; size/value 30x18: The same blue PLC, orange upward arrow, and orange tag arrangement is readily confused with the write icon.
  Correction: Use a structurally different read metaphor.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate candidate-09; option 3; attempt 1; stage source_visual; size/value source: The large blue eye above a rectangular object repeats the dominant eye-over-content silhouette of Read_I16 candidate-07; the embedded tag may look like inspecting a controller display rather than fetching data.
  Correction: Replace the eye-over-object design with an explicit transfer and a different silhouette.. Outcome: PASS after review of candidate-15.
- `VIS-DISTINCT-012`; candidate candidate-09; option 3; attempt 1; stage small_size; size/value 30x18: The large eye over rectangular content remains similar to the signed-read eye motif and does not show a transfer.
  Correction: Use a distinct source-to-buffer action.. Outcome: PASS after review of candidate-15.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The vertical PLC/tag stack resembles Write_Tag candidate-02 and the eye-over-content motif resembles Read_I16. Both need different concepts.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-SEM-001`; candidate candidate-10; option 1; attempt 1; stage source_visual; size/value source: A hand holds a tag at the side of a controller, but there is no indication whether it is inserting or removing the tag.
  Correction: Add a large explicit arrow pointing away from the controller.. Outcome: PASS after review of candidate-12.
- `SMALL-ACTION-006`; candidate candidate-10; option 1; attempt 1; stage small_size; size/value 30x18: The tag and hand suggest either insertion or removal; read and write cannot be distinguished.
  Correction: Make the outward motion explicit with a large separated arrow.. Outcome: PASS after review of candidate-12.
- `VIS-SEM-001`; candidate candidate-11; option 2; attempt 1; stage source_visual; size/value source: The funnel is the dominant conventional filter symbol, suggesting filtering tag data rather than reading it.
  Correction: Use an explicit transfer or receiving symbol rather than a funnel.. Outcome: PASS after review of candidate-14.
- `SMALL-RECOG-001`; candidate candidate-11; option 2; attempt 1; stage small_size; size/value 30x18: The funnel strongly communicates filtering and the source of the tag is absent.
  Correction: Replace the filter metaphor with recognizable read transfer.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The hand has no unambiguous outward direction and the funnel suggests filtering; other candidates remain failed. Retain the receiving tray and redesign the rest.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-13; option 2; attempt 1; stage small_size; size/value 30x18: The diagonal tag-to-buffer arrangement resembles the U8 card-extraction icon at native size.
  Correction: Choose a different silhouette and layout.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate candidate-13; option 2; attempt 1; stage source_visual; size/value source: The orange tag in the upper right and blue diagonal arrow to a navy buffer at lower left repeats the same dominant arrangement as Read_U8 candidate-08, differing chiefly in arrow direction and label.
  Correction: Use a structure other than diagonal upper-right tag and lower-left buffer.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The arrowed hand has a clear extraction direction but the diagonal tag-to-buffer composition repeats an unsigned getter layout. Other older candidates remain failed.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Scanner and signal receiver have distinct arrangements from the hand and download tray; the old arrow-and-tag design remains failed and must be replaced before final review.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `VIS-DISTINCT-012` (16 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.
- `VIS-SEM-001` (3 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `SMALL-RECOG-001` (2 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `SMALL-SHAPE-004` (1 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `SMALL-ACTION-006` (1 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
