from spiderLib import Base
import requests
from requests.exceptions import RequestException
class GetOnePage(Base.Base):
    def get_one_page(self):
        try:
            response = requests.get(self.url)
            response.encoding = response.apparent_encoding
            if response.status_code == 200:
                return response.text
            return None
        except RequestException:
            return None
