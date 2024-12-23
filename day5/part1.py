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


def check_rule(rule, update):
    num1 = rule.split("|")[0]
    num2 = rule.split("|")[1]
    if update.find(num1) == -1 or update.find(num2) == -1:  ## if a number from a rule isnt found in the update, ignore that rule
        return True
    elif update.find(num1) > update.find(num2): ## compare indexes to find if appears after second num
        return False
    else:
        return True



correct_order = []


for update in updates:
    rules_passed = 0
    for rule in rules:
        if check_rule(rule, update):
            rules_passed += 1
    if rules_passed == len(rules): # all rules passed
        correct_order.append(update)


sum = 0
for update in correct_order: 
    nums = update.split(",")
    print(nums)
    print(int(nums[int(len(nums)/2)]))
    sum += int(nums[int(len(nums)/2)])


print(sum)