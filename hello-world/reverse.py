list_str = input()
list_spl = list_str.split()
#list_spl.reverse()
#list_spl_reverse = list_spl
list_spl_reverse = list_spl[::-1] # alternative to reverse
list_spl_reverse = " ".join(list_spl_reverse) # join will only work with str
print(list_spl_reverse)