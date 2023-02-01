y = True

#  a loop to keep trying the code until it works
while y:
    #  try your risky code, without asking for permission
    try:
        x = int(input("Enter a whole number: "))
        #  i hate 0's and never want them in my code
        if 1 / x == 1 / x:
            y = False
    #  if its not a whole number we have an issue
    except ValueError:
        print("Retry")
    #  this tells you to never use 0's, see the above if block
    except ZeroDivisionError:
        print("Don't enter 0")
    #  this block always runs

    #  if we want to handle all other errors that could possibly happen
    #  except:
    #      print("Eroor")
    #  this block is set to a default of any and every error, but must be last!

    finally:
        print("***************************************")

#  now we can safely use our variable
print(x, "Squared is:", x * x)
