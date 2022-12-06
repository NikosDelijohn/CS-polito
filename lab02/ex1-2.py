#!/usr/bin/python3

def main():

    # Careful, function input() returns a STRING. In order to use it in 
    # numerical operations you must convert it (cast it) to an INTEGER/FLOAT via int()/float().
    R1_str = input("Provide R1 in Ω: ")
    R1_float = float(R1_str)

    R2_str = input("Provide R2 in Ω: ")
    R2_float = float(R2_str)

    R3_str = input("Provide R3 in Ω: ") 
    R3_float = float(R3_str)

    # R2 and R3 are in parallel 
    # PARALLEL: 1/Rtotal = 1/R1 + 1/R2
    R2_R3_total = (R2_float * R3_float) / (R2_float + R3_float)

    # R1 and R2_R3_total are in series 
    # SERIES: Rtotal = R1 + R2   
    R_total = R1_float + R2_R3_total

    print(f"The total Resistance of the Circuit is {R_total} Ω")    

if __name__ == "__main__":
    main()