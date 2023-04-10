def test_simple(expect):
    print("some stuff")
    print('hello')
    print('hi')
    expect("""\
some stuff
hello
hi
""")
    print('some more stuff')
    print('hello')
    expect("""\
some more stuff
hello
""")
