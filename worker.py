import redis
from rq import Worker, Queue, Connection

listen = ['high', 'default', 'low']

# redis_url = 'redis://localhost:6379'
redis_url = 'redis://redistogo:e9c37ff2c6f85f431a4b6d12a5557c5a@soapfish.redistogo.com:9722'

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
