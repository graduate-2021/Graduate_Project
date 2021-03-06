## Preprocessing
#### main.py
Preprocessing 폴더 안에서 ```python3 main.py```을 실행하면 전처리를 할 수 있다. 이 때 ```data_dir, result_dir, year```을 옵션으로 줄 수 있다. ```python3 main.py```는 ```python3 main.py --data_dir=../data --result_dir=../data --year=2018```과 동일하다. data_dir은 Electronics.json과 meta_Electronics.json이 있는 Directory의 경로이며 result_dir는 정제된 Data가 담길 경로이다. 당신의 환경에 맞게 변경하면 된다. 실행하면 Data에 대한 전처리 파일을 얻을 수 있다. 
_(모듈화 작업 계속 진행 중)_
#### get_review_by_year
```python3 get_review_by_year.py```는 ```python3 get_review_by_year.py --data_dir=../data --result_dir=../data --year=2018```과 동일하다. 실행하면 현재 설정한 값에 따른 정제된 ```review_{설정한 연도}.json```을 얻을 수 있다.
#### get_meta_by_review
```python3 get_meta_by_review.py```는 ```python3 get_meta_by_review.py --data_dir=../data --result_dir=../data --review_file=review_2018```과 동일하다. 실행하면 현재 설정한 값에 따른 정제된 ```meta_{설정한 연도}.json```을 얻을 수 있다. 이 meta data는 get_review_by_year를 실행해 나온 review file에 해당하는 상품에 대한 Meta Data이다
#### extract_column
```python3 extract_column.py --filename={File name} --column={Column name}```을 통해(filename, column name 필수) 설정한 파일에서 원하는 Column의 값을 파일로 얻을 수 있다. 이렇게 얻은 파일은 후에 DB Table 구성 자료에 쓰이게 된다. ```python3 extract_column.py --data_dir=../data --result_dir=../data --filename={File name} --column={Column name}```과 동일하다.
#### split_category
```python3 split_category.py --data_dir={Data directory} --result_dir={Result Directory} --filename={File name}```을 통해 Category 파일에서 각각 얻은 대분류, 중분류, 소분류 파일을 얻을 수 있다. 이렇게 얻은 파일은 후에 DB Table 구성 자료에 쓰이게 된다. ```python3 split_category.py```과 ```python3 split_category.py --data_dir=../data --result_dir=../data --filename=category_2018``` 동일하다.
