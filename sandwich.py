import pyinputplus as pyip
print('Let\'s make a sandwich')
print('DO you want bread or bun?')
bread = pyip.inputMenu(['bread', 'bun'])
print('What meat/protein do you want?')
meat = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'])
print('Do you want cheese?')
cheese = pyip.inputYesNo
if cheese == 'yes':
    print('What type of cheese do you want?')
    cheeseChoice = pyip.inputMenu(['swiss', 'cheddar', 'mozzarella'])
print('Do you want mustard?')
mustard = pyip.inputYesNo
print('Do you want mayo?')
mayo = pyip.inputYesNo
print('Do you want lettuce?')
lettuce = pyip.inputYesNo
print('Do you want tomato?')
tomato = pyip.inputYesNo
print('How many sandwiches do you want?')
sandwichNum = pyip.inputNum(min = 1)

 
    

