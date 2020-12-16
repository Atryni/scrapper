from .database.source_repository import Source, SourceRepository


class SourceCreator:
    @staticmethod
    def create(name: str, src: str, data: dict = None, source_type: str = Source.SOURCE_RSS, **kwargs) -> bool:
        source = Source(name=name, src=src, source_type=source_type, data=data)
        sr = SourceRepository()
        qb = sr.query_builder()
        source_new = not sr.contains(qb.src == src)
        if source_new:
            sr.insert(source)
        return source_new

    @staticmethod
    def delete(src: str) -> None:
        sr = SourceRepository()
        qb = sr.query_builder()
        sr.remove(qb.src == src)

    @staticmethod
    def builder(query: str, url_domain: str = None) -> str:
        from urllib.parse import quote
        encoded_query = quote(query)
        rss_sources = {
            'news.google.com': f'https://news.google.com/rss/search?q={encoded_query}&gl=PL&hl=pl&ceid=PL:pl',
            'nyaa.si': f'https://nyaa.si/?page=rss&q={encoded_query}&c=0_0&f=0',
        }
        if url_domain in rss_sources:
            return rss_sources[url_domain]
        else:
            return query
