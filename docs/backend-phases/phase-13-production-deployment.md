# Phase 13 — Production Deployment and Operations

## Objective
Deploy the backend to the approved production infrastructure with secure configuration, monitoring, backups, and a tested recovery and rollback plan.

## Infrastructure decisions
Confirm the hosting provider, database service, object/file storage, domain, email delivery provider, and payment provider. Do not assume a service has been purchased or configured. Verify current provider documentation and pricing before committing to a design.

An API hostname such as `api.glintpm.com` may be considered, but confirm DNS and domain ownership/configuration before using it.

## Implementation tasks
1. Document the production architecture and environment variables.
2. Configure production settings with debug disabled and secure host/origin settings.
3. Store secrets in the hosting platform's supported secret manager/environment configuration.
4. Provision PostgreSQL and restrict network/database access.
5. Configure a production-capable application server and reverse proxy/platform routing.
6. Configure HTTPS and verify certificate renewal.
7. Configure static assets and private media/object storage.
8. Configure email delivery and payment-provider production settings after sandbox approval.
9. Run migrations through a controlled release process.
10. Configure structured application logs and error monitoring.
11. Configure health checks and operational alerts.
12. Establish automated database backups and retention rules.
13. Perform and document a database restore test; a configured backup without a restore test is not sufficient evidence of recoverability.
14. Create a release checklist and rollback procedure.
15. Run post-deployment smoke tests for authentication, catalogue, enrollment, resources, support, notifications, and payment status handling.
16. Document incident response and access ownership.

## Security requirements
- Never run Django's development server as the production application server.
- Do not commit `.env` files or production secrets.
- Keep debug mode disabled.
- Enforce HTTPS.
- Restrict admin access appropriately.
- Apply least-privilege access to databases, storage, and deployment credentials.
- Avoid exposing internal errors or stack traces to clients.
- Ensure private resources remain private in production.

## Acceptance criteria
- Deployment is reproducible and documented.
- HTTPS and production security settings are verified.
- Database migrations and smoke tests pass.
- Backups are configured and a restore has been tested.
- Monitoring and rollback procedures exist.
- Production payment processing is enabled only after provider approval and end-to-end verification.

## Deliverables
Deployment configuration, environment-variable reference, release checklist, smoke-test results, backup/restore evidence, monitoring setup, and rollback/runbook documentation.

## Agent instruction
Do not declare the system production-ready merely because it is deployed. State exactly which checks were completed, which were not, and any remaining operational risks.
