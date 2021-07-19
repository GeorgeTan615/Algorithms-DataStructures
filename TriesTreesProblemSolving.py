"Student Name: George Tan Juan Sheng"
"Student ID: 30884128"

class Node1:
    """
    This class is a Node class which will be used in our SequenceDatabase class. Each node has a link, which is the possible
    childrens, data_freq which stores the frequency for the optimal string (highest frequency string up until that node), compar_num which is a 
    comparison number generated from the optimal string, compar_num_len where is the length of the compar_num, iD which is the 
    iD referring to the optimal string which is the fakelink.
    """
    def __init__(self, data_freq:int = 0, compar_num:int = 0, iD:int = 0, compar_num_len:int = 0) -> None:
        """
        This is the __init__ function of the Node1 class

        Time-complexity:Best and worst case O(1)
        Explanation: The function runs at constant time.

        Auxiliary-space complexity:O(1)
        Explanation: Although the function creates a list of size 5, the size of list is fixed, hence it runs at
                     constant time.

        Space-complexity: Input + Auxiliary
                        : O(1) + O(1)
                        : O(1)
        """
        self.link = [None] * 5
        self.data_freq = data_freq
        self.compar_num = compar_num
        self.compar_num_len = compar_num_len
        self.iD = iD

class SequenceDatabase:
    """
    This class will be implemented as a trie and be used to insert strings and also query the highest frequency string.
    """
    def __init__(self) -> None:
        """
        This is the __init__ function of the SequenceDatabase class.

        Time-complexity: Best and worst case  O(1)
        Explanation: The __init__ function runs at constant time.

        Auxiliary-space complexity: O(1)
        Explanation: The function always creates a list of size 4 and is of fixed size, hence it runs at constant time. 
                     Creating a new node also takes O(1) auxiliary-space complexity.

        Space-complexity: Input + Auxiliary
                        : O(1) + O(1)
                        : O(1)
        """
        self.root = Node1()
        self.table = [1,2,3,4]
        self.words = []
        self.idindex = 0

    def create_compar_num(self, key:str) -> int:
        """
        This function is used to create a number for comparison from the input key. As we will only have 
        4 possible input characters, which are A,B,C,D, we will be assigning number 1 to A, 2 to B, 3 to C 
        and 4 to D. For example, 'ABCD', will be generated a comparison number of 1234 which will be used later on.

        Pre-cond: Input key is a single nonempty string of uppercase letters in uppercase [A-D].
        Post-cond: A comparison number of same length with the key will be generated.

        Time-complexity: Best and worst case is O(n), where n is the size of key
        Explanation: O(n(loop through each letter of the key and calculate the nbr accordingly))
                   : O(n)

        Auxiliary-space complexity: O(1)
        Explanation: The function does not require any extra space and is an inplace function.

        Space-complexity: Input + auxiliary
                        : O(n) + O(1)                   where n is size of the key
                        : O(n)
        """
        nbr = 0 
        for char in key:
            index = ord(char)-65 
            nbr = (nbr*10) + self.table[index]
        return nbr
    
    def update_node_values(self, current:Node1, data:tuple) -> None:
        """
        This function is used to update the current node's values with the values from the node after current node.
        The function takes in the current node and also the data, which is a tuple containing the values from the node
        after the current node. The data tuple will be of size 4, data[0] is the iD, which refers to which word it is referring
        to, this iD also works as our fakelink, data[1] will be the frequency, data[2] will be the comparison number and 
        data[3] will be the comparison number's length. The length of comparison number is stored so that we can prevent
        taking lineear time to compute the length of comparison number in the functon.
        
        Pre-cond: The data tuple will be of size 4, data[0] is the iD, which refers to which word it is referring
                  to, this iD also works as our fakelink, data[1] will be the frequency, data[2] will be the comparison number and 
                  data[3] will be the comparison number's length.
        Post-cond: The current node's values will be updated with the details accordingly.

        Time-complexity: Best and worst case is O(1)
        Explanation: The function runs at constant time as it is just basic computations and if elses.

        Auxiliary-space complexity: O(1)
        Explanation: The function is an in place function and does not require extra space

        Space-complexity: Input + auxiliary
                        : O(1) + O(1)
                        : O(1)
        """
        if data[1] > current.data_freq:
            #data is a tuple (id, frequency, compar_num, compar_num_len)
            current.iD = data[0] 
            current.data_freq = data[1]
            current.compar_num = data[2]
            current.compar_num_len = data[3]

       #if frequency is same, will compare between their compar_num_len to determine the lexicographically smaller string
        elif data[1] == current.data_freq:         
            #when comparing between compar_num_len, if same length, determine which is the smaller compar_num and that is the lexicographically smaller string                
            if data[3] == current.compar_num_len:
                if data[2] < current.compar_num:
                    current.iD = data[0]
                    current.compar_num = data[2] 
            
            #if length is not the same, we will have to do padding of zeros accordingly and then compare again
            else:
                diff = current.compar_num_len - data[3]
                if diff > 0:
                    #if diff is positive, means the compar_num len of the node after current node is shorter, hence we need to pad the shorter compar_num len
                    temp_data2 = data[2] * (10**diff)       
                    if temp_data2 < current.compar_num:
                        current.iD = data[0]
                        current.compar_num = data[2] 
                        current.compar_num_len = data[3]
                else:
                    #if diff is negative, means the compar_num len of the node after current node is longer, hence we need to pad the shorter compar_num_len
                    diff = abs(diff)
                    temp_compare_num2 = current.compar_num * (10**diff)
                    if data[2] < temp_compare_num2:
                        current.iD = data[0]
                        current.compar_num = data[2] 
                        current.compar_num_len = data[3]
                        
    def addSequence(self, s:str) -> None:
        """
        This function takes an input string called s, and appropriately store s into the database represented by the instance of SequenceDatabase.

        Pre-cond: s will be a single nonempty string of uppercase letters in uppercase [A-D]
        Post-cond: The function will appropriately store s into the database represented by the instance of SequenceDatabase.

        Time-complexity: Best and worst case is O(len(s)),         where s is the input string
        Explanation: O(len(s) + len(s))     where s is the input string
                   : O(len(s)(used to generate the compar_num) + 
                     len(s)(recursively add each letters into the database, recursion depth is len(s) and the operation at each level takes O(1)))
                   : O(2len(s))
                   : O(len(s))

        Auxiliary-space complexity: O(len(s)), where s is the input string
        Explanation: This function creates len(s) nodes and each nodes has a data of list of fixed size.

        Space-complexity: Input + Auxiliary
                        : O(len(s)) + O(len(s))   where s is the input string
                        : O(2len(s))
                        : O(len(s))
        """
        key_indx = 0 
        current = self.root
        compare_num = self.create_compar_num(s)
        data = self.addSequence_aux(current, s, key_indx, compare_num)
        self.update_node_values(current,data)

    def addSequence_aux(self, current:Node1, key:str, key_indx:int, temp_compare_num:int) -> tuple:
        """
        This function is an auxiliary function of addSequence which will recursively call itself 
        to appropriately insert each letters of the key according to the input key_indx into the database.

        Pre-cond: key will be a single nonempty string of uppercase letters in uppercase [A-D]
        Post-cond: The function will appropriately store the letter, key[key_indx] , which is apart of the key 
                   into the database represented by the instance of SequenceDatabase.

        Time-complexity: Best and worst case is O(1)
        Explanation: The function runs at constant time at each level of recursion.

        Auxiliary-space complexity: O(1)
        Explanation: The function is an in place function and always create space a tuple of size 4, hence it is of constant time.

        Space-complexity: Input + Auxiliary
                        : O(n) + O(1)               where n is the size of the input key
                        : O(n)
        """
        if key_indx >= len(key):                    #Base case when we have reached the end of the word 
            #check if word already exists
            if current.link[0] is not None:                 
                current = current.link[0]                   
                current.data_freq += 1                      #if word exists, increment frequency by 1  
            
            #if word does not exist
            else:
                #store details for new word
                current.link[0] = Node1()   
                current = current.link[0]
                current.iD = self.idindex                   
                current.data_freq = 1
                current.compar_num = temp_compare_num
                current.compar_num_len = len(key)
                self.idindex += 1                           #increment idindex to be used for other words
                self.words.append(key)                      #append the just added word into class list, words
            return (current.iD, current.data_freq, current.compar_num, current.compar_num_len)
            
        else:
            key_alpha = key[key_indx]
            index = ord(key_alpha)-65+1
            if current.link[index] is not None:
                current = current.link[index]
            else:
                current.link[index] = Node1()
                current = current.link[index]
            data = self.addSequence_aux(current,key, key_indx+1, temp_compare_num)

        self.update_node_values(current,data)
        return (current.iD, current.data_freq, current.compar_num, current.compar_num_len)

    def query(self, q:str) -> str:
        """
        This function is used to return a string which have q as a prefix, a higher frequency in the database than
        any other string with q as a prefix, from the database. If two or more strings with prefix q are tied for 
        most frequent, the lexiographically least of them will be retrieved. If no such string exists, this function
        will return None.

        Pre-cond: q is a single(possibly empty) string of uppercase letters in uppercase [A-D]
        Post-cond: A string which have q as a prefix, a higher frequency in the database than any other string with q 
                   as a prefix, from the database will be retrieved. If two or more strings with prefix q are tied for 
                   most frequent, the lexiographically least of them will be retrieved. If no such string exists, this 
                   function will return None.

        Time-complexity: Best and worst case is O(len(q)) where q is the input string,q
        Explanation: O(len(q)(traverse according to the letters in q through the database to retrieve the string))
                   : O(len(q))

        Auxiliary-space complexity: O(1)
        Explanation: The function is an in place function and does not require any extra space.

        Space-complexity: Input + Auxiliary
                        : O(len(q)) + O(1)      where q is the input string,q
                        : O(len(q))
        """
        current = self.root
        if q == "":
            #if q is "", traverse to root and get the id and use it to retrieve the word from self.words
            if len(self.words) == 0:
                return None                                 #return None if there is no words added to the database
            return self.words[current.iD]

        for char in q:
            index = ord(char) - 65 +1
            if current.link[index] is None:
                return None
            else:
                current = current.link[index]
        return self.words[current.iD]

class Node2:
    """
    This class is a Node class which will be used in our OrfFinder class. Each node stores a link, which stores the possible childrens
    and also a list called suffix will store the suffix id that the node corresponds to.
    """
    def __init__(self) -> None:
        """
        This function is the __init__ function of Node2 class and sets each node's attributes to link and suffix.

        Time-complexity: Best and worst case is O(1)
        Explanation: The function runs at constant time.

        Auxiliary-space complexity: O(1)
        Explanation: The function is an in place function and always create a list of size 5 for self.link.

        Space-complexity: Input + Auxiliary
                        : O(1) + O(1)
                        : O(1)
        """
        self.link = [None]*5
        self.suffix = []                        #suffix will be a list of suffix id, which represents at which index of the word it appears at

class Trie:
    """
    This class is a class Trie and is used to create tries in our OrfFinder class.
    """
    def __init__(self) -> None:
        """
        The __init__ function just creates a Node object and assigns it to the Trie's root.

        Time-complexity: Best and worst case is O(1)
        Explanation: The function runs at constant time.

        Auxiliary-space complexity: O(1)
        Explanation: The function is an in place function.

        Space-complexity: Input + Auxiliary
                        : O(1) + O(1)
                        : O(1)
        """
        self.root = Node2()
    
    def insert(self, s:str, key_indx:int, suffix_id:int,reverse = False) -> None:
        """
        This function takes a string, s , a suffix_id, a key_indx which is the same value as suffix_id 
        and inserts this string into our trie in a reversed or non-reversed order based on the reverse input.
        If false, the string will be inserted in ascending order and if true, it will be inserted in descending order.

        Pre-cond: s will be a single non-empty string consisting only of uppercase [A-D].
        Post-cond: The input string will be inserted into the trie.

        Time-complexity: Best and worst case is O(n),         where n is the length of the input string,s
        Explanation: O(n)(recursively add each letters into the database, recursion depth is n and the 
                          operation at each level takes O(1)))
                   : O(n)

        Auxiliary-space complexity: O(n), where n is the length of input string, s
        Explanation: The function creates n nodes and each node has data of list of fixed sizes, hence O(n)

        Space-complexity: Input + Auxiliary
                        : O(n) + O(n),  where n is the length of input string,s 
                        : O(2n)
                        : O(n)
        """
        current = self.root
        if not reverse:
            data = self.insert_aux(current, s, key_indx, suffix_id)
        else:
            data = self.insert_aux_rev(current, s, key_indx, suffix_id)
        current.suffix.append(data)

    def insert_aux(self, current:Node2, key:str, key_indx:int, suffix_id:int) -> int:
        """
        This function is an auxiliary function of insert which will recursively call itself 
        to appropriately insert each letters of the key in ascending order according to the input key_indx into the database.
        It will also update the node's suffix list accordingly with the suffix_id.

        Pre-cond: key will be a single non-empty string consisting only of uppercase [A-D].
        Post-cond: The function will appropriately store the letter, key[key_indx] , which is apart of the key 
                   into the trie.

        Time-complexity: Best and worst case is O(1)
        Explanation: The function runs at constant time at each level of recursion.

        Auxiliary-space complexity: O(1)
        Explanation: The function is an in place function and does not require any extra space.

        Space-complexity: Input + Auxiliary
                        : O(1) + O(1)           
                        : O(1)
        """
        if key_indx >= len(key):                            #base case when we reached the end of the insert word
            if current.link[0] is not None:
                current = current.link[0]
            else:
                current.link[0] = Node2()
                current = current.link[0]
                current.suffix.append(suffix_id)            
            return suffix_id
            
        else:
            key_alpha = key[key_indx]
            index = ord(key_alpha)-65+1
            if current.link[index] is not None:
                current = current.link[index]
            else:
                current.link[index] = Node2()
                current = current.link[index]
            data = self.insert_aux(current,key, key_indx+1, suffix_id)

        current.suffix.append(data)
        return suffix_id

    def insert_aux_rev(self, current:Node2, key:str, key_indx:int, suffix_id:int) -> int:
        """
        This function is an auxiliary function of insert which will recursively call itself 
        to appropriately insert each letters of the key in descending order according to the input key_indx into the database.
        It will also update the node's suffix list accordingly with the suffix_id.

        Pre-cond: key will be a single non-empty string consisting only of uppercase [A-D].
        Post-cond: The function will appropriately store the letter, key[key_indx] , which is apart of the key 
                   into the trie.

        Time-complexity: Best and worst case is O(1)
        Explanation: The function runs at constant time at each level of recursion.

        Auxiliary-space complexity: O(1)
        Explanation: The function is an in place function and does not require any extra space.

        Space-complexity: Input + Auxiliary
                        : O(1) + O(1)           
                        : O(1)
        """
        if key_indx < 0:                            #base case when we reached the end of the insert word
            if current.link[0] is not None:
                current = current.link[0]
            else:
                current.link[0] = Node2()
                current = current.link[0]
                current.suffix.append(suffix_id)            
            return suffix_id
            
        else:
            key_alpha = key[key_indx]
            index = ord(key_alpha)-65+1
            if current.link[index] is not None:
                current = current.link[index]
            else:
                current.link[index] = Node2()
                current = current.link[index]
            data = self.insert_aux_rev(current,key, key_indx-1, suffix_id)

        current.suffix.append(data)
        return suffix_id
    
class OrfFinder:
    """
    This class allows us to get all the possible substrings of a word with a start as prefix and end as a suffix.
    """
    def __init__(self, genome:str) -> None:
        """
        This __init__ function takes in a string input, genome and creates a prefix of suffix tree and a suffix of prefix
        tree. This function also stores each letter of genome into a list and assigns it as a class attribute called words.

        Pre-cond: genome is a single non-empty string consisting only ofuppercase [A-D].
        Post-cond: Two tries will be created, a prefix of suffix trie and a suffix of prefix trie.

        Time-complexity: Best and worst case is O(N^2), where N is the length of genome.
        Explanation: O(N^2 + N^2) 
                   : O(N^2 (create prefix of suffix tree)+
                       N^2 (create suffix of prefix tree))
                   : O(2N^2)
                   : O(N^2)

        Auxiliary-space complexity: O(N), where N is the length of genome
        Explanation: O(N + N)
                   : O(N(auxiliary space for create prefix of suffix tree) + 
                     N(auxiliary space for create suffix of prefix tree))
                   : O(2N)
                   : O(N)

        Space-complexity: Input + Auxiliary
                        : O(N) + O(N),          where N is the length of genome
                        : O(N)
        """
        self.words = genome                                    
        self.trie1 = self.create_prefix_of_suffix_trie(genome)
        self.trie2 = self.create_suffix_of_prefix_trie(genome)

    def create_prefix_of_suffix_trie(self, genome:str) -> Trie:
        """
        This function takes a genome string and creates a prefix of suffix trie from the genome string.

        Pre-cond: genome is a single non-empty string consisting only of uppercase[A-D].
        Post-cond: A prefix of suffix trie will be created.

        Time-complexity: Best and worst case is O(N^2), where N is the length of the input genome string
        Explanation: O(N(N))
                   : O(N (loop through indexes of genome to get suffix id) (N (insert the word according to the suffix id in ascending order)))
                   : O(N (N))
                   : O(N^2)

        Auxiliary-space complexity: O(N), where N is the length of genome
        Explanation: O(N)
                   : O(N(space allocated to insert for all nodes))
                   : O(N)

        Space-complexity: Input + Auxiliary 
                        : O(N) + O(N)
                        : O(N)

        """
        trie = Trie()
        for i in range(len(genome)):
            trie.insert(genome,i,i, False)           #get all suffixes of the genome and insert it into the trie in ascending order
        return trie
            
    def create_suffix_of_prefix_trie(self, genome:str) -> Trie:
        """
        This function takes a genome string and creates a suffix of prefix trie from the genome string.

        Pre-cond: genome is a single non-empty string consisting only of uppercase[A-D].
        Post-cond: A suffix of prefix trie will be created.

        Time-complexity: Best and worst case is O(N^2), where N is the length of the input genome string
        Explanation: O(N(N))
                   : O(N (loop through indexes of genome to get suffix id) (N (insert the word according to the suffix id in descending order)))
                   : O(N (N))
                   : O(N^2)

        Auxiliary-space complexity: O(N), where N is the length of genome
        Explanation: O(N)
                   : O(N(space allocated to insert for all nodes))
                   : O(N)

        Space-complexity: Input + Auxiliary 
                        : O(N) + O(N)
                        : O(N)
        """

        trie = Trie()
        for i in range(len(genome)-1,-1,-1):
            trie.insert(genome, i, i, True)          #get all prefixes of genome and insert it into the trie in reversed order
        return trie
    
    def traverse(self, word:str,trie:Trie, reverse:bool) -> list:
        """
        This function takes a word and traverses into the trie according to the input word and returns
        the list of suffix id stored in the node.

        Pre-cond: word is a single non-empty string consisting of only uppercase[A-D]
        Post-cond: A list of suffix id will be returned.

        Time-complexity: Best and worst case is  O(n), where n is the length of the word
        Explanation: O(n(traverse through n nodes in the trie and returns the list of suffix id))

        Auxiliary-space complexity: O(1)
        Explanation: This function is an in place function and does not require any extra space.

        Space-complexity: Input + Auxiliary
                        : O(n) + O(1)
                        : O(n)
        """
        current = trie.root

        if not reverse:
            #if not reverse, travel according to the letters of word from index 0 ... n-1 and retrieve the suffix list                                     
            for char in word:
                index = ord(char) - 65 +1
                if current.link[index] is None:
                    return []
                else:
                    current = current.link[index]
        
        else:
            #if reverse, travel according to the letters of word from index n-1 ... 0 and retrieve the suffix list                                     
            for i in range(len(word)-1,-1,-1):
                char = word[i]
                index = ord(char) - 65 +1
                if current.link[index] is None:
                    return []
                else:
                    current = current.link[index]
        return current.suffix
    
    def find(self,start:str, end:str) -> list:
        """
        This function takes two strings start and end and returns a list of strings. This list contains all
        the substrings of genome which have start as a prefix and end as a suffix. Start and end does not overlap
        in the substring as well.

        Pre-cond: start and end are each a single non-empty string consisting of only uppercase[A-D]
        Post-cond: A list of strings will be returned. This list contains all the substrings of genome which have 
        start as a prefix and end as a suffix. Start and end does not overlap in the substring as well.

        Time-complexity: Best and worst case is O(len(start) + len(end) + U), where U is the number of characters in the output list.
        Explanation: O(len(start) + len(end) + U + U)
                   : O(len(start)(traverse through list and get list of suffix id) + 
                     len(end)(traverse through list and get list of suffix id) + 
                     U(compare between start_suffix and end_suffix list) + 
                     U(loop through result list))
                   : O(len(start) + len(end) + U)

        Auxiliary-space complexity: O(U), where U is the number of characters in the output list 
        Explanation: O(U + N + N + U )  where N is the length of genome
                   : O(U(space allocated for result) + N(space allocated for start_suffix) + N(space allocated for end_suffix)+
                     U(space allocated for ans))
                   : O(2N + 2U)       (However N is bounded by U)
                   : O(U)

        Space-complexity: Input + Auxiliary
                        : O(len(start) + len(end)) + O(U)
                        : O(len(start) + len(end) + U)     
        """
        start_suffix = self.traverse(start, self.trie1, False)          #retrieve the suffix list for start
        end_suffix = self.traverse(end, self.trie2, True)               #retrieve the suffix list for end
        result = []
        ans = []
        diff = len(start) + len(end) - 1

        #If one of the list is empty, means there is no substring
        if len(start_suffix) == 0 or len(end_suffix) == 0:
            return ans
        else:  
            #if the first element of end_suffix is smaller than first element of start_suffix, the values after that will still be smaller, and we won't find a substring
            if end_suffix[0] < start_suffix[0]:
                return ans
            #compare between both start_suffix and end_suffix values
            for i in range(len(end_suffix)):
                if end_suffix[i] < start_suffix[0]:
                    break 
                for j in range(len(start_suffix)):
                    if end_suffix[i] < start_suffix[j] or end_suffix[i] - start_suffix[j] < diff:   #as list is in order, we can terminate early in some occasions
                        break
                    elif end_suffix[i] - start_suffix[j] >= diff:             #check if substring is possible and does not overlap
                        result.append((start_suffix[j],end_suffix[i]))

        ans = []
        for data in result:
            start = data[0]
            end = data[1]
            ans.append(self.words[start:end+1])
        return ans





