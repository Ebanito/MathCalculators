# (c) 2025 Kristine May R. Guarte and Evan Miguel R. Montuya
# D. Load Distribution on a Beam

def main():
    uniform_load = float(input("What is the uniform load of the beam (N/m)?"))
    length = float(input("What is the Length of the beam (m)?"))
    
    force = uniform_load * length
    
    print(f"\nSo, the total load acting on the beam is {force:,.2f} N.")
    
if __name__ == "__main__":
 main()