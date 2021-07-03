import time

real_password = '1357'


def check_password(password):
    if len(password) != len(real_password):
        return False
    for x, y in zip(password, real_password):
        time.sleep(0.1)  # Simulates the wait time of the safe's mechanism
        if int(x) != int(y):
            return False
    return True


def crack_password():
    pass_range = range(4)
    guess = list(str(x) for x in pass_range)

    for idx in pass_range:
        for digit in range(10):
            guess[idx] = str(digit)
            guess_pass = ''.join(guess)

            start_time = time.perf_counter()
            hacked = check_password(guess_pass)
            elapsed_time = (round(time.perf_counter() - start_time, 1))

            if hacked:
                return guess_pass

            if elapsed_time == (idx + 2) / 10:
                break


t = time.perf_counter()
pwd = crack_password()
print(pwd)
elapsed = (round(time.perf_counter() - t, 1))
print(elapsed)
