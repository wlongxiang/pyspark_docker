# Pyspark docker environment

Run ``cd docker && docker-compose up`` to spin up 2 workers and 1 master.

Master UI is available at localhost:8080.

To verify the cluster is working, one can SSH into the master and run `pyspark` from shell (in oneliner: `docker exec -it docker_master_1 pyspark`), then you should be able to see
a spark-shell up and running and run some ad-hoc spark commands.

One can also submit a job by ssh into the master and run ``spark-submit <spark_job.py>``

