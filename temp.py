from time_travel_debugger import TimeTravelDebugger

x = 0

def f():
    global x
    temp = 0
    for i in range(10):
        temp += i
    x = temp


debugger = TimeTravelDebugger()
debugger.start_debugging(f)
debugger.debugger_cli()
