from Presets.Utils import translate_face
from Sudokus.DiagonalSudoku import DiagonalSudoku
from Sudokus.Sudoku import Sudoku
from Sudokus.WindowSudoku import WindowSudoku

Presets = [
    [
        ".....7.6.",
        "8.2...7..",
        ".1.3...5.",
        "7.....2..",
        "....3....",
        "..4.....5",
        ".6...5.1.",
        "..1...9.6",
        ".7.1.....",
    ],
    [
        ".....4.5.",
        "85.....7.",
        ".....5...",
        "1.7.5....",
        "...1.2...",
        "....9.3.1",
        "...5.....",
        ".1.....23",
        ".4.6.....",
    ]
]

def get_sudoku(index: int) -> Sudoku:
    face_texts = Presets[index]
    return WindowSudoku(
        translate_face(face_texts)
    )
