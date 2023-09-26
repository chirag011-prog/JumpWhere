def convert_to_positive_coordinates(input_coords):
    
    min_x = min(coord[0] for coord in input_coords)
    min_y = min(coord[1] for coord in input_coords)
    
   
    x_offset = abs(min_x)
    y_offset = abs(min_y)
    
    
    output_coords = [(coord[0] + x_offset, coord[1] + y_offset) for coord in input_coords]
    
    return output_coords

input_coords = [(1, -2), (-2, 4), (-1, -1), (-8, -3), (0, 4), (10, -3)]
output_coords = convert_to_positive_coordinates(input_coords)
print(output_coords)
