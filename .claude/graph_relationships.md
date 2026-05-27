# Django_project Graph Relationships

       ## Service Dependency Graph
       Django_project
-> Django project
-> Database: SQLite or file-backed local data store
-> Queues/Events: not present
-> Deployment: No standardized deployment command is documented; treat this as a local/manual project.

       ## Runtime Dependency Graph
       Django_project
-> Runtime: Python
-> Runtime: Django
-> Runtime: SQLite
-> Runtime: Django REST Framework

       ## Database Relationship Graph
       Django_project
-> SQLite or file-backed local data store

       ## API Consumer / Provider Graph
       Django_project
-> no formal API contract visible

       ## Queue Publisher / Consumer Graph
       Django_project
-> no broker or queue layer visible

       ## Shared Package Dependency Graph
       Django_project
-> no notable shared package layer beyond app-local dependencies

       ## Deployment Relationship Graph
       Django_project
       - No standardized deployment command is documented; treat this as a local/manual project.

       ## Cross-Repo Relationship Graph
       Django_project
-> no runtime dependency on sibling repos by default
