from prettytable import PrettyTable

def menu():
    table = PrettyTable(["No", "Menu"])
    table.add_row(["1", "Arithmetic Sequence"])
    table.add_row(["2", "If only 2 terms info is given"])
    table.add_row(["3", "Arithmetic Series"])
    print(table)

menu()
print("")
choice = input("Select menu: ")
print("")

def arithmetic1():
    print("Arithmetic Sequence")
    print("-------------------------------------")
    Un = int(input("Enter term number (n): "))
    a = int(input("Enter the first term: "))
    b = int(input("Enter the common difference ⏩ (U2-U1): "))
    print("Un = a + (n-1)b")
    print("U{} = {} + ({}-1){}".format(Un, a, Un, b))
    print("U{} = {} + {}.{}".format(Un, a, Un - 1, b))
    print("U{} = {} + {}".format(Un, a, (Un - 1) * b))
    final_result = a + (Un - 1) * b
    print("U{} = {}".format(Un, final_result))
    print("")
    back = str(input("Type ('y') if you want to see another menu: "))
    
    if back == ('y'):
        menu()
        choice = int(input("Enter menu number: "))
    if choice == 1:
        return arithmetic1()
    if choice == 2:
        return arithmetic2()
    if choice == 3:
        return arithmetic3()

def arithmetic2():
    print("------------------------------")
    term1 = int(input("Enter term number (n): "))
    print("------------------------------")
    term2 = int(input("Enter another term number (n): "))
    print("------------------------------")
    print("U{} = ".format(term1))
    print("U{} = ".format(term2))
    print("-------------------------------------")
    value1 = int(input("Enter value of U{}: ".format(term1)))
    print("-------------------------------------")
    value2 = int(input("Enter value of U{}: ".format(term2)))
    print("-------------------------------------")
    print("")
    
    print("U{} = {}".format(term1, value1))
    print("a + {}-1 = {}".format(term1, value1))
    print("a + {}b = {}".format(term1 - 1, value1))
    print("")
    print("U{} = {}".format(term2, value2))
    print("a + {}-1 = {}".format(term2, value2))
    print("a + {}b = {}".format(term2 - 1, value2))
    print("")
    print("Finding value of b............(Elimination method)")
    print("")
    print("a + {}b = {}".format(term2 - 1, value2))
    print("a + {}b = {}".format(term1 - 1, value1))
    print("__________________--")
    print("    {}b = {}".format(value2 - value1, (term2 - 1) - (term1 - 1)))
    print("      b = ", value2 - value1, "/", (term2 - 1) - (term1 - 1))
    nb = value2 - value1
    i21 = (term2 - 1) - (term1 - 1)
    b_value = int(nb / i21)
    print("      b = ", (b_value))
    print("")
    print("Finding value of a............(Substitution method)")
    print("a + {}b = {}".format(term1 - 1, value1))
    print("a + {}.{} = {}".format(term1 - 1, b_value, value1))
    print(" a +", (term1 - 1) * b_value, "= ", value1)
    print("     a =", value1, "-", (term1 - 1) * b_value)
    print("     a =", value1 - (term1 - 1) * b_value)
    print("")
    final_term = int(input("Determine term number? : "))
    final_term1 = final_term - 1
    a_value = value1 - (term1 - 1) * b_value
    print("a + ( n - 1 ) b")
    print(a_value, "+ (", final_term, "- 1 ).", b_value)
    print(a_value, "+ (", final_term - 1, ").", b_value)
    print(a_value, "+", final_term1 * b_value)
    print(a_value + final_term1 * b_value)
    print("")
    print("Thus, term number", final_term, "is", a_value + final_term1 * b_value)
    print("")
    back = str(input("Type ('y') if you want to see another menu: "))
    if back == ('y'):
        menu()
        choice = int(input("Enter menu number: "))
    if choice == 1:
        return arithmetic1()
    if choice == 2:
        return arithmetic2()
    if choice == 3:
        return arithmetic3()

def arithmetic3():
    print("")
    print("Arithmetic Series")
    print("-------------------------------------")
    Sn = int(input("Determine the sum of the first n terms: "))
    print("-------------------------------------")
    a = int(input("Enter the first term: "))
    print("-------------------------------------")
    b = int(input("Enter the common difference ⏩ [calculate U2-U1]: "))
    print("-------------------------------------")
    print("")
    print("Sn = n/2(2a + (n-1)b)")
    total = int((Sn / 2) * (2 * a + (Sn - 1) * b))
    print("S{} = {}".format(Sn, total))
    print("")
    print("Thus, the sum of the first", Sn, "terms is", total)
    print("")
    back = str(input("Type ('y') if you want to see another menu: "))
    if back == ('y'):
        menu()
        choice = int(input("Enter menu number: "))
    if choice == 1:
        return arithmetic1()
    if choice == 2:
        return arithmetic2()
    if choice == 3:
        return arithmetic3()

if choice == ('1'):
    arithmetic1()
elif choice == ('2'):
    arithmetic2()
elif choice == ('3'):
    arithmetic3()
else:
    print("Menu not available")
