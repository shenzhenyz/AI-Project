"""
Data preprocessing utilities for employee turnover analysis.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.impute import SimpleImputer


def handle_missing_values(df, strategy='median'):
    """
    Handle missing values in the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    strategy : str
        Imputation strategy ('mean', 'median', 'most_frequent', 'constant')
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with imputed values
    """
    df_clean = df.copy()
    
    # Handle 'NA' strings in survey data
    survey_cols = ['EnvironmentSatisfaction', 'JobSatisfaction', 'WorkLifeBalance']
    for col in survey_cols:
        if col in df_clean.columns:
            df_clean[col] = df_clean[col].replace('NA', np.nan)
            df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce')
    
    # Separate numeric and categorical columns
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df_clean.select_dtypes(include=['object']).columns.tolist()
    
    # Remove EmployeeID from processing
    if 'EmployeeID' in numeric_cols:
        numeric_cols.remove('EmployeeID')
    
    # Impute numeric columns
    if numeric_cols:
        numeric_imputer = SimpleImputer(strategy=strategy)
        df_clean[numeric_cols] = numeric_imputer.fit_transform(df_clean[numeric_cols])
    
    # Impute categorical columns with mode
    if categorical_cols:
        categorical_imputer = SimpleImputer(strategy='most_frequent')
        df_clean[categorical_cols] = categorical_imputer.fit_transform(df_clean[categorical_cols])
    
    return df_clean


def encode_categorical_variables(df, target_col='Attrition'):
    """
    Encode categorical variables.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    target_col : str
        Name of target variable column
        
    Returns:
    --------
    pd.DataFrame, dict
        Encoded dataframe and label encoders dictionary
    """
    df_encoded = df.copy()
    encoders = {}
    
    # Identify categorical columns (excluding target if it exists)
    categorical_cols = df_encoded.select_dtypes(include=['object']).columns.tolist()
    if target_col in categorical_cols:
        categorical_cols.remove(target_col)
    
    # Encode each categorical column
    for col in categorical_cols:
        le = LabelEncoder()
        df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
        encoders[col] = le
    
    # Encode target variable separately if it exists
    if target_col in df_encoded.columns:
        le_target = LabelEncoder()
        df_encoded[target_col] = le_target.fit_transform(df_encoded[target_col])
        encoders[target_col] = le_target
    
    return df_encoded, encoders


def create_features(df):
    """
    Create additional features from existing data.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with new features
    """
    df_feat = df.copy()
    
    # Salary-related features
    if 'MonthlyIncome' in df_feat.columns and 'PercentSalaryHike' in df_feat.columns:
        df_feat['SalaryHikeAmount'] = df_feat['MonthlyIncome'] * df_feat['PercentSalaryHike'] / 100
        df_feat['SalaryHikeRatio'] = df_feat['PercentSalaryHike'] / 100
    
    # Experience-related features
    if 'TotalWorkingYears' in df_feat.columns and 'YearsAtCompany' in df_feat.columns:
        df_feat['YearsBeforeCompany'] = df_feat['TotalWorkingYears'] - df_feat['YearsAtCompany']
        df_feat['CompanyTenureRatio'] = df_feat['YearsAtCompany'] / (df_feat['TotalWorkingYears'] + 1)
    
    # Promotion-related features
    if 'YearsSinceLastPromotion' in df_feat.columns and 'YearsAtCompany' in df_feat.columns:
        df_feat['PromotionFrequency'] = df_feat['YearsAtCompany'] / (df_feat['YearsSinceLastPromotion'] + 1)
        df_feat['RecentlyPromoted'] = (df_feat['YearsSinceLastPromotion'] <= 2).astype(int)
    
    # Manager relationship
    if 'YearsWithCurrentManager' in df_feat.columns and 'YearsAtCompany' in df_feat.columns:
        df_feat['ManagerStability'] = df_feat['YearsWithCurrentManager'] / (df_feat['YearsAtCompany'] + 1)
    
    # Job level and income
    if 'JobLevel' in df_feat.columns and 'MonthlyIncome' in df_feat.columns:
        df_feat['IncomePerLevel'] = df_feat['MonthlyIncome'] / df_feat['JobLevel']
    
    # Age and experience
    if 'Age' in df_feat.columns and 'TotalWorkingYears' in df_feat.columns:
        df_feat['CareerStartAge'] = df_feat['Age'] - df_feat['TotalWorkingYears']
    
    # Overtime indicator (if working hours > standard hours)
    if 'AvgWorkingHours' in df_feat.columns and 'StandardHours' in df_feat.columns:
        df_feat['OvertimeHours'] = df_feat['AvgWorkingHours'] - df_feat['StandardHours']
        df_feat['HasOvertime'] = (df_feat['OvertimeHours'] > 0).astype(int)
    
    return df_feat


def prepare_features_for_modeling(df, target_col='Attrition', drop_cols=None):
    """
    Prepare final feature set for modeling.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    target_col : str
        Name of target variable
    drop_cols : list, optional
        Columns to drop (e.g., EmployeeID, EmployeeCount, Over18)
        
    Returns:
    --------
    pd.DataFrame, pd.Series
        Features (X) and target (y)
    """
    if drop_cols is None:
        drop_cols = ['EmployeeID', 'EmployeeCount', 'Over18', 'StandardHours']
    
    # Remove columns that don't provide information
    cols_to_drop = [col for col in drop_cols if col in df.columns]
    X = df.drop(columns=cols_to_drop + [target_col] if target_col in df.columns else cols_to_drop)
    
    # Extract target if it exists
    if target_col in df.columns:
        y = df[target_col]
    else:
        y = None
    
    return X, y


def scale_features(X_train, X_test=None):
    """
    Scale features using StandardScaler.
    
    Parameters:
    -----------
    X_train : pd.DataFrame
        Training features
    X_test : pd.DataFrame, optional
        Test features
        
    Returns:
    --------
    np.ndarray, np.ndarray, StandardScaler
        Scaled training features, scaled test features (if provided), and scaler
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    
    if X_test is not None:
        X_test_scaled = scaler.transform(X_test)
        return X_train_scaled, X_test_scaled, scaler
    
    return X_train_scaled, scaler

