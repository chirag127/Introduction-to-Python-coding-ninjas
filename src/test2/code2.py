def minMaxLengthWords(inp):
    length = len(inp)
    si = ei = 0
    min_length = length
    min_start_index = max_length = max_start_index = 0
     
    while ei <= length:
        if (ei < length) and (inp[ei] != " "):
            ei += 1
        else:
            curr_length = ei - si
             
            if curr_length < min_length:
                min_length = curr_length
                min_start_index = si
                
            if curr_length > max_length:
                max_length = curr_length
                max_start_index = si
            ei += 1
            si = ei
                
    minWord = inp[min_start_index :
                  min_start_index + min_length]
        
    maxWord = inp[max_start_index : max_length]
     
    print(minWord)
    
     
# Driver Code
a = str(input())
minMaxLengthWords(a)
