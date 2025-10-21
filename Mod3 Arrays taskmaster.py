#Started a list with basic things I have to do regularly
to_do = ["stretch", "play words games", "pack lunch", "get grapes"]
done = []

#Functions to complete and view tasks
def task_did(task):
  if task in to_do:
    done.append(task)
    to_do.remove(task)
  
  else:
    print("You don't have to do that!\n")

def task_view(do, did):
  print("\n--- To Do ---")
  for i in range(len(do)):
      print(do[i])
  print("\n---Done---")
  for i in range(len(did)):
      print(did[i])
            
task_view(to_do, done)
task_adder = input("\nWhat task do you want to add? \n")

#If task is in the list, don't add it again, otherwise it gets added to to_do
if task_adder in to_do:
    print("\nYou already have to do it!")
else:
    to_do.append(task_adder)
    
task_doer = input("\nWhat task did you do? ")

#If the task that you did is already in the list, don't do it again.  Otherwise, its gets added to done  
if task_doer in done:
    print('\nYou already did that!')
else:
    task_did(task_doer)

task_view(to_do, done)


  

