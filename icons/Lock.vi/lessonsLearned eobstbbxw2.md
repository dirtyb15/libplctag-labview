# LabVIEW Icon Creator — Lessons Learned

Run: c5d3b0a990d44c6d9b6c960093b8c228
Skill version: 1.3.0

## Incident Evidence

- `VIS-DISTINCT-012`; candidate candidate-01; option 1; attempt 1; stage small_size; size/value 30x18: Closed lock still resembles the open-padlock unlock candidate in overall silhouette.
  Correction: Design a structurally different silhouette for this operation.. Outcome: PASS after review of candidate-01.
- `VIS-DISTINCT-012`; candidate candidate-02; option 2; attempt 1; stage small_size; size/value 30x18: Tag plus orange lock repeats the unlock tag-plus-lock layout.
  Correction: Design a structurally different silhouette for this operation.. Outcome: PASS after review of candidate-08.
- `VIS-SEM-001`; candidate candidate-03; option 3; attempt 1; stage source_visual; size/value source: The generated blue piece resembles a key entering a red socket rather than a latch securing a tag.
  Correction: Use an unmistakable locking metaphor without key-in-socket imagery.. Outcome: PASS after review of candidate-07.
- `VIS-DISTINCT-012`; candidate candidate-03; option 3; attempt 1; stage small_size; size/value 30x18: The connection remains visible, but the lock action is ambiguous.
  Correction: Design a structurally different silhouette for this operation.. Outcome: PASS after review of candidate-07.
- `VIS-DISTINCT-012`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x18: Shield-and-lock structure closely matches the unlock shield option.
  Correction: Design a structurally different silhouette for this operation.. Outcome: PASS after review of candidate-04.
- `VIS-DISTINCT-012`; candidate candidate-05; option 5; attempt 1; stage small_size; size/value 30x18: Clamp-and-tag structure closely matches the unlock clamp option and risks confusion with the size caliper.
  Correction: Design a structurally different silhouette for this operation.. Outcome: PASS after review of candidate-10.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Every concept has an opposing lock/unlock counterpart with substantially the same silhouette: padlock, tag-and-padlock, latch, shield-and-padlock, or clamp-and-tag.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-02; option 2; attempt 1; stage small_size; size/value 30x18: Diagonal blue tag with lower-right badge repeats the composition of Destroy Tag candidate 01; differing badge marks are insufficient.
  Correction: Use a different lock silhouette without a diagonal tag with lower-right badge.. Outcome: PASS after review of candidate-08.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The former unlock padlock, shield and clamp analogues were superseded by open ring, broken chain, open palm, turned key and raised barrier. The lock tag-and-badge resembles Destroy Tag candidate 01, and candidate 03 reads as key in socket. Replace both before reassessing.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-06; option 2; attempt 1; stage small_size; size/value 30x18: Upright tag crossed by a horizontal bar repeats the dominant construction of Destroy Tag shredder candidate 08.
  Correction: Choose a different lock silhouette without a horizontal bar across an upright tag.. Outcome: PASS after review of candidate-08.
- `VIS-DISTINCT-012`; candidate candidate-05; option 5; attempt 1; stage small_size; size/value 30x18: The blue C-shaped clamp to the left of an orange value or tag resembles Read I8 candidate 03 horseshoe magnet layout.
  Correction: Use a different silhouette than the C shape with orange object on the right.. Outcome: PASS after review of candidate-10.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The bolt across an upright tag resembles Destroy Tag shredder candidate 08, and the blue C clamp plus orange tag resembles Read I8 magnet candidate 03. The cage is distinct. Replace the close pairs.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-09; option 5; attempt 1; stage small_size; size/value 30x18: The large orange tag on a blue rectangle with white stripe resembles Tag Status candidate 06, and zipper teeth merge into a stripe.
  Correction: Use a substantially different securing silhouette without a blue rectangular background and centered orange tag.. Outcome: PASS after review of candidate-10.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The safe wheel, cage, padlock and shield differ; the blue rectangular pouch with orange tag and white stripe repeats Tag Status candidate 06 at 30x18. Replace the pouch.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `VIS-DISTINCT-012` (13 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.
- `VIS-SEM-001` (1 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
