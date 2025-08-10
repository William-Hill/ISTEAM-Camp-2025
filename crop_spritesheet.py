from PIL import Image
import os

# Define the sprite sheets you want to process
sprite_sheets = [
    # Gojo spritesheets
    ("gojo_frames/stand/gojo-stand.png", "output_stand"),
    ("gojo_frames/walk/gojo-walk.png", "output_walk"),
    ("gojo_frames/stance-2/stance-2.png", "output_stance_2"),
    ("gojo_frames/intro/intro.png", "output_intro"),
    ("gojo_frames/kick/kick.png", "output_kick"),
    ("gojo_frames/heavy-attack/heavy_attack.png", "output_heavy_attack"),
    ("gojo_frames/light-attack/light_attack.png", "output_light_attack"),
    ("gojo_frames/jump/jump.png", "output_jump"),
    ("gojo_frames/crouch/gojo-crouch.png", "output_crouch"),
    ("gojo_frames/dash/gojo-dash.png", "output_dash"),
    # Jin-Woo spritesheets
    ("jin-woo_frames/stand/Untitled 4.png", "output_jinwoo_stand"),
    ("jin-woo_frames/run/run.png", "output_jinwoo_run"),
    ("jin-woo_frames/jump/jump.png", "output_jinwoo_jump"),
    ("jin-woo_frames/light-attack/light-attack.png", "output_jinwoo_light_attack"),
    ("jin-woo_frames/heavy-attack/heavy_attack.png", "output_jinwoo_heavy_attack")
]

# Frame dimensions, counts, and offsets for each sheet
# Format: (width, height, count, x_offset) for each action
frame_configs = [
    # Gojo frame configs
    (33, 68, 4, 0),   # gojo-stand
    (35, 68, 8, 0),   # gojo-walk
    (40, 68, 1, 0),   # stance-2 - single frame, wider
    (40, 68, 8, 0),   # intro - estimated 8 frames
    (40, 68, 6, 0),   # kick - estimated 6 frames
    (45, 68, 5, 0),   # heavy_attack - estimated 5 frames
    (40, 68, 6, 0),   # light_attack - estimated 6 frames
    (40, 68, 4, 5),   # jump - with 5px x-offset to center frames 3 and 4
    (40, 68, 4, 0),   # crouch - wider to prevent cutting off frames 3 and 4
    (40, 68, 3, 0),   # dash - estimated 3 frames
    # Jin-Woo frame configs (estimated - will need adjustment)
    (35, 68, 4, 0),   # jinwoo-stand - taller frames to include feet
    (53, 68, 8, 0),   # jinwoo-run - larger frames
    (60, 68, 4, 0),   # jinwoo-jump - wider frames
    (70, 68, 6, 0),   # jinwoo-light-attack
    (45, 68, 5, 0)    # jinwoo-heavy-attack
]

for (sheet_file, output_folder), (frame_width, frame_height, frames, x_offset) in zip(sprite_sheets, frame_configs):
    os.makedirs(output_folder, exist_ok=True)
    
    sheet = Image.open(sheet_file).convert("RGBA")
    sheet_width, sheet_height = sheet.size
    
    for i in range(frames):
        # Apply different offsets for different frames
        if sheet_file == "gojo_frames/jump/jump.png":
            # Jump animation: frames 3 and 4 need more offset
            if i >= 2:  # frames 3 and 4 (0-indexed: 2, 3)
                frame_offset = 18  # more offset for frames 3 and 4
            else:
                frame_offset = 5   # less offset for frames 1 and 2
        elif sheet_file == "gojo_frames/light-attack/light_attack.png":
            # Light attack animation: frames 4, 5, and 6 need more offset
            if i == 3:  # frame 4 (0-indexed: 3)
                frame_offset = 10  # offset for frame 4
            elif i >= 4:  # frames 5 and 6 (0-indexed: 4, 5)
                frame_offset = 20  # more offset for frames 5 and 6
            else:
                frame_offset = 0   # no offset for frames 1, 2, and 3
        elif sheet_file == "gojo_frames/heavy-attack/heavy_attack.png":
            # Heavy attack animation: different offsets for different frames
            if i == 0:  # frame 1 (0-indexed: 0)
                frame_offset = -10  # more negative offset to make frame 1 less wide
            elif i == 2:  # frame 3 (0-indexed: 2)
                frame_offset = 0   # less offset for frame 3 to shift it to the right
            elif i == 3:  # frame 4 (0-indexed: 3)
                frame_offset = 20  # more offset for frame 4 to make it wider
            elif i == 4:  # frame 5 (0-indexed: 4)
                frame_offset = 25  # more offset for frame 5 to shift it to the left
            else:
                frame_offset = -10  # more negative offset to shift frame 2 further left
        elif sheet_file == "gojo_frames/intro/intro.png":
            # Intro animation: different offsets for different frames
            if i == 0:  # frame 1 (0-indexed: 0)
                frame_offset = -5  # negative offset to shift frame 1 left
            elif i == 1:  # frame 2 (0-indexed: 1)
                frame_offset = -10  # more negative offset to shift frame 2 further left
            elif i == 2:  # frame 3 (0-indexed: 2)
                frame_offset = 10  # positive offset to make frame 3 wider
            elif i == 3:  # frame 4 (0-indexed: 3)
                frame_offset = 15  # more positive offset to make frame 4 wider
            else:
                frame_offset = 0   # no offset for frames 5-8
        elif sheet_file == "jin-woo_frames/stand/Untitled 4.png":
            # Jin-Woo stand animation: different offsets for different frames
            if i == 0:  # frame 1 (0-indexed: 0)
                frame_offset = 8  # more negative offset to shift frame 1 further left
            elif i == 2:
                frame_offset = 20
            elif i == 3:
                frame_offset = 30
            else:
                frame_offset = 15  # negative offset to shift other frames left
        elif sheet_file == "jin-woo_frames/run/run.png":
            # Jin-Woo run animation: frame 1 needs to be shifted left
            if i == 0:  # frame 1 (0-indexed: 0)
                frame_offset = 8  # negative offset to shift frame 1 left
            elif i == 1:
                frame_offset = 37
            elif i == 2:
                frame_offset = 60
            elif i == 3:
                frame_offset = 95
            elif i == 4:
                frame_offset = 120
            elif i == 5:
                frame_offset = 145
            elif i == 6:
                frame_offset = 170
            elif i == 7:
                frame_offset = 207
            else:
                frame_offset = 0  # no offset for other frames
        elif sheet_file == "jin-woo_frames/jump/jump.png":
            # Jin-Woo jump animation: frame 1, 2, and 3 need to be shifted right
            if i == 0:  # frame 1 (0-indexed: 0)
                frame_offset = 10  # positive offset to shift frame 1 right
            elif i == 1:  # frame 2 (0-indexed: 1)
                frame_offset = 15  # positive offset to shift frame 2 right
            elif i == 2:  # frame 3 (0-indexed: 2)
                frame_offset = 35  # positive offset to shift frame 3 right
            else:
                frame_offset = 0  # no offset for other frames
        elif sheet_file == "jin-woo_frames/light-attack/light-attack.png":
            # Jin-Woo light attack animation: frame 1 needs to be shifted right
            if i == 0:  # frame 1 (0-indexed: 0)
                frame_offset = 5  # positive offset to shift frame 1 right
            elif i == 1:
                frame_offset = 10
            elif i == 2:
                frame_offset = 15
            elif i == 3:
                frame_offset = 20
            else:
                frame_offset = 0  # no offset for other frames
            y_offset = 10  # shift Jin-Woo up in the frame
        else:
            frame_offset = x_offset
        
        x_start = (i * frame_width) + frame_offset
        x_end = ((i+1) * frame_width) + frame_offset
        
        # Add vertical offset for Jin-Woo frames to crop lower
        if 'y_offset' not in locals():
            y_offset = 0
            if sheet_file == "jin-woo_frames/stand/Untitled 4.png":
                y_offset = 5  # Start cropping 5 pixels lower to include more feet
            elif sheet_file == "jin-woo_frames/stand/Untitled 4_2.png":
                y_offset = 5  # Start cropping 5 pixels lower to include more feet
        
        box = (x_start, y_offset, x_end, frame_height + y_offset)
        frame = sheet.crop(box)
        
        # Convert background to transparent
        # Get multiple background color samples for better detection
        bg_colors = [
            frame.getpixel((0, 0)),  # top-left
            frame.getpixel((frame.width-1, 0)),  # top-right
            frame.getpixel((0, frame.height-1)),  # bottom-left
            frame.getpixel((frame.width-1, frame.height-1))  # bottom-right
        ]
        
        # Create a new image with transparency
        transparent_frame = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        
        # Copy pixels, making background transparent
        for x in range(frame.width):
            for y in range(frame.height):
                pixel = frame.getpixel((x, y))
                # Check if pixel matches any of the background colors
                is_background = False
                for bg_color in bg_colors:
                    if (abs(pixel[0] - bg_color[0]) < 25 and 
                        abs(pixel[1] - bg_color[1]) < 25 and 
                        abs(pixel[2] - bg_color[2]) < 25):
                        is_background = True
                        break
                
                if is_background:
                    transparent_frame.putpixel((x, y), (0, 0, 0, 0))
                else:
                    transparent_frame.putpixel((x, y), pixel)
        
        # Extract just the filename without path and extension
        filename = os.path.basename(sheet_file).split('.')[0]
        transparent_frame.save(os.path.join(output_folder, f"{filename}_{i+1}.png"))

print("Frames have been successfully sliced into individual PNGs!")
