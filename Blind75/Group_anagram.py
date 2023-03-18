class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # #creating a hashmap
        # anagramDict={}
        
        # #result variable to store the output
        # result=[]
        
        
        # #iterating through the string
        # for word in strs:
        #     #sorting the string value and store it as key
        #     key=sorted(word)
            
        #     #we cannot keep the key as a string , so we can use tuple which is immutable
            
        #     key=tuple(key)
        #     #if not in hashmap then add it as a key
        #     if key not in anagramDict:
        #         #just insert the word if it is encountered first
        #         anagramDict[key]=[str(word)]
            
        #     #if the word is already there then append it to the list
        #     else:
        #          anagramDict[key].append(str(word))
                
        # for k,v in anagramDict.items():
        #     result.append(v)
            
        # return result 
        #create a hashmap
        hashmap={}  

        
        #iterate through the strs string 
        for s in strs:
            #if the sorted values are same then add i to sortedstr
            sortedStr = "".join(sorted(s))
            #if the sorted string is already is hashmap
            if sortedStr in hashmap:
                #then return the value of the specific key
                hashmap[sortedStr].append(s)

            #if the sorted string is not in hashmap add the key to the hashmap
            else:
                hashmap[sortedStr] = [s]
        #returning all the hashmap values
        result = hashmap.values()

        return result
