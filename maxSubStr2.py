# Find the longer substring inside a string that contains no repeated characters

def max_substr(inputstr):
    index1, indexmax = 0,0
    maxlen=0
    for c in inputstr:
        characters=set()
        substr=""
        for ch in inputstr[index1:]:
            if (ch not in characters):
                characters.add(ch)
                substr+=ch
            else:
                break
        if (len(substr) > maxlen):
            indexmax=index1
            maxlen=len(substr)
        index1+=1
    return(inputstr[indexmax:indexmax+maxlen])

  mystring="abcdabefghijklmaopq"
  print(max_substr(mystring))
