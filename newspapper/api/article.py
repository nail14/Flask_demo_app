from flask_combo_jsonapi import ResourceList, ResourceDetail
from combojsonapi.event.resource import EventsResource

from newspapper.models.database import db
from newspapper.models import Article
from newspapper.schemas import ArticleSchema
from newspapper.api.permissions.article import ArticlePermission


class ArticleBase:
    schema = ArticleSchema


class ArticleListEvents(EventsResource):
    def event_get_count(self, *args, **kwargs):
        return {"count": Article.query.count()}


class ArticleList(ArticleBase, ResourceList):
    events = ArticleListEvents
    data_layer = {
        "session": db.session,
        "model": Article,
    }


class ArticleDetail(ArticleBase, ResourceDetail):
    data_layer = {
        "session": db.session,
        "model": Article,
        "permission_patch": [ArticlePermission],
    }
