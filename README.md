# hdfs-ec
Erasure Coding Performance Testing in Apache Hadoop 3 HDFS 

My Project at CERN as part of openlab summer student projects
===
 * Test environment: Hadoop3
 * Test and evaluate erasure coding
   * get familiar with the Ereasure Code (EC) concept
   * enable the feature on hadoop3
   * perform basic writing and reading test - storing 10GB file with/without EC - single threaded
   * Try different codecs: New Java coder, RS, ISA-L and their configurations RS(6,3), RS(10,4) etc.
   * run TPCDS benchmark test on EC encoded data and compare the results with the one without EC
   * recovery speed of a single and double machine failures (comparing to traditional replication)
   * measure a single threaded reading speed when files are under single or double failure recovery
   * generate a lot of small files (100M) and store them with EC  - measure the impact of the number of blocks on the datanode GC reporting and read and write speed etc.

 * Evaluate triple namenode HA
   * Install and add 3rd namenode to hadoop3
   * Run through a few failure scenarios when two namenodes are going down
 * YARN Docker containers
   * reconfigure YARN to run on docker instead of on LinuxContainers
   * submit a basic docker image to yarn (could be even our client image), or some app like Zepplin etc.
   * create a docker image for NXCALS (with their software) and submit a spark job to read the NXCALS data with all dependencies encapsulated in such docker
 * Evaluate HDFS router-based federation
   * ref: https://hadoop.apache.org/docs/r3.1.2/hadoop-project-dist/hadoop-hdfs-rbf/HDFSRouterFederation.html


#### TPC-DS benchmarking in Spark using Spark SQL workloads

* Open spark-shell: <br/>
`spark-shell --conf spark.sql.catalogImplementation=in-memory --conf spark.security.credentials.hive.enabled=false --master yarn --num-executors 84 --driver-memory 16g --executor-memory 48g --executor-cores 4 --driver-cores 4 --jars /tmp/nseidan/spark-sql-perf/target/scala-2.11/spark-sql-perf_2.11-0.5.1-SNAPSHOT.jar`

* Generate TPC-DS dataset of 1TB: <br/>
`val tables = new com.databricks.spark.sql.perf.tpcds.TPCDSTables(spark.sqlContext, "/tmp/nseidan/tpcds-kit/tools", "1000")`

* Use json format and apply genData() function:<br/>
`tables.genData("/user/nseidan/1tb-json-rs-6-3", "json", true, true, true, false, "", 100)`

