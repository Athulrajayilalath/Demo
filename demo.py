from pyspark import SparkContext
sc = SparkContext(master='local',appName='asas').getOrCreate()
p =sc.parallelize([2,5,6,6])
p.foreach(print)

