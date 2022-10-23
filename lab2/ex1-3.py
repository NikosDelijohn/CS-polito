#!/usr/bin/python3 

FIVE_DIGIT_INTEGER = 12345

def main():

    # The `//` operator is the DIV operation (the quotient of the division)
    ones       = FIVE_DIGIT_INTEGER // 1      # 12345
    tens       = FIVE_DIGIT_INTEGER // 10     # 1234 
    hundreds   = FIVE_DIGIT_INTEGER // 100    # 123
    thousands  = FIVE_DIGIT_INTEGER // 1_000  # 12
    tens_of_th = FIVE_DIGIT_INTEGER // 10_000 # 1 

    # The `%` operator is the MOD operation (the remainder of the division)
    print(f"{tens_of_th % 10}") # 1     MOD 10 = 1
    print(f"{thousands  % 10}") # 12    MOD 10 = 2
    print(f"{hundreds   % 10}") # 123   MOD 10 = 3
    print(f"{tens       % 10}") # 1234  MOD 10 = 4
    print(f"{ones       % 10}") # 12345 MOD 10 = 5

if __name__ == "__main__":
    main()