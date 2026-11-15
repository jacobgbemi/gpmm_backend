# Phase 08 — Professional Resources

## Objective
Provide a secure catalogue of downloadable and viewable learning and professional resources.

## Resource types
Possible types include PDF, document, spreadsheet, video, external article, and template. Confirm supported types from the product requirements.

## Access levels
Possible access levels include Public, Registered users, Course students, and Premium. Define exact entitlement semantics before implementation.

## Implementation tasks
1. Implement resource categories and resource metadata.
2. Define publication status, resource type, access level, title, description, file/external reference, and ordering.
3. Select and document the file-storage provider before production uploads.
4. Store file metadata and storage references; avoid storing large file binaries directly in relational database fields.
5. Protect private files using authenticated download views, short-lived signed URLs, or another provider-supported secure mechanism.
6. Ensure access is checked server-side before a download URL is issued.
7. Prevent private storage paths or credentials from being exposed.
8. Add admin management for resource metadata and publication.
9. Add tests for each access tier and file availability state.

## API contract
- `GET /api/v1/resources/`
- `GET /api/v1/resources/{resource_id}/`
- `GET /api/v1/resources/categories/`

Add a download/access endpoint only after its storage and authorization design is approved.

## Tests
- Public and authenticated access behave as documented.
- Course-only and premium resources require valid entitlements.
- Unpublished resources are hidden.
- Unauthorized download attempts are denied.
- Missing or unavailable files return safe errors.

## Acceptance criteria
- Resource metadata is manageable in admin.
- Entitlement checks are enforced by the backend.
- Production file storage and download security are documented and tested.

## Deliverables
Resource models, APIs, storage integration decision, admin configuration, tests, and API documentation.

## Agent instruction
Do not assume a storage provider or expose private files through permanent public URLs. Verify provider-specific SDKs and URL-signing APIs against official documentation.
