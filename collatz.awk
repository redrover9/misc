#!/usr/bin/awk -f
BEGIN { print "Collatz Conjecture" 
printf "Enter an integer: "
getline num < "-"
do 
    if (num % 2 == 0) {
        num /= 2
        print num
        }
    else {
        num *= 3
        num += 1
        print num
        }
while (num != 1)
}
