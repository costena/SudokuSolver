from Presets.Utils import translate_face
from Sudokus.DiagonalSudoku import DiagonalSudoku
from Sudokus.Sudoku import Sudoku

Presets = [
    [
        ".46...31.",
        "5...9...6",
        "...4.7...",
        "..2...1..",
        ".7.....3.",
        "..5...7..",
        "...6.9...",
        "8...1...3",
        ".29...86.",
    ],
    [
        ".8.4.1...",
        "4.5...8..",
        ".7.5...9.",
        "6.9.1...8",
        "...8.3...",
        "3...2.7.1",
        ".3...4.7.",
        "..7...4.3",
        "...3.7.1.",
    ]
]

def get_sudoku(index: int) -> Sudoku:
    face_texts = Presets[index]
    return DiagonalSudoku(
        translate_face(face_texts)
    )
