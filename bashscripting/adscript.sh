#!/bin/bash
find /home/denver/bashscripting/perm -perm 777 | while read -r file; 
do
	chmod 755 $file
done
echo done
