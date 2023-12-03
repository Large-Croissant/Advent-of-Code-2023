import sys

def setup():
    r1 = {
        "zero" : "0",
        "one" : "1",
        "two" : "2",
        "three" : "3",
        "four" : "4",
        "five" : "5",
        "six" : "6",
        "seven" : "7",
        "eight" : "8",
        "nine" : "9"
    }
    r2 = {
        "zero"[::-1] : "0",
        "one"[::-1] : "1",
        "two"[::-1] : "2",
        "three"[::-1] : "3",
        "four"[::-1] : "4",
        "five"[::-1] : "5",
        "six"[::-1] : "6",
        "seven"[::-1] : "7",
        "eight"[::-1]:"8",
        "nine"[::-1] : "9"
    }    
    return r1, r2

def proc_line(line:str, rev:bool):
    num_dict, rev_num_dict = setup()
    using_spell = num_dict if not rev else rev_num_dict
    for i in range(len(line)):
        if str.isdigit(line[i]):
            return line[i]
        else:
            for j in range(i, len(line[i::1])+i):
                if line[i:j] in using_spell:
                    return using_spell[line[i:j]]
                
def full_proc_line(line):
    return (proc_line(line, False), proc_line(line[::-1], True))

def main(args):
    nums = []
    if len(args) > 2:
        print(f"Too many arguments")
        exit(1)
    elif len(args) == 2:
        in_file = args[1]
    else:
        in_file = input("Enter the file to be processed: ")
    print(f"Processing file \"{in_file}\"")
    
    # proc file
    with open(in_file) as file:
        for line in file:
            nums.append(full_proc_line(line))
    
    # proc nums
    sum = 0
    for n in nums:
        sum += int(f"{n[0]}{n[1]}")
    print(f"The sum is {sum}")
            


if __name__ == "__main__":
    main(sys.argv)