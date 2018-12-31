###########################################################################
#=========================================================================#
#                  solar.py      /        ANALYSING SOLAR PANEL DATA      #
#=========================================================================#
# This program was made to interpret the data coming from                 # 
# the solar panels. When any data file is given from the command line,    # 
# the program reads this data and gives the following output:             # 
# * The mean amount generated per day                                     # 
# * The maximum amount                                                    # 
# * The maximum amount observed day(s)                                    #
# * The minimum amount                                                    #
# * The minimum amount observed day(s)                                    #
# * And a graph of monthly (28-day chunk) data, standard deviations       #
#   with an equation that fits the data                                   #                       
#                                                                         #
#                                                                         #
#                                                                         #
#                <<<<<<< HOW TO USE THIS PROGRAM>>>>>>                    #
#                                                                         #
# the name of the program is entered in the command line with             #
# the data file to be used. A typical invocation of                       #
# the program would be:                                                   #
#                             python3 solar.py generation.dat             #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
# AUTHOR                                                                  #
#  Registration number 0000000                                            #                      
#  I hereby certify that this program is entirely my own work.            #
###########################################################################



"""#####################################################################################"""
"""                                           PART 0                                    """
"""                                      IMPORTING MODULS                               """
"""                                             &                                       """
"""                                   READING DATA FROM FILE                            """
"""#####################################################################################"""
# In this step modules needed were imported.
# math = in standard deviation function, for square root calculation
# pylab = for drawing graphics
# sys  =  for reading the data file at the command line
import math                        
import pylab
import sys

# In this part, program reads a file which  is given on the command line (for example: generation.dat)
# If you do not get the data file, produce an error message about it.
# it reads this file and assign the data in an array (all_data)


all_data=[]
try:
    with open(sys.argv[1], "r") as f:
        all_data=f.readlines()
except:
    print (" could not read any imput")
    exit(1)




"""#####################################################################################"""
"""                                      PART I                                         """
"""                                    FUNCTIONS                                        """
"""#####################################################################################"""

# this function return an ordinal number when it take a number.
# for example = when it takes 101, it returns with 101st

def ordinal_number(x):
    x = str(x)
    or_num = ""
    if x[-1] == "1":
        or_num = "st"
    elif x[-1] == "2":
        or_num = "nd"
    elif x[-1] == "3":
        or_num = "rd"
    else:
        or_num = "th"
    or_num = x + or_num
    return or_num

    
# this function is for sorting arrays.
# When you sent two array, the function  sorts them by first one
# Insertion sort algortim is used
def sorting (array_1,array_2):
    
    for i in range(0, len(array_1) - 1):
        for j in range (i + 1 , len(array_1)):
            if array_1[i] > array_1[j]:
                array_1[i] , array_1[j] = array_1[j] , array_1[i]
                array_2[i] , array_2[j] = array_2[j] , array_2[i]
    return array_1 , array_2


# This function is for calculate standard deviation.
# It works with an array and  return with a float number (sd_con) .
def st_dev (sd_vals):
    
    sd_ave = mean(sd_vals)
    lng = len(sd_vals)
    total = 0
    
    for i in range (0,lng):
        total = total +  (sd_ave - sd_vals[i]) ** 2
        
    sd_con = math.sqrt( 1 / (lng - 1) * total )
    return sd_con


# This function is for calculate mean.
# It works with an array and  return with a float number.
def mean (vals):
    total = 0
    lng=len(vals)
    for i in range (0,lng):
        total = total + vals[i]
    average = total / lng
    return average


"""#####################################################################################"""
"""                                      PART I                                         """
"""   In this section, the data in the data file is read and the data is classified.    """
"""                                                                                     """
"""#####################################################################################"""

# variables to be used throughout the program are defined.
explanation = []            # this array contains explanations 
days_array = []             # this array contains days
value_f_meter = []          # this array contains the reading of the generation meter at the end of that day
amount_per_day = []         # this array contains the amount of electricity generated in a day
numbers = "1234567890"      # this array contains numbers between 0-9, it is used to determine if a variable is a number.


# In this part, firstly check the data come from the file is an explanation or  a numerical value.
# If it is a numerical value, the program separates it two parts:
# 1- Day  Number   ( array name = days_array    )
# 2- The reading of the generation meter ( array name =  value_f_meter )
# These two data is held in the arrays with same index number.
for i in all_data:
    if  i[0] not in numbers :
        explanation += [i]
    else:
        space = i.find(" ")
        days_array += [i[0 :space]]
        other = (i[space + 1:])
        space = other.find(" ")
        if other  ==  -1:
            value_f_meter += [other]
        else:
            value_f_meter += [other[0:space]]

# In this part the day numbers  (days_array) were converted to integer,
# the reading of the generation meter at the end of that day (value_f_meter) was converted to float
for i in range (0,len(days_array)) :
    try:
        days_array[i] = int(days_array[i])
        value_f_meter[i] = float(value_f_meter[i])
    except:
        print ("There is a problem in your data file")
        exit(1)
        
     
"""#####################################################################################"""
"""                                      PART II                                        """
"""                           missing days are calculated                               """
"""                the amount of electricity generated in every day is calculated       """
"""#####################################################################################"""

# In this step, missing days are calculated
# when the days are sorted, anomalies are detected and the total value is distributed to the lost days.
# lost days and lost values are added to the end of the relevant series.
for i in range (0,len(days_array) - 1):
    if days_array[i + 1]-days_array[i] > 1:
        difference1 = (value_f_meter[i + 1]- value_f_meter[i]) / (days_array[i + 1] - days_array[i])
        difference = difference1
        for j in range (days_array[i] + 1,days_array[i + 1]):
            days_array += [j]
            value_f_meter += [value_f_meter[i] + difference]
            difference = difference + difference1

#using the sorting function, the lost days and values were settled in their places.               
days_array,value_f_meter = sorting(days_array,value_f_meter)

#the amount of electricity generated in every day is calculated
#and hold in an array (amount_per_day)
amount_per_day += [0]
for i in range (0,len(days_array) -1 ):
    amount_per_day += [value_f_meter[i + 1] - value_f_meter[i]]



"""#####################################################################################"""
"""                                      PART III                                       """
"""                  the requested outputs are calculated and printed                   """
"""#####################################################################################"""

# mean function is used to calculate the average.
mean_per_day = mean(amount_per_day)
# The mean amount generated per day is printed
print(("The mean amount generated per day  =  %.2f" %(mean_per_day)))


# in this section, for finding The maximum amount, max() is used.
# this function search maximum value in the amount of electricity generated in every day (amount_per_day)
# after finding maximum value, checked which days are and is the value repeated.
n = -1
string_char = ""
while True:
    try:
        n=days_array[amount_per_day.index(max(amount_per_day), n + 1)]
        ord_num = ordinal_number(str(n))
        string_char  =  string_char + ord_num + " day |  "
    except:break

    
# The maximum amount is printed
print("The maximum amount  = %.2f" %(amount_per_day[n]))

# The maximum amount observed day(s) is printed
print( "The maximum amount observed day(s)  = %s" %(string_char))


# in this section, for finding The maximum amount, max() is used.
# this function search maximum value in the amount of electricity generated in every day (amount_per_day)
# after finding maximum value, checked which days are and is the value repeated.
n=0
string_char = ""
while True:
    try:
        n=days_array[amount_per_day.index(min(amount_per_day), n + 1)]
        ord_num = ordinal_number(str(n))
        string_char  =  string_char + ord_num + " day |  "
    except:break

# The minimum amount is printed
print("The minimum amount =   %.2f " %(amount_per_day[n]))
# The minimum amount observed day(s) is printed
print( ("The minimum amount observed day(s) = %s" % (string_char)))



"""#####################################################################################"""
"""                                      PART IV                                        """
"""                       spliting the readings into 28-day chunks                      """
"""              calculate the mean and standard deviation  for each chunk              """
"""                                  graphicization                                     """
"""#####################################################################################"""

# variables to be used chunking proces are defined.
a28_days_chunk = []         # a temporary variable to divide the days into 28-day-chunks
mean_of_chunks = []         # this array contains every 28-day-chunks means.
sd_of_chunks = []           # this array contains every 28-day-chunks standard deviation.


# in this step, the values (days and  amount of electricity generated  ) are splited 28 days chunks
# st_dev  function is used to calculate the standard deviation of 28-day-chunks
# mean  function is used to calculate the average of 28-day-chunks
for i in range (1, len(amount_per_day) + 1):
    a28_days_chunk += [amount_per_day[i - 1]]
    if i % 28   ==   0:
        mean_of_chunks += [mean(a28_days_chunk)]
        sd_of_chunks += [st_dev(a28_days_chunk)]
        a28_days_chunk = []

#it makes a final chunk of days less than 28 days.     
if len(a28_days_chunk)!= 0:
    mean_of_chunks += [mean(a28_days_chunk)]
    sd_of_chunks += [st_dev(a28_days_chunk)]



# this section includes the calculation of the values to be used in the graphic.
# these values are:
#                   @ the average of 28-day-chunks
#                   @ the average of 28-day-chunks - standard deviation
#                   @ the average of 28-day-chunks + standard deviation
#                   @ an equation that fits the data                                                                      
###########################################################################    
# the equation used is:                                                   #
#    ________________________________________________                     #
#   |                                                |                    #
#   |   n                                            |                    #
#   |  ∑  (7 * sin (( 579 / 100 ) * ( x + 2 )) + 9 ) |                    #
#   |   0                                            |                    #
#   |________________________________________________|                    #
#                                                                         #
###########################################################################
x = []
mean_minus_sd = []
mean_plus_sd = []
for i in range(0,len(mean_of_chunks)):
    mean_minus_sd += [mean_of_chunks[i] - sd_of_chunks[i]]
    mean_plus_sd += [mean_of_chunks[i] + sd_of_chunks[i]]
    x += [7 * math.sin(5.79 * ((i + 2))) + 9]




##############################################
###########  graphicization  #################
##############################################
    
fig  =  pylab.figure ()
ax  =  fig.add_subplot (111)
ax.grid (True)
ax.set_xlabel ("28 Days Chunks")
ax.set_ylabel ("The Amount Of Electricity Generated")
ax.set_title ("ANALYSING SOLAR PANEL DATA")


# the plot of  28-day-chunks average 
ax.plot (mean_of_chunks,color = 'red', linestyle = 'solid',
         marker = 'o',markerfacecolor = 'red', markersize = 3)

# the plot of  28-day-chunks average - standard deviation
ax.plot (mean_minus_sd,color = 'black', linestyle = 'dashed',
         marker = 'o',markerfacecolor = 'black', markersize = 3)

# the plot of  28-day-chunks average + standard deviation
ax.plot (mean_plus_sd,color = 'black', linestyle = 'dotted',
         marker = 'o',markerfacecolor = 'black', markersize = 3)

# the plot of the quation that fits 28-day-chunks average 
ax.plot (x,color = 'green', linestyle = 'solid',
         marker = 'o',markerfacecolor = 'black', markersize = 0)



pylab.show ()












    
