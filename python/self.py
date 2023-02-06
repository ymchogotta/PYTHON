'''
class 클래스이름:
    def __init__(self):
        self.속성 = 값

속성(attribute)을 만들 때는 __init__ 메서드 안에서 self.속성에 값을 할당합니다.
'''

class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()    # 안녕하세요.

'''
__init__ 메서드는 james = Person()처럼 클래스에 ( )(괄호)를 붙여서 
인스턴스를 만들 때 호출되는 특별한 메서드입니다. 
즉, __init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화합니다.
'''