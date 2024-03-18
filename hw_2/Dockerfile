FROM pandoc/latex:latest

COPY resources hw_2/resources
RUN mkdir artifacts
COPY artifacts/task_2.tex artifacts
ENTRYPOINT ["pdflatex"]