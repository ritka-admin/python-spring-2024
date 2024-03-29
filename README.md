# python-spring-2024

### hw_1

Launch: `python3 task_N.py [ARGS]`

- task_1: `nl -b a` realization
- task_2: `tail` realization
- task_3: `wc` realization

### hw_2

Install requirements: `pip install -r hw_2/requirements.txt`

Launch: `python3 -m hw_2`

- task_1: generation of valid LaTeX table from python list of lists
- task_2: 
  - generation of LaTeX image from a given png
  - .tex to pdf conversion
  - module upload to index (using setuptools) (ref: https://test.pypi.org/project/tex-gen/)
- task_3: introduction of Dockerfile for pdf from tex generation
  - build: `docker build --tag tex_gen hw_2/`
  - run:
    ```commandline
    docker run --rm \
    --mount type=bind,source="$(pwd)"/hw_2/dockerfile_artifact,target=/data/dockerfile_artifacts \
    tex_gen \
    -output-directory dockerfile_artifacts  hw_2/artifacts/task_2.tex
    ```
    
### hw_3

Launch: `python3 -m hw_3`

- task_1: Matrix realization, `+`, `*`, `@` operator overloading
- task_2: Matrix realization via Numpy / self-made mixins
- task_3: Matrix `hash` realization + search for collision
