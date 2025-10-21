#Started with base weights
weigh_ins = [255, 251]
week_num= len(weigh_ins)

new_weight = float(input('It\'s Sunday, how much do you weigh (in lbs) today? '))

#adds new weight to list                 
weigh_ins.append(new_weight)

weight_avg = sum(weigh_ins) / (week_num + 1)

print("\nHere are your weights: ")

for i in range(len(weigh_ins)):
  print(f'On week {i} you weighed {weigh_ins[i]}')

print(f'\nYour average weight over {week_num+1} weeks is {weight_avg:.2f}\n')

  


