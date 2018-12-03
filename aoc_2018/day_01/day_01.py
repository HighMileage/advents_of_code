import csv

def inputs():
    with open('input_01.txt', 'r') as input_file:
        for value in csv.reader(input_file):
            yield int(value[0])


def main():
    observed_states = set()
    frequency = 0

    while True:
        for change in inputs():
            observed_states.add(frequency)
            frequency += change
            if frequency in observed_states:
                print('Duplicate frequency found at {}'.format(frequency))
                return

if __name__ == '__main__':
    main()
