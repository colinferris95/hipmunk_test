#Problem: Your job is to build an API that queries each provider via HTTP and returns a merged list containing all of their results.


from tornado import gen, ioloop, web
import urllib, json, operator

class MainHandler(web.RequestHandler):
    def get(self):
        
        #get the resource for each endpoint
        url = "http://45.55.150.116:9000/scrapers/expedia"
        response = urllib.urlopen(url)
        data_expedia = json.load(response)
        
        url = "http://45.55.150.116:9000/scrapers/travelocity"
        response = urllib.urlopen(url)
        data_travelocity = json.load(response)
        
        url = "http://45.55.150.116:9000/scrapers/orbitz"
        response = urllib.urlopen(url)
        data_orbitz = json.load(response)
        
        url = "http://45.55.150.116:9000/scrapers/priceline"
        response = urllib.urlopen(url)
        data_priceline = json.load(response)
        
        url = "http://45.55.150.116:9000/scrapers/united"
        response = urllib.urlopen(url)
        data_united = json.load(response)
       
        #just get the data without the results[] array
        json_string_expedia = data_expedia["results"]
   
        json_string_travelocity = data_travelocity["results"]
        
        json_string_orbitz = data_orbitz["results"]
        
        json_string_priceline = data_priceline["results"]
        
        json_string_united = data_united["results"]
        
        print(len(json_string_united) )
        
        print(json_string_united[0]["agony"])
        
        
        
        
        
        #merge arrays list(heapq.merge(json_string_expedia,json_string_travelocity,json_string_orbitz,json_string_priceline,json_string_united))
        
        
        #add all of the json together
        data = { 'results' : json_string_expedia + json_string_travelocity + json_string_orbitz + json_string_priceline + json_string_united }
        
        #sort by key 'agony'
        data["results"].sort(key=operator.itemgetter('agony'))
        
        #write json to page
        data = json.dumps(data)

        self.write(data)
  

 

#use correct endpoint
ROUTES = [
    (r"/flights/search", MainHandler),
] 

#
def run():    
    app = web.Application(
        ROUTES,
        debug=True,
    )
    app.listen(8000, address='45.55.150.116')
    ioloop.IOLoop.current().start()


if __name__ == "__main__":
    run()
    
    
	

