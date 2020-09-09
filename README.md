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


## How to publish a new image (manually)

- first you do `docker login` with your credentials to docker-hub
- then `docker build -t wlongxiang/pyspark-2.4.4:<version_tag> .`, this command will build your email with name pyspark and tag with 2.4.4
- verify your image is built successfully by `docker images`
- finally `docker push wlongxiang/pyspark-2.4.4:<version_tag>`, in the end this will be available in your docker repo
- now, everything should be able to run your image or use it in the docker-compose file, such as `docker run -it pyspark-2.4.4:<version_tag> bash`
