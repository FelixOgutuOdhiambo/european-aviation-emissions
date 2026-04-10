# ✈️ Emissions Extraction Notebook

## Overview

This notebook implements the end-to-end data pipeline for ingesting, transforming, enriching, and storing European aviation CO₂ emissions data.

It serves as the **development and validation environment** for the project before code is modularized into the `src/` pipeline.

---

## Role in the Project

This notebook is used for:

- Data ingestion from EUROCONTROL  
- Data cleaning and transformation  
- Data enrichment using external APIs  
- Validation of pipeline logic  
- Testing before production deployment  

---

## Pipeline Flow


---

## Key Steps

### 1. Data Ingestion
- Loads multi-year CO₂ datasets (2010–2025)
- Handles schema drift across files
- Combines datasets into a single DataFrame

---

### 2. Data Transformation
- Cleans country names and codes  
- Standardizes schema  
- Creates derived fields (e.g., DATE)  

---

### 3. Data Enrichment
- Fetches country metadata via REST API  
- Adds:
  - Region  
  - Subregion  
  - Coordinates  
  - Population  

---

### 4. Data Storage
- Writes processed data to Lakehouse  
- Uses Delta format for scalability  

---

## Development Approach

This notebook follows a structured workflow:

1. Develop and test logic interactively  
2. Validate outputs at each step  
3. Refactor into reusable functions  
4. Move finalized logic into `src/`  

---

## Relationship with `src/`

The notebook is the **source of truth for development**, while:

- `src/` contains modular, production-ready code  
- The same logic is replicated in structured Python modules  

---

## Output

The final dataset:

- Table: `EU_co2_emissions`  
- Format: Delta Lake  
- Usage:
  - Power BI dashboard  
  - Semantic model  
  - Analytical queries  

---

## Notes

- This notebook requires a Spark environment (Microsoft Fabric)  
- Not intended for standalone execution outside Spark  
- Use `src/` for production pipelines  

---

## Future Improvements

- Add parameterization (years, paths)  
- Integrate logging  
- Automate pipeline execution  
- Add data quality checks  

---

## 👤 Author
Felix Ogutu Odhiambo  
Aviation Analytics & Network Planning Specialist