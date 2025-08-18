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
    SIZE = 10

    # Validate words
    for word in words:
        if len(word) > SIZE:
            raise ValueError(f"Word too long to fit in {SIZE}x{SIZE} grid: '{word}'")

    # Place longer words first for better fitting
    words.sort(key=lambda s: -len(s))

    # Empty grid
    grid = [[None for i in range(SIZE)] for i in range(SIZE)]

    # Six directions: right, left, down, up, down-right, up-left
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]

    for word in words:
        placed = False
        attempts = 0
        max_attempts = 2000
        word_length = len(word)

        while not placed and attempts < max_attempts:
            attempts += 1
            dr, dc = random.choice(directions)
            r = random.randint(0, SIZE - 1)
            c = random.randint(0, SIZE - 1)

            end_r = r + dr * (word_length - 1)
            end_c = c + dc * (word_length - 1)
            if not (0 <= end_r < SIZE and 0 <= end_c < SIZE):
                continue

            # Check compatibility with current grid (allow matching intersections)
            conflict = False
            for i, ch in enumerate(word):
                rr = r + dr * i
                cc = c + dc * i
                cell = grid[rr][cc]
                if cell is not None and cell != ch:
                    conflict = True
                    break
            if conflict:
                continue

            # Place the word
            for i, ch in enumerate(word):
                rr = r + dr * i
                cc = c + dc * i
                grid[rr][cc] = ch
            placed = True

        if not placed:
            raise RuntimeError(f"Could not place word '{word}' after {max_attempts} attempts")

    # Fill remaining cells with random uppercase letters
    for i in range(SIZE):
        for j in range(SIZE):
            if grid[i][j] is None:
                grid[i][j] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

    return grid



# --- Main execution block. DO NOT MODIFY.  ---
if __name__ == "__main__":
    try:
        # Read words from first line (comma-separated)
        words_input = input("Input words (comma-separated): ").strip()
        #words_input = input().strip()
        words = [word.strip() for word in words_input.split(',')]
        # Generate the word search puzzle
        puzzle = create_crossword(words)
        
        # Print the result as a 2D grid
        for row in puzzle:
            print(''.join(row))
            
    except ValueError as e:
        print(f"Input Error: {e}", file=sys.stderr)
        sys.exit(1)
    except EOFError:
        print("Error: Not enough input lines provided.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)