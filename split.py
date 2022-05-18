#function
def split():
    lap = {}
    global running
    global hours, minutes, seconds
    hours_string = f'{hours}'
    minutes_string = f'{minutes}'
    seconds_string = f'{seconds}'
    if running:
        lap = hours_string + ':' + minutes_string + ':' + seconds_string
    split_label.config(text=lap)

#widget
split_button = tk.Button(text='split', height=5, width=7, font=('Arial', 20), command=split)
split_button.pack(side=tk.LEFT)

#label
split_label = tk.Label (text = '', font = ('Arial', 40))
split_label.pack(side=tk.LEFT)
