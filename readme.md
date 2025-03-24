# 🌍 Global Factor Data

본 패키지는 JKP의 글로벌 팩터 데이터를 쉽게 불러오는 Python 도구입니다.  
총 93개국, 13개 테마, 153개 팩터에 대한 시계열 데이터가 제공됩니다.

> 📚 **참고 논문**  
> Jensen, Theis Ingerslev, Bryan Kelly, and Lasse Heje Pedersen.  
> _Is there a replication crisis in finance?_, The Journal of Finance, 2023  
> 🔗 https://github.com/bkelly-lab/ReplicationCrisis

---

## 📁 데이터 출처

모든 데이터는 아래 Dropbox 폴더에서 제공되며,  
이 패키지는 해당 링크에서 데이터를 자동으로 받아옵니다.

📂 [Dropbox 링크](https://www.dropbox.com/scl/fo/zxha6i1zcjzx8a3mb2372/AN9kkos5H5UjjXUOqW3EuDs?rlkey=i3wkvrjbadft6hld863571dol&dl=0)

---

## 🔧 주요 함수

---

### 🟦 `get_market_returns(freq="monthly")`

모든 국가의 **시장 수익률**을 불러옵니다.

**Parameters**
- `freq` (`str`, optional): `"monthly"` 또는 `"daily"`

---

### 🟨 `get_gics()`

국가별 **GICS 섹터 수익률**을 불러옵니다.

---

### 🟩 `get_cmp()`

미국 내 **시가총액 그룹별** rank-weighted 특성 기반 포트폴리오 데이터를 제공합니다.

---

### 🟪 `get_factor_all(method="lms")`

모든 국가의 **팩터 수익률 데이터**를 불러옵니다.

**Parameters**
- `method` (`str`, optional):  
  - `"lms"`: 문헌에 부합하는 부호 규칙 기반 long-short 포트폴리오  
  - `"hml"`: 특성값 상/하위 포트폴리오 차이  
  - `"pfs"`: 특성값 기준 3개 포트폴리오 원본 데이터

⚠️ `daily` 데이터는 용량이 커서 Dropbox에서 직접 받는 것을 권장합니다.

---

### 🟥 `get_cluster_all(freq="monthly")`

모든 국가의 **클러스터(테마) 수익률**을 불러옵니다.

**Parameters**
- `freq` (`str`, optional): `"monthly"` 또는 `"daily"`

---

### 🟧 `get_factor(category="country", name="USA", freq="monthly")`

국가 또는 지역별 **팩터 수익률**을 불러옵니다.

**Parameters**
- `category` (`str`, optional): `"country"` 또는 `"region"`
- `name` (`str`): 국가명 또는 지역명
- `freq` (`str`, optional): `"monthly"` 또는 `"daily"`

🔍 사용 가능한 국가 및 지역명은 `get_country_classification()` 또는 업로드된 엑셀 파일 참고

---

### 🟫 `get_cluster(name="World", freq="monthly")`

각 지역의 **테마(클러스터) 수익률**을 불러옵니다.  
국가별 테마 수익률은 `get_cluster_all()`로 확인하세요.

**Parameters**
- `name` (`str`): 지역명
- `freq` (`str`, optional): `"monthly"` 또는 `"daily"`

---

## 📂 엑셀/메타 정보 불러오기

### 📄 `get_country_classification()`

국가명과 지역 구분 정보를 불러옵니다

---

### 📄 `get_factor_details()`

각종 팩터의 상세내용을 불러옵니다.

---

### 📄 `get_factor_cluster()`

153개 팩터의 테마 클러스터링 정보를 불러옵니다.

---

## 🙋‍♂️ 만든 사람

**Henry Lee**  
🔗 [linkedin.com/in/hyunyul-lee-34952096](https://www.linkedin.com/in/hyunyul-lee-34952096/)