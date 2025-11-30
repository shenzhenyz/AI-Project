# AI Project - Bibliography
## HumanForYou Employee Turnover Analysis

This document presents the academic and technical references used to guide our work on the HumanForYou employee turnover analysis project. Sources are organized by theme and include brief annotations explaining their relevance and contribution to the project.

---

## Methodological and Theoretical Sources

### Employee Turnover Theory

1. **Mobley, W. H. (1977). Intermediate linkages in the relationship between job satisfaction and employee turnover. *Journal of Applied Psychology*, 62(2), 237-240.**
   - **Relevance**: Foundational theory on the relationship between job satisfaction and turnover
   - **Contribution**: Guided our focus on job satisfaction as a key predictor variable
   - **Impact**: Informed feature selection and interpretation of results

2. **Griffeth, R. W., Hom, P. W., & Gaertner, S. (2000). A meta-analysis of antecedents and correlates of employee turnover: Update, moderator tests, and research implications for the next millennium. *Journal of Management*, 26(3), 463-488.**
   - **Relevance**: Comprehensive meta-analysis of turnover predictors
   - **Contribution**: Validated our selection of predictor variables (compensation, job satisfaction, organizational commitment)
   - **Impact**: Provided theoretical foundation for feature engineering

3. **Holtom, B. C., Mitchell, T. R., Lee, T. W., & Eberly, M. B. (2008). Turnover and retention research: A glance at the past, a closer review of the present, and a venture into the future. *The Academy of Management Annals*, 2(1), 231-274.**
   - **Relevance**: Review of turnover research methodologies
   - **Contribution**: Informed our methodological approach and model selection
   - **Impact**: Helped justify use of predictive modeling for turnover analysis

### Predictive Modeling in HR Analytics

4. **Fitz-enz, J. (2009). *The ROI of Human Capital: Measuring the Economic Value of Employee Performance* (2nd ed.). AMACOM.**
   - **Relevance**: Framework for measuring HR metrics and ROI
   - **Contribution**: Guided our approach to quantifying turnover costs and intervention effectiveness
   - **Impact**: Informed business case for retention initiatives

5. **Rasmussen, T., & Ulrich, D. (2015). Learning from practice: How HR analytics avoids being a management fad. *Organizational Dynamics*, 44(3), 236-242.**
   - **Relevance**: Best practices in HR analytics implementation
   - **Contribution**: Informed our methodology for model deployment and stakeholder communication
   - **Impact**: Guided presentation of results and recommendations

---

## Sources on Technical Aspects

### Machine Learning for Classification

6. **Breiman, L. (2001). Random forests. *Machine Learning*, 45(1), 5-32.**
   - **Relevance**: Theoretical foundation for Random Forest algorithm
   - **Contribution**: Justified use of Random Forest for handling mixed data types and feature importance
   - **Impact**: Selected Random Forest as one of our primary models

7. **Chen, T., & Guestrin, C. (2016). XGBoost: A scalable tree boosting system. *Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining*, 785-794.**
   - **Relevance**: XGBoost algorithm for gradient boosting
   - **Contribution**: Provided high-performance model option for comparison
   - **Impact**: Included XGBoost in model comparison

8. **Ke, G., Meng, Q., Finley, T., Wang, T., Chen, W., Ma, W., ... & Liu, T. Y. (2017). LightGBM: A highly efficient gradient boosting decision tree. *Advances in Neural Information Processing Systems*, 30.**
   - **Relevance**: LightGBM algorithm for efficient gradient boosting
   - **Contribution**: Provided fast and accurate model option
   - **Impact**: Included LightGBM in model comparison

### Handling Imbalanced Data

9. **Chawla, N. V., Bowyer, K. W., Hall, L. O., & Kegelmeyer, W. P. (2002). SMOTE: Synthetic minority over-sampling technique. *Journal of Artificial Intelligence Research*, 16, 321-357.**
   - **Relevance**: SMOTE algorithm for handling class imbalance
   - **Contribution**: Justified use of SMOTE to address imbalanced attrition data
   - **Impact**: Implemented SMOTE in preprocessing pipeline

10. **He, H., & Garcia, E. A. (2009). Learning from imbalanced data. *IEEE Transactions on Knowledge and Data Engineering*, 21(9), 1263-1284.**
    - **Relevance**: Comprehensive review of techniques for imbalanced classification
    - **Contribution**: Informed our approach to handling class imbalance and metric selection
    - **Impact**: Guided choice of evaluation metrics (ROC-AUC, Precision-Recall)

### Model Interpretation

11. **Lundberg, S. M., & Lee, S. I. (2017). A unified approach to interpreting model predictions. *Advances in Neural Information Processing Systems*, 30.**
    - **Relevance**: SHAP (SHapley Additive exPlanations) values for model interpretation
    - **Contribution**: Enabled explainable AI and feature importance analysis
    - **Impact**: Implemented SHAP values for model interpretation

12. **Molnar, C. (2020). *Interpretable Machine Learning: A Guide for Making Black Box Models Explainable*. Lulu.com.**
    - **Relevance**: Comprehensive guide to interpretable machine learning
    - **Contribution**: Informed our approach to model explainability and transparency
    - **Impact**: Guided feature importance analysis and model documentation

### Feature Engineering

13. **Zheng, A., & Casari, A. (2018). *Feature Engineering for Machine Learning: Principles and Techniques for Data Scientists*. O'Reilly Media.**
    - **Relevance**: Best practices for feature engineering
    - **Contribution**: Guided creation of derived features (e.g., promotion frequency, tenure ratios)
    - **Impact**: Informed feature engineering section of preprocessing

---

## Ethical and Societal Sources

### AI Ethics and Fairness

14. **European Commission. (2019). *Ethics Guidelines for Trustworthy AI*. European Commission.**
    - **Relevance**: Official guidelines for ethical AI development
    - **Contribution**: Framework for our ethics document (seven requirements)
    - **Impact**: Structured entire ethics approach and documentation

15. **Barocas, S., Hardt, M., & Narayanan, A. (2019). *Fairness and Machine Learning*. fairmlbook.org.**
    - **Relevance**: Comprehensive treatment of fairness in machine learning
    - **Contribution**: Informed our approach to bias detection and fairness metrics
    - **Impact**: Guided fairness analysis and protected attribute handling

16. **Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K., & Galstyan, A. (2021). A survey on bias and fairness in machine learning. *ACM Computing Surveys*, 54(6), 1-35.**
    - **Relevance**: Survey of bias and fairness in ML
    - **Contribution**: Informed our bias detection and mitigation strategies
    - **Impact**: Guided fairness evaluation procedures

### Privacy and Data Protection

17. **Voigt, P., & Von dem Bussche, A. (2017). *The EU General Data Protection Regulation (GDPR): A Practical Guide*. Springer.**
    - **Relevance**: Guide to GDPR compliance
    - **Contribution**: Informed our data privacy and governance approach
    - **Impact**: Guided data minimization and anonymization practices

18. **Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science*, 9(3-4), 211-407.**
    - **Relevance**: Theoretical foundation for privacy-preserving analytics
    - **Contribution**: Informed our understanding of privacy risks
    - **Impact**: Guided data handling and anonymization decisions

### HR Analytics Ethics

19. **Tambe, P., Cappelli, P., & Yakubovich, V. (2019). Artificial intelligence in human resources management: Challenges and a path forward. *California Management Review*, 61(4), 15-42.**
    - **Relevance**: Ethical considerations in HR AI applications
    - **Contribution**: Informed our approach to employee autonomy and transparency
    - **Impact**: Guided ethics document development

20. **Bogen, M., & Rieke, A. (2018). Help wanted: An examination of hiring algorithms, equity, and bias. *Upturn*.**
    - **Relevance**: Case studies of bias in HR algorithms
    - **Contribution**: Highlighted risks and informed our bias mitigation approach
    - **Impact**: Emphasized importance of fairness monitoring

---

## Project-Specific Sources

### HR Analytics Case Studies

21. **Kaggle. (2020). *HR Analytics Case Study*. https://www.kaggle.com/vjchoudhary7/hr-analytics-case-study**
    - **Relevance**: Source dataset for this project
    - **Contribution**: Provided the anonymized employee data
    - **Impact**: Foundation for all analysis
    - **Note**: Dataset is publicly available and properly cited

22. **IBM. (2019). *The Value of Training: How Organizations Are Closing the Skills Gap*. IBM Institute for Business Value.**
    - **Relevance**: Industry report on employee development
    - **Contribution**: Supported our recommendations on training and career development
    - **Impact**: Informed recommendations section

### Employee Retention Best Practices

23. **Bersin, J. (2013). *Predictive Analytics in Human Resources: A Primer*. Bersin by Deloitte.**
    - **Relevance**: Industry best practices for HR predictive analytics
    - **Contribution**: Informed our methodology and presentation approach
    - **Impact**: Guided model deployment recommendations

24. **Davenport, T. H., Harris, J., & Shapiro, J. (2010). Competing on talent analytics. *Harvard Business Review*, 88(10), 52-58.**
    - **Relevance**: Strategic approach to talent analytics
    - **Contribution**: Informed our business case and recommendations
    - **Impact**: Guided presentation of value proposition

### Statistical Methods

25. **Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning: Data Mining, Inference, and Prediction* (2nd ed.). Springer.**
    - **Relevance**: Comprehensive textbook on statistical learning
    - **Contribution**: Theoretical foundation for model selection and evaluation
    - **Impact**: Informed cross-validation and model comparison approaches

26. **James, G., Witten, D., Hastie, T., & Tibshirani, R. (2013). *An Introduction to Statistical Learning: with Applications in R*. Springer.**
    - **Relevance**: Accessible introduction to statistical learning
    - **Contribution**: Guided our approach to model evaluation and interpretation
    - **Impact**: Informed metric selection and model comparison

---

## Technical Documentation and Tools

### Python Libraries

27. **McKinney, W. (2010). Data structures for statistical computing in python. *Proceedings of the 9th Python in Science Conference*, 445, 51-56.**
    - **Relevance**: Pandas library documentation
    - **Contribution**: Primary tool for data manipulation
    - **Impact**: Used throughout data preprocessing and analysis

28. **Pedregosa, F., et al. (2011). Scikit-learn: Machine learning in Python. *Journal of Machine Learning Research*, 12, 2825-2830.**
    - **Relevance**: Scikit-learn library documentation
    - **Contribution**: Primary ML library for model development
    - **Impact**: Used for all model training and evaluation

29. **Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90-95.**
    - **Relevance**: Matplotlib library documentation
    - **Contribution**: Visualization tool
    - **Impact**: Used for all plots and visualizations

30. **Waskom, M. L. (2021). seaborn: statistical data visualization. *Journal of Open Source Software*, 6(60), 3021.**
    - **Relevance**: Seaborn library documentation
    - **Contribution**: Statistical visualization tool
    - **Impact**: Used for exploratory data analysis visualizations

---

## Copyright and Publication Licenses

All sources cited in this bibliography are used in accordance with their respective copyright and publication licenses:

- **Academic Papers**: Used under fair use for research and educational purposes, with proper citation
- **Books**: Used under fair use for research purposes, with proper citation
- **Open Source Software**: Used under their respective open source licenses (BSD, MIT, Apache, etc.)
- **Kaggle Dataset**: Used in accordance with Kaggle's terms of service and dataset license
- **Industry Reports**: Used under fair use for research purposes, with proper citation

All sources are properly cited using standard academic citation formats. No copyrighted material has been reproduced without permission.

---

## Annotation Summary

### Most Impactful Sources

1. **European Commission Ethics Guidelines**: Structured our entire ethical approach
2. **Mobley (1977) & Griffeth et al. (2000)**: Provided theoretical foundation for variable selection
3. **Chawla et al. (2002) SMOTE**: Critical for handling imbalanced data
4. **Lundberg & Lee (2017) SHAP**: Enabled model interpretability
5. **Barocas et al. (2019) Fairness Book**: Guided fairness analysis

### Source Categories

- **Theoretical Foundation**: 5 sources
- **Technical Implementation**: 10 sources
- **Ethics and Fairness**: 6 sources
- **Project-Specific**: 4 sources
- **Tools and Documentation**: 5 sources

---

**Document Version:** 1.0  
**Last Updated:** [Date]  
**Total Sources:** 30

