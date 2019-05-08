from spiderLib import ParseOnePage
class Main(ParseOnePage.ParseOnePage):
    def main(self):
        html = self.get_one_page()
        res = self.parse_one_page(html)
        return res
       
    
