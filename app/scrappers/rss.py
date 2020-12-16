from typing import Iterator, List

from .scrapper import ScrapperInterface
from ..database.source_data_repository import SourceData, SourceDataRepository
from ..database.source_repository import SourceRepository, Source


class RssScrapper(ScrapperInterface):
    def job(self) -> List[SourceData]:
        new_entries = []
        for source in self.__get_sources():
            for source_data in self.__fetch(source):
                saved_new_entry = self.__save_source_data(source, source_data)
                if saved_new_entry:
                    new_entries.append(source_data)
        return new_entries

    @staticmethod
    def __get_sources() -> Iterator[Source]:
        sr = SourceRepository()
        qb = sr.query_builder()
        sources = sr.search(qb.source_type == Source.SOURCE_RSS)
        for source in sources:
            # Convert dict data to controllable object
            yield Source(**source)

    @staticmethod
    def __fetch(source: Source) -> Iterator[SourceData]:
        import feedparser
        feed = feedparser.parse(source.src)
        if 'entries' in feed:
            for item in feed['entries']:
                yield SourceData(**{
                    'title': item.get('title'),
                    'link': item.get('link'),
                    'pub_date': item.get('published'),
                    'description': item.get('summary'),
                    'data': {
                        'guid': item.get('guid', None),
                    }
                })

    @staticmethod
    def __save_source_data(source: Source, source_data: SourceData):
        sdr = SourceDataRepository(name=source.name)
        qb = sdr.query_builder()
        is_source_data_new = not sdr.contains(qb.link == source_data.link)
        if is_source_data_new:
            sdr.insert(source_data)
        return is_source_data_new
