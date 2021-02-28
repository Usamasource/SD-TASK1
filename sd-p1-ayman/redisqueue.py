import redis

def enqueue_url(url):
   data = {
       'url' = url
   }

   