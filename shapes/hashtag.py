from shapes.base import BaseShape


class HashtagTriangle(BaseShape):
    """
    Creates awesome triangular shapes using the 
    hashtag symbol. Check this out:

        #
       ##
      ###
     ####
    ##### 
    """

    symbol = "#"
    minimum_size = 2

    def _create_shape(self) -> list:
        shape = []
        for i in range(self.size):
            spaces = (self.size - i - 1) * " "
            symbols = (i + 1) * self.symbol
            shape.append(f"{spaces}{symbols}")
        return shape