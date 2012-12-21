import yappi
from test_utils import assert_raises_exception, test_passed

def foo():
    for i in range(1000000): pass
def foo1():
    for i in range(1000000): pass
def foo2():
    for i in range(1000000): pass
def bar():
    for i in range(1000000): pass
def bar1():
    for i in range(1000000): pass
def bar2():
    for i in range(1000000): pass
def foo3():
    for i in range(1000000): pass
    
def foo_child1():
    foo1()
    bar1()
def foo_child2():
    foo2()
    bar2()
    
def test1():
    bar()
    foo()
    foo_child1()
    foo_child2()

yappi.start(profile_threads=False)
foo()
foo2()
foo_child1()
yappi.stop()
fstats = yappi.get_func_stats()
fstats.print_all()
fstats.save("foo1")
yappi.clear_stats()

yappi.start(builtins=True, profile_threads=False)
test1()
yappi.stop()
fstats = yappi.get_func_stats()
fstats.save("foobar1")
yappi.clear_stats()

yfs = yappi.YFuncStats()
yfs.add("foo1").add('foobar1')
yfs.sort(sort_type=yappi.SORTTYPE_TTOT).print_all() 
yfs.save('callgrind.out', 'callgrind')
foobar_stat = yfs.find_by_name('test1')
