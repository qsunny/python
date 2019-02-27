# -*- coding:utf-8 -*-
"""
seft define override dict
"""
__author__="aaron.qiu"

from pprint import pprint

class MeasureBenchmark(object):
    """测量基准"""
    fix_multiple = 1000
    startNum = 0
    endNum = 0
    slope_rate = 0
    fix = 0

    def __init__(self, inch, startNum, endNum):
        self.inch = inch
        self.startNum = startNum
        self.endNum = endNum
        self.slope_rate = (endNum - startNum)/self.fix_multiple
        self.fix = inch*self.fix_multiple

    def get_slope(self):
        """获取对应范围的斜率"""
        return self.slope_rate

    def __str__(self):
        return "inch:{},startNum:{},endNum:{},slope_rate:{},fix_multiple:{},fix:{}".format(self.inch,self.startNum,self.endNum, self.slope_rate,self.fix_multiple,self.fix)

    __repr__ = __str__


def get_range_benchmark(random_read_num,bench_list=None):
    if(bench_list is None):
        return None
    for benchmark in bench_list:
        # startNum = getattr(benchmark, "startNum")
        endNum = getattr(benchmark, "endNum")
        if(random_read_num <= endNum):
            '''查找到指定范围区间的值'''
            return benchmark

    return None

if __name__ == "__main__":
    # 读取到的测量值
    read_test_num_value = 3357
    sl_range = [(861, 1857), (1857, 2854), (2854, 3857),(3857,4852),(4852,5850),(5850,6850),(6850,7846),(7846,8818),(8818,9809)]
    bench_march_list = []
    test_inch = 1;
    for sr_range in sl_range:
        startNum = sr_range[0]
        endNum = sr_range[1]
        measure_benchmark = MeasureBenchmark(test_inch,startNum,endNum)
        test_inch += 1
        # print(measure_benchmark)
        bench_march_list.append(measure_benchmark)


    # for benchmark in bench_march_list:
    #     # pprint(benchmark)
    #     slope_rate = benchmark.get_slope()
    #     print(slope_rate)

    measure_mark = get_range_benchmark(read_test_num_value,bench_march_list)
    pprint(measure_mark)
    startNum = getattr(measure_mark,"startNum")
    # 与区间起始值相差的值
    mark_index = read_test_num_value - startNum
    pprint(mark_index)
    range_slope = getattr(measure_mark, "slope_rate")
    # 与区间起始值偏移量
    mark_shift = mark_index/range_slope
    pprint(mark_shift)
    fix_num = getattr(measure_mark, "fix")
    fix_multiple = getattr(measure_mark, "fix_multiple")
    test_result = (mark_shift + fix_num)/fix_multiple
    pprint(test_result)
    #     # print("startNum:%s ,endNum:%s",startNum,endNum)
    #     if(read_test_num_value <= endNum):
    #         '''查找到指定范围区间的值'''
    #         slope_rate = endNum-startNum/divide_num








