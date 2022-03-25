def residence_validator(res_dict):

    res_names = []

    # checking for each condition
    for res_name in res_dict.keys():
        if (
            res_dict[res_name][0] > res_dict[res_name][1] or
            res_dict[res_name][2] > 500 or
            res_dict[res_name][0] + res_dict[res_name][1] * 2 > res_dict[res_name][2] or
            'e' in res_name
        ):
            res_names.append(res_name)  # if any of the conditions are met then add to list

    return res_names


valid_residences = residence_validator({'Adelaide': [230, 15, 250], 'Brant': [100, 175, 445], 'Leonard': [150, 300, 669], 'Gordon': [400, 200, 732]})
print(valid_residences)