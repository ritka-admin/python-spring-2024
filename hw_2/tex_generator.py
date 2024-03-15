from typing import Protocol


class Stringable(Protocol):
    def __str__(self) -> str:
        pass


def generate_tex_table(table: list[list[Stringable]]) -> str:
    """
    Generates LaTeX table from the provided list of rows.

    Parameters:
        table: list of rows of the initial table

    Returns:
        LaTeX-compilable representation of a table
    """
    result: str = "\n".join(["\\documentclass[12pt]{article}", "\\begin{document}\n", "$\n"])
    table_str: list[list[str]] = [list(map(lambda x: str(x), lst)) for lst in table]

    if len(table_str) > 0:
        hline: str = "\\hline\n"
        max_length: int = max(map(lambda x: len(x), table_str))
        column_layout: str = "|".join(["c" for _ in range(max_length)])
        result += f"\\begin{{array}}{{|{column_layout}|}}\n"
        filled_rows: list[list[str]] = list(map(
                lambda x: x + ["" for _ in range(max_length - len(x))] if len(x) < max_length else x,
                table_str
            )
        )
        glued_rows: list[str] = list(map(lambda x: " & ".join(x) + "\\\\\n", filled_rows))
        tex_table: str = hline.join(glued_rows)
        result += "{0}{1}{0}".format(hline, tex_table)
        result += "\\end{array}\n$\n\n\\end{document}"

    result += "\\end{document}"
    return result
