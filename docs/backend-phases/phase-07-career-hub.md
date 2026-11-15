# Phase 07 — Career Hub

## Objective
Provide a backend job-listing catalogue with categories, search/filtering, and user saved jobs.

## Implementation tasks
1. Implement job categories and job listing records.
2. Include approved fields such as title, employer, location, work arrangement, description, requirements, application URL/contact, publication date, expiry date, and status.
3. Support draft, published, expired, and archived states as approved.
4. Provide filtering by category, location, work arrangement, and other approved fields.
5. Add search and pagination.
6. Exclude expired or unpublished jobs from ordinary listing results.
7. Implement saved-job records with duplicate prevention and user ownership.
8. Provide admin workflows for reviewing and publishing listings.
9. Do not scrape third-party job sites or republish copyrighted listings without authorization.
10. Do not claim a listing is verified unless a documented verification process has been completed.

## API contract
- `GET /api/v1/jobs/`
- `GET /api/v1/jobs/{job_id}/`
- `GET /api/v1/jobs/categories/`
- `GET /api/v1/jobs/saved/`
- `POST /api/v1/jobs/{job_id}/save/`
- `DELETE /api/v1/jobs/{job_id}/save/`

## Tests
- Search, filters, and pagination work.
- Expired and unpublished jobs are excluded.
- Users can save and unsave jobs.
- Duplicate saves are prevented.
- Users cannot access another user's saved-job records.

## Acceptance criteria
- Staff can manage job listings.
- Users can browse and save eligible listings.
- API permissions and expiry rules are tested.

## Deliverables
Career Hub models, APIs, admin configuration, tests, and documented listing rules.

## Agent instruction
An application-tracking feature is not included by default. Build it only if the product requirements explicitly approve it.
