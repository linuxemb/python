acro = ['BY THE WAY', 'LAUGHT OF LIGHT']
acro_len = [3, 3]
keys = ['BY', 'LAUGHT']
text = "BY THE WAY I THINK LAUGHT OF LIGHT I DI" # LIGHT BY THE WAY"
list_text = text.split()
#list_text = text.split((" "))

cnt = 0
step = 0 # count where it is itering now
print(f"list_text {list_text}")
# def find_all_key1():
#     """ find all key in keys, return the index of each occurrence
#         idx[] list keep track all index of key in list text
#         here idx [] = [0,5] 
#     """
#     global cnt
#     idx = []list_text
#                 cnt +=1
#                 iter = list_text.index(each)
#              #   breakpoint()
#                 idx.append(list_text.index(each))
#                 print(f'idx = {idx}')
#                 print(list_text.index(each))
#                 print(f'step={step}')
#         print ('iter, cnt') #
#         print(iter, cnt)
    #print (f'iter, cnt = {iter}')_list}')
#         print(f'each= {each}')_list}')
#             cnt +=1
#             iter = list_text.index(each)found_word
#            # breakpoint()
#             idx.append(list_text.index(each))
#             print(f'idx = {idx}')text.index('BY')
#     print(iter, cnt)
#     #print (f'iter, cnt = {iter}')
#     for e in idx:
#         print(idx[e],end = '')
 #   return    idx  




def upCase(string):
    """  define newstring append each old string to it 
        transfer to upper if is letters

    """
    newstring = ""
    for i in string:
        ordcode = ord (i)
        if (ordcode >= 97  and ordcode <= 122):
            newstring += chr(ordcode -32)
        else:
            newstring += i
    return newstring


def replace(ph, replace_from, replace_to):
    """ find location of replace_From in string and replace it with replace_To
            ex replace("I think BY the way it is ...", "BY THE WAY", "BTW")
    """
    for i in range (len(replace_from)) :     # take int as iterator
        if (ph [i: i+len(replace_from)] == replace_from): # retrive the slice of replace from phrase
            ph = ph[:i] + replace_to + ph[i+ len(replace_from) : ]
    print(f'\nreplace from - {replace_from}\n')        
    print(f'\n ---replace {ph} with {replace_from} to {replace_to}\n---' )
    return ph       

 
 
def acro(string):
    """ change string occurence with the supported phrases to acronms corresponsding
    """
    #list of phrases and acronyms where the index of each has a relation
    phrases = ["BY THE WAY", "LAUGH OUT LOUD", "OH MY GOD", "FOR YOUR INFORMATION", "AS FAR AS I KNOW"]
    acronyms = ["BTW", "LOL", "OMG", "FYI", "AFAIK"]
    string = upCase(string)
    counter = 0
    
    #loops thorugh the phrases and sees if there is a match, if there is a match it will call the replace function
    for i in phrases:
        while i in string:
        #for j in string:

            string = replace(string, phrases[counter], acronyms[counter])
        #adds 1 to counter to get to next index
        counter += 1
    print(f'string in acor= {string}')
    return string



def find_words (text, search):
    dtext = text.split()
    dsearch = search.split()

    #breakpoint()
    found_word = 0
    idx_list = []
    for text_word in dtext:
        for search_word in dsearch:
            if  search_word == text_word:
                found_word +=1
                idx = text.index(search_word)
                print(f'idx ={idx}')
                idx_list.append(idx)

       
        print(f'idx_list= [ {idx_list}]')
    print(f'found_word = {found_word}')
    if found_word == len(dsearch):
        print(f'found the {search} in {text} ')
        return found_word,idx_list
    else :
        return False

def main(): 
    userString = input("Enter a String: ")
    print()
    print("transfer")
    #getting rid of basic punctuation
    punc = [33,34,39,44,45,46,58,59,63]
    for i in userString:   #### from user string iter and replace 
        if ord(i) in punc:
            userString = replace(userString,i,"")  # change punc to space
    
    print(acro(userString))
# def get_slice(idx):
#     global acro_len, text
#     for each in range(len(key_idx)):
#         breakpoint()

#     # print (f'each = {each}') 
#         lenth = acro_len[each]
#         print(f'acro_len[0] lenth ; {lenth}')
#         slice_list = text [key_idx[each]:lenth] #take the "by the way" slice out from text_list
#         print(f'slice_list= {slice_list}')
#     return slice_list
#  dtext = text.split()
#  dsearch = search.split()

# look_for = 'BY THE WAY'
# lensearch,idx_list =find_words(text, 'BY THE WAY')
# lensearch =find_words(text,  look_for)
# new_list =[]
#reslut= lensearch =find_words(text, 'LAUGHT OF LIGHT')
# print(f'lensearch = {lensearch}')

#list_text_new = 
# list_text[0:3] = 'B'
# list_text [3:7] = 'T'
# # list_text [7] = 'W'
# sl= ['BTW']
# # taking slice [ 0--7] replace with BTW
# print(f'--list_text ={list_text}----' )

# start = idx_list[0]
# len_look_for = len[look_for]
#sice_list= {slice_list}')
# #list_before = list_text[:0]
# list_before = list_text[0:start]
# print(f'--list_before ={list_before}----' )

# list_slice =  sl # list_text [0:7]


# list_after = list_text [3:-1]
# breakpoint()
# print(f'--list_after ={list_after}----' )
# new_list = list_before + list_slice + list_after
# print("==== new list ==={new_list}")
# print(new_list)

#print(reslut)
# key_idxreslut= find_all_key1()  ## return the char  location is not ok 
# print("key_idx")
# print(key_idx)


# need to slice the list_text based on the idx from key_idx list one by one 
# then compare the slice list with the acro
#get_slice(key_idx)


    #global acro_len, text


# for each in range(len(key_idx)):
#     breakpoint()

#     lenth = acro_len[each]
#     print(f'acro_len[0] lenth ; {lenth}')
#     slice_list = text [key_idx[each]:lenth] #take the "by the way" slice out from text_list
#     print(f'slice_list= {slice_list}')

main()