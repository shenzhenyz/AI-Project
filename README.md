# HumanForYou Employee Turnover Analysis

## Project Overview

This project analyzes employee turnover at HumanForYou, a pharmaceutical company in India with approximately 4,000 employees experiencing a 15% annual turnover rate. The goal is to identify factors influencing turnover and develop predictive models to help reduce attrition.

## Project Structure

```
.
├── data/                    # Data files (CSV and ZIP)
│   ├── general_data.csv
│   ├── manager_survey_data.csv
│   ├── employee_survey_data.csv
│   └── in_out_time.zip
├── notebooks/               # Jupyter notebooks
│   └── employee_turnover_analysis.ipynb
├── src/                     # Python modules
│   ├── data_loader.py
│   ├── preprocessing.py
│   └── model_evaluation.py
├── reports/                 # Generated reports and documents
│   ├── ethics_document.md
│   └── bibliography.md
├── requirements.txt
└── README.md
```

## Data Description

### general_data.csv
Contains employee HR data including:
- Demographics (Age, Gender, MaritalStatus)
- Job information (JobRole, JobLevel, Department)
- Compensation (MonthlyIncome, PercentSalaryHike, StockOptionLevel)
- Experience (TotalWorkingYears, YearsAtCompany, YearsSinceLastPromotion)
- **Target variable**: Attrition (Yes/No)

### manager_survey_data.csv
Manager assessments:
- JobInvolvement (1-4 scale)
- PerformanceRating (1-4 scale)

### employee_survey_data.csv
Employee satisfaction survey:
- EnvironmentSatisfaction (1-4 scale)
- JobSatisfaction (1-4 scale)
- WorkLifeBalance (1-4 scale)
- Note: Contains "NA" values for missing responses

### in_out_time.zip
Working hours data with arrival and departure times for 2015.

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Place all data files in the `data/` directory
2. Open the Jupyter notebook:
```bash
jupyter notebook notebooks/employee_turnover_analysis.ipynb
```

## Methodology

1. **Data Loading & Exploration**: Load and explore all datasets
2. **Data Preprocessing**: Handle missing values, encode categorical variables, feature engineering
3. **Exploratory Data Analysis**: Identify patterns and relationships
4. **Feature Engineering**: Create new features from working hours data
5. **Model Development**: Train multiple classification models
6. **Model Evaluation**: Compare models using appropriate metrics
7. **Model Interpretation**: Use SHAP values to understand feature importance
8. **Recommendations**: Propose actionable insights for reducing turnover

## Key Metrics

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC
- Feature Importance

## Deliverables

1. **Jupyter Notebook**: Complete analysis with code and visualizations
2. **Ethics Document**: Ethical considerations and methodology
3. **Bibliography**: Academic and technical references
4. **Presentation**: 20-minute presentation of findings

## Authors

Data Analysis Team

## License

This project is for academic purposes.

