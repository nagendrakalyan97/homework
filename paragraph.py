import sys


def justify_paragraph(paragraph, width):
    words = paragraph.split()
    lines, current_line, final_lines = [], [], []
    current_width = 0

    for word in words:
        if current_width + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_width += len(word)
            # print(f"current line is : {current_line},\n current width is : {current_width}")
        else:
            lines.append(current_line)
            current_line = [word]
            current_width = len(word)
            # print(f"In else block and line is {lines},\n current line is : {current_line},\n current width is : {current_width}")

    if current_line:
        lines.append(current_line)

    for line in lines:
        length_of_item = sum(len(word) for word in line)
        # print(f"length_of_item: {length_of_item}")
        spaces_needed = width - length_of_item
        # print(f"spaces_needed :{spaces_needed}")
        num_gaps = len(line) - 1
        if num_gaps > 0:
            spaces_per_gap = spaces_needed // num_gaps
            extra_spaces = spaces_needed % num_gaps
            justified_line = line[0]
            for i in range(1, len(line)):
                justified_line += ' ' * (spaces_per_gap + (i <= extra_spaces))
                justified_line += line[i]
        else:
            justified_line = line[0] + ' ' * spaces_needed

        final_lines.append(justified_line)

    return final_lines


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Pass the arguments \n 1. Paragraph\n 2. Width of line")
    else:
        paragraph = sys.argv[1]
        width = int(sys.argv[2])
        justified_text = justify_paragraph(paragraph, width)
        for line in range(0, len(justified_text)):
            print(f'Array[{line + 1}] = "{justified_text[line]}"')
