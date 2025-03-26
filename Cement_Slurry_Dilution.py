# (c) 2025 Kristine May R. Guarte and Evan Miguel R. Montuya
# A. Cement Slurry Dilution

def main():
    volume_2 = float(input("What is the final volume of the solution (L)?"))
    concentration_1 = float(input("What is the initial concentration of the solution (g/L)?"))
    concentration_2 = float(input("What is the final comcentration of the solution (g/L)?"))
    
    volume_1 = (concentration_2 * volume_2) / concentration_1
    
    print(f"\nSo, you need {volume_1:,.2f} liters of the original slurry.")
    
if __name__ == "__main__":
 main()