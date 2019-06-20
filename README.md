Problem: build an API that queries mutilpe HTTP endpoints and return a merged list conatining all of the results sorted by agony

To solve this problem, I decided to stick with the technology used in the searchrunner api, the tornado webserver
I needed to gather all of the resources and sort them by a specific key. 
The first implementation I did used the urllib library. This provided the correct answer, but the HTTP calls were too slow,
So I switched to the torando.httpclient, AsyncHTTPClient. This allowed me to yield multiple endpoints in an asynchronous fashion. 
This made the api much faster.

To run the server, use the same command as the searchrunner api, python -m flightsearchapi

Reference: https://github.com/Hipmunk/hipproblems/tree/master/searchrunner
