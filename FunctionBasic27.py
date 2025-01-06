from datetime import datetime

def merge_sort(list):
    return []


def test_perf(func,*args,**kwargs):
    start_time = datetime.now()
    func(*args,**kwargs)
    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"The function took {total_time} to execute")


test_perf(merge_sort,[1,2,3])