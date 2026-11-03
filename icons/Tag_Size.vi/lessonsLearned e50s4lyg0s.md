# LabVIEW Icon Creator — Lessons Learned

Run: c042ab6ce415410ab3215588c69b6702
Skill version: 1.3.0

## Incident Evidence

- `VIS-CONCEPT-002`; candidate candidate-01; option 1; attempt 1; stage source_visual; size/value source: A B inside a tag has no size or count cue and may be read as a Boolean or byte datatype tag.
  Correction: Add a strong measurement or count symbol to the B-tag.. Outcome: PASS after review of candidate-10.
- `VIS-CONCEPT-002`; candidate candidate-03; option 3; attempt 1; stage source_visual; size/value source: A B above a box containing a tag does not communicate a size or count.
  Correction: Add an explicit count or capacity cue distinct from simple tag packaging.. Outcome: PASS after review of candidate-12.
- `VIS-CONCEPT-002`; candidate candidate-04; option 4; attempt 1; stage source_visual; size/value source: A tag over a panel marked only B communicates a byte label rather than the buffer's size or count.
  Correction: Use a large count symbol with B in a readout so it represents byte count.. Outcome: PASS after review of candidate-13.
- `VIS-DISTINCT-012`; candidate candidate-05; option 5; attempt 1; stage source_visual; size/value source: Orange brackets enclosing a blue tag repeat the dominant orange-brackets-around-blue-object structure of PLC_Attributes.ctl candidate-14.
  Correction: Use a structurally different size metaphor rather than a bracketed central object.. Outcome: PASS after review of candidate-18.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Three options label bytes without conveying size or count. The bracketed tag resembles the separately reviewed PLC attributes cluster. Retain the vertical dimension concept and revise the rest.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-ACTION-006`; candidate candidate-06; option 1; attempt 1; stage small_size; size/value 30x18: The orange dimension arrowheads collapse into blunt bars, weakening the size cue.
  Correction: Use much larger arrowheads with more separation from the arrow shaft.. Outcome: PASS after review of candidate-10.
- `SMALL-ACTION-006`; candidate candidate-02; option 2; attempt 1; stage small_size; size/value 30x18: On closer comparison the arrowheads compress into near-square ends, weakening the dimension cue.
  Correction: Make the top and bottom arrowheads significantly larger than the shaft.. Outcome: PASS after review of candidate-11.
- `SMALL-TEXT-007`; candidate candidate-07; option 3; attempt 1; stage small_size; size/value 30x18: The B collapses to a dark blob and cannot reliably indicate bytes.
  Correction: Make B substantially larger and use fewer large count blocks.. Outcome: PASS after review of candidate-12.
- `SMALL-TEXT-007`; candidate candidate-08; option 4; attempt 1; stage small_size; size/value 30x18: The hash mark merges into a dark shape at 30x18, so the byte-count label is not reliably readable.
  Correction: Widen the hash openings and simplify the readout so #B has more pixels.. Outcome: PASS after review of candidate-13.
- `VIS-DISTINCT-012`; candidate candidate-09; option 5; attempt 1; stage source_visual; size/value source: The C-shaped jaws grip a tag and closely resemble the tag-clamp lock/unlock concepts, implying clamping rather than size.
  Correction: Replace the clamp with a distinctly measuring or counting concept.. Outcome: PASS after review of candidate-18.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: Both dimension-arrow options lose their arrowheads at 30x18, the B and #B count marks become unclear in two others, and the C-shaped jaw design resembles the lock/unlock clamp. Revise before final comparison.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-ACTION-006`; candidate candidate-14; option 5; attempt 1; stage small_size; size/value 30x18: The ruler's white notches largely disappear, leaving an orange diagonal band across a tag and weakening the measuring cue.
  Correction: Use a much thicker ruler with two huge high-contrast ticks, or a different measurement cue.. Outcome: PASS after review of candidate-18.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The horizontal and vertical measurement arrows, counted blocks and #B readout differ in layout, but the diagonal ruler loses its measurement notches at 30x18. Replace it and compare the final five again.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-CONCEPT-002`; candidate candidate-15; option 5; attempt 2; stage source_visual; size/value source: The orange bar has two full-width black bands and resembles a striped band rather than a ruler.
  Correction: Use short partial tick marks from one edge of an unmistakable ruler silhouette.. Outcome: PASS after review of candidate-18.
- `SMALL-RECOG-001`; candidate candidate-15; option 5; attempt 2; stage small_size; size/value 30x18: At 30x18 the bar reads as a striped diagonal mark, not reliably as a measuring tool.
  Correction: Use partial ruler ticks that preserve the measuring-tool silhouette.. Outcome: PASS after review of candidate-18.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The full-width stripes on the ruler read as a striped bar. Revise the last option before comparing the final five.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `SMALL-TEXT-007`; candidate candidate-16; option 5; attempt 3; stage small_size; size/value 30x18: The B is too small and its counters become indistinct; the ruler ticks also merge into the diagonal band.
  Correction: Retire this crowded concept and use a layout with a much larger byte mark and distinct size cue.. Outcome: PASS after review of candidate-18.
- `VIS-DISTINCT-012`; candidate Not available; option Not available; attempt Not available; stage source_visual; size/value Not available: The diagonal-ruler concept has exhausted three attempts and still loses its byte mark at 30x18. Retire it and introduce a distinct fifth concept.
  Correction: Not available. Outcome: PASS after comparison of the final selected set.
- `VIS-MARGIN-005`; candidate candidate-17; option 5; attempt 1; stage source_visual; size/value source: The horizontal tag outline extends within about two percent of each side of the master, leaving cramped edge clearance.
  Correction: Reduce the whole tag to the central 70 percent of the canvas while keeping the #B bold.. Outcome: PASS after review of candidate-18.

## Generalized Lessons

- `VIS-CONCEPT-002` (4 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.
- `VIS-DISTINCT-012` (7 occurrence(s)): Concepts with different names or intended explanations can converge on the same primary metaphor, action cue, and structural composition.
  Recovery: Retire or regenerate the colliding candidate using a different primary metaphor or structural composition. Do not attempt recovery solely through recoloring, restyling, or minor repositioning.
- `SMALL-ACTION-006` (3 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `SMALL-TEXT-007` (3 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `SMALL-RECOG-001` (1 occurrence(s)): An essential visual cue became unreadable, merged, or disappeared at a required small output size.
  Recovery: Enlarge or simplify the failed cue, widen required gaps, and regenerate only the affected concept.
- `VIS-MARGIN-005` (1 occurrence(s)): A candidate's visible structure or rendering did not satisfy a required semantic or visual invariant.
  Recovery: Correct the visual cause identified by the evidence and regenerate only the affected concept.

These are recorded observations and possible improvements for later review. They do not authorize changing this skill during an icon run.
