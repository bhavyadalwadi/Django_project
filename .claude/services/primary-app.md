# Primary App

## Responsibility
Main runtime for `Django_project`.

## Dependencies
- Python
- Django
- SQLite
- Django REST Framework

## Inbound APIs
- No formal inbound API is visible.

## Outbound APIs
- No confirmed external provider or downstream API.

## Databases Used
- SQLite or file-backed local data store

## Queues / Topics
- No queue/topic layer visible.

## Critical Workflows
- Django project structure with separate practice projects under one repo
- Simple stock model with ticker, open, close, and volume fields
- API-style stock list view using Django REST Framework response patterns
- Local SQLite-backed development setup suitable for framework learning

## Failure Modes
- Project maturity is uneven; expect weaker docs, less automation, and more manual assumptions than the active product repos.

## Scaling Concerns
- current implementation appears intentionally lightweight
- there is no evidence of multi-service scaling machinery unless repo docs add it

## Operational Concerns
- start from repo-local `.claude/` docs and Graphify summary before code changes
- validate environment assumptions before debugging logic

## Important Source Files
- `README.md`
- `Stock_site/stocks/views.py`
- `Stock_site/stocks/models.py`
- `Stock_site/manage.py`
- `README.MD`

## Dangerous Code Paths
- Project maturity is uneven; expect weaker docs, less automation, and more manual assumptions than the active product repos.

## Testing Strategy
- No standardized automated test command is visible.

## Known Technical Debt
- Pending work is unknown from current repo docs.
