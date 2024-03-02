# task_3 artifacts

- ```commandline
    $ wc -
    fsdfsdfsdaf
    sdfsdfsdfdasf
    ddsdsd  sd sd s d       saddfdfdfd   asd
    \n\n\n\n\n\n\t\t\\n\

      5      10     136 -
    ```
  ```commandline
    $ python3 task_3.py
    fsdfsdfsdaf                                               
    sdfsdfsdfdasf
    ddsdsd  sd sd s d       saddfdfdfd   asd
    \n\n\n\n\n\n\t\t\\n\

        5       10      136     -
    ```
  
- ```commandline
  $ wc resources/task_1 
  76  197 1764 resources/task_1
  ```
  
  ```commandline
  $ python3 task_3.py resources/task_1 
        76      197     1764    resources/task_1
  ```
  
- ```commandline
  $ wc resources/many_lines_file resources/task_1 
  15   15  109 resources/many_lines_file
  76  197 1764 resources/task_1
  91  212 1873 total  
  ```
  
  ```commandline
  $ python3 task_3.py resources/many_lines_file resources/task_1
        15      15      109     resources/many_lines_file
        76      197     1764    resources/task_1
        91      212     1873    total
  ```
    
- ```commandline
  $ wc resources/task_1 - resources/empty 
     76     197    1764 resources/task_1
  ffff
  dddd
  \n    t
      3       4      24 -
      8       2      14 resources/empty
     87     203    1802 total

    ```
  
  ```commandline
  $ python3 task_3.py resources/task_1 - resources/empty
        76      197     1764    resources/task_1
  ffff
  dddd
  \n    t
        3       4       24      -
        8       2       14      resources/empty
        87      203     1802    total

  ```
  
- ```commandline
  $ python3 task_3.py resources/task_4
  Could not open file: resources/task_4
  ```