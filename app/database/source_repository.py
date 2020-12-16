from .repository import Repository, EntityInterface


class SourceRepository(Repository):
    def __init__(self):
        super().__init__(table_name='sources')


class Source(EntityInterface):
    SOURCE_RSS = 'source_rss'
    SOURCE_WWW = 'source_www'

    def __init__(self, name: str, src: str, data: dict = None, source_type: str = SOURCE_RSS, **kwargs):
        self.__name = name
        self.__source_type = source_type
        self.__src = src
        self.__data = {} if data is None else data

    def to_dict(self):
        return {
            'name': self.__name,
            'src': self.__src,
            'source_type': self.__source_type,
            'data': self.__data,
        }

    @property
    def name(self) -> str:
        return self.__name

    @property
    def src(self) -> str:
        return self.__src

    @property
    def source_type(self) -> str:
        return self.__source_type

    @property
    def data(self) -> dict:
        return self.__data
