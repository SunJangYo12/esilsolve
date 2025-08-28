from esilsolve import ESILSolver

xx = ESILSolver("frida://attach/remote/192.168.0.100:27042/6448")

print(xx.r2api.r2p.cmd(":i"))
#xx = ESILSolver("/bin/ls")

#import r2pipe
#xx = r2pipe.open("frida://attach/remote/192.168.0.100:27042/6448")
#print(xx.cmd(":i"))
