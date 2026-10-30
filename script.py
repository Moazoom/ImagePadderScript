from PIL import Image

def add_white_border(input_path, output_path, final_size=512, border_width=120):
    inner_size = final_size - (2 * border_width)
    icon = Image.open(input_path).convert("RGBA")
    icon.thumbnail((inner_size, inner_size), Image.Resampling.LANCZOS)
    
    final_image = Image.new("RGBA", (final_size, final_size), (255, 255, 255, 255))

    icon_width, icon_height = icon.size
    x = (final_size - icon_width) // 2
    y = (final_size - icon_height) // 2

    final_image.paste(icon, (x, y), icon)
    
    final_image.save(output_path, "PNG")
    print("Completed Successfully")

if __name__ == "__main__":
    input_file = "input.png"
    output_file = "icon.png"
    
    add_white_border(input_file, output_file, final_size=512, border_width=120)