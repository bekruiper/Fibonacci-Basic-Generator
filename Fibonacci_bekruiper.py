import PySimpleGUI as sg
import re
# Window
layout = [[sg.Text("Welcome to Fibonacci Basic Generator")],
          [sg.Text("Please introduce a number to generate sequence")],
          [sg.Input(key='-INPUT-')],
          [sg.Button('Generate', key='-GENERATE-'), sg.Exit()]]
window = sg.Window('Fibonacci Basic Generator', layout)
event, values = window.read()


# Function


def fibonacci_gen(n) -> int:
    yield 0
    prev2 = 0
    prev1 = 1
    result_list = []
    for i in range(n):
        result = prev1+prev2
        prev2 = prev1
        prev1 = result
        result = re.sub("(\d)(?=(\d{3})+(?!\d))", r"\1,", "%d" % result)
        yield result


# Trigger
while True:
    event, values = window.read()
    try:
        n = int(values['-INPUT-'])
    except:
        pass

    # Result
    if event == '-GENERATE-':
        try:
            for i in fibonacci_gen(n):
                result_list = list(fibonacci_gen(n))
            str_result_list = ""
            for i in result_list:
                str_result_list += "{}{}".format(i, " / ")
            new_list = str_result_list[:-len("/")]
            sg.popup('Your Sequence', str_result_list)
        except:
            sg.popup('Error!', 'Invalid Input')

    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        break
