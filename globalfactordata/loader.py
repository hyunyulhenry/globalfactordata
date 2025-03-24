from pathlib import Path
import pickle
import pandas as pd

# 현재 파일 기준 data 폴더 경로
DATA_DIR = Path(__file__).resolve().parent / "data"

def load_data_url() -> dict:
    """data_url.pkl 파일을 불러옵니다."""
    path = DATA_DIR / "data_url.pkl"
    with open(path, "rb") as f:
        return pickle.load(f)

def get_country_classification() -> pd.DataFrame:
    """국가명과 지역 구분 정보를 불러옵니다."""
    path = DATA_DIR / "Country Classification.xlsx"
    return pd.read_excel(path)

def get_factor_details() -> pd.DataFrame:
    """각종 팩터의 상세내용을 불러옵니다."""
    path = DATA_DIR / "Factor Details.xlsx"
    return pd.read_excel(path)

def get_factor_cluster() -> pd.DataFrame:
    """153개 팩터의 테마 클러스터링 정보를 불러옵니다."""
    path = DATA_DIR / "Cluster Labels.csv"
    return pd.read_csv(path)
