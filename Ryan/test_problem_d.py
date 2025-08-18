import sys
import random

def create_crossword(words: list) -> list:
    """
    Generate a 10x10 word search puzzle containing the given words.
    
    Args:
        words: A list of words to include in the puzzle.
        
    Returns:
        A 2D array (list of lists) representing the word search puzzle.
    """
    # WRITE YOUR CODE HERE
    SIZE = 10  # size of the grid (10x10)

    # Normalize and validate words
    cleaned_words = []
    seen = set()
    for word in words:
        word = word.strip().upper()  # remove spaces around, convert to uppercase
        if not word or word in seen:  # skip empty strings or duplicates
            continue
        if len(word) > SIZE:  # reject words too long to fit in the grid
            raise ValueError(f"Word too long to fit in {SIZE}x{SIZE} grid: '{word}'")
        cleaned_words.append(word)  # add cleaned word to the list
        seen.add(word) 

    # Place longer words first 
    cleaned_words.sort(key=len, reverse=True)

    # Create empty grid
    grid = [[None for i in range(SIZE)] for j in range(SIZE)]

    directions = [
        (0, 1),   # right →
        (0, -1),  # left ←
        (1, 0),   # down ↓
        (-1, 0),  # up ↑
        (1, 1),   # down-right ↘
        (-1, -1), # up-left ↖
        (1, -1),  # down-left ↙
        (-1, 1)   # up-right ↗
    ]

    for word in cleaned_words:
        placed = False
        attempts = 0
        max_attempts = 2000  # prevent infinite loops if a word can't be placed
        word_length = len(word)

        while not placed and attempts < max_attempts:
            attempts += 1
            # Randomly pick a direction and a starting point
            row_direction, col_direction = random.choice(directions)
            start_row = random.randint(0, SIZE - 1)
            start_col = random.randint(0, SIZE - 1)

            # Calculate ending position based on chosen direction
            end_row = start_row + row_direction * (word_length - 1)
            end_col = start_col + col_direction * (word_length - 1)

            # Skip if the word would go out of bounds
            if not (0 <= end_row < SIZE and 0 <= end_col < SIZE):
                continue

            # Check if the word can fit
            has_conflict = False
            for letter_index, letter in enumerate(word):
                current_row = start_row + row_direction * letter_index
                current_col = start_col + col_direction * letter_index
                cell_value = grid[current_row][current_col]
                if cell_value is not None and cell_value != letter: #checks for conflicts in each cell
                    has_conflict = True
                    break
            if has_conflict:
                continue

            # Place the word
            for letter_index, letter in enumerate(word):
                current_row = start_row + row_direction * letter_index
                current_col = start_col + col_direction * letter_index
                grid[current_row][current_col] = f'[{letter}]'
            placed = True

        # If word can't be placed
        if not placed:
            raise RuntimeError(f"Could not place word '{word}' after {max_attempts} attempts")

    # Fill any empty spaces with random letters
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] is None:
                grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    print("Words placed in puzzle:", ", ".join(cleaned_words)) #prints placed words
    return grid


# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        
        # Generate the word search puzzle
        puzzle = create_crossword(words)

        # Print the result as a 2D grid with row/col indices
        # Print the result as a 2D grid with even spacing (handles [A] too)
        size = len(puzzle)

        # Determine a fixed width that fits all cells and headers
        cell_w = max(3, max(len(cell) for row in puzzle for cell in row))  # at least 3 for "[A]"
        head_w = max(cell_w, len(str(size - 1)))
        row_label_w = max(2, len(str(size - 1)))

        # Build column header line
        header_cells = " ".join(f"{c:>{head_w}}" for c in range(size))
        print(" " * (row_label_w + 1) + header_cells)
        print(" " * (row_label_w + 1) + "-" * len(header_cells))

        # Print each row with fixed-width cells
        for r, row in enumerate(puzzle):
            line = " ".join(f"{cell:^{cell_w}}" for cell in row)  # center each cell
            print(f"{r:>{row_label_w}} {line}")

            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)