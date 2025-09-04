# 📊 Multiplication Table Generator

def get_number():
    while True:
        try:
            num = int(input("🔢 Enter a number to display its multiplication table: "))
            return num
        except ValueError:
            print("❌ Invalid input. Please enter a valid integer.")

def display_table(num):
    print(f"\n📈 Multiplication Table for {num}:\n")
    for i in range(1, 11):
        print(f"{num:>2} × {i:>2} = {num * i:>3}")
    print("\n✅ Done!")

if __name__ == "__main__":
    number = get_number()
    display_table(number)

