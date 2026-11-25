
# Manufacturing Cost and Profitability Analysis

# Number of products
n = int(input("Enter number of products: "))

# Profit target percentage
profit_target = float(input("Enter required profit target percentage: "))

# Lists to store product details
product_names = []
total_costs = []
selling_prices = []
profits = []

for i in range(n):

    print("\nEnter details of Product", i + 1)

    name = input("Enter product name: ")

    quantity = int(input("Enter production quantity: "))
    material_cost = float(input("Enter material cost per unit: "))
    labour_cost = float(input("Enter labour cost per unit: "))
    wastage_percent = float(input("Enter wastage percentage: "))
    machine_cost = float(input("Enter total machine cost: "))
    selling_price = float(input("Enter selling price per unit: "))

    # Validate input details
    if (quantity <= 0 or material_cost < 0 or
        labour_cost < 0 or wastage_percent < 0 or
        wastage_percent > 100 or machine_cost < 0 or
        selling_price < 0):

        print("Invalid production details!")
        continue

    # Calculate material cost
    total_material = material_cost * quantity

    # Calculate labour cost
    total_labour = labour_cost * quantity

    # Calculate wastage cost
    wastage_cost = total_material * wastage_percent / 100

    # Calculate total manufacturing cost
    total_cost = total_material + total_labour + wastage_cost + machine_cost

    # Calculate total selling amount
    total_selling = selling_price * quantity

    # Calculate profit or loss
    profit = total_selling - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percent = (profit / total_cost) * 100
    else:
        profit_percent = 0

    # Store product details
    product_names.append(name)
    total_costs.append(total_cost)
    selling_prices.append(total_selling)
    profits.append(profit)

    # Display manufacturing details
    print("\n========== MANUFACTURING REPORT ==========")

    print("Product Name:", name)
    print("Production Quantity:", quantity)
    print("Material Cost: Rs.", round(total_material, 2))
    print("Labour Cost: Rs.", round(total_labour, 2))
    print("Wastage Cost: Rs.", round(wastage_cost, 2))
    print("Machine Cost: Rs.", round(machine_cost, 2))

    print("------------------------------------------")

    print("Total Manufacturing Cost: Rs.", round(total_cost, 2))
    print("Total Selling Amount: Rs.", round(total_selling, 2))
    print("Profit / Loss: Rs.", round(profit, 2))
    print("Profit Percentage:", round(profit_percent, 2), "%")

    # Check profit target
    if profit_percent >= profit_target:
        print("Status: Profit Target Achieved")

    elif profit > 0:
        print("Status: Profit Earned but Target Not Achieved")

    else:
        print("Status: Loss Occurred")

# Display final summary
print("\n========== PRODUCTION SUMMARY ==========")

for i in range(len(product_names)):

    print("\nProduct:", product_names[i])
    print("Total Cost: Rs.", round(total_costs[i], 2))
    print("Selling Amount: Rs.", round(selling_prices[i], 2))
    print("Profit / Loss: Rs.", round(profits[i], 2))

print("\nManufacturing Analysis Completed!")
