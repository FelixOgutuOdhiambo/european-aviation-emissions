# 📊 Data Sources

This project integrates multiple data sources to build a comprehensive aviation emissions analytics dataset.

---

# 1. EUROCONTROL CO₂ Emissions Data

## Source
- Base URL:
  https://www.eurocontrol.int/performance/data/download/csv

- Provider: EUROCONTROL  
- Dataset: CO₂ emissions by state  

---

## Access Pattern

Data is dynamically retrieved using:


### Example:


---

## Coverage
- Period: 2010 – 2025  
- Granularity: Monthly  
- Level: Country / State  

---

## Data Fields

- STATE_NAME  
- STATE_CODE  
- YEAR  
- MONTH  
- CO2_QTY_TONNES  
- TF (Flights)  


## Data Processing

### Schema Handling
- Missing columns handled dynamically  
- Schema drift managed across years  

### Cleaning
- Standardized country names  
- Removed whitespace and inconsistencies  

### Transformation
- Created DATE field from YEAR + MONTH  
- Converted CO₂ values to numeric  

---

## Limitations

- Aggregated at country level (no route-level detail)  
- No aircraft-level emissions breakdown  
- Naming inconsistencies across years  

---

# 2. Country Metadata (REST API)

## Source
https://restcountries.com/v3.1/all

## API Configuration
