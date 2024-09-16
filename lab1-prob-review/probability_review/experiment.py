def expected_value_single(temp_pmf):
        e_value = 0.0
        for value in temp_pmf:
            e_value += (value * temp_pmf[value])
        return e_value
    
    # def variance_single(temp_pmf, temp_exp_val):
    #     dev = {} # squared deviations
    #     for key in temp_pmf:
    #         if temp_pmf[key] < 0:
    #             raise ValueError("variance_single: Outcomes with negative probabilities received.")
    #         # deviation^2
    #         temp = pow(key-temp_exp_val,2)
    #         # If squared deviation is not in the key of the dictionary,
    #         # create a new key and assign it the pmf probability
    #         # otherwise, add the pmf probability to that key's value.
    #         if temp not in dev.keys():
    #             dev[temp] = temp_pmf[key]
    #         else:
    #             dev[temp] += temp_pmf[key]
    #     return expected_value_single(dev)

    marginal_x = {}
    marginal_y = {}
    exp_xy = 0.0
    for key in pmf:
        if pmf[key] < 0.0:
            raise ValueError("covariance: Outcomes with negative probabilities received.")
        exp_xy += key[0]*pmf[key]*key[1]

        x_2 = pow(key[0], 2)
        if x_2 not in marginal_x.keys():
            marginal_x[x_2] = pmf[key]
        else:
            marginal_x[x_2] += pmf[key]

        y_2 = pow(key[1], 2)
        if y_2 not in marginal_y.keys():
            marginal_y[y_2] = pmf[key]
        else:
            marginal_y[y_2] += pmf[key]

    # COV[X,Y] = E[XY] - E[X]E[Y]
    cov_xy = exp_xy - (exp_x * exp_y)

    # COV[X,X] = E[X^2] - E[X]^2
    exp_x_2 = expected_value_single(marginal_x)
    print(f"DEBUG exp_x_2: {exp_x_2}")
    cov_xx = exp_x_2 - pow(exp_x, 2)

    # COV[Y,Y] = E[Y^2] - E[Y]^2
    exp_y_2 = expected_value_single(marginal_y)
    print(f"DEBUG exp_y_2: {exp_y_2}")
    cov_yy = exp_y_2 - pow(exp_y, 2)



    ###################################
    # Finish Implementation Here
    # sigma should be of the form: [[COVxx, COVxy][COVyx, COVyy]]
    # COVxx, COVyy: variances of the individual random variables
    # COVxy, COVyx: covariances, or how "correlated".
        # > 0 : if one goes up, the other goes up
        # 0 : uncorrelated

    if not pmf:
        raise ValueError("covariance: Empty pmf.")

    if not np.isclose(sum(pmf.values()), 1.0):
        raise ValueError("covariance: Probabilities do not sum to one.")

    # print(f"DEBUG pmf\n: {pmf}")
    exp_val = expected_value(pmf)
    exp_x = exp_val[0]
    exp_y = exp_val[1]
    exp_xy = 0.0

    og_mat = np.zeros([2,1])
    for key in pmf:
        if pmf[key] < 0.0:
            raise ValueError("covariance: Outcomes with negative probabilities received.")
        og_mat[0] = key[0]*pmf[key] - exp_x
        og_mat[1] = key[1]*pmf[key] - exp_y
        exp_xy += key[0]*pmf[key]*key[1]
    # print(f"DEBUG og_mat: {og_mat}")

    og_mat_transposed = np.transpose(og_mat)
    # print(f"DEBUG og_mat_transposed: {og_mat_transposed}")

    solution = np.matmul(og_mat, og_mat_transposed)
    # print(f"DEBUG solution:\n{solution}")

    # for key in pmf:
    #     sigma[0][0] += key[0]*pmf[key]*solution[0][0] - exp_x
    #     sigma[0][1] += key[0]*pmf[key]*solution[0][1] - exp_xy
    #     sigma[1][0] += key[0]*pmf[key]*solution[1][0] - exp_xy
    #     sigma[1][1] += key[1]*pmf[key]*solution[1][1] - exp_y

    # print(f"DEBUG exp_x: {exp_x}")
    # print(f"DEBUG exp_xy: {exp_xy}")
    # print(f"DEBUG exp_y: {exp_y}")

    sigma[0][0] = solution[0][0]
    sigma[0][1] = solution[0][1]
    sigma[1][0] = solution[1][0]
    sigma[1][1] = solution[1][1]
    # sigma = [[cov_xx, cov_xy],[cov_xy, cov_yy]]