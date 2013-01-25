#!/bin/bash
limit=10
cnt=""
if [ -f Score.txt ]
then 
	cnt=1
	while [ -f Score_${cnt}.txt ] 
	do
		let cnt=cnt+1
	done
	mv Score.txt Score_${cnt}.txt
fi

inpfolder="input${cnt}"
if [ ! -d $inpfolder ]
then
	mkdir $inpfolder
fi

for ((i=1;i<=$limit ;i++));
do

	wget -q --cookies=on --keep-session-cookies --save-cookies cookie --timeout 10 -O ${inpfolder}/${i}.gif  "http://epaper.timesofindia.com/epsignup/captcha.aspx?token=0.705541077733014"
	key=$(grep "key" cookie | cut  -f7)
	./enhancer.py ${i}.gif ${key} ${cnt}
done

rm cookie

success=$(grep "1" Score.txt |wc -l)
fail=$(grep "0" Score.txt |wc -l)
total=$(expr $success + $fail )
prob=$(awk 'BEGIN{ print '$success' / '$total' }')
echo Success :$success  and Total : $total
echo Success Probability : $prob
echo $prob >> Probability.txt
