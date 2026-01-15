# UK MetOffice Climate Platform

A production-style climate data platform that ingests UK MetOffice datasets, normalizes climate metrics, exposes REST APIs, and visualizes insights through an interactive dashboard.

This project is designed with **scalability, clarity, and data integrity** in mind and demonstrates backend, data, and UI engineering best practices.

---

## Key Features

-  Ingests UK MetOffice climate datasets (text-based sources)
-  Normalized PostgreSQL data model (analytics-ready)
-  REST APIs built using Django REST Framework
-  Interactive dashboard with Chart.js & Bootstrap
-  Fully Dockerized (Backend + PostgreSQL)
-  Cloud-deployable architecture

---

##  System Architecture

```
UK MetOffice Dataset
        ↓
Ingestion Pipeline (Django Management Command)
        ↓
PostgreSQL (Normalized Climate Facts)
        ↓
REST APIs (Django REST Framework)
        ↓
Web Dashboard (Chart.js)
```

---

##  Tech Stack

| Layer      | Technology |
|-----------|------------|
| Backend   | Django, Django REST Framework |
| Database  | PostgreSQL |
| Frontend  | HTML, Bootstrap 5, Chart.js |
| DevOps    | Docker, Docker Compose |

---

##  Project Structure

```
metoffice-climate-platform/
│
├── backend/
│   ├── backend/            # Django project configuration
│   ├── climate/            # Core app (models, APIs, UI)
│   ├── manage.py
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## ▶ Running the Project (Local)

### Prerequisites
- Docker
- Docker Compose

### Steps

```bash
git clone https://github.com/Rajprithvi2021/metoffice-climate-platform.git
cd metoffice-climate-platform
docker compose up --build
```

---

##  Access Points

- **Dashboard:** http://localhost:8000/
- **API Root:** http://localhost:8000/api/

---

##  API Endpoints

### Metric List
```
GET /api/metrics/
```

### Monthly Climate Data
```
GET /api/weather/monthly/?metric_id=<id>&year=<year>
```

### Annual Climate Trend
```
GET /api/weather/annual/?metric_id=<id>
```

All APIs return **clean, frontend-ready JSON responses**.

---

##  Dashboard Capabilities

- Metric selection (e.g., Tmax – UK)
- Monthly climate visualization by year
- Long-term annual trend analysis
- Smooth animations and tooltips
- Clean, executive-style UI

---

##  Design Decisions

- Clear separation of ingestion, storage, API, and UI layers
- Normalized schema for analytics and extensibility
- Idempotent ingestion (safe re-runs)
- Consumer-first API design
- Minimal but insight-driven UI

---

##  Configuration Notes

- PostgreSQL is used exclusively (no SQLite)
- Database configuration is handled via Docker environment variables
- Sensitive files and data are excluded using `.gitignore`

---

##  Author

**Prithvi Raj**  
GitHub: https://github.com/Rajprithvi2021

---

##  Notes for Reviewers

This project was approached as a **data platform problem**, not just a Django assignment.

The architecture is designed to be easily extended for:
- Additional regions
- New climate parameters (Rainfall, Tmin, etc.)
- Scheduled ingestion jobs
- Cloud deployment (AWS / GCP / Azure)

Happy to walk through the design and implementation decisions.