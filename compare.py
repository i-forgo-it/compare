import sys
import shutil
import os

def compare_files(file1, file2):
    """Compare the content of two files and return the differences."""
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        file1_lines = f1.readlines()
        file2_lines = f2.readlines()

    differences = []
    for line in file1_lines:
        if line not in file2_lines:
            differences.append(line.strip())

    for line in file2_lines:
        if line not in file1_lines:
            differences.append(line.strip())

    return differences

def main():
    if '-f' in sys.argv:
        try:
            # Get the file name provided after the -f flag
            index = sys.argv.index('-f') + 1
            original_file = sys.argv[index]
            copy_file = original_file.replace('.txt', 'copy.txt')

            if os.path.exists(original_file):
                # If the copy file doesn't exist, create it by copying the original file
                if not os.path.exists(copy_file):
                    shutil.copyfile(original_file, copy_file)

                # Compare the original file with the copy
                differences = compare_files(original_file, copy_file)

                # Check if either the -all or -result flag is present
                if '-all' in sys.argv:
                    if differences:
                        with open(original_file, 'r') as f:
                            print(f.read())
                elif '-result' in sys.argv:
                    if differences:
                        for diff in differences:
                            print(diff)
                else:
                    print("Error: You need to use the -result or -all flag.")
                    sys.exit(1)

                # Update the copy with the current content of the original file
                shutil.copyfile(original_file, copy_file)
            else:
                print(f"Error: The file '{original_file}' does not exist.")

        except IndexError:
            print("Error: Please provide a file name after the -f flag.")
    else:
        print("Usage: python script.py -f example.txt [-all | -result]")

if __name__ == "__main__":
    main()
