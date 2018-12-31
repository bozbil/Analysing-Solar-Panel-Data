# Introduction to Programming in Python Assignment: Analysing Solar Panel Data

If you look at the roofs of houses in Colchester and Wivenhoe, you will see that some of them are fitted with photovoltaic panels which generate electricity from incident sunlight. The amount of electricity generated per day obviously depends on the length of the day but also on factors such as the weather: cloud and rain reduce the amount of sunlight, the ambient temperature affects the mobility of electrons, and so on. Some people who have solar panels take a reading each day, so that they are able to work out how much electricity they have generated.

## The task
You are asked to write a program that reads in a file of such daily readings which is given on the command line. Your program should take precisely one command-line argument, the name of this file. An example file, generation.dat, is provided, taken from a real solar panel installation, so a typical invocation of your program would be

```bash
python3 solar.py generation.dat
```

Each line of **generation.dat** normally contains two numbers: the first denotes the day and is an integer starting from zero, while the second is the reading of the generation meter at the end of that day. Hence, to determine the amount of electricity generated in day N, one would subtract the reading for day N - 1 from that of day N. Note that there is not a reading for every day in the file (because the person recording the data forgot or was away), so you need to do something sensible to handle such events. Some lines in the file start with # and are to be interpreted as comments. When the data have been read in, you should make your **solar.py**:

1. First list item
First nested list item
     - Second nested list item


- Print out:

   - the mean amount generated per day
   - the minimum amount generated per day, and the day or days on which this happened
   - the maximum amount generated per day, and the day or days on which this happened
   - Split the readings into 28-day chunks and calculate the mean and standard deviation (s.d.) of each chunk

- Produce a plot containing the following lines:

   - the mean amount generated in each 28-day chunk (a red line)
   - the mean amount plus one s.d. (a black line)
   - the mean amount minus one s.d. (a black line)
- Finally, you should find an equation that fits the data reasonably well and calculate the correlation coefficient between values calculated from your equation and the 28-day chunk means. The nature of the equation that you need to fit will become apparent when you view the plot of the 28-day chunks. You should draw this line on the plot in green.
