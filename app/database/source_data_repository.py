from .repository import Repository, EntityInterface


class SourceDataRepository(Repository):
    def __init__(self, name: str):
        super().__init__(table_name="".join([char for char in name if char.isalnum()]))


class SourceData(EntityInterface):
    def __init__(self, title: str, link: str, pub_date: str, description: str = None, data: dict = None):
        self.__title = title
        self.__link = link
        self.__pub_date = pub_date
        self.__description = description
        self.__data = {} if data is None else data

    def to_dict(self):
        return {
            'title': self.__title,
            'link': self.__link,
            'pub_date': self.__pub_date,
            'description': self.__description,
            'data': self.__data,
        }

    @property
    def title(self) -> str:
        return self.__title

    @property
    def link(self) -> str:
        return self.__link

    @property
    def pub_date(self) -> str:
        return self.__pub_date

    @property
    def description(self) -> str:
        return self.__description

    @property
    def data(self) -> str:
        return self.data
