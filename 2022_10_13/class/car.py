class Car:
    # __init__ => 생성자 메소드
    def __init__(self, type, speed):
        self.type = type
        self.speed = speed
        print(f'{self.type} 객체가 하나 생성되었습니다.')

    def move(self):
        print(self.type + "가 " + str(self.speed) + " 속도로 움직입니다.")

    def speed_up(self, amount):
        self.speed += amount

    def speed_down(self, amount):
        self.speed -= amount

c = Car('스포츠카', 100)
c.speed_up(10)
c.move()
c.speed_down(10)
c.move()