
Yappi
===================

[![Build Status](https://drone.io/bitbucket.org/sumerc/yappi/status.png)](https://drone.io/bitbucket.org/sumerc/yappi/latest)

Motivation:
===================
CPython standard distribution is coming with three profilers. cProfile, Profile and hotshot. 
cProfile module is implemented as a C module based on lsprof, Profile is in pure Python and the 
hotshot can be seen as a small subset of a cProfile. The motivation to implement a new profiler is
that all of these profilers lacks the support of multi-threaded programs. If you want to profile a 
multi-threaded application, you must give an entry point to these profilers and then maybe merge 
the outputs. None of these profilers is designed to work on long-running multi-threaded application. 
While implementing a game server, it turns out that is is impossible to profile an application 
retrieve the statistics then stop and then start later on on the fly(without affecting the profiled
application). With the experience of implementing a game server in Python, we have identified most 
of the problems, tricky parts regarding profiler usage and so, we have come up with simple but 
powerful requirements.

Features:
===================
* Ability to hook underlying threading model events/properties. (*new in 0.92*)
* Decorator to profile individual functions easily. (*new in 0.92*)
* Profiler results can be saved in callgrind and pstat formats. (new in 0.82) 
* Profiler results can be merged from different sessions on-the-fly. (new in 0.82)
* Profiler results can be easily converted to pstats. (new in 0.82) 
* Supports profiling per-thread CPU time. See http://en.wikipedia.org/wiki/CPU_time for details. (new in 0.62)
* Profiling of multithreaded Python applications transparently. 
* Profiler can be started from any thread at any time.
* Ability to get statistics at any time without even stopping the profiler.
* Various flags to arrange/sort profiler results.
  
Limitations:
===================
* Latest version of Yappi supports Python 2.6.x <= x <= Python.3.4






