class Remove_Duplicates_List():
 def remove_duplicates_list(self):

  my_list = [1, 2, 2, 3, 4, 4, 5]

  new_list = list(set(my_list))

  print(new_list)
list_dup = Remove_Duplicates_List()
list_dup.remove_duplicates_list()