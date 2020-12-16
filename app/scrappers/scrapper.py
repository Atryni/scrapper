from typing import Iterator, List

from ..database.source_data_repository import SourceData
from ..database.source_repository import Source


class ScrapperInterface:
    def job(self) -> List[SourceData]:
        pass

    @staticmethod
    def __get_sources() -> Iterator[Source]:
        pass

    @staticmethod
    def __fetch(source: Source):
        pass

    @staticmethod
    def __save_source_data(source: Source, source_data: SourceData):
        pass
