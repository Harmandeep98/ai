# How to access base class


class Chai:

    def __init__(self, type_, strenght):
        self.type = type_
        self.stenght = strenght

# With code dupluication
# class GingerChai(Chai):
#     def __init__(self, type_, strenght, spice_level):
#         self.type = type_
#         self.stenght = strenght
#         self.spice_level = spice_level

# Explicit Call 
# class GingerChai(Chai):
#     def __init__(self, type_, strenght, spice_level):
#         Chai.__init__(self, type_, strenght)
#         self.spice_level = spice_level

# With super
class GingerChai(Chai):
    def __init__(self, type_, strenght, spice_level):
        super().__init__(type_, strenght)
        self.spice_level = spice_level