# works with Python 3.7.0b3

import asyncio
import os
import subprocess as sbp
import csv

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

#asyncio.run(res_proc('./emu'))

if __name__ == '__main__':

    dpm_dims = [2,4,8,16] # lhs
    dpn_dims = dpm_dims   # rhs
    dpk_dims = [64,128,256,512] #common dim

    # bram dimensions
    brams_big = [256,512,1024,2048]
    brams_small = [8,16,32,64]

    # matrices that have to be tested
    mat_rowlist = [2,4,8,16,32]
    mat_collist = [64,128,256,512,1024,2048,4096]

    m_bram = 256
    n_bram = 256

    # first run the emu instatiattions
    # with the required dimensions
    # temporary bram variables
    tm_bram = 1
    tn_bram = 1

    dir='build'
    exec_cmd=''
    for dk in dpk_dims:
        for dm in dpm_dims:
            for dn in dpn_dims:
                #bram size setup
                if(dm>dn):
                    tm_bram = int(dm/dn * m_bram)
                    tn_bram = int(n_bram)
                if(dn>dm):
                    tn_bram = int(dn/dm * n_bram)
                    tm_bram = int(n_bram)
                if(dm==dn):
                    tm_bram = int(m_bram)
                    tn_bram = int(n_bram)

                exec_cmd = './'+dir+"/{0}x{1}x{2}_{3}_{4}/emu".format(dm,dk,dn,tn_bram,tm_bram)
                # make the environment variables
                os.environ["M"] = str(dm)
                os.environ["N"] = str(dn)
                os.environ["K"] = str(dk)
                os.environ["LHPM"] = str(tm_bram)
                os.environ["RHPM"] = str(tn_bram)
                ts = sbp.Popen(["make","instemu"])
                ts.wait()

                asyncio.run(res_proc(exec_cmd))

