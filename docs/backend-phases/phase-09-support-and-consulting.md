# Phase 09 — Job Support and Consulting Enquiries

## Objective
Allow prospective and existing customers to submit structured enquiries for GlintPM technical support and consulting.

## Enquiry fields
- Full name
- Email address
- WhatsApp number
- Country
- Support category
- Preferred support option
- Estimated hours
- Project or task description
- Required completion date
- Additional information
- Authenticated user reference, when available
- Status and created/updated timestamps

## Approved category options
- Primavera P6 Scheduling
- Project Controls
- Project Planning
- Technical Job Support
- Other

## Preferred support options
- Hourly Support
- Prepaid Package
- Monthly Retainer
- Custom Quote

## Implementation tasks
1. Implement the SupportEnquiry model and server-side validation.
2. Allow guest enquiries if required by the product requirements; associate the user when authenticated.
3. Validate email, phone/WhatsApp, country, dates, and text lengths.
4. Add spam and abuse controls, including appropriate throttling.
5. Create an admin workflow for reviewing and updating enquiries.
6. Define statuses with the business owner. Candidate statuses: New, Under Review, Awaiting Customer Response, Quoted, Accepted, In Progress, Completed, Closed, Rejected.
7. Ensure users can view only their own enquiries if enquiry history is enabled.
8. Avoid promising prices, response times, or service outcomes not approved by GlintPM.
9. Protect enquiry details as personal and potentially commercially sensitive information.

## API contract
- `POST /api/v1/support/enquiries/`
- Optional authenticated history:
  - `GET /api/v1/support/enquiries/`
  - `GET /api/v1/support/enquiries/{enquiry_id}/`

## Tests
- Valid and invalid enquiry submissions.
- Guest and authenticated submission behavior.
- Throttling and validation.
- Users cannot view other customers' enquiries.
- Staff-only status updates.

## Acceptance criteria
- Enquiries are stored reliably and appear in admin.
- API validation and ownership rules pass.
- No unapproved pricing or response-time promises are returned.

## Deliverables
Enquiry model, serializer, API, admin workflow, tests, and API documentation.

## Agent instruction
Do not add live chat, automated quotations, or CRM integrations unless separately approved.
