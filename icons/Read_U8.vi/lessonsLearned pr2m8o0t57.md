# LabVIEW Icon Creator — Lessons Learned

Run: f45173932cdd4e2ca118c2b5f50b2777
Skill version: 1.3.0

## Incident Evidence

- `SMALL-TEXT-007`; candidate candidate-03; option 3; attempt 1; stage small_size; size/value 30x18: At 30x18 the U8 strokes run together and the two 8 counters are too small for reliable reading.
  Correction: Separate U and 8, enlarge both counters and simplify the lens.. Outcome: PASS after review of candidate-06.
- `VIS-DISTINCT-012`; candidate candidate-04; option 4; attempt 1; stage source_visual; size/value source: The U8 card above a tray and upward arrow repeats the same structure as candidate-02; changing the card color does not distinguish it.
  Correction: Use a structurally different extraction metaphor.. Outcome: PASS after review of candidate-08.
- `SMALL-TEXT-007`; candidate candidate-04; option 4; attempt 1; stage small_size; size/value 30x18: The italic angled U8 has small counters and is difficult to distinguish reliably.
  Correction: Use upright large characters with clear space and counters in a different composition.. Outcome: PASS after review of candidate-08.
- `SMALL-TEXT-007`; candidate candidate-05; option 5; attempt 1; stage small_size; size/value 30x18: The small 8 counters and tight U8 spacing make the exact type difficult to read reliably.
  Correction: Enlarge U8, increase letter spacing and open the 8 counters.. Outcome: PASS after review of candidate-07.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Candidates 02 and 04 both show a tray under an upward arrow with U8 above; candidates 03, 04 and 05 also lose reliable U8 legibility at 30x18. Revisions and a new comparison are required.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The previously failed card still repeats candidate 02's tray and upward arrow. The revised lens and outlet resolve U8 readability; a structurally different fifth concept remains necessary.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.

## Generalized Lessons

- `SMALL-TEXT-007` (3 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-DISTINCT-012` (3 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
