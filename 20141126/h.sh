#!/bin/sh

echo "hadoop jar /home/zxy/20141126/xb20141126.jar " | su - hdfs
echo "hadoop fs -cat xb20141126.out/part-r-00000" | su - hdfs > demo1
