FROM pandoc/latex:latest

RUN apk add python3
RUN apk add py3-pip
COPY . hw_2/
RUN pip install -r hw_2/requirements.txt
RUN pip install -i https://test.pypi.org/simple/ tex-gen
RUN python3 -m hw_2
RUN mkdir artifacts
ENTRYPOINT ["pdflatex"]