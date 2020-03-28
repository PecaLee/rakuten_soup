from rakuten import get_goods_info
from save import save_to_file

goods = get_goods_info()
save_to_file(goods)