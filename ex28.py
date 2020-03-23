 True and True
# 1. TRUE
 False and True
# 2. FALSE
 1 == 1 and 2 == 1
# 3. FALSE
 "test" == "test"
# 4. TRUE
 1 == 1 or 2 != 1
# 5.  TRUE
 True and 1 == 1
# 6. TRUE
 False and 0 != 0
# 7. FALSE
 True or 1 == 1
# 8. TRUE
 "test" == "testing"
# 9. FALSE
 1 != 0 and 2 == 1
# 10. FALSE
 "test" != "testing"
#  11. FALSE
 "test" == 1
# 12. FALSE
 not (True and False)
# 13. TRUE
 not (1 == 1 and 0 != 1)
# 14. FALSE
 not (10 == 1 or 1000 == 1000)
# 15. FALSE
 not (1 != 10 or 3 == 4)
# 16. TRUE
 not ("testing" == "testing" and "Zed" == "Cool Guy")
# 17. TRUE
 1 == 1 and (not ("testing" == 1 or 1 == 0))
# 18. TRUE
 "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
# 19. FALSE
 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
# 20. TRUE
I will also give you a trick to help you figure out the more complicated ones toward the end.
Whenever you see these Boolean logic statements, you can solve them easily by this simple process:
1. Find an equality test (== or !=) and replace it with its truth.
2. Find each and/or inside parentheses and solve those first.
3. Find each not and invert it.
4. Find any remaining and/or and solve it.
5. When you are done you should have True or False.
I will demonstrate with a variation on #20:
3 != 4 and not (” t e s ting ” != ” t e s t ” or ”Python” == ”Python ” )
Here’s me going through each of the steps and showing you the translation until I’ve boiled it down to
a single result:
1. Solve each equality test:
3 != 4 is True: True and not ("testing" != "test" or "Python" == "Python")
"testing" != "test" is True: True and not (True or "Python" == "Python")
"Python" == "Python": True and not (True or True)
2. Find each and/or in parentheses ():
(True or True) is True: True and not (True)
3. Find each not and invert it:
not (True) is False: True and False
4. Find any remaining and/or and solve them:
True and False is False
With that we’re done and know the result is False.