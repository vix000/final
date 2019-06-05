import os
import falcon
from mongo import InsertMongoConnector
from scraper.scraper import Scraper
from reader.reader import Reader


class MainResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        scraper = Scraper("clothing", req.params['identifier'])
        mongo_connector = InsertMongoConnector(req.params)
        mongo_connector.insert()
        resp.body = scraper.run


class ResultsResource(object):
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        reader = Reader(req.params['filename'])
        resp.body = reader.read_file


class FalconManager(object):
    def __init__(self, app,  main_resource, routes):
        self.app = app
        self.main_resource = main_resource
        self.routes = routes
        self.add_routes()

    def add_routes(self):
        for key, value in self.routes.items():
            app.add_route(key, value)


app = falcon.API()
main_resource = MainResource()
results_resource = ResultsResource()
routes = {
    '/main': main_resource,
    '/results': results_resource,
}

manager = FalconManager(app, main_resource, routes)
