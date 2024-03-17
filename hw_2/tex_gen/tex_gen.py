from typing import Protocol


class Stringable(Protocol):
    def __str__(self) -> str:
        pass


def generate_tex_doc(body: str, libraries: list[str] = None) -> str:
    """
    Generates LaTeX article-style document with the given body.

    Parameters:
        body: contents of the document
        libraries: list of libraries to include in the document

    Returns:
        LaTeX-compilable article-style document
    """

    packages: list[str] = [f"\\usepackage{{{lib}}}" for lib in libraries] if libraries is not None else []
    header: str = "\n".join(["\\documentclass[12pt]{article}", *packages, "\\begin{document}\n", "$\n"])
    end: str = "\\end{document}"
    return f"{header}{body}{end}"


def generate_tex_table(table: list[list[Stringable]]) -> (str, list[str]):
    """
    Generates LaTeX table from the provided list of rows.

    Parameters:
        table: list of rows of the initial table

    Returns:
        Tuple of
            1) LaTeX-compilable representation of a table;
            2) libraries that it is dependent on.
    """

    result: list[str] = []
    table_str: list[list[str]] = [[str(elem) for elem in row] for row in table]

    if len(table_str) > 0:
        hline: str = "\\hline\n"
        row_length: int = len(table_str[0])

        if not all(map(lambda row: len(row) == row_length, table_str)):
            raise ValueError("All rows in a table should be of a same length")

        column_layout: str = "|".join(["c"] * row_length)
        glued_rows: list[str] = list(map(lambda x: " & ".join(x) + "\\\\\n", table_str))
        tex_table: str = hline.join(glued_rows)

        result.append(f"\\begin{{array}}{{|{column_layout}|}}\n")
        result.append("{0}{1}{0}".format(hline, tex_table))
        result.append("\\end{array}\n$\n\n")

    return "".join(result), []


def generate_tex_image(image_path: str) -> (str, list[str]):
    """
    Generates LaTeX image including code.

    Parameters:
        image_path: path to the image to include in .tex document

    Returns:
        Tuple of
            1) LaTeX-compilable representation of an included image;
            2) libraries that it is dependent on.
    """

    return f"$\\includegraphics[width=5cm, height=4cm]{{{image_path}}}$\n\n", ["graphicx"]

