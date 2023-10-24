#!/usr/bin/python3
def multiple_returns(sentence):
    tuple = ()
    if len(sentence) == 0:
     tuple = None
    else:
       tuple = len(sentence), sentence[0]
       return tuple
    

    if __name__ == "__main__":
       
        sentence = "At school, I learnt C!"
        length, first = multiple_returns(sentence)
        print("Length: {:d} - First character: {}".format(length, first))
