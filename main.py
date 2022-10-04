subjects = ["comp sci", "engineering", "chemistry", "DCG", "english", "maths"]
#print(type(subjects)) # dont print stuff the end user does not need to know as it may confuse and frustrate them 
def userselect(str, type):
  global userSelect
  while True:
    try:
      userSelect = int(input(str))
      if type == 0:
        if userSelect > len(subjects) or userSelect <= -1:
          raise("out of bounds error")
      elif type == 1: 
        if userSelect > len(subjects)-1 or userSelect <= -1:
          raise("out of bounds error")
      break
    except:
      print("invalid value\n")
  print("\n\n")
  return(userSelect)

def printsubs():
  global subjects
  global e
  e = 0
  print("This array is",len(subjects),"elements long") # array is just a better name than list in my opinion java > python
  for i in subjects:
    print(e, "=", i)
    e+=1
  print("\n\n")

printsubs()


tempobj = input("input a new object: ")
tempindex = userselect("input a number from the list: ", 0)
subjects.insert(tempindex,tempobj)
printsubs()


tempobj = userselect("input a number to remove from the list: ", 1)
del(subjects[tempobj])
printsubs()
