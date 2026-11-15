# Phase 01 — Backend Foundation and Project Setup

## Objective
Create a secure, maintainable Django backend foundation for the GlintPM mobile application.

## Read first
Review the project overview, product requirements, system architecture, backend architecture, API specification, coding-agent guidelines, security guidelines, and development roadmap. Inspect the existing repository before changing files. Preserve established conventions unless a documented reason requires a change.

## Technology direction
- Python and Django
- Django REST Framework (DRF)
- PostgreSQL
- Django Admin; use Django Unfold if it is compatible with the selected Django version
- API namespace: `/api/v1/`
- Environment-based configuration
- Automated tests

Use maintained, mutually compatible versions. Verify versions and installation instructions against current official documentation. Do not invent package names, APIs, or configuration options.

## Implementation tasks
1. Inspect the repository, current dependencies, existing documentation, and Git status.
2. Record the proposed backend structure and any assumptions before implementation.
3. Create or configure the Django project and settings split, for example:
   - `config/settings/base.py`
   - `config/settings/development.py`
   - `config/settings/production.py`
4. Configure environment variables and provide a safe `.env.example`. Never commit secrets.
5. Configure PostgreSQL using environment-based connection settings.
6. Install and configure DRF and establish the `/api/v1/` routing structure.
7. Create a `common` app for shared utilities and infrastructure.
8. Add a minimal health endpoint that confirms application availability without exposing secrets or internal configuration.
9. Configure Django Admin and, if selected, Django Unfold.
10. Configure logging, timezone, static files, and media settings appropriate to the project stage.
11. Add initial automated tests and update the backend README with setup and run instructions.

## Suggested structure
```text
backend/
  config/
    settings/
      __init__.py
      base.py
      development.py
      production.py
    urls.py
    asgi.py
    wsgi.py
  apps/
    common/
  tests/
  manage.py
  requirements/
  .env.example
  README.md
```
Adapt this to the existing repository rather than duplicating or restructuring files unnecessarily.

## Tests
- Project starts with development settings.
- Database connection works.
- Health endpoint returns the documented response.
- API version root resolves.
- Admin login page loads.
- Tests run without requiring production secrets.

## Acceptance criteria
- Reproducible local setup is documented.
- Secrets are excluded from source control.
- PostgreSQL and DRF are configured.
- Health endpoint and initial tests pass.
- No unrelated frontend or product functionality is implemented in this phase.

## Deliverables
Working backend foundation, dependency manifest, `.env.example`, setup documentation, initial tests, and a short implementation report listing files changed, commands run, test results, and unresolved decisions.

## Agent instruction
Do not proceed to Phase 02 until the foundation is working and the acceptance criteria are demonstrated.
