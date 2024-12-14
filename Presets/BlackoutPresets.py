from Presets.Utils import translate_face, translate_killer_cages
from Sudokus.BlackoutSudoku import BlackoutSudoku
from Sudokus.KillerSudoku import KillerSudoku
from Sudokus.Sudoku import Sudoku

Presets = [
    [
        "3.0.6..15",
        "7...019..",
        "8....3.0.",
        ".2.510467",
        "07.....82",
        "..3..40..",
        "409.76...",
        "...08.24.",
        "1...4.7.0",
    ],
    [
        ".420.63..",
        ".....1.20",
        ".03.....6",
        "0.16534..",
        "2....0..7",
        "...29810.",
        "65...9038",
        "4...05.9.",
        "1.03..7..",
    ]
]

def get_sudoku(index: int) -> Sudoku:
    face_texts = Presets[index]
    return BlackoutSudoku(
        translate_face(face_texts)
    )
