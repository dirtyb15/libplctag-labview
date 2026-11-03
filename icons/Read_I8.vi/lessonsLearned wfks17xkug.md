# LabVIEW Icon Creator — Lessons Learned

Run: dc288f1bd2ba4520b195f4b7f3e564ad
Skill version: 1.3.0

## Incident Evidence

- `SMALL-RECOG-001`; candidate candidate-02; option 2; attempt 1; stage small_size; size/value 30x18: The eight counter spaces merge and I8 is not reliably readable in the small drop.
  Correction: Retire the droplet concept or make the label much larger and higher contrast.. Outcome: PASS after review of candidate-09.
- `SMALL-RECOG-001`; candidate candidate-05; option 5; attempt 1; stage small_size; size/value 30x18: The angled I8 label is too small and softened to read reliably.
  Correction: Use an unrotated and larger I8 label.. Outcome: PASS after review of candidate-07.
- `VIS-SEM-001`; candidate candidate-05; option 5; attempt 1; stage source_visual; size/value source: The key inserted in a socket suggests unlocking rather than reading a typed buffer value and risks confusion with Unlock.vi.
  Correction: Use a different extraction metaphor that does not resemble a key or lock.. Outcome: PASS after review of candidate-07.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The crane, faucet, magnet, display and key have different silhouettes, but the faucet label becomes unreadable and the key suggests unlock. Replacements are required before acceptance.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-SEM-001`; candidate candidate-06; option 2; attempt 1; stage source_visual; size/value source: A plain orange I8 rectangle attached to a blue vertical line resembles a flag; the promised dispenser and extraction are absent.
  Correction: Use an explicit retrieval action and an unambiguous buffer object.. Outcome: PASS after review of candidate-09.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The ticket looks like a flag with no legible dispenser or read action. Microscope, crane, magnet and output display are distinct. Replace ticket and reassess.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-08; option 2; attempt 1; stage small_size; size/value 30x18: Blue hand at left, orange card in the middle, dark device at right duplicates Read Tag candidate 12 composition.
  Correction: Use an extraction layout without a hand and device in this arrangement.. Outcome: PASS after review of candidate-09.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The blue hand pulling an orange card from a dark device repeats the same layout as Read Tag candidate 12; replace it and compare the final set.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `SMALL-RECOG-001` (2 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-SEM-001` (2 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-DISTINCT-012` (4 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
