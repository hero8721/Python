class HEX_parse:

    def __init__(self):
        # ///////LISTS///////////////////////////////////
        self.FLASH = []
        self.ADDR = []
        # ///////LISTS///////////////////////////////////

    def parse(self, file):

        for line in file:
            # ///////RECORD AREA///////////////////////////////////
            record = line[7:9]
            data = line[9:73]
            # ///////RECORD AREA///////////////////////////////////

            # ///////FLAGS///////////////////////////////////
            i = 0
            # ///////FLAGS///////////////////////////////////

            if record == "00":
                # ///////FLASH AREA///////////////////////////////////
                while i < 64:
                    str_val = str(data[i] + data[i + 1])
                    hex_val = int(str_val, 16)
                    self.FLASH.append(hex_val)
                    i += 2

                # ///////FLASH AREA///////////////////////////////////

        return self.FLASH

# if __name__ == "__main__":
#     app = HEX_parse()
#     app.parse(file=open(""))

