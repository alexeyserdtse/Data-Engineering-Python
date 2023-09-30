def check_time_str(time):
    # split input into list contain [hh,mm] and check inserted value
    if ':' in time:
        time_spl = time.split(':')
    else:
        print('Wrong format inserted')
        exit()

    # validate hh:mm ranges:
    if int(time_spl[0]) not in range(24):
        print('Hour must be between 0 and 23')
        exit()

    if int(time_spl[1]) not in range(59):
        print('Minute must be between 0 and 59')
        exit()

    return time_spl


def time_to_text():
    time_voc = {
        '00': ''
    }


if __name__ == '__main__':
    user_input_time = input('Please enter hh:mm formated time: ')

    splt = check_time_str(user_input_time)

    print(splt)
