import re

codes = []
location = (__file__)
target_filepath = location.rstrip('run_me.py')

print("Reading text from input...")

with open(target_filepath + '\input.txt', 'r') as input_file:

    print("Stripping codes from text...")
    for line in input_file:    
        code = re.search('.{5}-.{5}-.{5}', line)
        if code != None:
            codes.append(code.group())

print("Writing codes to output...")

with open(target_filepath + '\output.txt', 'w') as output_file:

    for code in codes:
        output_file.write(code + '\n')

print("Done!")

input('Press Enter to Continue!')