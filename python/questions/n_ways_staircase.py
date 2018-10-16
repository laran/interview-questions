def ways_to_climb(num_steps, max_step_size):
    """
    Calculate the number of ways to climb a certain number of steps
    given a maximum step size.

    This approach uses a dynamic-programming approach

    :param num_steps:
    :param max_step_size:
    :return:
    """
    # initialize base cases
    memo = {0: 1, 1: 1}

    # we already know the answer when num_steps < 2. so solve for num_steps > 1
    for current_step in range(2, num_steps + 1):
        memo[current_step] = 0

        # accumulate the sum of combinations for all step sizes from 1 to min(current_step, max_step_size)
        for step_size in range(1, min(current_step, max_step_size) + 1):
            memo[current_step] = memo[current_step] + memo[current_step - step_size]

    return memo[num_steps]