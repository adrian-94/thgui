#!/bin/bash
#
#$ -S /bin/bash
#$ -cwd
#$ -pe smp 4
#$ -l big_mem=true
#$ -q all.q

file1=$1
file2=${file1/_R1_/_R2_}
file4=${file1/fastq.gz/tophat}/
tophat2 -p 3 --b2-very-sensitive -G 
/LaCie/tophatgui/mm10Genes.gtf -o
$file4 /LaCie/tophatgui/mm10/mm10 $file1 $file2
