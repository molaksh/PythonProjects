import matplotlib
import random

matplotlib.use('TkAgg')
import matplotlib.pyplot as plot

def successive_heads(trials,heads_in_a_row):
    count = 0
    i=0
    for i in range(trials):
        if random.random() < 0.5:
            count += 1
            if count == heads_in_a_row:
                #return i+1
                break
        else:
            count = 0
    return i+1        

def avg_no_of_flips(experiments):
    total_flips = 0
    flips_for_three_successive_heads = 0
    for i in range(experiments):
        flips_for_three_successive_heads = successive_heads(100,3)
        total_flips = total_flips + flips_for_three_successive_heads
        average_flips = total_flips/experiments

        if(i+1 == experiments):
            print()
            print("Experiments: ", experiments)
            print("Average flips", average_flips)

    return average_flips



def main():

   experiments = [1,10,100,1000,10000,100000]
   average_flip_list = []

   for i in experiments:
       average_flip_list.append(avg_no_of_flips(i))

#    print(experiments)
#    print(average_flip_list)




   plot.plot(experiments, average_flip_list, label='3 tails in sequence',\
          marker='*', color='b', linestyle='-')

   plot.xlabel('Experiments')
   plot.ylabel('Average')

   plot.legend()
   plot.grid()

   plot.xscale('log')

   plot.xlim(-0.1, 100001)
   plot.ylim(-1, 25)

   #plot.savefig("sample-plot.pdf") 
   #plot.savefig("sample-plot.png") 
   plot.show()
    



main()

