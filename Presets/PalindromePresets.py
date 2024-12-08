from Presets.Utils import translate_face, translate_bezel, translate_lines
from Sudokus.ContinuousSudoku import ContinuousSudoku
from Sudokus.PalindromeSudoku import PalindromeSudoku
from Sudokus.Sudoku import Sudoku

Presets = [
    (
        [
            "....1...5",
            "3..6.2.4.",
            ".1....3..",
            "7.4......",
            ".3.5.....",
            "2...6..1.",
            "8....7..2",
            ".9.4..8..",
            "..7....9.",
        ],
        [
            r"../......",
            r".\.......",
            r"..\......",
            r"...\.../.",
            r"...././..",
            r".....\...",
            r"....../..",
            r"...../...",
            r".........",
        ]
    ),
    (
        [
            "7...5...3",
            ".6.3.9.5.",
            "..4...1.6",
            ".2.9.7.1.",
            "8...6...2",
            ".5.1.4.3.",
            "4.2...3..",
            ".9.8.1.2.",
            "1...3...9",
        ],
        [
            r"./.......",
            r"\........",
            r".\.%.....",
            r"..%......",
            r".........",
            r"......\..",
            r".....%.\.",
            r"....%.../",
            r".........",
        ]
    ),
    (
        [
            "7.9...5..",
            ".......9.",
            ".........",
            "...7.5...",
            ".........",
            ".........",
            ".........",
            ".9.......",
            ".........",
        ],
        [
            r".........",
            r".../\\...",
            r"..//.\\..",
            r"../......",
            r"......./.",
            r".\\...//.",
            r"..\\../..",
            r".........",
            r".........",
        ]
    )
]

def get_sudoku(index: int) -> Sudoku:
    face_texts, lines_texts = Presets[index]
    return PalindromeSudoku(
        translate_face(face_texts),
        translate_lines(lines_texts),
    )
