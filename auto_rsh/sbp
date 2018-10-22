# works with Python 3.7.0b3

import asyncio

# create an async subporcess

# stdin and stdout and stderr are


async def res_proc(cmd):
    proc = await asyncio.create_subprocess_exec(
        cmd,
        stdout = asyncio.subprocess.PIPE,
        stderr = asyncio.subprocess.PIPE,
        stdin = asyncio.subprocess.PIPE)
    i = 0
    while True:
        # flush out stdout lines from the buffer
        line = await proc.stdout.readuntil(separator = b'\n')
        lineb = line.decode()
        i=i+1
        print("Number:{}, line:{} ".format(i,lineb.replace("\n","")))
        if (lineb.find("Enter rows depth cols")!=-1):
            print("* Oops ----*")
            proc.stdin.write(b'2 256 4\n')
            proc.stdin.write(b'1 1\n')
            proc.stdin.write(b'0 0\n')
            print("* Oops ----*")

asyncio.run(res_proc('./emu'))





