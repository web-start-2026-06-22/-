from sqlmodel import SQLModel, Field
from typing import Optional

class Emp3(SQLModel, table=True):
    # 없으면 클래스명이 테이블명이 된다.
    # __tablename__="emp"
    
    # empno: int = Field(primary_key = True)
    empno: int | None = Field(
        default = None,
        primary_key = True
    )
    ename: str
    job: str
    # mgr: int | None = None
    mgr: Optional[int] = None
    hierdate: str
    sal: float
    # comm: float | None = None
    comm: Optional[float] = None
    deptno: int = Field(
        foreign_key='dept3.deptno'
    )
    
    # # 모든 변수 검증
    # @model_validator(mode='before')
    # @classmethod
    # def empty_to_none(cls, values ):
    #     return { key : ( value if value != "" else None) for key, value in values.items() }