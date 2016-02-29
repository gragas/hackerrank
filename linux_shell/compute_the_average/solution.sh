read N
total=0
for i in $(seq 1 $N)
do
	read number
	total=$((total + number))
done
printf %.3f $(echo "$total / $N" | bc -l)
