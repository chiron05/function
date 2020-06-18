def most_frequent(string1):
    mydict={}
    a=string1.count("a")
    print("Output:\n")
    if(a>0):
        mydict["a"]= str(a)

    b = string1.count("b")
    if (b > 0):
        mydict["b"] = str(b)


    c = string1.count("c")
    if (c > 0):
        mydict["c"] = str(c)


    d = string1.count("d")
    if (d > 0):
        mydict["d"] = str(d)


    e = string1.count("e")
    if (e > 0):
        mydict["e"] = str(e)


    f = string1.count("f")
    if (f > 0):
        mydict["f"] = str(f)


    g = string1.count("g")
    if (g > 0):
        mydict["g"] = str(g)


    h = string1.count("h")
    if (h > 0):
        mydict["h"] = str(h)


    i = string1.count("i")
    if (i > 0):
        mydict["i"] = str(i)


    j = string1.count("j")
    if (j > 0):
        mydict["j"] = str(j)


    k = string1.count("k")
    if (k > 0):
        mydict["k"] = str(k)


    l = string1.count("l")
    if (l > 0):
        mydict["l"] = str(l)


    m = string1.count("m")
    if (m > 0):
        mydict["m"] = str(m)


    n = string1.count("n")
    if (n > 0):
        mydict["n"] = str(n)


    o = string1.count("o")
    if (o > 0):
        mydict["o"] = str(o)


    p = string1.count("p")
    if (p > 0):
        mydict["p"] = str(p)

    q = string1.count("q")
    if (q > 0):
        mydict["q"] = str(q)


    r = string1.count("r")
    if (r > 0):
        mydict["r"] = str(r)


    s = string1.count("s")
    if (s > 0):
        mydict["s"] = str(s)


    t = string1.count("t")
    if (t > 0):
        mydict["t"] = str(t)


    u = string1.count("u")
    if (u > 0):
        mydict["u"] = str(u)


    v = string1.count("v")
    if (v > 0):
        mydict["v"]= str(v)


    w = string1.count("w")
    if (w > 0):
        mydict["w"] = str(w)


    x = string1.count("x")
    if (x > 0):
        mydict["x"] = str(x)


    y = string1.count("y")
    if (y > 0):
        mydict["y"] = str(y)


    z = string1.count("z")
    if (z > 0):
        mydict["z"] = str(z)

    list1=list(mydict.items())
    print(list1)
    tuple1=tuple(list1)
    tuple1=sorted(mydict.items(),reverse=True, key=lambda x: x[1])
    for num in tuple1:
        print(num[0]+" =0"+num[1])

string=str(input("Please enter a string: "))
most_frequent(string)