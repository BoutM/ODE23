# Creation of the Original ODE23 method uzilized
def ode23(de_fcn, tspan, y0, tol, h0, maxh):

    t_history = [tspan[0]]
    y_history = [y0]
    a_history = [1]
    f_evals = 0
    h_history = [h0]

    h = h0
    t = tspan[0]
    y = np.array(y0)
    alpha = 1

    
    # Loop until you reach the end time
    while t<=tspan[1]:
        # Midpoint
        k0, f_evals = de_fcn(t, y)
        k1, f_evals = de_fcn(t + 0.5*h, y + 0.5*h*k0)
        y_m = y + h*k1

        # Runge-Kutta 
        k2, f_evals = de_fcn(t + .75*h, y + 0.75*h*k1)
        y_rk3 = y + h*(2*k0/9 + k1/3 + 4*k2/9)

        # Error and gamma factor
        e = np.linalg.norm(y_m - y_rk3)
        gamma = (tol/e)**(1/3)

        if e <= tol:
            # Saving the step
            y_history.append(y_rk3.tolist())
            t_history.append(t)

            y = y_rk3
            t = t + h

            # Creating of the next optimal h
            alpha = 1.05 * alpha
            h_opt = h * gamma * alpha
            h = min(h_opt, maxh)

            # Appending Step Variables
            a_history.append(alpha)
            h_history.append(h_opt)

        # When the Tolerence is not met:
        else:
            alpha = .7 * alpha
            h_opt = h * gamma * alpha
            h = min(h_opt, maxh)

            # Appending Step Variables
            a_history.append(alpha)
            h_history.append(h_opt)

    return np.array(y_history), np.array(t_history), f_evals, a_history, h_history
