#!/usr/bin/env python3
# copyright (c) 2019 Mitsuhiko Sato. All Rights Reserved.
# Mitsuhiko Sato ( E-mail: mitsuhikoevolution@gmail.com )
#coding:UTF-8

import gzip, os
import subprocess
from joblib import Parallel, delayed
from Bio import SeqIO
from argparse import ArgumentParser

def mean_qual(in_file):
    if in_file[-3:]==".gz":
        fhr=gzip.open(in_file,"rt")
    else:
        fhr=open(in_file,"r")
    print("Check quality "+in_file)
    count=0
    qual=[]
    for rec in SeqIO.parse(fhr,"fastq"):
        if len(qual) > 0: 
            pos=0
            for q in rec.letter_annotations["phred_quality"]:
                qual[pos]+=int(q)
                pos+=1
        else:
            qual=rec.letter_annotations["phred_quality"]
        count+=1
    fhr.close()

    qual2=[]
    for qu in qual:
        qual2.append(float(qu)/count)
    return in_file, qual2


def main():
    parser=ArgumentParser(description="",usage="python3 qc_par_bp.py -t num_threds -p output_prefix fastq[.gz]...", epilog="")
    parser.add_argument("files",nargs="*",type=str,metavar="str",help="fastq files")
    parser.add_argument("-t",type=int,metavar="int",default=2,help="num threads (default=2)") 
    parser.add_argument("-p",type=str,metavar="str",default="quality_check",help="output prefix (default=quality_check)")
    parser.add_argument("-s",type=float,metavar="float",default=10,help="pdf width (default=10)")
    args = parser.parse_args()

    quality = Parallel(n_jobs=int(args.t))( [delayed(mean_qual)(f) for f in args.files])
    out="filename\tFR\tposition\tmean_qual\n"
    for q in quality:
        pos=0
        if q[0].find("_R1") > 0:
            for qu in  q[1]:
                out+=q[0]+"\tR1\t"+str(pos+1)+"\t"+str(q[1][pos])+"\n"
                pos+=1
        elif q[0].find("_R2") > 0:
            for qu in  q[1]:
                out+=q[0]+"\tR2\t"+str(pos+1)+"\t"+str(q[1][pos])+"\n"
                pos+=1
        else:
            for qu in  q[1]:
                out+=q[0]+"\tN\t"+str(pos+1)+"\t"+str(q[1][pos])+"\n"
                pos+=1

    fhw=open(args.p+".txt","w")
    fhw.write(out)
    fhw.close()
    cmd=["Rscript", os.path.dirname(os.path.abspath(__file__))+"/qc_par_bp.r", args.p, str(args.s)]
    subprocess.call(cmd)

    
if __name__ == '__main__': main()

