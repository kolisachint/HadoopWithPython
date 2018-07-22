
import pyspark

from pyspark import SparkContext

def main():

   sc = SparkContext(appName='SparkWordCount')

   input_file = sc.textFile('/user/kolisachint/resources/input.txt')
   counts = input_file.flatMap(lambda line: line.split()) \
                     .map(lambda word: (word, 1)) \
                     .reduceByKey(lambda a, b: a + b)
   counts.saveAsTextFile('/user/kolisachint/resources/spark/output')

   sc.stop()

if __name__ == '__main__':
   main()
