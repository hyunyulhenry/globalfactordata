from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import time
import os
import pickle

def get_download_links_from_dropbox(url: str, max_scrolls: int = 50) -> pd.DataFrame:
    """Dropbox 폴더 URL에서 .csv 파일명과 다운로드 링크를 추출해 DataFrame으로 반환"""

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,8000')

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(3)  # 페이지 초기 로딩 대기

    # 스크롤 끝까지 내리기
    def scroll_to_bottom():
        last_height = driver.execute_script("return document.body.scrollHeight")
        for _ in range(max_scrolls):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    scroll_to_bottom()

    rows = driver.find_elements(By.XPATH, '//div[@role="row"]')
    data = []

    for row in rows:
        try:
            if ".csv" in row.text:
                filename = next(line for line in row.text.split('\n') if line.endswith('.csv'))
                link_el = row.find_element(By.XPATH, './/a[contains(@href, ".csv")]')
                href = link_el.get_attribute("href")
                data.append({
                    "name": filename.replace('.csv', ''),
                    "link": href.replace("dl=0", "dl=1")
                })
        except:
            continue

    driver.quit()
    return pd.DataFrame(data)


# Dropbox 링크 모음

dropbox_urls = {
    "meta": "https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AN9kkos5H5UjjXUOqW3EuDs?dl=0&rlkey=i3wkvrjbadft6hld863571dol",
    "factor_monthly": "https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AHmASi3ogroo4kZaPmEWx4g/Country%20Factors?dl=0&rlkey=i3wkvrjbadft6hld863571dol&subfolder_nav_tracking=1",
    "factor_daily": "https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AHWDwl1wiNbgTji4Op5T4AI/Country%20Factors%20Daily?dl=0&rlkey=i3wkvrjbadft6hld863571dol&subfolder_nav_tracking=1",
    "regional_cluster_monthly": "https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AFli1Og0HAhy8CC27IT4fEs/Regional%20Clusters?rlkey=i3wkvrjbadft6hld863571dol&subfolder_nav_tracking=1&dl=0",
    "regional_cluster_daily": "https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AOvoCWhIjSNMpCbtos6mK0k/Regional%20Clusters%20Daily?dl=0&rlkey=i3wkvrjbadft6hld863571dol&subfolder_nav_tracking=1",
    "regional_factor_monthly": "https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AOQyJMkibR1UKjaYwQb20Wk/Regional%20Factors?dl=0&rlkey=i3wkvrjbadft6hld863571dol&subfolder_nav_tracking=1",
    "regional_factor_daily": "https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AOQyJMkibR1UKjaYwQb20Wk/Regional%20Factors?dl=0&rlkey=i3wkvrjbadft6hld863571dol&subfolder_nav_tracking=1"
}

# 실행 결과 저장
dict_info = {}

for key, url in dropbox_urls.items():
    print(f"[+] Fetching: {key}")
    dict_info[key] = get_download_links_from_dropbox(url)

# meta 정보를 monthly / daily로 구분
dict_info['meta_monthly'] = dict_info['meta'][~dict_info['meta']['name'].str.contains('daily', case=False)]
dict_info['meta_daily'] = dict_info['meta'][dict_info['meta']['name'].str.contains('daily', case=False)]
dict_info['meta_daily']['name'] = dict_info['meta_daily']['name'].str.replace('_daily', '', case=False, regex=False)

del dict_info['meta']

# 저장 경로 설정
save_path = os.path.join(os.getcwd(),"globalfactordata",  "data", "data_url.pkl")

# dict_info 저장
with open(save_path, "wb") as f:
    pickle.dump(dict_info, f)