# Graph Report - Django_project  (2026-05-26)

## Corpus Check
- 49 files · ~69,201 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 181 nodes · 159 edges · 40 communities (24 shown, 16 thin omitted)
- Extraction: 90% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 16 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d303d8cb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]
- [[_COMMUNITY_Community 9|Community 9]]
- [[_COMMUNITY_Community 10|Community 10]]
- [[_COMMUNITY_Community 11|Community 11]]
- [[_COMMUNITY_Community 12|Community 12]]
- [[_COMMUNITY_Community 13|Community 13]]
- [[_COMMUNITY_Community 25|Community 25]]
- [[_COMMUNITY_Community 26|Community 26]]
- [[_COMMUNITY_Community 27|Community 27]]
- [[_COMMUNITY_Community 28|Community 28]]
- [[_COMMUNITY_Community 29|Community 29]]
- [[_COMMUNITY_Community 30|Community 30]]
- [[_COMMUNITY_Community 31|Community 31]]
- [[_COMMUNITY_Community 32|Community 32]]
- [[_COMMUNITY_Community 33|Community 33]]
- [[_COMMUNITY_Community 34|Community 34]]
- [[_COMMUNITY_Community 35|Community 35]]
- [[_COMMUNITY_Community 36|Community 36]]
- [[_COMMUNITY_Community 37|Community 37]]
- [[_COMMUNITY_Community 38|Community 38]]
- [[_COMMUNITY_Community 39|Community 39]]

## God Nodes (most connected - your core abstractions)
1. `Django_project Project Context` - 16 edges
2. `Primary App` - 15 edges
3. `Django_project Architecture` - 14 edges
4. `Django_project Workflows` - 10 edges
5. `Album` - 9 edges
6. `Django_project Coding Rules` - 9 edges
7. `Django_project [Archived]` - 8 edges
8. `UserForm` - 7 edges
9. `UserFormView` - 6 edges
10. `StockList` - 6 edges

## Surprising Connections (you probably didn't know these)
- `Meta` --uses--> `Stock`  [INFERRED]
  Stock_site/stocks/serializers.py → Stock_site/stocks/models.py
- `IndexView` --uses--> `Album`  [INFERRED]
  Music_site/music/views.py → Music_site/music/models.py
- `DetailView` --uses--> `Album`  [INFERRED]
  Music_site/music/views.py → Music_site/music/models.py
- `AlbumCreate` --uses--> `Album`  [INFERRED]
  Music_site/music/views.py → Music_site/music/models.py
- `AlbumUpdate` --uses--> `Album`  [INFERRED]
  Music_site/music/views.py → Music_site/music/models.py

## Communities (40 total, 16 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.13
Nodes (14): CreateView, DeleteView, Meta, UserForm, Album, Song, AlbumCreate, AlbumDelete (+6 more)

### Community 1 - "Community 1"
Cohesion: 0.26
Nodes (5): APIView, Stock, Meta, StockSerializer, StockList

### Community 2 - "Community 2"
Cohesion: 0.4
Nodes (3): AppConfig, MusicConfig, StocksConfig

### Community 3 - "Community 3"
Cohesion: 0.12
Nodes (16): Business Purpose, Critical Dependencies, Current Architecture Themes, Deployment Model, Django_project Project Context, Environments, Important APIs, Important Databases (+8 more)

### Community 4 - "Community 4"
Cohesion: 0.12
Nodes (15): Critical Workflows, Dangerous Code Paths, Databases Used, Dependencies, Failure Modes, Important Source Files, Inbound APIs, Known Technical Debt (+7 more)

### Community 11 - "Community 11"
Cohesion: 0.2
Nodes (9): Current status, Django_project, Django_project [Archived], Key files, Maintenance note, Resume value, Run locally, What is inside (+1 more)

### Community 25 - "Community 25"
Cohesion: 0.13
Nodes (14): Auth Flow, Caching Layers, Deployment Topology, Django_project Architecture, End-to-End Request Flows, Event-Driven Architecture, Failover Behavior, Frontend / Backend Interaction (+6 more)

### Community 26 - "Community 26"
Cohesion: 0.18
Nodes (10): Debugging, Deployment, Django_project Workflows, Feature Rollout, Incident Response, Local Development, Migrations, Observability Investigation (+2 more)

### Community 27 - "Community 27"
Cohesion: 0.2
Nodes (9): API Conventions, Architecture Patterns, Database / Migration Patterns, Django_project Coding Rules, Error Handling / Logging, Naming / Structure, State Management, Testing Conventions (+1 more)

### Community 28 - "Community 28"
Cohesion: 0.29
Nodes (6): Critical Entrypoints, Django_project Onboarding, First Read, How To Start Reasoning, Local Run Baseline, Module Map

### Community 29 - "Community 29"
Cohesion: 0.5
Nodes (3): Django_project Decision Log, Graphify-first repo discovery, Preserve repo separation

### Community 30 - "Community 30"
Cohesion: 0.5
Nodes (3): Critical Entrypoints, Read First, Top-Level Modules

## Knowledge Gaps
- **93 isolated node(s):** `Meta`, `Migration`, `Migration`, `Django settings for website project.  Generated by 'django-admin startproject' u`, `WSGI config for website project.  It exposes the WSGI callable as a module-level` (+88 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **16 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Are the 6 inferred relationships involving `Album` (e.g. with `IndexView` and `DetailView`) actually correct?**
  _`Album` has 6 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Meta`, `Migration`, `Migration` to the rest of the system?**
  _93 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._
- **Should `Community 3` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._
- **Should `Community 4` be split into smaller, more focused modules?**
  _Cohesion score 0.12 - nodes in this community are weakly interconnected._
- **Should `Community 25` be split into smaller, more focused modules?**
  _Cohesion score 0.13 - nodes in this community are weakly interconnected._