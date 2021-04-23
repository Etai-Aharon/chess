

def piece_options(type: str, pos_id: int, arrey_map):
    options_list = []

    if type.__contains__('w_pawn'):
        # wight pawn step
        for step in range(1, 3):
            test = pos_id + (step*8)
            if 0 < test < 65:
                if not arrey_map[test][2]:
                    options_list.append(test)
                    if test > 24:
                        break
                else:
                    break

    if type.__contains__('b_pawn'):
        # black pawn step
        for step in range(1, 3):
            test = pos_id - (step*8)
            if 0 < test < 65:
                if not arrey_map[test][2]:
                    options_list.append(test)
                    if test < 41:
                        break
                else:
                    break

    elif type.__contains__('rook'):
        # rook : check upward
        for step in range(1, 8):
            test = pos_id + (step*8)
            if 0 < test < 65:
                if not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # rook : check downward
        for step in range(1, 8):
            test = pos_id - (step*8)
            if 0 < test < 65:
                if not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # rook : check left
        for step in range(1, 8):
            test = pos_id - step
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('H'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # rook : check right
        for step in range(1, 8):
            test = pos_id + step
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('A'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

    elif type.__contains__('bishop'):
        # bishop : check upward right
        for step in range(1, 8):
            test = pos_id + (step*9)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('A'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # bishop : check downward right
        for step in range(1, 8):
            test = pos_id - (step*7)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('A'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # bishop : check upward left
        for step in range(1, 8):
            test = pos_id + (step*7)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('H'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # bishop : check downward left
        for step in range(1, 8):
            test = pos_id - (step*9)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('H'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

    elif type.__contains__('king'):
        # king : check upward right
        test = pos_id + 9
        if 0 < test < 65:
            if not arrey_map[test][2] and not (str(arrey_map[test][0]).__contains__('A')):
                options_list.append(test)

        # king : check downward right
        test = pos_id - 7
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('A'):
                options_list.append(test)

        # king : check upward left
        test = pos_id + 7
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('H'):
                options_list.append(test)

        # king : check downward left
        test = pos_id - 9
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('H'):
                options_list.append(test)

        # king : check upward
        test = pos_id + 8
        if 0 < test < 65:
            if not arrey_map[test][2]:
                options_list.append(test)

        # king : check downward
        test = pos_id - 8
        if 0 < test < 65:
            if not arrey_map[test][2]:
                options_list.append(test)

        # king : check left
        test = pos_id - 1
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('H'):
                options_list.append(test)

        # king : check right
        test = pos_id + 1
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('A'):
                options_list.append(test)

    elif type.__contains__('queen'):
        # queen : check upward
        for step in range(1, 8):
            test = pos_id + (step*8)
            if 0 < test < 65:
                if not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # queen : check downward
        for step in range(1, 8):
            test = pos_id - (step*8)
            if 0 < test < 65:
                if not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # queen : check left
        for step in range(1, 8):
            test = pos_id - step
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('H'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # queen : check right
        for step in range(1, 8):
            test = pos_id + step
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('A'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # queen : check upward right
        for step in range(1, 8):
            test = pos_id + (step*9)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('A'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # queen : check downward right
        for step in range(1, 8):
            test = pos_id - (step*7)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('A'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # queen : check upward left
        for step in range(1, 8):
            test = pos_id + (step*7)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('H'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

        # queen : check downward left
        for step in range(1, 8):
            test = pos_id - (step*9)
            if 0 < test < 65:
                if str(arrey_map[test][0]).__contains__('H'):
                    break
                elif not arrey_map[test][2]:
                    options_list.append(test)
                else:
                    break

    elif type.__contains__('knight'):
        restrict_left = ['A', 'B']
        restrict_right = ['H', 'G']
        # knight : check #1
        test = pos_id - 17
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('H'):
                options_list.append(test)

        # knight : check #2
        test = pos_id - 15
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('A'):
                options_list.append(test)

        # # knight : check #3
        # test = pos_id - 10
        # if 0 < test < 65:
        #     if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('H' or 'G'):
        #         options_list.append(test)

        # knight : check #3
        test = pos_id - 10
        if 0 < test < 65:
            if not arrey_map[test][2] and not any(val in arrey_map[test][0] for val in restrict_right):
                options_list.append(test)

        # knight : check #4
        test = pos_id - 6
        if 0 < test < 65:
            if not arrey_map[test][2] and not any(val in arrey_map[test][0] for val in restrict_left):
                options_list.append(test)

        # knight : check #5
        test = pos_id + 6
        if 0 < test < 65:
            if not arrey_map[test][2] and not any(val in arrey_map[test][0] for val in restrict_right):
                options_list.append(test)

        # knight : check #4
        test = pos_id + 10
        if 0 < test < 65:
            if not arrey_map[test][2] and not any(val in arrey_map[test][0] for val in restrict_left):
                options_list.append(test)

        # knight : check #5
        test = pos_id + 15
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('H'):
                options_list.append(test)

        # knight : check #4
        test = pos_id + 17
        if 0 < test < 65:
            if not arrey_map[test][2] and not str(arrey_map[test][0]).__contains__('A'):
                options_list.append(test)

    return options_list
