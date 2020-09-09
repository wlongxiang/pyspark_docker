# Pyspark docker environment

 - Checkout the master branch to run latest spark version
 - Run ``docker-compose up`` to spin up 2 workers and 1 master (or you can also set COMPOSE_FILE env to a diff. compose file)
 - Go to http://localhost:8080 to see the spark master UI
 - Run `docker exec -it pyspark_docker_master_1 bash` to shell into the spark container
 - Ready to go!

Supported spark versions: v2.4.1, v.2.4.4. You can check out specific brach and run the same commands above.

Some examples to test out:

Suppose you are already in docker master shell,

- word count: `spark-submit /code/wordcount.py /data/logs.txt`

