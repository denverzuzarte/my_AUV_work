echo -n "number of star = "

read num
i=0
while [ $i -lt $num ]
do
	j=$(($num-1-$i));
	while [ $j -lt $num ]
	do
		echo -n "*"
		((j++))
	done
	echo ""
	((i++))
done

