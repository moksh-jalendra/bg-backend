from rembg import remove, new_session
import os

# Pre-load the TINY model session (only ~4MB)
# This prevents the server from crashing during image processing
session = new_session("u2netp") 

def bg_remove(input_path):
    output_path = "photo-withoutbg.png"
    
    with open(input_path, 'rb') as i:
        input_data = i.read()
        # Process using the lightweight session
        output_data = remove(input_data, session=session)
        
        with open(output_path, 'wb') as o:
            o.write(output_data)
    
    return output_path