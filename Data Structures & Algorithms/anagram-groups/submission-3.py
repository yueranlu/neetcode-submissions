class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # create a hashmap: key = tuple where each index = where letter woudl be and, and the value = the the number of occurences of a certain letter
                        #   Value = list of words that have that arrangement
        # creates dictionary with 
        res = defaultdict(list)

        #iterate through each word in the list
        for word in strs:
            count = [0]*26
            # create empty 26 index list
            for letter in word:
            #iterate through each letter in the word:
                count[ord(letter)-ord("a")] += 1
                # add 1 to index when a letter appears:
            res[tuple(count)].append(word)
        return list(res.values())
            #everytime this same list appears add it to the hashmap

        #when done iterating return only the values of the hashmap




    



        