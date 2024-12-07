from Presets.Utils import translate_face, translate_blocks
from Sudokus.Sudoku import Sudoku
from Sudokus.ZigzagSudoku import ZigzagSudoku

Presets = [
    (
        [
            "..7..12..",
            ".8......3",
            "5.1....4.",
            "84......7",
            "...6.5...",
            "7......26",
            ".7....8.4",
            "3......9.",
            "..89..4..",
        ],
        [
            "..<<<<<..",
            "^<<<^>>^<",
            "^^.^^<^.^",
            "_^^.<<^^<",
            ">>^^<<>^<",
            "^.^^<<.^<",
            ">^^_.<^^_",
            ">^<<^>^<<",
            "^>>>^<<^<",
        ]
    )
]


def get_sudoku(index: int) -> Sudoku:
    face_texts, block_texts = Presets[index]
    return ZigzagSudoku(
        translate_face(face_texts),
        translate_blocks(block_texts),
    )
