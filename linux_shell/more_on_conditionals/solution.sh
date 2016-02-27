read A
read B
read C
if [ "$A" -eq "$B" ] && [ "$A" -eq "$C" ]
then
	echo "EQUILATERAL"
elif ([ "$A" -eq "$B" ] && [ "$A" -ne "$C" ]) || \
     ([ "$A" -eq "$C" ] && [ "$A" -ne "$B" ]) || \
     ([ "$B" -eq "$C" ] && [ "$B" -ne "$A" ])
then
	echo "ISOSCELES"
else
	echo "SCALENE"
fi

	   
