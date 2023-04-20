from difflib import SequenceMatcher
  
with open('7TH-A.txt') as first_file,open('7TH-B.txt') as second_file:
      
    # Reading Both Text Files
    file1 = first_file.read()
    file2 = second_file.read()
      
    # Comparing Both Text Files
    ab = SequenceMatcher(None, file1,
                         file2).ratio()
      
    # converting decimal output in integer
    result = int(ab*100)
    print(f"{result}% Plagiarized Content")