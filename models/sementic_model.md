# Semantic Model – EU Aviation CO₂ Emissions

## Overview

The semantic model (`eu_co2_model`) provides the analytical layer for the project, enabling efficient querying, KPI calculation, and dashboard visualization in Power BI.

It is designed to support:
- Emissions analysis  
- Flight activity tracking  
- Time-based trends  
- KPI calculations  

---

## Model Structure

The model follows a **star schema design** with fact and dimension tables.

### 🔹 Fact Table
- `eu_co2_emissions`

### 🔹 Dimension Tables
- `dim_date`

### 🔹 Supporting Table
- `DAX` (Measures)

---

## Tables Description

### eu_co2_emissions (Fact Table)

Contains the core dataset:

| Column | Description |
|--------|------------|
| DATE | Month-level date |
| STATE_NAME | Country name |
| STATE_CODE | Country code |
| CO2_QTY_TONNES | Total emissions |
| FLIGHTS | Number of flights |

---

### dim_date (Dimension Table)

Supports time-based analysis:

| Column | Description |
|--------|------------|
| Date | Calendar date |
| Year | Year |
| Month | Month |
| Month Name | Month label |
| Quarter | Quarter |

---

### DAX Table (Measures Layer)

Contains calculated measures used in reporting.

---

## Relationships

The model uses a primary relationship:


- Type: One-to-Many  
- Direction: Single (dim → fact)  

---

## Key Measures

### CO₂ Metrics
- Total CO₂ Emissions  
- CO₂ per Flight  

### Operational Metrics
- Total Flights  

### Derived Metrics
- Average CO₂ per Flight  

---

## Analytical Capabilities

The model enables:

### Time Analysis
- Yearly trends  
- Monthly seasonality  

### Geographic Analysis
- Country-level comparisons  
- Emissions distribution  

### Efficiency Analysis
- CO₂ per flight benchmarking  

---

## 👤 Author
Felix Ogutu Odhiambo  
Aviation Analytics & Network Planning Specialist