def calculate_sirup_replacement(sirup_in_glass, current_dilution, recommended_dilution):
  sirup_to_replace = (sirup_in_glass * (current_dilution - recommended_dilution)) / recommended_dilution
  return sirup_to_replace

sirup_in_glass = float(input("Enter the amount of sirup in your glass (in ml): "))
current_dilution = float(input("Enter the current dilution of the sirup in your glass (%): "))
recommended_dilution = float(input("Enter the recommended dilution (%): "))

sirup_to_replace = calculate_sirup_replacement(sirup_in_glass, current_dilution, recommended_dilution)

print(f"Replace {sirup_to_replace:.2f} ml of your sirup with water.")
