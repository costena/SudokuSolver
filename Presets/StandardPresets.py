from Presets.Utils import translate_face
from Sudokus.StandardSudoku import StandardSudoku
from Sudokus.Sudoku import Sudoku

Questions = [
    [
        "5..2...4.",
        "...6.3...",
        ".3...9..7",
        "..3..7...",
        "..7..8...",
        "6......2.",
        ".8......3",
        "...4..6..",
        "...1..5..",
    ]
]

def get_sudoku(index: int) -> Sudoku:
    return StandardSudoku(translate_face(Questions[index]))
