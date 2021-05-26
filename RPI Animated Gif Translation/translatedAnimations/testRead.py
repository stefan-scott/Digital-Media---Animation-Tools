def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

data = open("sample5_hex.anim", "r")
n_frames = int(data.readline())

frames = []
for a in range(n_frames):
    cur_frame = []
    for i in range(32):
        row = data.readline()
        row = row.split(" ")
        cur_row = []
        for j in range(32):
            col = row[j]
            cur_row.append(col)
        cur_frame.append(cur_row)
    frames.append(cur_frame)

