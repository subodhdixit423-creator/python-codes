class person:
    def_int_(self,name,age)
    self.name=Name
    self.age=age

    def display_person_info(self)
        print(f"name:{self.name}")
        print(f"age:{self.age}")


        class employee(person):
            def_int_(self,name,age,employee_id,salary):
            super()._int_(name,age)
            self.employee_id=employee_id
            self.salary=salary

            def display_employee_info(self):
                print(f"employee ID:{self.employee_id}")
                print(f"salary:₹{self.salary}")


                class manager(employee,person)
                    def_int_(self,name,age,employee_id,salary,deoartment)
                    super()._int_(name,age,employee_id,salary)
                    self.department=department


                    def display_manager_info(self):
                        print("\n---manager details---")
                        self.display_person_info()
                        slef.display_employee_info()
                        print(f"department:{self.department}")


                        def approve_leave(self)
                            print(f"{self.name}has approved the leave request.")


                            manager1=manager(
                                name"Dipak Patil",
                                age=40
                                employee_id="M101",
                                salary=85000,
                                department="IT"
                            )


                            manager1.display_manager_info()
                            manager1.approve_leave



    

