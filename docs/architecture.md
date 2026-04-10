# Architecture

## Overview

This project follows a modern data architecture:

Notebook → Lakehouse → SQL → Semantic Model → Power BI

---

## Layers

### 1. Ingestion
- PySpark notebook loads EUROCONTROL data

### 2. Storage
- Data stored in Lakehouse (Delta)

### 3. Transformation
- Cleaning and standardization

### 4. Enrichment
- REST Countries API integration

### 5. Modeling
- Semantic model for KPIs

### 6. Visualization
- Power BI dashboard