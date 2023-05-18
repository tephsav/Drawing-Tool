import os
import drawingTool


def main():
    input_file_name = f"input{index}.txt"
    output_file_name = f"output{index}.txt"

    if not os.path.isfile(input_file_name):
        print("File not found!")
        return

    if os.path.isfile(output_file_name):
        os.remove(output_file_name)

    drawing_tool = drawingTool.DrawingTool()
    drawing_tool.choose_actions(input_file_name, output_file_name)


if __name__ == '__main__':
    index = input("Select file number (1-4): ")
    main()