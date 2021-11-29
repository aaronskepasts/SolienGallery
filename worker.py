import os
import redis
from rq import Worker, Queue, Connection

#-----------------------------------------------------------------------

listen = ["high", "default", "low"]

redis_url = "redis://redistogo:f4b8b77d71204a3ec6ef21f8b5f5b38c@tarpon.redistogo.com:10223/"
conn = redis.from_url(redis_url)

#-----------------------------------------------------------------------

if __name__ == "__main__":
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()