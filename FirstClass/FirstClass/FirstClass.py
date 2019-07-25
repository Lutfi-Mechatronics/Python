


# Data Structure
class MyClass:
    # Atributes of MyClass()
    number = 0
    name= "noname"

def main():
    me = MyClass()
    me.number=1337
    me.name="Lutfi"

    MyClass.number =3
    MyClass.name="Ishwin"

    empty = MyClass()

    print("{0}{1}{2}{3}".format("Name : ",me.name,", number",me.number ))
    print("{0}{1}{2}{3}".format("Name : ",MyClass.name,", number",MyClass.number ))
    print("{0}{1}{2}{3}".format("Name : ",empty.name,", number",empty.number ))
main()
