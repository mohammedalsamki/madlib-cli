import re


def read_template():
    """
    Returns the mad_temp_result.txt file 
    """
    file = open("madlib_cli/assets/mad_temp_result.text",'r')
    cont = file.read()
    return cont  
  
def parse_template(const):
  list =[]
  resive =re.findall(r'\{.*?\}', const)
  for i in resive:
        list.append(i.strip("{ }"))   
  return list

def merge(const , words):  

   
    list = parse_template(const)  
    
    return (re.sub(r' {[^}]*}',' {}',const)).format(*words) 

def copyFile_from_text(texts):
    print(texts)
    file = open('assets/filled_template.txt','w')
    file.write(texts)

if __name__ == "__main__":
    print("Welcome to Madlib Game :)")
    print("we will asked you to input some words to play this game!")
    cont = read_template()
    list = parse_template(cont)
    words=[]
    for i in range(len(list)):
        words.append(input("enter a {} ".format(list[i])))
    copyTo = merge(cont, words)
    copyFile_from_text(copyTo)
