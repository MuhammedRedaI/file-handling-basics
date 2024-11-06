# # open a file, 'r' for read, 'r+' for read and write, 'w' for write
# f = open('test.txt', 'r')
# print(f.mode)
# # have to close the file to avoid errors
# f.close()

# using context manager allows us not to insert 'close()'
with open('test.txt', 'r') as f:
    ## reading the content, u can pass size as a parameter
    # f_content = f.read()
    # print(f_content)

    ## advance reading using 'read()'
    # size = 10
    # f_content = f.read(size)
    # including " end = '*' " so we get a better visualization about each chunk and each iteration or we can use 'f.tell()'
    # while len(f_content) > 0:
    #     print(f_content, end = '*')
    #     # redefining the 'f_content' cuz it pick up from where we ended last time
    #     f_content = f.read(size)
    ## seperating to content by lines, use 'readline' to print to first line
    # f_conent = f.readlines()
    # print(f_content)

    ## to read the content from the file efficiently use a loop
    # for line in f:
    #     print(line, end='')

    # # using f.seek()
    # size = 10
    # f_content = f.read(size)
    # print(f_content, end='')

    # print(f.tell())
    # f.seek(0)

    # f_content = f.read(size)
    # print(f_content)

    # writing to files: 
    ## giving a name to non_existed  file to create it
    # with open('test2.txt', 'w') as f: 
    #     f.write('Test')
    #     #to handle duplicates, and overwrite
    #     f.seek(0)
    #     f.write('tEST')

    # # creating a copy
    # with open('test.txt', 'r') as rf:
    #         with open('test_copy.txt', 'w') as wf:
    #             for line in rf:
    #                 wf.write(line)

    # working with photos as bytes
    # with open('images.jpg', 'rb') as rf:
    #        with open('imgages_copy.jpg', 'wb') as wf:
    #              for line in rf:
    #                  wf.write(line)
