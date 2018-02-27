# scrapy-hakka-sample

## Usage

```
$ docker-compose up
```

## Set task queue and Fire


```python
import redis
import json

conn = redis.Redis()

a = {
    "spider_name": "myspider",
    "initial_params": {
        "start_urls": [
        	# set start urls
        ]
    }
}

b = json.dumps(a)

# Fire Task!
conn.lpush("scrapy:myspider", b)
```

# Author

K.Himeno