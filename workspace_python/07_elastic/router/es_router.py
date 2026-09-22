from fastapi import APIRouter
# from elasticsearch import Elasticsearch, helpers
from elasticsearch import helpers
# from config import ELASTIC_ENDPOINT, ELASTIC_API_KEY
# import json
# from pathlib import Path  # 경로 관련 라이브러리
from util import es, load_documents, formatter


router = APIRouter(tags=["엘라스틱서치 관련 라우터"])

# es = Elasticsearch(
#     ELASTIC_ENDPOINT,  # 쉽게 말해 DB 연결 주소
#     api_key=ELASTIC_API_KEY,  # 쉽게 말해 DB 계정
# )


@router.get("/es/health")
def health():
    connected = es.ping()
    print("엘라스틱서치 연결 상태 : ", connected)
    return {
        "connected": connected,
        "msg": "Elasticsearch 연결 " + "성공" if connected else "실패",
    }


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


# insert는 아니지만
# 행동을 하는 것은 post가 어울린다.
@router.post("/es/create")
def create_index():
    result = {"msg": None}

    if es.indices.exists(index="computer"):
        print("computer index가 이미 존재합니다.")

        result["msg"] = "computer index가 이미 존재합니다."
        return result

    # indices는 index의 복수형 중에 하나
    es.indices.create(
        index="computer",
        mappings={
            "properties": {
                "id": {"type": "integer"},
                "title": {
                    "type": "text"
                },  # 유연한 값 : 백터로 분석해서 유연한 검색이 가능하다
                "category": {
                    "type": "keyword"
                },  # 정확한 값 : 딱 완전 똑같은 단어로 검색이 가능하다
                "price": {"type": "integer"},
                "rating": {"type": "float"},
                "created_at": {"type": "date"},
                "content": {"type": "text"},
            }
        },
    )
    print("index 생성 완료")
    result["msg"] = "index 생성 완료"
    return result


@router.post("/es/insert/bulk")
# insert할 건데
# insert 대신 수집한다 뜻의 ingest를 한 번 써봤다.
def ingest_documents():
    documents = load_documents()

    actions = []
    for doc in documents:
        actions.append(
            {
                "_index": "computer",
                "_id": doc["id"],  # '_id': doc.get('id', None),
                "_source": doc,
            }
        )

    success, errors = helpers.bulk(es, actions, stats_only=False)
    print("success", success)
    print("errors", len(errors), errors)

    return {"msg": {"success": success, "errors": errors}}


# print(Path(__file__).resolve().parents[2])
# print(Path(__file__).resolve().parents[1]) # 부모 폴더 경로
# print(Path(__file__).resolve().parents[0])

# def load_documents():
#     BASE_DIR = Path(__file__).resolve().parents[1]
#     DOCUMENT_FILE = BASE_DIR / "data" / "data.json"  # 경로 합치기
#     result = {}
#     try:  # 혹시 파일이 없을까봐
#         with open(DOCUMENT_FILE, "r", encoding="utf-8") as file:
#             # print(file) 포장지만 나왔다.

#             # json을 딕셔너리로 변환
#             result = json.load(file)
#             # 참고로 딕셔너리를 json으로 변환 하려면 json.dump()
#             # print(d)
#     except Exception as e:
#         print("open 하다가 오류 발생 : ", e)

#     return result


@router.get("/es/select/all")
def select_all():
    # 걍 전체 선택
    # select * from computer
    # response = es.search(
    #         index='computer',
    #         query={'match_all': {} }
    #     )

    # ORDER BY
    # select * from computer order by price desc
    # response = es.search(
    #     index='computer',
    #     query={'match_all': {} },
    #     sort=[
    #         {
    #             'category' : {
    #                 'order': 'asc'
    #             },
    #             'price':{
    #                 'order': 'desc'
    #             }
    #         }
    #     ]
    # )
    # print(response)
    # return response

    # limit, offset
    # '''
    #     select * from computer
    #     -- limit 5, 10 # 5개 건너뛰고 6번째부터 10개

    #     offset 5 # 5개 건너뛰고
    #     limit 10 # 10개
    # '''
    # response = es.search(
    #         index='computer',
    #         query={'match_all': {} },
    #         sort=[{'id' : {'order': 'asc'}}],
    #         from_ = 3, # 3개 건너뛰고
    #         size = 4   # 4개
    #     )

    # '''
    #         select * from computer
    #         -- limit 5, 10 # 5개 건너뛰고 6번째부터 10개

    #         offset 5 # 5개 건너뛰고
    #         limit 10 # 10개
    #     '''
    # response = es.search(
    #     index='computer',
    #     query={'match_all': {} },
    #     sort=[{'id' : {'order': 'asc'}}],
    #     from_ = 3, # 3개 건너뛰고
    #     size = 4   # 4개
    # )

    # GROUP BY
    # select category from computer
    # group by category
    # aggregation 집합
    response = es.search(
        index="computer",
        query={"match_all": {}},
        aggs={
            "categories": {  # 우리 컬럼이 아니라 정해진 문법
                "terms": {"field": "category"}  # 타겟으로 지정할 컬럼명 : category
            }
        },
    )

    """
     "aggregations": {
        "categories": {
          "doc_count_error_upper_bound": 0,
          "sum_other_doc_count": 0,
          "buckets": [
            {
              "key": "노트북",
              "doc_count": 3
            },
            {
              "key": "네트워크",
              "doc_count": 2
            },
            {
              "key": "모니터",
              "doc_count": 1
            },
            {
              "key": "저장장치",
              "doc_count": 1
            },
            {
              "key": "주변기기",
              "doc_count": 1
            }
          ]
        }
      }
    },
    """

    results = []
    for hit in response["hits"]["hits"]:
        document = hit.get("_source", {})
        results.append(document)

    return {"msg": {"results": response, "total": response["hits"]["total"]["value"]}}


# match
# where랑 비슷함
# 백터 검색 (자연어 검색)
# 검색어를 분석한 뒤에 토큰 단위로 검색
# '노트북에' 로 검색하면 '노트북을'도 나온다
@router.get("/es/select/match")
def match(keyword: str):
    response = es.search(index="computer", query={"match": {"content": keyword}})

    return {"msg": formatter(response)}

# multi_match
# 여러 필드에서 match 검색
@router.get("/es/select/multi_match")
def multi_match(keyword: str):
    response = es.search(
        
        index="computer",
                         query={"multi_match": {
                             'query': keyword,
                             'fields': ['title','content']
                             }}
                         )
    return { "msg": formatter(response) }


# term
# select의 like 처럼 정확히 일치하는 것
@router.get("/es/select/term")
def term(keyword: str):
    response = es.search(
        
        index="computer",
                         query={"term": {
                            #  'category': keyword
                             'content': keyword
                             }}
                         )
    return { "msg": formatter(response) }

# gte : >= greater than equal
# gt : > greater than
# lte : <= less than equal
# lt : < less than
@router.get('/es/select/range')
def range_(max:int, min:int = 0):
    response = es.search(
        index="computer",
            query={"range": {
                'price':{
                    'gte': min,
                    'lte': max
                }
                }}
        )
    
    return { "msg": formatter(response) }

# bool 복합 쿼리
# filter : 쿼리가 참인 것 검색 (스코어 계산을 하지 않아 빠르다)
# must : 쿼리가 참인 것 검색
# must_not : 거짓인 것만 검색
# shuold : 쿼리가 참인 것의 점수를 높인다, 여러개 쓰면 OR
@router.get('/es/select/filter')
def filter_(category, keyword):
    response = es.search(
        index="computer",
        query={"bool": {
            'filter': [{
                'term' :{'category': category}
            }],
            'must': [
                {
                    'match': {'content': keyword}
                }
            ]
        }}
    )
    
    return { "msg": formatter(response) }

@router.get('/es/select/orderby')
def filter_(sort_field, order = 'asc'):
    
    if order != 'asc' and order != 'desc':
        return {"msg": 'order는 asc 또는 desc여야 합니다'}
    
    response = es.search(
        index="computer",
        query={"match_all": {}},
        sort=[{
            sort_field: {'order': order}
        }],
        size=20
    )
    
    return { "msg": formatter(response) }

# 전달인자로 dict 형태를 완성해서 줬을 때
@router.post('/es/crud/insert')
def insert_document(document : dict):
    response = es.index(
        index='computer',
        id=document.get('id', -1),
        document=document
    )

    return {
        'response': response,
        "msg": 'document 추가 완료'    
    }

@router.get('/es/crud/select')
def select_document(id):
    try :
        # es.search 사용해도 되고
        # _id로 검색할 때는 get도 사용 가능하다
        response = es.get(
            index='computer',
            id=id
        )
        print('response : ', response)
        
        result = response.get('_source')
    
    except Exception as e :
        print(e)
        
    return {
        'result': result,
        'msg': 'document 조회 완료'
    }
    
@router.put('/es/crud/update')
def update_document(id, document: dict):
    result = {}
    try :
        result = es.update(
            index='computer',
            id=id,
            doc=document
        )
    
    except Exception as e :
            print(e)
    
    return result


@router.put('/es/crud/update/field')
def update_document(id, price:int, rating:float):
    result = {}
    try :
        result = es.update(
            index='computer',
            id=id,
            doc={
                'price': price,
                'rating': rating
            }
        )
    
    except Exception as e :
            print(e)
    
    return result

@router.delete('/es/crud/delete')
def delete_document(id):
    result = {}
    try:
        result = es.delete(
            index='computer',
            id=id
        )
        
    except Exception as e:
        print(e)
    
    return result
