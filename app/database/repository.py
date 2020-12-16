from collections import Mapping
from typing import Optional, List, Iterable, Union, Callable, Any

from tinydb import Query
from tinydb.table import Document


class EntityInterface:
    def to_dict(self):
        pass


class Repository:
    def __init__(self, table_name: str):
        from main import db
        self.__table = db.table(table_name)

    @staticmethod
    def query_builder() -> Query:
        return Query()

    def insert(self, document: Union[Mapping, EntityInterface]) -> int:
        class_with_to_dict_def = getattr(document, "to_dict", None)
        if callable(class_with_to_dict_def):
            document = document.to_dict()
        return self.__table.insert(document)

    def search(self, cond: Union[Query, Any]) -> List[Document]:
        return self.__table.search(cond)

    def contains(self, cond: Optional[Union[Query, Any]] = None, doc_id: Optional[int] = None) -> bool:
        return self.__table.contains(cond, doc_id)

    def remove(self, cond: Optional[Union[Query, Any]] = None, doc_ids: Optional[Iterable[int]] = None, ) -> List[int]:
        return self.__table.remove(cond, doc_ids)

    def update(self,
               fields: Union[Mapping, Callable[[Mapping], None]],
               cond: Optional[Union[Query, Any]] = None,
               doc_ids: Optional[Iterable[int]] = None, ) -> List[int]:
        return self.__table.update(fields, cond, doc_ids)

    def get(self, cond: Optional[Union[Query, Any]] = None, doc_id: Optional[int] = None, ) -> Optional[Document]:
        return self.__table.get(cond, doc_id)
