from __future__ import print_function
from pyspark.sql import SparkSession
from pyspark.sql import types
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: mysparkjob arg1 arg2 ", file=sys.stderr)
        exit(-1)

    session = SparkSession.builder.getOrCreate()
    raw_coupons = session.read.csv(sys.argv[1])

    coupons = raw_coupons.select(raw_coupons['_c0'].alias('tkt_number'),
                             raw_coupons['_c1'].alias('cpn_number').cast(types.IntegerType()),
                             raw_coupons['_c2'].alias('origin'),
                             raw_coupons['_c3'].alias('destination'),
                             raw_coupons['_c4'].alias('airline'),
                             raw_coupons['_c6'].alias('amount').cast(types.FloatType()))

    origin = coupons[coupons['destination'] == 'MAD'].groupby('origin').sum('amount')
    origin_top10 = origin.sort("sum(amount)", ascending=False).limit(10)

    rdd_test = origin_top10.rdd.map(list)
    rdd_test.saveAsTextFile(sys.argv[2])
    sc.stop()