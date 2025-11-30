"""
Data loading utilities for HumanForYou employee turnover analysis.
"""

import pandas as pd
import numpy as np
import zipfile
import os
from pathlib import Path


def load_general_data(data_path='data/general_data.csv'):
    """
    Load the general HR data.
    
    Parameters:
    -----------
    data_path : str
        Path to the general_data.csv file
        
    Returns:
    --------
    pd.DataFrame
        Loaded general data
    """
    df = pd.read_csv(data_path)
    print(f"Loaded general_data.csv: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def load_manager_survey(data_path='data/manager_survey_data.csv'):
    """
    Load manager survey data.
    
    Parameters:
    -----------
    data_path : str
        Path to the manager_survey_data.csv file
        
    Returns:
    --------
    pd.DataFrame
        Loaded manager survey data
    """
    df = pd.read_csv(data_path)
    print(f"Loaded manager_survey_data.csv: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def load_employee_survey(data_path='data/employee_survey_data.csv'):
    """
    Load employee survey data.
    
    Parameters:
    -----------
    data_path : str
        Path to the employee_survey_data.csv file
        
    Returns:
    --------
    pd.DataFrame
        Loaded employee survey data
    """
    df = pd.read_csv(data_path)
    print(f"Loaded employee_survey_data.csv: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def load_working_hours_data(zip_path='data/in_out_time.zip', in_time_path=None, out_time_path=None):
    """
    Load working hours data from ZIP file or individual CSV files.
    
    Parameters:
    -----------
    zip_path : str, optional
        Path to the in_out_time.zip file
    in_time_path : str, optional
        Path to in_time.csv file (if not in ZIP)
    out_time_path : str, optional
        Path to out_time.csv file (if not in ZIP)
        
    Returns:
    --------
    tuple
        (in_time_df, out_time_df) DataFrames with arrival and departure times
    """
    in_time_df = None
    out_time_df = None
    
    # Try loading from individual CSV files first
    if in_time_path and out_time_path:
        try:
            # Read CSV files - first column is EmployeeID (may have empty header)
            in_time_df = pd.read_csv(in_time_path)
            out_time_df = pd.read_csv(out_time_path)
            
            # Fix EmployeeID column if it has empty name
            if in_time_df.columns[0] == '' or in_time_df.columns[0].startswith('Unnamed'):
                in_time_df.rename(columns={in_time_df.columns[0]: 'EmployeeID'}, inplace=True)
            if out_time_df.columns[0] == '' or out_time_df.columns[0].startswith('Unnamed'):
                out_time_df.rename(columns={out_time_df.columns[0]: 'EmployeeID'}, inplace=True)
            
            # Convert EmployeeID to int if it's a string
            if in_time_df['EmployeeID'].dtype == 'object':
                in_time_df['EmployeeID'] = in_time_df['EmployeeID'].astype(str).str.strip('"').astype(int)
            if out_time_df['EmployeeID'].dtype == 'object':
                out_time_df['EmployeeID'] = out_time_df['EmployeeID'].astype(str).str.strip('"').astype(int)
            
            print(f"Loaded in_time.csv: {in_time_df.shape}")
            print(f"Loaded out_time.csv: {out_time_df.shape}")
            return in_time_df, out_time_df
        except Exception as e:
            print(f"Could not load from CSV files: {e}")
            import traceback
            traceback.print_exc()
    
    # Try loading from ZIP file
    if zip_path and os.path.exists(zip_path):
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # List files in zip
                file_list = zip_ref.namelist()
                print(f"Files in ZIP: {file_list}")
                
                for file_name in file_list:
                    if 'in_time' in file_name.lower():
                        in_time_df = pd.read_csv(zip_ref.open(file_name))
                        print(f"Loaded {file_name}: {in_time_df.shape}")
                    elif 'out_time' in file_name.lower():
                        out_time_df = pd.read_csv(zip_ref.open(file_name))
                        print(f"Loaded {file_name}: {out_time_df.shape}")
        except Exception as e:
            print(f"Could not load from ZIP file: {e}")
    
    # Try default CSV file paths if nothing else worked
    if in_time_df is None or out_time_df is None:
        try:
            if os.path.exists('data/in_time.csv'):
                in_time_df = pd.read_csv('data/in_time.csv')
                if in_time_df.columns[0] == '' or in_time_df.columns[0].startswith('Unnamed'):
                    in_time_df.rename(columns={in_time_df.columns[0]: 'EmployeeID'}, inplace=True)
                if in_time_df['EmployeeID'].dtype == 'object':
                    in_time_df['EmployeeID'] = in_time_df['EmployeeID'].astype(str).str.strip('"').astype(int)
                print(f"Loaded data/in_time.csv: {in_time_df.shape}")
            if os.path.exists('data/out_time.csv'):
                out_time_df = pd.read_csv('data/out_time.csv')
                if out_time_df.columns[0] == '' or out_time_df.columns[0].startswith('Unnamed'):
                    out_time_df.rename(columns={out_time_df.columns[0]: 'EmployeeID'}, inplace=True)
                if out_time_df['EmployeeID'].dtype == 'object':
                    out_time_df['EmployeeID'] = out_time_df['EmployeeID'].astype(str).str.strip('"').astype(int)
                print(f"Loaded data/out_time.csv: {out_time_df.shape}")
        except Exception as e:
            print(f"Could not load default CSV files: {e}")
            import traceback
            traceback.print_exc()
    
    return in_time_df, out_time_df


def merge_all_data(general_df, manager_df, employee_df, in_time_df=None, out_time_df=None):
    """
    Merge all data sources on EmployeeID.
    
    Parameters:
    -----------
    general_df : pd.DataFrame
        General HR data
    manager_df : pd.DataFrame
        Manager survey data
    employee_df : pd.DataFrame
        Employee survey data
    in_time_df : pd.DataFrame, optional
        Arrival times data
    out_time_df : pd.DataFrame, optional
        Departure times data
        
    Returns:
    --------
    pd.DataFrame
        Merged dataset
    """
    # Start with general data
    merged_df = general_df.copy()
    
    # Merge manager survey
    merged_df = merged_df.merge(manager_df, on='EmployeeID', how='left')
    
    # Merge employee survey
    merged_df = merged_df.merge(employee_df, on='EmployeeID', how='left')
    
    # If working hours data is provided, merge it
    if in_time_df is not None and out_time_df is not None:
        # Process working hours data (calculate features)
        hours_features = process_working_hours(in_time_df, out_time_df)
        merged_df = merged_df.merge(hours_features, on='EmployeeID', how='left')
    
    print(f"Merged dataset shape: {merged_df.shape}")
    return merged_df


def process_working_hours(in_time_df, out_time_df):
    """
    Process working hours data to extract features.
    
    Parameters:
    -----------
    in_time_df : pd.DataFrame
        Arrival times
    out_time_df : pd.DataFrame
        Departure times
        
    Returns:
    --------
    pd.DataFrame
        Features derived from working hours
    """
    # Convert time columns to datetime
    time_cols = [col for col in in_time_df.columns if col != 'EmployeeID']
    
    # Calculate working hours per day
    working_hours_features = []
    
    for emp_id in in_time_df['EmployeeID']:
        emp_in = in_time_df[in_time_df['EmployeeID'] == emp_id].iloc[0]
        emp_out = out_time_df[out_time_df['EmployeeID'] == emp_id].iloc[0]
        
        daily_hours = []
        late_arrivals = 0
        early_departures = 0
        
        for col in time_cols:
            in_time = pd.to_datetime(emp_in[col], errors='coerce')
            out_time = pd.to_datetime(emp_out[col], errors='coerce')
            
            if pd.notna(in_time) and pd.notna(out_time):
                hours = (out_time - in_time).total_seconds() / 3600
                daily_hours.append(hours)
                
                # Check for late arrival (after 9:30 AM)
                if in_time.hour > 9 or (in_time.hour == 9 and in_time.minute > 30):
                    late_arrivals += 1
                
                # Check for early departure (before 5:30 PM)
                if out_time.hour < 17 or (out_time.hour == 17 and out_time.minute < 30):
                    early_departures += 1
        
        avg_hours = np.mean(daily_hours) if daily_hours else np.nan
        std_hours = np.std(daily_hours) if daily_hours else np.nan
        total_days = len(daily_hours)
        
        working_hours_features.append({
            'EmployeeID': emp_id,
            'AvgWorkingHours': avg_hours,
            'StdWorkingHours': std_hours,
            'TotalWorkingDays': total_days,
            'LateArrivals': late_arrivals,
            'EarlyDepartures': early_departures,
            'LateArrivalRate': late_arrivals / total_days if total_days > 0 else 0,
            'EarlyDepartureRate': early_departures / total_days if total_days > 0 else 0
        })
    
    return pd.DataFrame(working_hours_features)

