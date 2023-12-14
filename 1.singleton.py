'''
유일한 객체가 생성되도록 해주는 싱글톤 패턴을 구현하기 위해서는 __new__ 메서드를 재 정의해준 후 해당 메서드 내에서 이미 객체가 생성됐다면 객체를 생성해주지 않도록만 처리해주면 됩니다.
객체의 생성 여부는 모든 클래스 객체의 속성 변수로 _instance를 추가한 후 해당 변수로 관리하도록 해주면 되겠습니다.
'''
class Foo(object):
    def __new__(cls, *args, **kwargs):
        print("__new__ is called\n")
        instance = super().__new__(cls)
        return instance

    def __init__(self):
        print("__init__ is called\n")


s = Foo()
print(s)
print("=====================================================")
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):         # 클래스 객체에 _instance 속성이 없다면
            print("__new__ is called\n")
            # super() -> 상위 클래스의 인스턴스를 가져올수 있음
            cls._instance = super().__new__(cls)  # 클래스의 객체를 생성하고 cls._instance로 바인딩( 메모리에 객체로 생성하여 if문으로 필터링 )
        return cls._instance                      # cls._instance를 리턴


    def __init__(self, data):
        print("__init__ is called\n")
        self.data = data


s1 = Singleton(5)

s2 = Singleton(4)
s2._instance = None
# s3 = Singleton(s)
s2.data = 6
print(s1.data)
print(s2.data)
# print(s3.data)