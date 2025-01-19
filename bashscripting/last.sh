#!/bin/bash

#organising
echo first folder
read to
echo second folder
read from
find $from -type f -name "*.cpp" | while read -r file; 
do	
	cp $file $to
done
echo done with part 1

#compilation
echo $to
cd $to

for file in /$to/*;
do
	g++ $file -o $(basename $file .cpp).out
done
echo done with part 2
#ayeeeeee

#evaluation

echo input file

read inp

echo correct output file

read outp
find /$to/* -type f -name "*.out" | while read -r file; 
do
	$file
done

