from elasticsearch import Elasticsearch
from config import ELASTIC_ENDPOINT, ELASTIC_API_KEY, GEMINI_API_KEY
from pathlib import Path # 경로 관련 라이브러리
import json
from google import genai

# 엘라스틱서치를 클라우드에서 연결
es = Elasticsearch(
    ELASTIC_ENDPOINT, # 쉽게 말해 DB 연결 주소
    api_key = ELASTIC_API_KEY # 쉽게 말해 DB 계정
)

# gemini 연결
gemini = genai.Client(api_key=GEMINI_API_KEY)

def load_documents():
    result = {}
    # print('__file__', __file__)

    # __file__ : 현재 실행한 파일의 전체 경로
    # print(Path(__file__).resolve().parents[2])
    # print(Path(__file__).resolve().parents[1]) # 부모 폴더 몇 개 올라가는지
    # print(Path(__file__).resolve().parents[0])

    BASE_DIR = Path(__file__).resolve().parents[0]
    DOCUMENT_FILE = BASE_DIR / 'data' / 'data.json' # 경로 합치기
    # Path에서는 / 가 더하기 역할을 한다.
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





connected = es.ping()
print('엘라스틱서치 연결 상태 : ', connected)


def formatter(resp):
    results = []
    # 우리가 넣은 내용만 쏙 빼온다
    for hit in resp["hits"]["hits"]:
        document = hit.get("_source", {})

        results.append({"document": hit.get("_source", {}), "score": hit.get("_score")})

    return {"results": results, "total": resp["hits"]["total"]["value"]}




    


# #########################
# # index 생성(table 생성)
# #########################
# def create_index():
    
#     if es.indices.exists(index='computer'):
#         print('computer index가 이미 존재합니다.')
#         return
    
#     es.indices.create(
#         index='computer',
#         mappings={
#             'properties': {
#                 'id': {'type': 'integer'},
#                 'title': {'type': 'text'}, # 유연한 값 : 백터로 분석해서 유연한 검색이 가능하다
#                 'category': {'type': 'keyword'}, # 정확한 값 : 딱 완전 똑같은 단어로 검색이 가능하다
#                 'price': {'type': 'integer'},
#                 'rating': {'type': 'float'},
#                 'created_at': {'type': 'date'},
#                 'content': {'type': 'text'}
#             }
#         }
#     )
#     print('index 생성 완료')
    
# # create_index()

# # insert할 건데
# # insert 대신 수집한다 뜻의 ingest를 한 번 써봤다.
# def ingest_documents():
#     documents = load_documents()
    
#     actions = []
#     for doc in documents :
#         actions.append({
#             '_index': 'computer',
#             '_id': doc['id'], # '_id': doc.get('id', None),
#             '_source' : doc
#         })
    
#     success, errors = helpers.bulk(es, actions, stats_only=False)
#     print('success', success)
#     print('errors', len(errors), errors)
    
# ingest_documents()

