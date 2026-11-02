# Specification: Complete and validate the LabVIEW icon collection

## Objective

Create a complete, visually differentiated icon set for every `.vi` and `.ctl` file under `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork`. Continue the work until every source file has a finished, validated set and the collection-wide visual review has passed. A batch, a draft, a progress report, or a passing structural check alone is not completion.

This specification defines the work and its acceptance criteria. It does not itself activate a Codex Goal or implement the validator.

## Continuation mechanism

Use a persistent Codex Goal in this chat for execution. The Goal should state the objective above and the completion gates in this specification. Keep the Goal active while useful work remains; do not mark it complete because a turn ended, a batch finished, a budget is nearly exhausted, or a report was written. At each continuation, read the ledger, run the validator, and take the next actionable step. Preserve the work and report a genuine blocker if progress requires external action. Interruptions, service availability, and budget limits can pause a Goal; this specification cannot override those limits or guarantee uninterrupted execution.

Suggested Goal text:

> Complete the LabVIEW icon collection in accordance with this specification. Inventory every `.vi` and `.ctl` in the source tree, create and validate five distinct icon options for each, and complete the collection-wide visual comparison. Resume from the durable ledger and existing assets. Mark the Goal complete only after every required set and the final collection audit pass. Preserve the source VIs and controls.

A Goal must be created explicitly through the available Codex Goal mechanism. It is not created merely by saving this document.

## Scope and output locations

- Source root: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork`.
- Discover source files recursively, case-insensitively matching `.vi` and `.ctl`. Exclude the output and owned working directories from the source inventory. Record relative paths and content hashes. Re-inventory before final acceptance so additions, removals, and changed source files are detected.
- The initial inventory contained 32 VIs and 2 controls in the repository root. Treat that as a starting snapshot, not a fixed completion count.
- Final icon output root: `C:\repos\3rd Party Repos\libplctag-labview-documentation-fork\icons`. The user requested this location for the icon sets. This specification resides separately in `Icon Sets` at the user's request.
- Give each source file its own output folder named for the complete source filename, including `.vi` or `.ctl`, such as `icons\Read_I16.vi`. If source files in different directories have the same filename, mirror enough of their relative source directories under `icons` to avoid collisions; record the mapping in the ledger.
- Preserve existing files and drafts. Do not modify the original VIs or controls, delete earlier work, overwrite an existing accepted package, or create a ZIP unless the user requests it.

## Required deliverables for each source file

Follow the applicable `labview-icon-creator` skill and its current runtime and QA instructions. Each set must contain five independently designed, visually accepted options for the source file's actual function. Each option must include its independent square raster master, 29 × 29, 30 × 23, and 30 × 18 PNGs, and a nine-frame ICO as required by that skill. Include a manifest identifying the source, concepts, files, hashes, review evidence, and publication status. Use the skill's runner for staging, validation, and publication; do not manufacture passing reviews or bypass failed gates. Use white backgrounds unless the user changes that requirement.

Inspect source behavior with an appropriate LabVIEW-capable tool before choosing the visual metaphor. Record enough source evidence to distinguish, for example, a typed getter from a tag read, a typed setter from a PLC write, and automatic platform-based library-path selection from a user-facing picker.

## Distinctness and visual review

The user's requirement applies across files: an icon for one VI or control must not be readily mistaken for an icon for another. Plan five structurally distinct concepts within each set, and maintain a collection-wide registry of visible signatures: function, dominant silhouette, objects, action cue, composition, orientation, and any necessary datatype label. Compare proposed signatures with the registry before generation and compare the resulting artwork after generation. Differences limited to color, a minor position change, or a tiny badge are insufficient.

Typed read and set icons must clearly distinguish operation, signedness, and width at the required PNG sizes. The exact datatype label must be legible; use a capital `I` that cannot be mistaken for `1`. Check opposing operations, especially create/destroy, lock/unlock, read/write, and typed read/set, directly against each other. Reject and redesign candidates that look too alike, misrepresent the function, depend on illegible detail, or become ambiguous at 30 × 18. Make the final cross-file judgment using the actual accepted artwork, including native-size and enlarged previews. A numerical similarity score may flag a pair but cannot prove semantic or structural distinctness.

Review every master and the skill's native and magnified previews at 29 × 29, 30 × 23, 30 × 18, and the 16 × 16 ICO stress frame. Record candidate-specific observations, failures, corrections, and accepted-source hashes. Follow the skill's retry limits and failure-handling rules. A candidate is not accepted merely because an image exists.

## Durable ledger and workflow

Create a machine-readable ledger under `icons` and maintain it throughout the run. It must map each inventoried source path and hash to its output folder, working run, candidate IDs, accepted master hashes, review records, final manifest, and current state. Use states such as `not_started`, `planned`, `generated`, `review_required`, `revision_required`, `set_validated`, and `collection_validated`. Record attempts and meaningful blockers without discarding prior successful work.

For each source file:

1. Verify source meaning and plan five distinct concepts, checking the global signature registry.
2. Generate independent masters using the skill's supported adapter and concurrency limits. Preserve successful images after transfer or packaging failures.
3. Inspect the masters and required previews. Record real observations, revise failures, and perform the within-set comparison.
4. Stage and validate the set with the skill's runner. Preserve the run until publication succeeds. Track a set that has passed local review separately from the final collection-wide acceptance.
5. Update the ledger atomically, run the validator, and continue to the next actionable item. Do not end the job after reporting an intermediate batch.

Once all sets are locally validated, perform the collection-wide comparison and correct conflicts. If a reviewed master changes, invalidate dependent derivatives, hashes, and distinctness reviews, then regenerate and re-review the affected package. Publish and mark the collection complete only when all gates below pass. The existing plan calls for publication after cross-file review; do not present local drafts as finished sets.

## Validator specification

Implement a repeatable local command that reads the actual source tree, ledger, manifests, review evidence, and packaged assets. It must be safe to rerun and must not mutate source VIs or controls. It should print a concise summary, list the next actionable failures, and return a nonzero exit code unless every mandatory machine-checkable gate passes. The report must distinguish structural validation from visual judgment.

The validator must check:

- Every currently inventoried source file maps to exactly one intended output set; detect duplicate mappings, missing entries, stale source hashes, and source inventory changes.
- Every source has five accepted options and the required masters, PNG derivatives, ICOs, and manifest; drafts and failed candidates cannot count toward completion.
- PNG formats and dimensions are correct; every required ICO frame is present and decodable. Check the skill's other deterministic package requirements, including hashes and geometry, using its runner where available.
- Each accepted candidate has the required source and size reviews with candidate-specific evidence, and the recorded reviewed hash matches the actual master. Ensure failed reviews are not treated as acceptance.
- A within-set distinctness review and an up-to-date collection-wide review cover the accepted candidates. Flag stale reviews if any relevant accepted asset or inventory changes.
- Missing, failed, or stale items remain actionable in the ledger. A partially published set is a failure.

Optional similarity metrics can generate a review queue, but a low similarity score must never automatically certify distinctness. The validator can verify that a review record exists and matches the assets; it cannot establish that the review's visual judgment is correct.

Test the validator with meaningful fixtures or controlled temporary copies: missing file, incorrect dimension or frame, changed master hash, failed or missing review, duplicate source mapping, stale collection review, and a valid minimal package. Do not corrupt the user's assets to test failure cases.

## Completion gates

All of the following must be true before reporting the work complete or marking the Goal complete:

1. The final source inventory and ledger agree, and every source file has a correctly mapped output folder.
2. Each source has five accepted options, all required derivatives and ICO frames, and a valid manifest.
3. Source-specific behavior and all size reviews are recorded against the actual accepted masters.
4. The within-set and full cross-file visual comparisons pass, including signedness, width, and opposing actions at 30 × 18.
5. The validator exits successfully against the final files, and the skill's package validation and publication checks pass.
6. The final response links the output location and reports any material limitations. If a genuine blocker or system limit prevents completion, report the exact state and preserve all work; never describe partial output as complete.

## Existing work and recovery

Existing drafts are under `icons` in folders including `Choose_Lib.vi`, `Create_Tag.vi`, `Destroy_Tag.vi`, `Error_Info.vi`, `Lock.vi`, `Read_I16.vi`, `Read_Tag.vi`, `Tag_Size.vi`, `Tag_Status.vi`, `Unlock.vi`, and `Write_Tag.vi`. Reconcile the actual files and runner state rather than assuming all drafts are complete or valid. Earlier reviews identified ambiguous create/destroy designs, similar lock/unlock compositions, and unreadable typed labels. Preserve and reuse suitable masters after checking their provenance; revise only failures. The interrupted `Write_Tag.vi` run was not published, so recover its actual saved candidates and pending jobs before generating replacements.
