import requests
import json
import urllib.parse
import time


class Bulk_Scrapper:
    def __init__(self, ngrok_app_url) -> None:
        self.base_url = ngrok_app_url+'/search?query='
        self.session=requests.session()
        self.session.headers = {
            'ngrok-skip-browser-warning': 'any-value'
        }

    def _server_down_handler(self, url):
        start_wait = time.time()
        while True:
            if int(time.time() - start_wait) > 200:
                return "Timed Out"
            response = self.session.get(url)
            if response.status_code == 404 or response.status_code != 200:
                time.sleep(1)
                continue
            else:
                break
        return response.json()
    
    def _server_restart_handler(self, url):
        self.session.get(self.qurery_handler('_Restart_Server'))
        res = self._server_down_handler(url)
        if res == "Timed Out":
            print('Server Timed Out. Please Check the Server Manually')
        else:
            return res

    def qurery_handler(self, query):
        if isinstance(query, str):
            queries = {'query': [query]}
        elif isinstance(query, list):
            queries = {'query': query}
        else:
            raise ValueError("Query must be a string or a list of strings")
        
        json_query = json.dumps(queries)
        encoded_query = urllib.parse.quote(json_query)
        url = f'{self.base_url}{encoded_query}'
        return url


    def Scrape(self, query):
        url=self.qurery_handler(query)        
        res = self.session.get(url)
        if res.status_code == 404:
            res = self._server_down_handler(url)
            if res == "Timed Out":
              return 'Server Timed Out. Please Check the Server Manually'
        else:
            res = res.json()


        out = res['success']
        count = 0
        while len(res['failed']) !=0:
            if count > 5:
                break
            re_list = res['failed']
            url=self.qurery_handler(re_list)
            res = self._server_restart_handler(url)
            out.update(res['success'])
            count +=1

        return out
