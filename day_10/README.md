# Day 10

Today I've decided to include how my code looked like at the moment I got the second answer (in `raw.py`),
just because I'm chuffed that I got the recursive function in part 2 correct on the first time :D

Here's my thought process behind today's puzzle, since the code may seem quite far removed from the puzzle description.

## Part 1

The description of the order in which you need to pick the adapters is surprisingly long, given that it boils down to ordering all the numbers from the input in an increasing order. You then need to add a 0 to the beginning and the largest number from the input + 3 to the end (which I missed the first time I submitted an answer), and calculate all the differences between the two consecutive numbers in the list you get. Finally you can use a `Counter` to count the differences and get the required product.

## Part 2

I've noticed that all the differences on the list were either 1 or 3, so my first thought was that the adapters on the ends of those differences (and thus the difference itself) could not be changed. My initial idea was to extract the chains of consecutive 1s, get the number of possibilities for each chain, and multiply the results to get the answer. (Since those chains were separated by 3s, changing one chain would not affect the number of possibilites in any other chain, i.e. the chains are independent.)

To find the pattern for calculating the number of possibilities I wrote down a few chains of 1s and started working out the possibilites by hand. I've noticed that if the sum of the first two elements at any time was greater than 3 your only option is to put the first element aside and consider what's left, but if it's 3 or less you have a choice of adding them together or keeping them separate. I've turned that into a function and instinctively decorated it with `lru_cache`, which required using tuples as arguments, as lists are not hashable. I plugged in the differences, and the output turned out to be correct.

I've noticed afterwards that I forgot about my idea of extracting the chains of 1s and just plugged in the whole list of differences at once, but thanks to `lru_cache` I got the answer almost immediately anyway. I tried running the script without it, and it seems it would take quite a while to get an answer ^^'
