# Tournament Processing Tool
# This script reads the results of a tournament from an input file, filters and sorts participants based on
# their points, and writes the processed results to an output file.

def process_tournament(input_file: str, output_file: str) -> None:
    """
    Processes tournament data from the input file and writes the results to the output file.

    Args:
        input_file (str): The file path for the input data.
        output_file (str): The file path for the output results.
    """

    def sort_key(item):
        return item[1]

    with open(input_file, 'r') as file:
        k = int(file.readline().strip())
        participants = []
        for line in file:
            data = line.strip().split()
            if len(data) >= 3:
                name = f"{data[1][0]}. {data[0]}"
                points = int(data[2])
                participants.append((name, points))

    second_tour_participants = [(name, points) for name, points in participants if points > k]
    second_tour_participants.sort(key=sort_key, reverse=True)

    with open(output_file, 'w') as file:
        file.write(f"{len(second_tour_participants)}\n")
        for i, (name, points) in enumerate(second_tour_participants, start=1):
            file.write(f"{i}) {name} {points}\n")


def main() -> None:
    """
    The main function that initiates the tournament processing.
    """
    input_file = 'first_tour.txt'
    output_file = 'second_tour.txt'

    process_tournament(input_file, output_file)
    print(f"The results of the second round have been written to the file {output_file}")


# Running the main function
main()
