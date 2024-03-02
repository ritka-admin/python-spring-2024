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
  $ wc task_1.py 
  76  197 1764 task_1.py
  ```
  
  ```commandline
  $ python3 task_3.py task_1.py 
        76      197     1764    task_1.py
  ```
  
- ```commandline
  $ wc task_1.py task_2.py 
  76  197 1764 task_1.py
  80  182 1796 task_2.py
  156  379 3560 total
  ```
  
  ```commandline
  $ python3 task_3.py task_1.py task_2.py 
        76      197     1764    task_1.py
        80      182     1796    task_2.py
        156     379     3560    total
  ```
    
- ```commandline
  $ wc task_3.py - task_2.py 
       70     201    1920 task_3.py
  ffff
  dddd
  \n    t
        3       4      18 -
       74     173    1664 task_2.py
      147     378    3602 total
    ```
  
  ```commandline
  $ python3 task_3.py task_3.py - task_2.py 
          70      201     1920    task_3.py
  ffff
  dddd
  \n    t
          3       4       18      -
          74      173     1664    task_2.py
          147     378     3602    total
  ```
  
- ```commandline
  $ python3 task_3.py task_4.py
  Could not open file: task_4.py
  ```