# Phase 02 — Database Design and Core Models

## Objective
Implement the initial relational data model for the GlintPM app, consistent with the approved database and backend architecture.

## Read first
Review `database-design.md`, `backend-architecture.md`, `system-architecture.md`, and the product requirements. Inspect current migrations and models.

## Critical decision
Confirm the custom user model strategy before creating the first project migrations. If a custom user model is required, establish it before dependent models are migrated. Do not casually switch user models after migrations have been applied.

## Proposed Django apps
- `common`
- `users`
- `courses`
- `enrollments`
- `career`
- `resources`
- `support`
- `payments`
- `notifications`

Create apps only where they fit the approved architecture; avoid unnecessary fragmentation.

## Core entities to assess
- User and UserProfile
- CourseCategory, Course, CourseTrack
- CourseModule, Lesson
- Cohort, CohortSession
- Enrollment, LessonProgress
- JobCategory, JobListing, SavedJob
- ResourceCategory, Resource
- SupportEnquiry
- Payment
- Notification, NotificationPreference

Use the existing database design as the source of truth. Confirm fields, relationships, ownership, deletion behavior, status choices, and optionality before implementation. Do not add speculative product features.

## Implementation tasks
1. Map each approved entity to its Django app.
2. Define primary keys, foreign keys, many-to-many relationships, timestamps, and status fields.
3. Define uniqueness constraints and database-level checks where appropriate.
4. Add indexes for expected filtering, lookup, and ordering patterns.
5. Define `on_delete` behavior deliberately; protect financial and audit history from accidental deletion.
6. Implement models and migrations in a migration-safe order.
7. Register operational models in Django Admin with useful list displays, filters, search, and read-only audit fields where appropriate.
8. Add model-level validation where it is appropriate, while keeping critical integrity rules in the database and service layer as well.
9. Add tests for constraints, relationships, defaults, and validation.
10. Update the data model documentation to match the implemented schema.

## Tests
- Migrations apply cleanly to a fresh database.
- Constraints prevent duplicate or invalid records.
- Relationships and deletion rules behave as designed.
- Model validation and admin configuration work.
- Tests cover important edge cases.

## Acceptance criteria
- Implemented schema matches approved documentation.
- Migrations are committed and reproducible.
- No secrets or production data are included.
- No unexplained schema divergence remains.

## Deliverables
Models, migrations, admin registrations, model tests, and updated schema documentation.

## Agent instruction
If the documented schema is ambiguous or conflicts with the existing implementation, stop and report the conflict rather than silently choosing a design.
