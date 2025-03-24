import os
import pickle
import pandas as pd
from .loader import load_data_url

data_url = load_data_url()

# 공통 로딩 함수
def get_csv_from_dict(df: pd.DataFrame, file_name: str) -> pd.DataFrame:
    row = df[df["name"] == file_name]
    if row.empty:
        raise ValueError(f"'{file_name}' 항목이 존재하지 않습니다.")
    url = row.iloc[0]["link"]
    return pd.read_csv(url)

# 각 함수 정의
def get_market_returns(freq: str = "monthly") -> pd.DataFrame:
    return get_csv_from_dict(data_url[f"meta_{freq}"], "market_returns")

def get_gics() -> pd.DataFrame:
    return get_csv_from_dict(data_url["meta_monthly"], "industry_gics")

def get_cmp() -> pd.DataFrame:
    return get_csv_from_dict(data_url["meta_monthly"], "cmp")

def get_factor_all(method: str = "lms") -> pd.DataFrame:
    if method not in ["lms", "hml", "pfs"]:
        raise ValueError("method는 'lms', 'hml', 'pfs' 중 하나여야 합니다.")
    return get_csv_from_dict(data_url["meta_monthly"], method)

def get_cluster_all(freq: str = "monthly") -> pd.DataFrame:
    return get_csv_from_dict(data_url[f"meta_{freq}"], "clusters")

def get_factor(category: str = 'country', name: str = 'USA', freq: str = "monthly") -> pd.DataFrame:
    key = "factor" if category == "country" else "regional_factor"
    return get_csv_from_dict(data_url[f"{key}_{freq}"], name)

def get_cluster(name: str = 'World', freq: str = "monthly") -> pd.DataFrame:
    return get_csv_from_dict(data_url[f"regional_cluster_{freq}"], name)
