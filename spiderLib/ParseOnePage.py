from spiderLib import GetOnePage
import re
class ParseOnePage(GetOnePage.GetOnePage):
    def parse_one_page(self,html):
        pattern = re.compile(self.get_rule,re.S)
        items = re.findall(pattern,html)
        return items;
