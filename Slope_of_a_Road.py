# (c) 2025 Kristine May R. Guarte and Evan Miguel R. Montuya
# E. Slope of a Road

def main():
    rise = float(input("What is the rise of the road (m)?"))
    horizontal_distance = float(input("What is the horizontal distance of the roam (m)?"))
    
    slope = (rise / horizontal_distance) * 100
    
    print(f"\nSo, the slope of the road is {slope:,.2f} %.")
    
if __name__ == "__main__":
 main()
