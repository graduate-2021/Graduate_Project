# Da, GO! Shopping Mall
- Project 진행 과정과 추천, 데이터 결과에 대한 자료는 README.pdf를 읽어주세요
- Da, GO! Shopping Mall
  - http://54.180.154.189:8000/
- Data : Amazon Electronics Data
  - https://nijianmo.github.io/amazon/index.html
---
## Environment
    Python : 3.8.10
    Pandas : 1.2.4
    tqdm : 4.62.1
    Scikit-learn : 0.24.2
    Django : 3.2.5
    Scipy : 1.6.2
---
## Preprocessing
#### main.py
  Preprocessing 폴더 안에서 ```python3 main.py```을 실행하면 전처리를 할 수 있다. 이 때 ```data_dir, result_dir, year```을 옵션으로 줄 수 있다. ```python3 main.py```는 ```python3 main.py --data_dir=../data --result_dir=../data --year=2018```과 동일하다. data_dir은 Electronics.json과 meta_Electronics.json이 있는 Directory의 경로이며 result_dir는 정제된 Data가 담길 경로이다. 당신의 환경에 맞게 변경하면 된다. 실행하면 Data에 대한 전처리 파일을 얻을 수 있다. 
_(모듈화 작업 계속 진행 중)_
#### get_review_by_year
  ```python3 get_review_by_year.py```는 ```python3 get_review_by_year.py --data_dir=../data --result_dir=../data --year=2018```과 동일하다. 실행하면 현재 설정한 값에 따른 정제된 ```review_{설정한 연도}.json```을 얻을 수 있다.
