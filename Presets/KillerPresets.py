from Presets.Utils import translate_face, translate_killer_cages
from Sudokus.KillerSudoku import KillerSudoku
from Sudokus.Sudoku import Sudoku

Presets = [
    (
        [
            "..7..4.92",
            "4..3.7...",
            ".168....4",
            "94.2.6...",
            ".......8.",
            "2.5.384..",
            ".23.5....",
            ".5.693...",
            "1.....5.3",
        ],
        [
            ".11<.15.25<<<<.7",
            ".13<^.9<.15<.8^",
            ".14.14^.23.11<.7^<",
            "^^.18^<<.3.6<",
            ">^^<.4.7<.15<",
            ".9<.21.12<<.10<.9",
            ".21<^<.15<<.22.14",
            ".8^.13^.14<>^^",
            "^^^.12<^^^<",
        ]
    )
]

def get_sudoku(index: int) -> Sudoku:
    face_texts, killer_cage_texts = Presets[index]
    return KillerSudoku(
        translate_face(face_texts),
        translate_killer_cages(killer_cage_texts)
    )
