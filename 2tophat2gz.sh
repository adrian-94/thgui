#!/bin/bash -x
for infile in ./SEQfiles/*.gz;
do
	gunzip -S .fastq $infile
done

for infile in ./SEQfiles/*.fastq;
do
	new_filename_mapped=${infile/fastq/samfile_mapped}
	new_filename_unmapped=${infile/fastq/samfile_unmapped}
	./tophat2 -o TophatOutputpiper/ -p 11 ./indexes/sacCer3 $infile
	echo $infile
        echo $new_filename_unmapped
	samtools view -h -o $new_filename_unmapped   ./TophatOutputpiper/unmapped.bam
	samtools view -h -o $new_filename_mapped   ./TophatOutputpiper/accepted_hits.bam
done
