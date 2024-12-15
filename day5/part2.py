f = open("input.txt")
rules = []
updates = []
nextsegment = False
for line in f.readlines():
    if line == "\n":
        nextsegment = True
    else:
        if not nextsegment:
            rules.append(line.strip())
        else:
            updates.append(line.strip())


def correct_for_rule(rule, update):
    num1 = rule.split("|")[0]
    num2 = rule.split("|")[1]
    if update.find(num1) == -1 or update.find(num2) == -1:  ## if a number from a rule isnt found in the update, ignore that rule
        return True
    elif update.find(num1) > update.find(num2): ## compare indexes to find if appears after second num
        return False
    else:
        return True



correct_order = []
incorrect_order = []
for update in updates:
    rules_passed = 0
    for rule in rules:
        if correct_for_rule(rule, update):
            rules_passed += 1
    if rules_passed == len(rules): # all rules passed
        correct_order.append(update)
    else: 
        incorrect_order.append(update)




corrected = []
for update in incorrect_order:
    rules_passed = 0
    nums = update.split(",")
    i = 0
    while i < len(rules)-1:
        if correct_for_rule(rules[i], ",".join(nums)):
            # corrected.append(update)
            pass
        else:
            num1 = rules[i].split("|")[0]
            num2 = rules[i].split("|")[1]
            nums.remove(num2)
            nums.insert(nums.index(num1)+1, num2)
            i = 0 # run thru all rules again
        i += 1

    corrected.append(",".join(nums)) 
    

   
print(corrected)
sum = 0
for update in corrected: 
    nums = update.split(",")
    sum += int(nums[int(len(nums)/2)])

print(sum)
