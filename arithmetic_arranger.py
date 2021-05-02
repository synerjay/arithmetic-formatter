import re 

# import regex for checks

# Input is arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

# Output is 
#    32      3801      45      123
# + 698    -    2    + 43    +  49
# -----    ------    ----    -----

def arithmetic_arranger(problems, solve = False):

    #First make variables to make the final product
    if (len(problems) > 5):
      return "Error: Too many problems."

    first = ""
    second = ""
    lines = ""
    sumx = ""
    string = ""
    for problem in problems:
      if(re.search(r"[^\s0-9.+-]", problem)):
        if (re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
      
      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]

      # Another check to see if number length is greater than or equal to 5

      if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
        return 'Error: Numbers cannot be more than four digits.'
      

      # Try to solve the sum IF the bool is true in the second argument
      sum = ""
      if (operator == "+"):
        sum = str(int(firstNumber) + int(secondNumber))
      elif(operator == "-"):
        sum = str(int(firstNumber) - int(secondNumber))


      length = max(len(firstNumber), len(secondNumber)) + 2
      top = str(firstNumber).rjust(length) # justifies the number to the right
      bottom = operator + str(secondNumber).rjust(length - 1) #since operator here we subtract length by 1
      line = ""
      res = str(sum).rjust(length)
      for _ in range(length):
        line += "-" 
        # making the dash lines between the answers and the operators
      
      # To prevent spacing on the last problem we must have a condition

      #[-1] indicates the last problem item on the problem array
      # Because we are in a loop, we must connect all the lines in every iteration
      if problem != problems[-1]:
        first += top + '    '
        second += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else:
        first += top
        second += bottom
        lines += line
        sumx += res

  # Check to see if solve argument is TRUE,
  # This should be outside the loop
    if solve: 
      string = first + "\n" + second + "\n" + lines + "\n" + sumx 
    else:
      string = first + "\n" + second + "\n" + lines
    return string
 
