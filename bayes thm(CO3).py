p_yes = 0.6
p_no = 0.4
p_x_given_yes = 0.7
p_x_given_no = 0.2

p_yes_given_x = (p_x_given_yes * p_yes) / (
    p_x_given_yes * p_yes + p_x_given_no * p_no
)

p_no_given_x = 1 - p_yes_given_x

print("Posterior Probability (Yes):", p_yes_given_x)
print("Posterior Probability (No):", p_no_given_x)
