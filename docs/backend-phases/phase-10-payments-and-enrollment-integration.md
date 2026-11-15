# Phase 10 — Payments and Enrollment Integration

## Objective
Integrate the approved payment provider and activate paid course enrollments only after independently verified successful payment.

## Mandatory provider decision
Before coding:
1. Confirm which provider GlintPM has selected for each supported market/currency.
2. Read the provider's current official API and webhook documentation.
3. Confirm supported currencies, payment methods, settlement rules, sandbox process, refund process, and webhook-signature verification.
4. Record the integration design and any country/currency limitations.

Do not invent provider endpoints, SDK methods, request fields, signature algorithms, or webhook behavior.

## Payment data
Define a Payment record with approved fields such as:
- User and intended course/track/enrollment reference
- Amount and currency
- Provider
- Internal payment reference
- Provider transaction reference
- Status
- Initiation and verification timestamps
- Relevant non-sensitive provider metadata

Never store raw card numbers, CVVs, PINs, or other prohibited payment credentials.

## Implementation tasks
1. Keep authoritative prices in backend-managed course/track pricing data.
2. Calculate the amount and currency on the server; never trust client-submitted totals.
3. Create a payment initiation service using the provider's documented flow.
4. Persist an internal reference before redirecting or handing off to the provider.
5. Implement provider status verification using documented server-side mechanisms.
6. Implement the provider webhook using its documented signature/authenticity verification.
7. Make webhook processing idempotent so repeated events do not duplicate activation.
8. Verify payment reference, amount, currency, merchant/account context, and final status.
9. Activate the relevant enrollment only after verified successful payment.
10. Use database transactions to keep payment and enrollment state consistent.
11. Log safe audit information without storing secrets or sensitive payment data.
12. Document failure, cancellation, timeout, duplicate-event, and refund handling.

## API contract
- `POST /api/v1/payments/initiate/`
- `GET /api/v1/payments/{payment_id}/`
- Webhook route pattern: `POST /api/v1/payments/webhooks/{provider}/`

The actual webhook route and payload handling must follow the selected provider's official requirements.

## Tests
- Successful sandbox payment and verified activation.
- Failed, cancelled, pending, and expired payment states.
- Invalid webhook signature/authenticity.
- Duplicate webhook delivery.
- Amount/currency/reference mismatch.
- User cannot view another user's payment.
- Client cannot activate an enrollment by altering request fields.
- Transaction rollback on activation failure.

## Acceptance criteria
- No enrollment is activated from an unverified client claim.
- Webhook processing is secure and idempotent.
- Server-side pricing is authoritative.
- Sandbox end-to-end tests pass.
- Provider limitations and operational procedures are documented.

## Deliverables
Provider decision record, payment models/services/APIs, webhook integration, enrollment activation integration, tests, and operational documentation.

## Agent instruction
Do not proceed with production payment credentials until sandbox verification and security review are complete. Verify all provider-specific syntax against current official documentation.
