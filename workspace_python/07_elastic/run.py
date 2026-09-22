

# dotenv 사용법
from dotenv import load_dotenv
load_dotenv()

import os
key1 = os.getenv('key1')
key2 = os.getenv('key2')
key3 = os.getenv('key3')

print('key1 : ', key1)
print('key2 : ', key2)
print('key3 : ', key3)

from config import ELASTIC_ENDPOINT, ELASTIC_API_KEY
from elasticsearch import Elasticsearch

es = Elasticsearch(
    ELASTIC_ENDPOINT, # 쉽게 말해 DB 연결 주소
    api_key = ELASTIC_API_KEY # 쉽게 말해 DB 계정
)

connected = es.ping()
print('엘라스틱서치 연결 상태 : ', connected)

# 파일 읽기
from pathlib import Path # 경로 관련 라이브러리
print('__file__', __file__)

# __file__ : 현재 실행한 파일의 전체 경로
print(Path(__file__).resolve().parents[2])
print(Path(__file__).resolve().parents[1])
print(Path(__file__).resolve().parents[0])

BASE_DIR = Path(__file__).resolve().parents[0]
DOCUMENT_FILE = BASE_DIR / 'data' / 'data.json' # 경로 합치기
# Path에서는 / 가 더하기 역할을 한다.

import json
def load_documents():
    result = {}
    try : # 혹시 파일이 없을까봐
        with open(DOCUMENT_FILE, 'r', encoding='utf-8') as file:
            # print(file) 포장지만 나왔다.
            
            # json을 딕셔너리로 변환
            result = json.load(file)
            # 참고로 딕셔너리를 json으로 변환 하려면 json.dump()
            # print(d)
    except Exception as e :
        print('open 하다가 오류 발생 : ', e)
        
    return result
    
# 엘라스틱서치의 특징

# 모든 요청은 REST API를 사용한다.
# 즉 주소기반으로 CRUD한다.

# 엘라스틱서치 Vs RDBMS
# index : table
# document : 줄, row, record, 튜플
# field : column
# mapping : int, varchar 등의 타입

#########################
# index 생성(table 생성)
#########################
def create_index():
    
    if es.indices.exists(index='computer'):
        print('computer index가 이미 존재합니다.')
        return
    
    es.indices.create(
        index='computer',
        mappings={
            'properties': {
                'id': {'type': 'integer'},
                'title': {'type': 'text'}, # 유연한 값 : 백터로 분석해서 유연한 검색이 가능하다
                'category': {'type': 'keyword'}, # 정확한 값 : 딱 완전 똑같은 단어로 검색이 가능하다
                'price': {'type': 'integer'},
                'rating': {'type': 'float'},
                'created_at': {'type': 'date'},
                'content': {'type': 'text'}
            }
        }
    )
    print('index 생성 완료')
    
# create_index()

# insert할 건데
# insert 대신 수집한다 뜻의 ingest를 한 번 써봤다.
from elasticsearch import helpers
def ingest_documents():
    documents = load_documents()
    
    actions = []
    for doc in documents :
        actions.append({
            '_index': 'computer',
            '_id': doc['id'], # '_id': doc.get('id', None),
            '_source' : doc
        })
    
    success, errors = helpers.bulk(es, actions, stats_only=False)
    print('success', success)
    print('errors', len(errors), errors)
    
ingest_documents()

