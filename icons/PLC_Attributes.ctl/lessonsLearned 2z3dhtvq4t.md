# LabVIEW Icon Creator — Lessons Learned

Run: 28c7edf07dd3405b81051f73a6bf0af4
Skill version: 1.3.0

## Incident Evidence

- `VIS-DETAIL-004`; candidate candidate-01; option 1; attempt 1; stage source_visual; size/value source: Rack includes unrequested small PLC lettering and many tiny panel marks.
  Correction: Use a plain unlabeled industrial automation rack with only three thick module slots and simple sliders.. Outcome: PASS after review of candidate-10.
- `SMALL-TEXT-007`; candidate candidate-01; option 1; attempt 1; stage small_size; size/value 30x18: PLC lettering collapses to indistinct pale pixels in the rack.
  Correction: Remove all lettering and fine panel details.. Outcome: PASS after review of candidate-10.
- `VIS-CONCEPT-002`; candidate candidate-02; option 2; attempt 1; stage source_visual; size/value source: The source depicts a game controller, not an industrial programmable logic controller.
  Correction: Depict a rectangular industrial PLC rack with vertical modules; no gamepad, handles or buttons.. Outcome: PASS after review of candidate-07.
- `VIS-DETAIL-004`; candidate candidate-03; option 3; attempt 1; stage source_visual; size/value source: The PLC rack contains unsolicited lettering and many miniature details.
  Correction: Use a simple unlabeled industrial PLC rack over three thick field bars.. Outcome: PASS after review of candidate-14.
- `SMALL-TEXT-007`; candidate candidate-03; option 3; attempt 1; stage small_size; size/value 30x18: The small PLC text and module details dissolve into ambiguous blocks.
  Correction: Remove the lettering and simplify the rack silhouette.. Outcome: PASS after review of candidate-14.
- `VIS-CONCEPT-002`; candidate candidate-04; option 4; attempt 1; stage source_visual; size/value source: The controller is a video-game gamepad, not an industrial PLC.
  Correction: Use an industrial rectangular PLC module with screw terminals and two simple configuration knobs.. Outcome: PASS after review of candidate-09.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Two candidates depict gamepads instead of PLCs, and two rack designs include unreadable incidental letters. Retain the gear module and review a corrected final set.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-CONCEPT-002`; candidate candidate-06; option 1; attempt 2; stage source_visual; size/value source: The rack is a plain rectangle with two hairline dividers and lacks recognizable industrial PLC features.
  Correction: Add a large terminal strip and distinct module form while keeping sliders.. Outcome: PASS after review of candidate-10.
- `SMALL-SHAPE-004`; candidate candidate-06; option 1; attempt 2; stage small_size; size/value 30x18: The rack looks like a generic dark block next to sliders, not identifiable PLC hardware.
  Correction: Use larger terminal blocks and strong module divisions.. Outcome: PASS after review of candidate-10.
- `VIS-CONCEPT-002`; candidate candidate-08; option 3; attempt 2; stage source_visual; size/value source: Three undetailed rectangles above bars do not identify industrial PLC equipment.
  Correction: Add large industrial terminal blocks and a mounting profile while retaining the three list bars.. Outcome: PASS after review of candidate-14.
- `SMALL-SHAPE-004`; candidate candidate-08; option 3; attempt 2; stage small_size; size/value 30x18: The rectangular blocks and bars are ambiguous generic list geometry.
  Correction: Show a bold terminal strip and an industrial mounting outline.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Rack-with-sliders and rack-with-list images are over-simplified generic blocks that no longer establish PLC context. Retain the industrial wrench, knobs and gear options, then compare replacements.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-SHAPE-004`; candidate candidate-11; option 3; attempt 3; stage small_size; size/value 30x18: The three orange list bars merge into one orange block, losing the list cue.
  Correction: Replace the list with fewer, larger separated configuration elements.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The rack-and-list candidate loses its separate rows at 30x18; replace it and compare the final selection.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-MARGIN-005`; candidate candidate-13; option 3; attempt 1; stage source_visual; size/value source: Orange brace tips extend to within approximately one percent of each side of the source canvas, leaving insufficient edge clearance.
  Correction: Keep the complete rack and both braces within the central 75 percent of the square canvas.. Outcome: PASS after review of candidate-14.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The cluster-braces image has insufficient source edge clearance; replace it before final comparison.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `VIS-DETAIL-004` (2 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `SMALL-TEXT-007` (2 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-CONCEPT-002` (4 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-DISTINCT-012` (4 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.
- `SMALL-SHAPE-004` (3 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-MARGIN-005` (1 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
