"""
In this script, you will be able to calculate
the number of blocks needed to fence any plot of land
"""

#Dimension of the plot of land
length_of_land = int(input("Please enter the length of the land in feet: "))
width_of_land = int(input("Please enter the width of the land in feet: "))
length_of_land = (length_of_land*2) + (width_of_land*2)
print("The length of the land in feet is: ", length_of_land)
feet_to_meter = round(length_of_land * 0.3048)
length_of_land = feet_to_meter
print(f"The length of the land in meter is: {length_of_land} metres")

#Space for the gate
gate_space = int(input("Please enter the space for gate in feet: "))

# Convert feet to metre
gate_space_in_metres = round(gate_space * 0.3048)
print(f"The space alloted for gate in metres is: {gate_space_in_metres} metres")

total_land_space = length_of_land - gate_space_in_metres
print(f"The total land space to fence in metres is: {total_land_space} metres")

"""
Calculate the number of pillars needed
within a space of 3-3 metres
"""
num_of_columns = round(total_land_space / 3)
print(f"The number of columns needed are: {num_of_columns}")


"""
Dimension of blocks
6 inches block: 450mm x 150mm
9 inches block: 450mm x 225mm
"""
size_of_block = int(input("Please enter the length of the block in mm: "))
block_size_meters = (size_of_block / 1000)
print(block_size_meters)
num_of_coaches = int(input("Please enter the number of coaches: "))
num_of_blocks_first_coach = round(total_land_space / block_size_meters)
print(f"The number of needed blocks for first coach is: {num_of_blocks_first_coach}")
total_num_of_blocks = num_of_blocks_first_coach * num_of_coaches
print(f"Total number of blocks needed for {num_of_coaches} coaches are: {total_num_of_blocks}") 
allowance = round((total_num_of_blocks * 0.1) + total_num_of_blocks)
print(f"The grand total number of blocks needed for a {length_of_land} x {width_of_land} are: {allowance}")
