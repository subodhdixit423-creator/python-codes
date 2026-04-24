#base class
class vehicle:
    def move(self):
        print("driving on the road")

        #subclass car
        class car(vehicle):
            def move(self):
                print("driving on the road")


                #subclass bicycle
                class bicycle(vehicle):
                    def move(self):
                        print("peadling on the road")


                        #demonstrating polymorphism
                        vehivles = [car(),bicycle()]

                        for v in vehicles:
                            v.move()
                            
                