# IF  Statements

print("""
Introduction to the if Statement:
     We’ll start by looking at the most basic type of if statement.
      In its simplest form, it looks like this:
          if <expr>:
            <statement>
---<expr> is an expression evaluated in a Boolean context, as 
discussed in the section on Logical Operators in the Operators and Expressions in Python tutorial.
---<statement> is a valid Python statement, which must be indented. (You will see why very soon.)
If <expr> is true (evaluates to a value that is “truthy”), then <statement> is executed. If <expr> is false, then <statement> is skipped over and not executed.

Note that the colon (:) following <expr> is required. Some programming languages require <expr> to be enclosed in parentheses, but Python does not.

Here are several examples of this type of if statement:

>>> x = 0
>>> y = 5

>>> if x < y:                            # Truthy
...     print('yes')
...
yes
>>> if y < x:                            # Falsy
...     print('yes')
...

>>> if x:                                # Falsy
...     print('yes')
...
>>> if y:                                # Truthy
...     print('yes')
...
yes

>>> if x or y:                           # Truthy
...     print('yes')
...
yes
>>> if x and y:                          # Falsy
...     print('yes')
...

>>> if 'aul' in 'grault':                # Truthy
...     print('yes')
...
yes
>>> if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
...     print('yes')
...

""")


arbic = int(input("arbic : "))
eng = int(input("eng : "))
history = int(input("history : "))

total = arbic+eng+history
# the Condition

if arbic > 10 and eng > 50 and history > 50:
    # if this Condition is true
    print(f"the markes  arbic{arbic} , eng {eng}, history{history}")
    print(F"successful .....{total} ", "....here the Condition is true")
else:
    # if this Condition is false
    print(f"the markes  arbic{arbic} , eng {eng}, history{history}")
    print("faild", ".....here the Condition is false")
