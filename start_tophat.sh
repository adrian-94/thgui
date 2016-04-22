#!/bin/bash
#
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 4
#$ -l big_mem=true

for x in LaCie/tophatgui/*_R1_*.fastq
do
./tophat_script.sh $x
done
