from typing import Iterable, List, Dict, Tuple, Set, Optional

from Consts import Down, Right
from Types import PointType, DirectionType


def translate_face(face_texts: Iterable[str]):
    return [
        [
            int(face_char) if face_char != '.' else None
            for face_char in face_text
        ]
        for face_text in face_texts
    ]

KillerCageType = Tuple[int, List[PointType]]

def translate_killer_cages(killer_cage_texts: Iterable[str]) -> List[KillerCageType]:
    killer_cages: List[KillerCageType] = []
    killer_cage_map: Dict[PointType, KillerCageType] = {}
    links: Dict[PointType, List[PointType]] = {}

    def process_links(position: PointType, killer_cage: KillerCageType) -> None:
        link_positions = links.pop(position, None)
        if link_positions is not None:
            killer_cage[1].extend(link_positions)
            for link_position in link_positions:
                killer_cage_map[link_position] = killer_cage
                process_links(link_position, killer_cage)

    for y, killer_cage_text in enumerate(killer_cage_texts):
        x: int = 0
        is_reading_number: bool = False
        number_text: str = ""
        for killer_cage_char in killer_cage_text:
            if is_reading_number:
                if killer_cage_char in "0123456789":
                    number_text += killer_cage_char
                    continue
                killer_cage = (int(number_text), [(x, y)])
                number_text = ""
                killer_cages.append(killer_cage)
                killer_cage_map[(x, y)] = killer_cage
                process_links((x, y), killer_cage)
                is_reading_number = False
                x += 1
            match killer_cage_char:
                case '.':
                    is_reading_number = True
                    continue
                case '<':
                    killer_cage = killer_cage_map[(x - 1, y)]
                    killer_cage[1].append((x, y))
                    killer_cage_map[(x, y)] = killer_cage
                    process_links((x, y), killer_cage)
                case '^':
                    killer_cage = killer_cage_map[(x, y - 1)]
                    killer_cage[1].append((x, y))
                    killer_cage_map[(x, y)] = killer_cage
                    process_links((x, y), killer_cage)
                case '>':
                    links.setdefault((x + 1, y), []).append((x, y))
                case '_':
                    links.setdefault((x, y + 1), []).append((x, y))
            x += 1
        if len(number_text) > 0:
            killer_cage = (int(number_text), [(x, y)])
            killer_cages.append(killer_cage)
            killer_cage_map[(x, y)] = killer_cage
            process_links((x, y), killer_cage)
    return killer_cages

BlockType = List[PointType]

def translate_blocks(block_texts: Iterable[str]) -> List[BlockType]:
    blocks: List[BlockType] = []
    block_map: Dict[PointType, BlockType] = {}
    links: Dict[PointType, List[PointType]] = {}

    def process_links(position: PointType, block: BlockType) -> None:
        link_positions = links.pop(position, None)
        if link_positions is not None:
            block.extend(link_positions)
            for link_position in link_positions:
                block_map[link_position] = block
                process_links(link_position, block)

    for y, block_text in enumerate(block_texts):
        x: int = 0
        for block_char in block_text:
            match block_char:
                case '.':
                    block = [(x, y)]
                    blocks.append(block)
                    block_map[(x, y)] = block
                    process_links((x, y), block)
                case '<':
                    block = block_map[(x - 1, y)]
                    block.append((x, y))
                    block_map[(x, y)] = block
                    process_links((x, y), block)
                case '^':
                    block = block_map[(x, y - 1)]
                    block.append((x, y))
                    block_map[(x, y)] = block
                    process_links((x, y), block)
                case '>':
                    links.setdefault((x + 1, y), []).append((x, y))
                case '_':
                    links.setdefault((x, y + 1), []).append((x, y))
            x += 1
    return blocks

BezelType = Tuple[PointType, DirectionType]

def translate_bezel(bezel_texts: Iterable[str]) -> List[BezelType]:
    bezels: List[BezelType] = []
    if bezel_texts is None:
        return bezels
    for y, bezel_text in enumerate(bezel_texts):
        x: int = 0
        for bezel_char in bezel_text:
            match bezel_char:
                case '.':
                    x += 1
                case '_':
                    bezels.append(((x, y), Down))
                    x += 1
                case '|':
                    bezels.append(((x - 1, y), Right))
    return bezels


def translate_lines(lines_texts: Iterable[str]) -> List[List[PointType]]:
    lines: List[List[PointType]] = []
    line_map: Dict[PointType, Optional[List[PointType]]] = {}
    if lines_texts is None:
        return lines
    for y, lines_text in enumerate(lines_texts):
        for x, lines_char in enumerate(lines_text):
            position = x, y
            if position in line_map:
                continue
            line_map[position] = None
            if lines_char == '.':
                continue
            current_char = lines_char
            current_x = x
            current_y = y
            line: List[PointType] = [position]
            line_map[position] = line
            while current_char != '.':
                sibling_position: PointType = (0, 0)
                match current_char:
                    case '>': sibling_position = (current_x + 1, current_y)
                    case '|': sibling_position = (current_x, current_y + 1)
                    case '<': sibling_position = (current_x - 1, current_y)
                    case '^': sibling_position = (current_x, current_y - 1)
                    case '/': sibling_position = (current_x - 1, current_y + 1)
                    case '%': sibling_position = (current_x + 1, current_y - 1)
                    case '\\': sibling_position = (current_x + 1, current_y + 1)
                    case '`': sibling_position = (current_x - 1, current_y - 1)
                sibling_x, sibling_y = sibling_position
                old_line = line_map.get(sibling_position)
                if old_line is not None:
                    line.extend(old_line)
                    lines.remove(old_line)
                    break
                line_map[sibling_position] = line
                sibling_char = lines_texts[sibling_y][sibling_x]
                line.append(sibling_position)
                current_x = sibling_x
                current_y = sibling_y
                current_char = sibling_char
            lines.append(line)
    return lines
