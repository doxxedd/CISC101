def residence_string_to_dict(res_string):
    res_elements = res_string.split(' ')

    res_dict_to_return = {}  # empty dict


    # filling up dict
    for i in range(0, len(res_elements), 4):
        res_dict_to_return[res_elements[i]] = [int(res_elements[i + 1]), int(res_elements[i + 2]), int(res_elements[i + 3])]

    return res_dict_to_return


res_dict = residence_string_to_dict("Adelaide 230 15 250 Brant 100 175 445 Leonard 150 300 669 Gordon 400 200 732")
print(res_dict)