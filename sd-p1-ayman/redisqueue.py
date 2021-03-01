import redis

def enqueue_url(f,url):
   data = {
      'function' = f 
      'url' = url
   }

   
