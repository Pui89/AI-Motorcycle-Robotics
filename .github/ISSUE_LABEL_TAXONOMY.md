# PUI89 AI Step-Through Scooter — Issue label taxonomy

This file documents recommended labels; it does not create GitHub labels automatically. Create and verify repository labels separately before any automation depends on them.

## Recommended labels
- Type: `type:bug`, `type:feature`, `type:research`, `type:documentation`
- Priority: `priority:critical`, `priority:high`, `priority:normal`, `priority:low`
- Status: `status:needs-triage`, `status:blocked`, `status:in-progress`, `status:needs-evidence`, `status:ready-for-review`
- Evidence: `evidence:concept`, `evidence:synthetic`, `evidence:simulated`, `evidence:bench-tested`, `evidence:field-validated`, `evidence:independently-verified`
- Risk: `risk:safety`, `risk:security`, `risk:privacy`, `risk:licensing`

## Triage rules
1. Apply labels only after human review.
2. Use the highest justified priority; do not infer urgency from unsupported claims.
3. Label evidence by the strongest directly linked evidence, not the roadmap.
4. Safety, security, privacy, and licensing concerns require explicit review.
5. Request missing evidence rather than treating absence as proof of failure.

This taxonomy is workflow guidance, not certification, a safety case, field validation, or proof of capability.
