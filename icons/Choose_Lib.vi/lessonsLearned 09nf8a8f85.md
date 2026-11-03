# LabVIEW Icon Creator — Lessons Learned

Run: 3dd2ce99abfd47c984bf3c32d3e3218b
Skill version: 1.3.0

## Incident Evidence

- `SMALL-RECOG-001`; candidate candidate-01; option 1; attempt 1; stage small_size; size/value 30x18: The chosen branch differs only by color; there is no independent selection cue.
  Correction: Use a large distinct selection mark on one branch.. Outcome: PASS after review of candidate-06.
- `VIS-SEM-001`; candidate candidate-03; option 3; attempt 1; stage source_visual; size/value source: An orange gear above a blue folder suggests folder settings, not selection of an OS-specific library file.
  Correction: Show a clear platform-dependent library file selection.. Outcome: PASS after review of candidate-09.
- `VIS-SEM-001`; candidate candidate-05; option 5; attempt 1; stage source_visual; size/value source: A magnifier over a computer suggests inspecting a computer, not selecting a platform-specific library file.
  Correction: Show a clear platform-dependent library file selection.. Outcome: PASS after review of candidate-08.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidates 02 and 04 use an input, horizontal arrow, and file; their small previews share the same overall composition.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate candidate-07; option 3; attempt 1; stage small_size; size/value 30x18: The dominant orange upright form emerging from a navy container resembles Create Tag candidate 15.
  Correction: Use a selection concept without an upright orange object over a blue receptacle.. Outcome: PASS after review of candidate-09.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidate 07 has the same orange shape emerging from navy receptacle as Create Tag candidate 15 at 30x18; replace it. Compare the remaining concepts again afterward.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `SMALL-RECOG-001` (1 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-SEM-001` (2 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-DISTINCT-012` (3 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
