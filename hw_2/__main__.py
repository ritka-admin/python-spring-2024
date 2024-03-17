from pdflatex import PDFLaTeX
from tex_gen import generate_tex_doc, generate_tex_image, generate_tex_table


if __name__ == '__main__':
    table = [
        ["he", "hell", "hello"],
        ["lol", "kek", "azaza"],
        [i for i in range(3)]
    ]

    table_tex, table_libs = generate_tex_table(table)
    image_tex, image_libs = generate_tex_image("hw_2/resources/image.png")

    with open("hw_2/artifacts/task_1.tex", 'w') as file:
        file.write(generate_tex_doc(table_tex, table_libs))

    with open("hw_2/artifacts/task_2.tex", 'w') as file:
        body: str = f"{table_tex}{image_tex}"
        file.write(generate_tex_doc(body, table_libs + image_libs))

    pdfl = PDFLaTeX.from_texfile("hw_2/artifacts/task_2.tex")
    pdf, log, completed_process = pdfl.create_pdf()

    with open("hw_2/artifacts/task_2.pdf", 'wb') as file:
        file.write(pdf)

