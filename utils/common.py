
def set_grid_weights(frame, grid_values, pos="col"):
    for k, v in grid_values.items():
        if pos == "col":
            frame.grid_columnconfigure(k, weight=v)
        if pos == "row":
            frame.grid_rowconfigure(k, weight=v)
    return
