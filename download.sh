#!/bin/bash
limit=10
for ((i=0;i<=$limit ;i++));
do
#echo $i
wget -q -O $i.gif "http://epaper.timesofindia.com/epsignup/captcha.aspx?token=0.498004082079339"
./enhancer.py ${i}.gif
done
