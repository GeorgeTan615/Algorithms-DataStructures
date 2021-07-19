"Name: George Tan Juan Sheng"
"Student_ID: 30884128"


def counting_sort_stable_num_col(new_list:list, col:int) -> list:
	"""
	This function takes a list of integers and a column, and sorts the list of strings in ascending order based on the col,
    by picturing that the integers are right aligned and the most right column is 0. This 
	function then returns the sorted list of integers based on the col'th digit.

    Pre-cond: col must be bigger or equal to 0, cannot be negative.
    Post-cond: Return sorted list based on col'th digit.

	Time-complexity: Best-Case = Worst-case complexity is O(n), where n is the size of the input list
	Explanation: O(base+base+n+(base+n))           
				=O(base(create count array , aka buckets of base 10, hence creating 10 buckets) + 
				base(looping count array and initialise empty list) + n(adding the right items into count array) + 
				(n + base)(loop through count array and rebuild original list))
				=O(3base + 3n)
				=O(n) (since base is constant at 10)

	Auxiliary space complexity: O(n), where n is the size of input list 
	Explanation: We would need to create count array which takes base space, however base is constant at 10 so we do not 
				include it in our space complexity. We would also need to place n number of items into the count array. 
				Hence, our auxiliary space complexity would result in O(n).

	Space complexity = Input + Auxiliary space
					 = O(n+n)	(where n is the size of input list)
					 = O(n)
	"""
	if new_list ==[]:
		return []									

	base= 10                                        
	count_array = [None]*(base)                     #Initialise count_array using base, as 9 is our max item

	for i in range(len(count_array)):
		count_array[i] = []

	for item in new_list:
		index = item//(base**col) % base			#Will get the 1 digit of the whole number according to col
		count_array[index].append(item)                  

	index  = 0                                      #Index as slot to put the elements accordingly back into new_list
	for i in range(len(count_array)):   
		for j in range(len(count_array[i])):
			new_list[index] = count_array[i][j]
			index += 1                                    
	return new_list

def radix_sort_number(new_lst:list) -> list:  
	"""
	This function takes a list of integers and sorts it. The function returns a sorted list in ascending order.
	This function does not modify original list.

    Post-cond: Return list is sorted. Original list will not be modified.

	Time-complexity: Best-Case = Worst-case complexity is  O(nk), where n is the number of elements in new_lst and k is the greatest number of 
					digits in any elements in new_lst
	Explanation: O(n + n+ k(n)) 
				=O(n(loop through input list to find max words)+ n(create copy of input list) + k(k is our max words, and we will be calling counting sort k times)*n(counting_sort has a time complexity of O(n))))
				= O(n + nk)
				= O(nk)

	Auxiliary space complexity: O(n), where n is the size of input list 
	Explanation: Our auxiliary space complexity would be based on the counting sort algorithm we call, which is O(n). 
				We would need to create count array which takes base space, however base is constant at 10 so we do 
				not include it in our space complexity. We would also need to place n number of items into the count array and this requires O(n) space. 
				Before calling counting sort over and over, we would also need to create a copy of the input list which requires
				O(n) space. Hence, our auxiliary space complexity is O(n+n), resulting as O(n) regardless how many times we call counting sort 
				since after every counting sort function, the memory is deleted.

	Space complexity = Input + Auxiliary space
					 = O(nk+n)	(where n is the size of input list and k is the greatest number of digits in any element )
					 = O(nk)
	"""
	if new_lst != []:   
		max_words = len(str(new_lst[0]))
	else:
		max_words = 0								

	for item in new_lst:
		if len(str(item)) > max_words:                  
			max_words = len(str(item))                  #Get the maximum amount of digits in any element in new_lst

	copy_lst = []
	for item in new_lst:
		copy_lst.append(item)							#Create a copy of input list

	for i in range(max_words):                          
		counting_sort_stable_num_col(copy_lst,i)			
	
	return copy_lst			

def best_interval(transactions:list,t:int) -> tuple:
	"""
	This function takes a list of integers, transactions and an integer, t and returns a tuple of best_t 
	and count which determines which interval of length t contains the most transactions in the list transactions. 
	Best_t is the time such that the interval starting at best_t and ending at best_t + t contains more elements from 
	transactions than any other interval of length t. Count is the number of elements in the interval of length t starting at best_t.

    Pre-cond: The list transactions is a unsorted list of non-negative integers. t is a non negative integer.
    Post-cond: Returns a tuple of best_t and count which determines which interval of length t contains the most transactions in the list transactions.

	Time-complexity: Best-Case = Worst-case complexity = O(nk), where n is the number of elements in new_lst and k is the greatest number of 
					digits in any elements in new_lst
	Explanation: O(nk + n)
				=O(nk(call radix sort on the list transactions) + n(loop through the list sorted transactions))
				=O(nk)

	Auxiliary space complexity: O(n), where n is the size of the list. 
	Explanation: We will be calling radix sort on our list of transactions and radix sort has an auxiliary space complexity of O(n). 
				This function does need any more auxiliary space hence our resulting auxiliary space complexity is O(n).
	
	Space complexity = Input + Auxiliary space
					 = O(nk+n)	(where n is the size of input list k is the greatest number of digits in any elements in new_lst)
					 = O(nk)
	"""
	start = 0													#we will be using start and end to traverse the list,start is the start of our interval and end is the end of our interval
	end = 0													
	pot_count = 0												#pot_count, aka potential count is used to keep track of count in each interval
	count = 0													#count, aka best count will be the highest amount of transactions 
	best_t = 0													
	best_t_pos = 0 												#will be used to store the index of our best_t value in the list

	if transactions ==[]:
		return (0,0)											

	sorted_transactions = radix_sort_number(transactions)

	while end < len(sorted_transactions):						
		interval = sorted_transactions[start] + t				
		if sorted_transactions[end] <= interval:				#check if our item at end is within our interval
			pot_count = end-start+1							
			end += 1											#keep track of the count within interval and increment end
		else:
			if pot_count == 0 :												
				pot_count = end-start							#this is to keep track of potential count for cases where after item at end is not within interval and start is incremented, end is still not within interval

			if pot_count> count:								
				count = pot_count								
				best_t_pos = start								
			pot_count = 0										#reset pot_count to 0 as we are moving on to next interval
			start += 1											

	if end-start > count:										#this is to account for cases where the while loop was exited before pot_count of the last interval was able to compare with count 
		count = end-start
		best_t = sorted_transactions[start]						
		best_t_pos = start
	else:
		best_t = sorted_transactions[best_t_pos]

	if sorted_transactions[best_t_pos + count-1] - sorted_transactions[best_t_pos] < t: #this is to check if our best_t is at it's most minimal time
		best_t = sorted_transactions[best_t_pos+count-1] - t							
		if best_t < 0:											#this is to check if our minimal time is negative, if negative then make it to 0
			best_t = 0
	
	
	return (best_t,count)


def split(word:str) -> list:
    """
    This function takes a string of word and splits the input word into its alphabets into a list form. 
    If the input word is an empty string, the function returns an empty string in a list.

    Post-cond: Returns a list of alphabets splitted from input word, or returns a list of empty string if input is an empty string. 

    Time-complexity: Best-Case = Worst-case complexity is O(n) where n is the length of the word.
    Explanation: We will be looping for each word in our input which is n times, hence O(n).


    Auxiliary space complexity: Auxiliary space complexity is O(n), where n is the length of the input word.
    Explanation: We will be needed to create a new list of size n in order to put each alphabets of our input word, 
                which is of length n.

	Space complexity = Input + Auxiliary space
					 = O(n+n)	(where n is the length of input word)
					 = O(n)
    """
    if word == "":
        return [""]
    return [char for char in word]

def counting_sort_anagram(new_list:list) -> str:
    """
    This function takes a list of alphabets and sorts the list of alphabets in ascending order, and then returns
    a string combining all of the sorted alphabets.

    Pre-cond: Each element in list must be single character alphabet.
    Post-cond: Returns a sorted string according to the input list's alphabets.

    Time-complexity: Best-Case = Worst-case complexity is O(n), where n is the size of the input list and m is the ascii number of the biggest alphabet we can 
                    find in the list, subtracted by 97, however m is bounded by 26, hence our worst case
    Explanation: O(n+m+m+n+(m+n)+n)
                where m is the ascii number of the biggest alphabet we can find in the list, subtracted by 97
                =O(n(finding maximum alhabet) + m(creating count array, aka buckets) + m(looping count array and initialise empty list)
                +n(adding the right items into count array)+m+n(loop through count array and rebuild original list)+n(call join to combine alphabets in list to form string)
                = O(4n + 3m) 
                = O(n+m) (however m is always bounded by 26 as we are using base 26, hence m is a constant)
                = O(n)

    Auxiliary space complexity: O(n), where n is the size of our input list.
    Explanation: We would need to create count array which takes m space, where m is the ascii number of the biggest alphabet we can find in the list, subtracted by 97 .
                We would also need to place n number of items into the count array. Hence, O(n+m). However since m is always 
                bounded by 26 since we are using base 26, we can conclude that m is a constant, resulting in our final auxiliary
                space complexity being O(n).

	Space complexity = Input + Auxiliary space
					 = O(n+n)	(where n is the size of input list)
					 = O(n)
    """
    if new_list == [""]:
        return ""
    max_item = ord(new_list[0])-97                  #Get ascii number for alphabet and minus 97, 
                                                    #we will be using base 26, where 'a' is index 0 ,'b' is index 1 and so on

    for item in new_list:
        item = ord(item)-97
        if item > max_item:
            max_item = item 
    
    count_array = [None]*(max_item+1)               #Create count array based on our max_item, aka buckets
    for i in range(len(count_array)):
        count_array[i] = []
    
    for item in new_list:
        count_array[ord(item)-97].append(item)      #Put the item into their respective buckets based on their index
    
    index = 0 

    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            new_list[index] = count_array[i][j]
            index +=1                               #Rebuild our original list 
    
    res = "".join(new_list)                         #Combine alphabets in list to form string
                     
    return res

def counting_sort_alpha(new_list:list,col:int,max_letters:int) -> list:
    """
    This function takes a list of tuple(which consists of a string and its respective index in the list) or strings, 
    a column and the number of max letters,and sorts the list of strings in ascending order based on the col 
    which is the column,by picturing that the strings are left aligned and the most right column is 0. This 
    function then returns the sorted list of strings based on the col'th alphabet.

    **Special note**
    The reason why this counting sort function accounts for list of tuple or strings is because later on in words
    with anagrams function, we will store list1 in a form that each strings will be attached with its respective index
    in the original list, making it easier for us to find the element when we want to output the words with anagrams.
    List2 will just be stored as list of strings. Hence, this function includes the algorithm to sort either list of strings
    or list of tuple of strings and the index.

    Pre-cond: col must be bigger or equal to 0, cannot be negative.
    Post-cond: Return sorted list based on col'th alphabet.

    Time-complexity: Best-Case = Worst-case complexity is O(n), where n is the size of the input list
    Explanation: O(base+base+n+(base+n))           
                =O(base(create count array , aka buckets of base 27, hence creating 27 buckets) + 
                base(looping count array and initialise empty list) + n(adding the right items into count array) + 
                (n + base)(loop through count array and rebuild original list))
                =O(3base + 3n)
                =O(n) (since base is constant at 27)

    Auxiliary space complexity: O(n), where n is the size of input list 
    Explanation: We would need to create count array which takes base space, however base is constant at 27 so we do not include it in our 
                space complexity. We would also need to place n number of items into the count array. Hence, O(n)
    
	Space complexity = Input + Auxiliary space
					 = O(n+n)	(where n is the size of input list)
					 = O(n)
    """
    base = 27
    count_array = [None]*(base)                                         #Initialise count_array using base, base = 27
    for i in range(len(count_array)):
        count_array[i] = []

    if isinstance(new_list[0],tuple):                                    #Check if our input is list of tuples or strings
        for item in new_list:                                            #If is tuple, we will just add a [0] as index to the back of our element to access the word, as our tuple is stored like ("word",index)    
            if len(item[0]) < max_letters:                              
                if max_letters-col <= len(item[0]):                      #check if the input col has reached the words as our words are left aligned
                    position = abs(max_letters-len(item[0]) - col)       #if has reached, get the position of alphabet of the word based on the column
                    index = ord(item[0][-(position+1)])-96               #calculate the index based on the alphabet we have gotten
                else:
                    index = 0                                            #if have not reached, index will just be 0 
            else:
                index = ord(item[0][-(col+1)])-96                   

            count_array[index].append(item)                              #put item into its respective bucket

    else :                                                               #same block of code as the if block above, but this block of code accounts for when we are inputting list of strings, hence no indexing is added behind the element
        for item in new_list:
            if len(item) != max_letters:
                if max_letters-col <= len(item):
                    position = abs(max_letters-len(item) - col)
                    index = ord(item[-(position+1)])-96
                else:
                    index = 0
            else:
                index = ord(item[-(col+1)])-96

            count_array[index].append(item)          

    index  = 0                                                             #Index as slot to put the elements into original list
    for i in range(len(count_array)):
        for j in range(len(count_array[i])):
            new_list[index] = count_array[i][j]
            index += 1                                          
    return new_list

def radix_sort_alpha(new_lst:list):
    """
    This function takes a list of strings and sorts it. The function returns a sorted list in ascending order.
    This function does not modify original list.

    **Special note**
    The reason why this counting sort function accounts for list of tuple or strings is because later on in words
    with anagrams function, we will store list1 in a form that each strings will be attached with its respective index
    in the original list, making it easier for us to find the element when we want to output the words with anagrams.
    List2 will just be stored as list of strings. Hence, this function includes the algorithm to sort either list of strings
    or list of tuple of strings and the index.

    Post-cond: Return list is sorted. Original list will not be modified.

    Time-complexity: Best-Case = Worst-case complexity is O(nk), where n is the size of the input list and k is the number of 
    characters in the longest string in our input list.
	Explanation: O(n + n+ k(n)) 
				=O(n(loop through input list to find max letters)+ n(create copy of input list) + k(k is our max letters, and we will be calling counting sort k times)*n(counting_sort has a time complexity of O(n))))
				= O(n + nk)
				= O(nk)

    Auxiliary space complexity: O(n), where n is the size of input list 
    Explanation: Our auxiliary space complexity would be based on the counting sort algorithm we call, which is O(n). 
                We would need to create count array which takes base space, however base is constant at 27 so we do 
                not include it in our space complexity. We would also need to place n number of items into the count array and this requires O(n) space. 
                Before calling counting sort over and over, we would also need to create a copy of the input list which requires
                O(n) space. Hence, our auxiliary space complexity is O(n+n), resulting as O(n) regardless how many times we call counting sort 
                since after every counting sort function, the memory is deleted.
    
	Space complexity = Input + Auxiliary space
					 = O(nk+n)	(where n is the size of input list and k is the number of characters in the longest string in our input list)
					 = O(nk)
    """

    max_letters = 0
    if isinstance(new_lst[0],tuple):                #Check whether input is list of tuples or list of strings
        for item in new_lst:
            if len(item[0]) > max_letters:          #if is list of tuples, add indexing behind item to access the word
                max_letters = len(item[0])    
    else:
        for item in new_lst:
            if len(item) > max_letters:             #if is list of strings, we will access the item straight
                max_letters = len(item)    

    copy_lst = []
    for item in new_lst:
        copy_lst.append(item)                       #create a copy of input list

    for i in range(max_letters):
        counting_sort_alpha(copy_lst,i,max_letters)
    
    return copy_lst

def remove_duplications(lst:list) -> list:
    """
    This function takes a sorted list of elements and delete any duplicates that are in the input list. Hence, returning 
    a list that has no duplicates.

    Post-cond: Return list wil have no duplicates.

    Time-complexity: Best-Case = Worst-case complexity is O(n), where n is the size of the input list.
    Explanation: Inside our while loop either i or i and j is incremented, hence i will be either equal to j or bigger
                than j. The maximum number i can increment until is, less than length of our list minus one, hence O(n).
                Slicing of list is O(n) as well, hence our resulting time-complexity is O(n).

    Auxiliary space complexity: O(1)
    Explanation: This remove duplication function is an in place algorithm. We are only swapping between items in the list
                and incrementing our indexes.
    
	Space complexity = Input + Auxiliary space
					 = O(n+1)	(where n is the size of input list)
					 = O(n)
    """
    i = 0 
    j = 0
    while i < len(lst)-1:
        if lst[i+1] == lst[j]:
            i += 1
        else:
            lst[i+1], lst[j+1] = lst[j+1], lst[i+1]
            j += 1
            i += 1
    return lst[:j+1]                        #list[0.....j] is contains all unique elements

def words_with_anagrams(list1:list,list2:list) -> list:
    """
    This function takes two lists of strings, list1 and list2 and returns the words in list1 which have an 
    anagram in the second list. 

    Pre-cond: Both input lists will be lists of strings where all characters are lowercase a-z. Neither list contains duplicate strings, but there may be strings which appear in both lists.
    Post-cond: Returns a list of strings from list1 which have at least one anagram appearing in list2.

    Time-complexity: Best-Case = Worst-case complexity is O(L1M1 + L2M2), where L1 is the number of elements in list1, L2 is the number of elements in list2,
                    M1 is the number of characters in the longest string in list1 and M2 is the number of characters 
                    in the longest string in list2.
    Explanation:O(L1*(M1+M1)+L2*(M2+M2)+ L1M1 + L2M2 + L2 + (L1M2 or L2M1))
                =O(L1(call counting sort anagram after calling split on L1 items)*(M1(call counting sort anagram on M1 size of list input)+M1(call split on M1 length of string input)))
                +O(L2(call counting sort anagram after calling split on L2 items)*(M2(call counting sort anagram on M2 size of list input)+M2(call split on M2 length of string input)))
                +L1M1(call radix sort on anagram list1) + L2M2(call radix sort on anagram list2)+ L2(call remove duplications on anagram list2)
                +(L1M2 or L2M1))(we will loop maximum L1 or L2 items as loop will terminate earlier, if the word in list1 that we are pointing at now has the same initials as word in 
                list2 that we are pointing at,but the two words are not equal, we will compare alphabet by alphabet between the two words and decide which word is bigger depending on 
                which alphabet is bigger, if each alphabets of the word are equal, the loop will terminate after executing M1 or M2 times depending on which is smaller)
                = O(3L1M1 + 3L2M2 + L2 + L1M2(we will put L1M2 here just for visual purposes, doesn't matter if its L1M2 or L2M2 as both are bounded by L1M1 and L2M2))
                = O(L1M1 +L2M2)    (L2 and L1M2 are removed as they are both bounded by either L1M1 or L2M2)

    Auxiliary space complexity: O(L1 + L2 + (L1 +L1) + (L2+L2))   (where L1 is the number of elements in list1 and L2 is the number of elements in list2)
                              =O(3L1 +3L2)
                              =O(L1+L2)        
    Explanation: We would need O(L1 + L2) to create the anagram_list1 and anagram_list2 as we will be appending L1 items and L2 items into an empty list.
                We would then need O(L1+L1) + O(L2+L2) when calling radix sort alpha on anagram list1 and anagram list2.
                Hence, resulting O(L1+L2) as our auxiliary space complexity.

	Space complexity = Input + Auxiliary space
					 = O(L1M1+L2M2+L1+L2)	(where L1 is the number of elements in list1, L2 is the number of elements in list2,
                                            M1 is the number of characters in the longest string in list1 and M2 is the number of characters 
                                            in the longest string in list2.)
                     = (L1M1+L2M2)
    """
    anagram_list1 = []
    anagram_list2 = []

    if list1 == [] or list2 == []:
        return []

    for i in range(len(list1)):
        anagram_list1.append((counting_sort_anagram(split(list1[i])),i))        #form a list of tuples, where each tuple consists of words in list1 in anagram form, together with its respective index in list1

    for j in range(len(list2)):
        anagram_list2.append((counting_sort_anagram(split(list2[j]))))          #form a list of strings, where each string is a word in list1 in anagram form

    sorted_anagram_list1 = radix_sort_alpha(anagram_list1)                      
    sorted_anagram_list2 = radix_sort_alpha(anagram_list2)
    sorted_anagram_list2 = remove_duplications(sorted_anagram_list2)            

    p1 = 0          #pointer 1 will be in used in sorted anagram list1 to point at elements
    p2 = 0          #pointer 2 will be in used in sorted anagram list2 to point at elements
    res = []

    while p1<len(sorted_anagram_list1) and p2 < len(sorted_anagram_list2):
        word1 = sorted_anagram_list1[p1][0]                                     #word in list1 based on index p1
        word2 = sorted_anagram_list2[p2]                                        #word in list2 based on index p2
        if word1 == "" or word2 == "":                                          #this block of code will account for cases when either word1 or word2 is an empty string
            if word1 == "" and word2 != "":                                     
                p1 += 1
            elif word1 != "" and word2 == "":                                   
                p2+=1
            elif word1 == "" and word2 == "":                                   #if word1 and word2 are both empty string, this is a match
                index = sorted_anagram_list1[p1][1]
                res.append(list1[index])                                        
                p1 += 1                                                         

        elif word1[0] == word2[0]:                                              #this block of code account for cases when word1 and word2 has the same initials
            if word1 == word2:                                                  
                index = sorted_anagram_list1[p1][1]
                res.append(list1[index])                                         
                p1 += 1
            else:                                                               #if word1 and word2 has same initials but are not a match, this block will be executed
                copy_p1 = p1                                                    #save initial value of p1
                copy_p2 = p2                                                    #save initial value of p2
                for i in range(len(word1)):                                     #this loop will be used to compare each alphabets of word1 and word2
                    if i >= len(word2):                                         
                        p2 +=1                                                  #this will account cases where word1 is longer than word2 and word1[:len(word2)] == word2
                        break   
                    if word1[i] > word2[i]:                                     
                        p2 +=1                                                  
                        break
                    elif word1[i] < word2[i]:
                        p1 += 1
                        break
                    else:
                        continue
                if p1 == copy_p1 and p2 == copy_p2:                             #this will account cases where word2 is longer than word1 and word2[:len(word2)] == word1
                    p1 +=1                                                      #if no change to p1 or p2, means word2 is longer than word1 and word2[:len(word2)] == word1, thus increment p1
                    
        elif word1[0] < word2[0]: 
            p1 += 1
        
        else:
            p2 += 1
    
    return res


