class Interval:
    def __init__(self, s, e):
        self.start = s
        self.end = e


def mergeIntervals(intervals):
    # for i in intervals:
    #     print(i.start, i.end)

    intervals.sort(key = lambda x:x.start)


    result = [intervals[0]]
    for i in intervals[1:]:
        # print(i.start, i.end)
        prev = result[-1]
        if i.start > prev.start and i.start < prev.end:
            prev.end = max(i.end, prev.end)
        else:
            result.append(i)

    for i in result:
        print(i.start, i.end)


def mergeIntervalTest():
    intervals = [Interval(1,3), Interval(5,7), Interval(2,5)]
    mergeIntervals(intervals)


mergeIntervalTest()