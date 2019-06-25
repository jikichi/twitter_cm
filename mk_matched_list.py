#fav, ret, follow３つを満たしているユーザーIDを返す
def mk_matched_list(fav, ret, follow):
    set_lst1 = set(fav)
    set_lst2 = set(ret)
    set_lst3 = set(follow)
    matched_list = set_lst1 & set_lst2 & set_lst3
    return list(matched_list)