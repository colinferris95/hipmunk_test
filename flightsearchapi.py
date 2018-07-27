#Problem: Your job is to build an API that queries each provider via HTTP and returns a merged list containing all of their results. (sorted by agony)

#use for handling json
import json, operator

#tornado webserver
from tornado import gen, ioloop, web

#async client
from tornado.httpclient import AsyncHTTPClient

#also for handling json
from tornado.escape import json_decode, json_encode


class MainHandler(web.RequestHandler):
    #async keywords
    @gen.coroutine
    def get(self):
        
        #get all the fetchs from the aync call function
        f_exp = async_calls("http://localhost:9000/scrapers/expedia")
        f_tra = async_calls("http://localhost:9000/scrapers/travelocity")
        f_orb = async_calls("http://localhost:9000/scrapers/orbitz")
        f_pri = async_calls("http://localhost:9000/scrapers/priceline")
        f_uni = async_calls("http://localhost:9000/scrapers/united")
        
    
        #yeild the async fetches
        f_exp = yield f_exp
        f_tra = yield f_tra
        f_orb = yield f_orb
        f_pri = yield f_pri
        f_uni = yield f_uni
        
        
        #format our json resources
        data_expedia = format_json_resource(f_exp.body)
        data_travelocity = format_json_resource(f_tra.body)
        data_orbitz = format_json_resource(f_orb.body)
        data_priceline = format_json_resource(f_pri.body)
        data_united =format_json_resource(f_uni.body)
        
        
        #make one big merged list
        data = { 'results' : data_expedia + data_travelocity + data_orbitz + data_priceline + data_united }
        
        # sort by key 'agony'
        data["results"].sort(key=operator.itemgetter('agony'))
        
        
        #get data into a format that can write to browser
        data = json.dumps(data)

        self.write(data)
        self.finish()


#aysnc fetch function to get endpoints        
def async_calls(url):

    #start up our aysnc client
    http_client = AsyncHTTPClient()
    
    #fetch the endpoint    
    response =  http_client.fetch(url)
        
   
    return response
  
  
#json formatting function to prepare json for merging    
def format_json_resource(json_resource):
    json_raw = json_decode(json_resource)
    
    json_non_array = json_raw["results"]
    
    return json_non_array
    
    
#use correct endpoint
ROUTES = [
    (r"/flights/search", MainHandler),
] 

#main function
def run():    
    app = web.Application(
        ROUTES,
        debug=True,
    )
    app.listen(8000)
    
    print "Server (re)started. Listening on port 8000"
    
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
    
    
	

