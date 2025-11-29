# AI for HumanForYou - Employee Attrition Prediction

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Ethics: AI Guidelines](https://img.shields.io/badge/Ethics-EU%20AI%20Guidelines-green.svg)](https://ec.europa.eu/digital-single-market/en/news/ethics-guidelines-trustworthy-ai)

## 📋 Project Overview

This AI project addresses the employee turnover challenge faced by **HumanForYou**, a pharmaceutical company based in India with approximately 4,000 employees. With an annual attrition rate of 15%, the company experiences significant operational and financial impacts.

Our mission is to **identify key factors influencing employee turnover** and develop predictive models to help management implement targeted retention strategies.

## 🎯 Business Objectives

### Problem Statement
HumanForYou's high turnover rate creates three major challenges:

1. **Project Delays**: Departing employees leave projects incomplete, damaging reputation with clients and partners
2. **HR Resource Strain**: Maintaining large recruitment teams to continuously find replacement talent
3. **Onboarding Costs**: New employees require training and time to become fully operational

### Project Goals
- Identify the most influential factors driving employee attrition
- Build predictive models to forecast turnover risk
- Propose actionable recommendations to improve employee retention
- Ensure ethical AI practices throughout the analysis

## 📊 Dataset Description

### Data Sources

The HR department provided anonymized employee data across multiple CSV files, with each employee identified by a unique `EmployeeID`.

#### 1. General HR Data (`general_data.csv`)
Employee demographics and work-related information for 2015:

| Feature | Description |
|---------|-------------|
| **Age** | Employee age in 2015 |
| **Attrition** | Target variable: Did employee leave in 2016? |
| **BusinessTravel** | Travel frequency (Non-Travel, Travel_Rarely, Travel_Frequently) |
| **DistanceFromHome** | Distance in km from home to office |
| **Education** | Level: 1=Pre-college, 2=College, 3=Bachelor, 4=Master, 5=PhD |
| **EducationField** | Field of study |
| **JobLevel** | Hierarchical level (1-5) |
| **JobRole** | Position within company |
| **MaritalStatus** | Single, Married, or Divorced |
| **MonthlyIncome** | Gross monthly salary (rupees) |
| **NumCompaniesWorked** | Previous employers count |
| **PercentSalaryHike** | Salary increase % in 2015 |
| **StockOptionLevel** | Company stock investment level |
| **TotalWorkingYears** | Total work experience |
| **TrainingTimesLastYear** | Training days in 2015 |
| **YearsAtCompany** | Company seniority |
| **YearsSinceLastPromotion** | Years since last promotion |
| **YearsWithCurrentManager** | Years under current manager |

#### 2. Manager Survey Data (`manager_survey_data.csv`)
Manager assessments from February 2015:

- **JobInvolvement**: Work engagement (1=Low, 2=Average, 3=High, 4=Very High)
- **PerformanceRating**: Annual performance (1=Low, 2=Good, 3=Excellent, 4=Beyond Expectations)

#### 3. Employee Survey Data (`employee_survey_data.csv`)
Employee quality of life survey from June 2015:

- **EnvironmentSatisfaction**: Workplace environment (1-4 scale)
- **JobSatisfaction**: Job satisfaction (1-4 scale)
- **WorkLifeBalance**: Work-life balance (1=Poor, 2=Satisfactory, 3=Very Satisfactory, 4=Excellent)

*Note: Contains NA values for non-respondents*

#### 4. Time Clock Data (`in_out_time.zip`)
Employee arrival and departure times for January 1 - December 31, 2015

### Data Origin
Dataset inspired by: [HR Analytics Case Study on Kaggle](https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study)

## 🛠️ Technical Stack

```python
# Core Libraries
pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=1.0.0

# Visualization
matplotlib>=3.4.0
seaborn>=0.11.0
plotly>=5.0.0

# Machine Learning
xgboost>=1.5.0
lightgbm>=3.3.0
imbalanced-learn>=0.9.0

# Notebook
jupyter>=1.0.0
ipywidgets>=7.6.0

# Model Interpretation
shap>=0.40.0
lime>=0.2.0
```

## 📦 Installation

```bash
# Clone repository
git clone https://github.com/yourusername/humanforyou-attrition-ai.git
cd humanforyou-attrition-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Extract time clock data
unzip data/raw/in_out_time.zip -d data/raw/
```

## 🚀 Quick Start

```python
# Load and prepare data
from src.data_processing import load_and_merge_data
from src.feature_engineering import create_features

# Load datasets
df = load_and_merge_data(
    general='data/raw/general_data.csv',
    manager='data/raw/manager_survey_data.csv',
    employee='data/raw/employee_survey_data.csv',
    timeclock='data/raw/in_out_time/'
)

# Feature engineering
df_processed = create_features(df)

# Train model
from src.models import train_attrition_model

model, metrics = train_attrition_model(df_processed)
print(f"Model AUC-ROC: {metrics['auc']:.3f}")

# Generate predictions
predictions = model.predict_proba(X_test)[:, 1]
```

## 📁 Project Structure

```
humanforyou-attrition-ai/
├── data/
│   ├── raw/                          # Original CSV files
│   ├── processed/                    # Cleaned datasets
│   └── features/                     # Engineered features
├── notebooks/
│   ├── 01_exploratory_analysis.ipynb # EDA and data quality
│   ├── 02_feature_engineering.ipynb  # Feature creation
│   ├── 03_modeling.ipynb             # Model development
│   ├── 04_model_evaluation.ipynb     # Performance analysis
│   └── 05_interpretability.ipynb     # SHAP/LIME analysis
├── src/
│   ├── data_processing.py            # Data loading and cleaning
│   ├── feature_engineering.py        # Feature creation
│   ├── models.py                     # ML model implementations
│   ├── evaluation.py                 # Metrics and validation
│   └── utils.py                      # Helper functions
├── reports/
│   ├── ethics_assessment.pdf         # Ethics deliverable
│   ├── bibliography.pdf              # Academic references
│   └── figures/                      # Visualizations
├── presentation/
│   └── final_presentation.pdf        # Project defense slides
├── requirements.txt
└── README.md
```

## 🔬 Methodology

### 1. Data Preparation & Exploration
- **Data Integration**: Merge multiple CSV files by EmployeeID
- **Missing Value Analysis**: Handle NA values in survey data
- **Outlier Detection**: Identify and treat anomalies
- **Class Imbalance**: Address 15% attrition rate (imbalanced dataset)

### 2. Feature Engineering
- **Time-based Features**: Extract patterns from clock-in/clock-out data
  - Average working hours
  - Overtime frequency
  - Punctuality metrics
- **Derived Features**: 
  - Salary-to-market ratios
  - Promotion velocity
  - Travel burden index
- **Interaction Features**: Cross-feature relationships

### 3. Model Development
Algorithms tested:
- Logistic Regression (baseline)
- Random Forest
- Gradient Boosting (XGBoost, LightGBM)
- Neural Networks

**Handling Class Imbalance**:
- SMOTE (Synthetic Minority Over-sampling)
- Class weights adjustment
- Stratified cross-validation

### 4. Model Evaluation
Key metrics:
- **AUC-ROC**: Overall discrimination ability
- **Precision & Recall**: Balance false positives/negatives
- **F1-Score**: Harmonic mean
- **Business Impact**: Cost-benefit analysis of interventions

### 5. Model Interpretability
- **SHAP Values**: Feature importance and contribution
- **LIME**: Local instance explanations
- **Feature Importance**: Top drivers of attrition

## 📈 Expected Results

### Key Insights
Analysis will reveal:
- Most influential attrition factors (e.g., salary, work-life balance, career growth)
- High-risk employee profiles
- Department-specific patterns
- Early warning indicators

### Recommendations
Actionable strategies such as:
- Targeted retention programs for high-risk groups
- Compensation adjustments
- Career development pathways
- Work-life balance improvements

## 🛡️ Ethics & Compliance

### Ethical Framework (EU AI Guidelines)

This project adheres to the **7 Requirements for Trustworthy AI**:

#### 1. Human Autonomy
- Predictions inform decisions, not replace human judgment
- Employees maintain agency over career choices
- Management retains final decision-making authority

#### 2. Technical Robustness
- Model validation on holdout test sets
- Regular retraining on updated data
- Monitoring for concept drift

#### 3. Privacy & Data Governance
- Fully anonymized employee data (EmployeeID pseudonyms)
- No personally identifiable information (PII)
- Secure data storage and access controls
- GDPR compliance considerations

#### 4. Transparency
- Model interpretability (SHAP/LIME)
- Clear documentation of methodology
- Open communication with stakeholders

#### 5. Fairness & Non-Discrimination
- Bias testing across demographics (age, gender, education)
- Fairness metrics (demographic parity, equalized odds)
- Mitigation strategies for identified biases

#### 6. Societal Well-being
- Focus on employee retention, not replacement
- Promote positive work environment improvements
- Environmental impact: reduced recruitment footprint

#### 7. Accountability
- Clear ownership of model decisions
- Regular audits and performance reviews
- Feedback mechanisms for continuous improvement

### Vigilance Points
- **Avoid discriminatory predictions** based on protected attributes
- **Prevent self-fulfilling prophecies** (model affecting behavior)
- **Ensure data representativeness** across all employee segments
- **Monitor unintended consequences** of retention interventions

## 📚 Bibliography Structure

### Methodological References
- Machine learning techniques for imbalanced classification
- Feature engineering best practices
- Time series analysis for workforce data

### Technical References
- Scikit-learn, XGBoost, SHAP documentation
- Research papers on employee attrition modeling

### Ethical & Societal References
- EU Ethics Guidelines for Trustworthy AI
- GDPR compliance for HR analytics
- Fairness in machine learning literature

### Domain-Specific References
- HR analytics case studies
- Pharmaceutical industry retention strategies
- Organizational psychology research

## 📊 Deliverables

### 1. Ethics Assessment Document
Comprehensive analysis of ethical considerations covering:
- Data privacy and anonymization
- Bias detection and mitigation
- Transparency and interpretability
- Societal impact assessment

### 2. Bibliography
Annotated list of academic and technical references with:
- Source classification by theme
- Justification for inclusion
- Copyright compliance verification

### 3. Jupyter Notebook
Complete analysis pipeline including:
- Data preprocessing and EDA
- Feature engineering process
- Model training and comparison
- Results interpretation
- Final recommendations

### 4. Final Presentation (20 minutes)
Results-oriented presentation covering:
- Dataset generation and preprocessing
- Algorithm selection rationale
- Performance metrics and analysis
- Model improvement iterations
- Final model selection justification
- Business recommendations

## 🎯 Success Metrics

- **Model Performance**: AUC-ROC > 0.80
- **Business Impact**: Projected reduction in turnover costs
- **Actionable Insights**: Clear recommendations accepted by management
- **Ethical Compliance**: Pass all 7 EU AI guideline requirements

## 👥 Team & Contributions

*Add your team members and their roles here*

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- HumanForYou HR Department for providing anonymized data
- Original Kaggle dataset contributors
- European Commission for AI Ethics Guidelines

## 📞 Contact

For questions or collaboration opportunities, please open an issue or contact the project team.

---

**⚠️ Disclaimer**: This is an educational AI project. All employee data is anonymized and used solely for analytical purposes to improve workplace satisfaction and retention.
