# #
# # Simple recursive function that adds the array up
# #
# def mysum(L):
#     return 0 if not L else L[0] + mysum(L[1:])
# print(mysum([1, 2, 3, 4, 5, 6, 7 ]))
#
#
# #
# # simple recursion when dealing with a tree
# #
# def sumtree(L):
#     tot = 0
#     for x in L:
#         if not isinstance(x ,list): # checks to see if x is an integer in list if so add it
#             tot  += x
#         else:
#             tot += sumtree(x)
#     return tot
#
# print(sumtree([1,[2,[3,[4,[5,]]]]]))

# #
# #intresting pop exmpale with walking up a tree and adding values
# #
# def sumtree2(L):
#     tot = 0
#     items = list(L)
#     while items:
#         front = items.pop(0)
#         if not isinstance(front, list):  # checks to see if x is an integer in list if so add it
#             tot += front
#         else:
#             tot += sumtree2(front)
#     return tot
#
#
# print(sumtree2([1,[33,[3,[4,[33,]]]]]))


